from typing import Iterator
from pytia.framework.drafting_interfaces.drawing_sheet import DrawingSheet
from pytia.framework.system_interfaces.collection import Collection
from pytia.framework.cat_types.general import cat_variant


class DrawingSheets(Collection):
    def __init__(self, com_object):
        super().__init__(com_object, child_object=DrawingSheet)
        self.drawing_sheets = com_object

    @property
    def active_sheet(self) -> DrawingSheet:
        return DrawingSheet(self.drawing_sheets.ActiveSheet)

    def add(self, i_drawing_sheet_name: str) -> DrawingSheet:
        return DrawingSheet(self.drawing_sheets.Add(i_drawing_sheet_name))

    def add_detail(self, i_drawing_sheet_name: str) -> DrawingSheet:
        return DrawingSheet(self.drawing_sheets.AddDetail(i_drawing_sheet_name))

    def item(self, i_index: cat_variant) -> DrawingSheet:
        return DrawingSheet(self.drawing_sheets.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        return self.drawing_sheets.Remove(i_index)

    def __getitem__(self, n: int) -> DrawingSheet:
        if (n + 1) > self.count:
            raise StopIteration
        return DrawingSheet(self.drawing_sheets.item(n + 1))

    def __iter__(self) -> Iterator[DrawingSheet]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'DrawingSheets(name="{self.name}")'
