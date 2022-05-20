from typing import TYPE_CHECKING
from pytia.framework.drafting_interfaces.drawing_sheets import DrawingSheets
from pytia.framework.in_interfaces.document import Document
from pytia.framework.knowledge_interfaces.parameters import Parameters
from pytia.framework.knowledge_interfaces.relations import Relations

if TYPE_CHECKING:
    from pytia.framework.drafting_interfaces.drawing_root import DrawingRoot


class DrawingDocument(Document):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.drawing_document = com_object

    @property
    def drawing_root(self) -> "DrawingRoot":
        from pytia.framework.drafting_interfaces.drawing_root import DrawingRoot

        return DrawingRoot(self.drawing_document.DrawingRoot)

    @property
    def parameters(self) -> Parameters:
        return Parameters(self.drawing_document.Parameters)

    @property
    def relations(self) -> Relations:
        return Relations(self.drawing_document.Relations)

    @property
    def sheets(self) -> DrawingSheets:
        return DrawingSheets(self.drawing_document.Sheets)

    @property
    def standard(self) -> int:
        return self.drawing_document.Standard

    @standard.setter
    def standard(self, value: int):
        self.drawing_document.Standard = value

    def isolate(self) -> None:
        return self.drawing_document.Isolate()

    def update(self) -> None:
        return self.drawing_document.Update()

    def __repr__(self):
        return f'DrawingDocument(name="{self.name}")'
