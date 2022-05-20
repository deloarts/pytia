from pytia.framework.drafting_interfaces.drawing_sheet import DrawingSheet
from pytia.framework.drafting_interfaces.drawing_document import DrawingDocument


class DrawingRoot(DrawingDocument):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.drawing_root_com = com_object

    @property
    def active_sheet(self) -> DrawingSheet:
        return DrawingSheet(self.drawing_root_com.ActiveSheet)

    @active_sheet.setter
    def active_sheet(self, value: DrawingSheet):
        self.drawing_root_com.ActiveSheet = value

    def reorder_sheets(self, i_ordered_sheets: tuple) -> None:
        sheets = [x.com_object for x in i_ordered_sheets]
        return self.drawing_root_com.reorder_Sheets(sheets)

    def __repr__(self):
        return f'DrawingRoot(name="{self.name}")'
