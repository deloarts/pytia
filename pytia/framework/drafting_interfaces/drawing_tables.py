from typing import Iterator
from pytia.framework.drafting_interfaces.drawing_table import DrawingTable
from pytia.framework.system_interfaces.collection import Collection


class DrawingTables(Collection):
    def __init__(self, com_object):
        super().__init__(com_object, child_object=DrawingTable)
        self.drawing_tables = com_object

    def add(
        self,
        i_position_x: float,
        i_position_y: float,
        i_number_of_row: int,
        i_number_of_column: int,
        i_row_height: float,
        i_column_width: float,
    ) -> DrawingTable:
        return DrawingTable(
            self.drawing_tables.Add(
                i_position_x,
                i_position_y,
                i_number_of_row,
                i_number_of_column,
                i_row_height,
                i_column_width,
            )
        )

    def item(self, i_index: int) -> DrawingTable:
        return DrawingTable(self.drawing_tables.Item(i_index))

    def remove(self, i_index: int) -> None:
        return self.drawing_tables.Remove(i_index)

    def __getitem__(self, n: int) -> DrawingTable:
        if (n + 1) > self.count:
            raise StopIteration
        return DrawingTable(self.drawing_tables.item(n + 1))

    def __iter__(self) -> Iterator[DrawingTable]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'DrawingTables(name="{self.name}")'
