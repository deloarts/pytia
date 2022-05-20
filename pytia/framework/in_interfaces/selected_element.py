from pytia.framework.in_interfaces.document import Document
from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.system_interfaces.any_object import AnyObject


class SelectedElement(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.selected_element = com_object

    @property
    def document(self) -> Document:
        return Document(self.selected_element.Document)

    @property
    def leaf_product(self) -> AnyObject:
        return AnyObject(self.selected_element.LeafProduct)

    @property
    def reference(self) -> Reference:
        return Reference(self.selected_element.Reference)

    @property
    def type(self) -> str:
        return self.selected_element.Type

    @property
    def value(self) -> AnyObject:
        return AnyObject(self.selected_element.Value)

    def get_coordinates(self) -> tuple:
        vba_function_name = "get_coordinates"
        vba_code = """
        Public Function get_coordinates(selected_element)
            Dim ioPoint (2)
            selected_element.GetCoordinates ioPoint
            get_coordinates = ioPoint
        End Function
        """
        system_service = self.application.system_service
        return system_service.evaluate(
            vba_code, 0, vba_function_name, [self.com_object]
        )

    def __repr__(self):
        return f'SelectedElement(name="{self.name}")'
