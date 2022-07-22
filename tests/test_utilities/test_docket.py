"""
    Tests the docket utility.
"""
import os
from pathlib import Path
from tempfile import gettempdir

from pytia.const import BACKGROUND_VIEW, FOREGROUND_VIEW
from pytia.utilities.docket import export_docket_as_pdf
from pytia.wrapper.documents.drawing_documents import PyDrawingDocument

template_name = "pytia_test_docket_template"
test_name = "pytia_test_docket"
temp_folder = gettempdir()
config = {
    "texts": [
        {"name": "text.partnumber", "value": "Partnumber", "view": "bg"},
        {"name": "property.partnumber", "value": "partnumber", "view": "fg"},
        {"name": "text.material", "value": "Material", "view": "bg"},
        {"name": "property.material", "value": "pytia.material", "view": "fg"},
        {"name": "text.date", "value": "Date", "view": "bg"},
        {"name": "object.date", "value": "%d.%m.%Y", "view": "fg"},
        {"name": "property.notfound", "value": "pytia.notfound", "view": "fg"},
        {"name": "wrong_type.material", "value": "pytia.material", "view": "fg"},
    ],
    "views": [
        {
            "name": "isometric 1",
            "x": 100,
            "y": 100,
            "max_width": 100,
            "max_height": 100,
            "definition": (
                -0.707107,
                0.707107,
                0.000000,
                -0.408248,
                -0.408248,
                0.816497,
            ),
        },
        {
            "name": "isometric 2",
            "x": 225,
            "y": 75,
            "max_width": 50,
            "max_height": 50,
            "definition": (
                0.707107,
                -0.707107,
                0.000000,
                0.408248,
                0.408248,
                -0.816497,
            ),
        },
    ],
}


def test_import():
    """ """
    from pytia.utilities.docket import DocketConfig  # noqa: F401
    from pytia.utilities.docket import create_docket_from_template  # noqa: F401
    from pytia.utilities.docket import export_docket_as_pdf  # noqa: F401


def test_create_docket_from_template():
    """
    Tests if the created docket is of instance PyDrawingDocument.

    This test requires preparation:
    - A part with properties must be created.
    - A template drawing with texts must be created.
    Preparation is done automatically.

    This test requires CATIA running.
    """

    from pytia.utilities.docket import DocketConfig, create_docket_from_template
    from pytia.wrapper.documents.drawing_documents import PyDrawingDocument
    from pytia.wrapper.documents.part_documents import PyPartDocument

    def prepare_docket_template() -> str:
        with PyDrawingDocument() as drawing_document:
            drawing_document.new(name=template_name)

            sheet = drawing_document.drawing_document.sheets.active_sheet
            foreground_view = sheet.views.item(FOREGROUND_VIEW)
            background_view = sheet.views.item(BACKGROUND_VIEW)

            foreground_texts = foreground_view.texts
            background_texts = background_view.texts

            active_text = background_texts.add("text_partnumber", 0, 30)
            active_text.name = "text.partnumber"
            active_text = foreground_texts.add("property_partnumber", 50, 30)
            active_text.name = "property.partnumber"

            active_text = background_texts.add("text_material", 0, 20)
            active_text.name = "text.material"
            active_text = foreground_texts.add("property_material", 50, 20)
            active_text.name = "property.material"

            active_text = background_texts.add("text_date", 0, 10)
            active_text.name = "text.date"
            active_text = foreground_texts.add("object_date", 50, 10)
            active_text.name = "object.date"

            background_view.activate()
            factory = background_view.factory_2d

            factory.create_line(50, 50, 150, 50)
            factory.create_line(150, 50, 150, 150)
            factory.create_line(150, 150, 50, 150)
            factory.create_line(50, 150, 50, 50)

            factory.create_line(200, 50, 250, 50)
            factory.create_line(250, 50, 250, 100)
            factory.create_line(250, 100, 200, 100)
            factory.create_line(200, 100, 200, 50)

            foreground_view.activate()
            return drawing_document.save_as(folder=temp_folder)

    def prepare_part_document() -> PyPartDocument:
        test_x = 50
        test_y = 80
        test_z = 20

        part_document = PyPartDocument()
        part_document.new(name=test_name)

        main_body = part_document.bodies.main_body

        reference_plane = part_document.part.create_reference_from_object(
            part_document.part.origin_elements.plane_xy
        )
        profile_sketch = main_body.sketches.add(reference_plane)
        part_document.part.in_work_object = profile_sketch

        factory2D1 = profile_sketch.open_edition()
        factory2D1.create_line(test_x / 2, test_y / 2, test_x / 2, -test_y / 2)
        factory2D1.create_line(test_x / 2, -test_y / 2, -test_x / 2, -test_y / 2)
        factory2D1.create_line(-test_x / 2, -test_y / 2, -test_x / 2, test_y / 2)
        factory2D1.create_line(-test_x / 2, test_y / 2, test_x / 2, test_y / 2)

        profile_sketch.close_edition
        part_document.part.in_work_object = profile_sketch
        part_document.part.update()
        part_document.part.shape_factory.add_new_pad(profile_sketch, test_z)
        part_document.part.update_object(main_body)

        part_document.properties.create(name="pytia.material", value="1.0037")
        part_document.save_as(folder=temp_folder)

        return part_document

    template = prepare_docket_template()
    part_document = prepare_part_document()

    docket_config = DocketConfig.from_dict(config)
    docket = create_docket_from_template(
        template=template,
        document=part_document,
        config=docket_config,
    )
    part_document.close()

    assert isinstance(docket, PyDrawingDocument)


def test_export_docket_as_pdf():
    """Test the export_docket_as_pdf function. Tests if the pdf is created."""
    with PyDrawingDocument() as docket:
        docket.current()
        export_path = export_docket_as_pdf(
            docket=docket, name=test_name, folder=temp_folder
        )

    assert os.path.exists(export_path)

    os.remove(Path(temp_folder, template_name + ".CATDrawing"))
    os.remove(Path(temp_folder, test_name + ".CATPart"))
    os.remove(Path(temp_folder, test_name + ".pdf"))


if __name__ == "__main__":
    from pytia.log import log

    log.set_level_debug()
    log.add_stream_handler()

    test_import()
    test_create_docket_from_template()
    test_export_docket_as_pdf()
