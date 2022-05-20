from pytia.framework.drafting_interfaces.drawing_document import DrawingDocument
from pytia.framework.mec_mod_interfaces.part_document import PartDocument
from pytia.framework.cat_mat_interfaces.material_document import MaterialDocument
from pytia.framework.product_structure_interfaces.product_document import (
    ProductDocument,
)

document_type = {
    "CATPart": PartDocument,
    "CATProduct": ProductDocument,
    "CATDrawing": DrawingDocument,
    "CATMaterial": MaterialDocument,
}
