from pytia.framework.drafting_interfaces.drawing_leaders import DrawingLeaders
from pytia.framework.drafting_interfaces.drawing_text import DrawingText
from pytia.framework.system_interfaces.any_object import AnyObject


class DrawingTable(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.drawing_table = com_object

    @property
    def anchor_point(self) -> int:
        return self.drawing_table.AnchorPoint

    @anchor_point.setter
    def anchor_point(self, value: int):
        self.drawing_table.AnchorPoint = value

    @property
    def angle(self) -> float:
        return self.drawing_table.Angle

    @angle.setter
    def angle(self, value: float):
        self.drawing_table.Angle = value

    @property
    def compute_mode(self) -> int:
        return self.drawing_table.ComputeMode

    @compute_mode.setter
    def compute_mode(self, value: int):
        self.drawing_table.ComputeMode = value

    @property
    def leaders(self) -> DrawingLeaders:
        return DrawingLeaders(self.drawing_table.Leaders)

    @property
    def number_of_columns(self) -> int:
        return self.drawing_table.NumberOfColumns

    @property
    def number_of_rows(self) -> int:
        return self.drawing_table.NumberOfRows

    @property
    def x(self) -> float:
        return self.drawing_table.x

    @x.setter
    def x(self, value: float):
        self.drawing_table.x = value

    @property
    def y(self) -> float:
        return self.drawing_table.y

    @y.setter
    def y(self, value: float):
        self.drawing_table.y = value

    def add_column(self, i_col: int) -> None:
        return self.drawing_table.AddColumn(i_col)

    def add_row(self, i_row: int) -> None:
        return self.drawing_table.AddRow(i_row)

    def get_cell_alignment(self, i_row: int, i_col: int) -> int:
        return self.drawing_table.GetCellAlignment(i_row, i_col)

    def get_cell_border_type(self, i_row: int, i_col: int) -> int:
        return self.drawing_table.GetCellBorderType(i_row, i_col)

    def get_cell_name(self, i_row: int, i_col: int) -> str:
        return self.drawing_table.GetCellName(i_row, i_col)

    def get_cell_object(self, i_row: int, i_col: int) -> DrawingText:
        return DrawingText(self.drawing_table.GetCellObject(i_row, i_col))

    def get_cell_string(self, i_row: int, i_col: int) -> str:
        return self.drawing_table.GetCellString(i_row, i_col)

    def get_cells_merge(self, o_list_of_merge_cells: tuple) -> None:
        return self.drawing_table.GetCellsMerge(o_list_of_merge_cells)

    def get_column_size(self, i_col: int) -> float:
        return self.drawing_table.GetColumnSize(i_col)

    def get_merge_infos(
        self,
        i_row: int,
        i_col: int,
        o_first_row: int,
        o_first_col: int,
        o_nb_row: int,
        o_nb_col: int,
    ) -> None:
        return self.drawing_table.GetMergeInfos(
            i_row, i_col, o_first_row, o_first_col, o_nb_row, o_nb_col
        )

    def get_row_size(self, i_row: int) -> float:
        return self.drawing_table.GetRowSize(i_row)

    def invert_mode(self, i_mode: int) -> None:
        return self.drawing_table.InvertMode(i_mode)

    def merge_cells(self, i_first_row, i_first_col, i_nb_row_merge, i_nb_col_merge):
        return self.drawing_table.MergeCells(
            i_first_row, i_first_col, i_nb_row_merge, i_nb_col_merge
        )

    def move(self, i_delta_x: float, i_delta_y: float) -> None:
        return self.drawing_table.Move(i_delta_x, i_delta_y)

    def remove_column(self, i_col: int) -> None:
        return self.drawing_table.RemoveColumn(i_col)

    def remove_row(self, i_row):
        return self.drawing_table.RemoveRow(i_row)

    def rotate(self, i_delta_angle: float) -> None:
        return self.drawing_table.Rotate(i_delta_angle)

    def set_cell_alignment(self, i_row: int, i_col: int, i_align: int) -> None:
        return self.drawing_table.SetCellAlignment(i_row, i_col, i_align)

    def set_cell_border_type(self, i_row: int, i_col: int, i_type: int) -> None:
        return self.drawing_table.SetCellBorderType(i_row, i_col, i_type)

    def set_cell_name(self, i_row: int, i_col: int, i_name: str) -> None:
        return self.drawing_table.SetCellName(i_row, i_col, i_name)

    def set_cell_object(self, i_row: int, i_col: int, i_text: DrawingText) -> None:
        return self.drawing_table.SetCellObject(i_row, i_col, i_text.com_object)

    def set_cell_string(self, i_row: int, i_col: int, i_string: str) -> None:
        return self.drawing_table.SetCellString(i_row, i_col, i_string)

    def set_column_size(self, i_col: int, i_col_size: float) -> None:
        return self.drawing_table.SetColumnSize(i_col, i_col_size)

    def set_row_size(self, i_row: int, i_row_size: float) -> None:
        return self.drawing_table.SetRowSize(i_row, i_row_size)

    def un_merge_cells(self, i_row: int, i_col: int) -> None:
        return self.drawing_table.UnMergeCells(i_row, i_col)

    def __repr__(self):
        return f'DrawingTable(name="{self.name}")'
