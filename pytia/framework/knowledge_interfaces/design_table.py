from typing import TYPE_CHECKING
from pytia.framework.knowledge_interfaces.relation import Relation

if TYPE_CHECKING:
    from pytia.framework.knowledge_interfaces.parameter import Parameter


class DesignTable(Relation):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.design_table = com_object

    @property
    def columns_nb(self) -> int:
        return self.design_table.ColumnsNb

    @property
    def configuration(self) -> int:
        return self.design_table.Configuration

    @configuration.setter
    def configuration(self, value: int):
        self.design_table.Configuration = value

    @property
    def configurations_nb(self) -> int:
        return self.design_table.ConfigurationsNb

    @property
    def copy_mode(self) -> bool:
        return self.design_table.CopyMode

    @copy_mode.setter
    def copy_mode(self, value: bool):
        self.design_table.CopyMode = value

    @property
    def file_path(self) -> str:
        return self.design_table.FilePath

    @file_path.setter
    def file_path(self, value: str):
        self.design_table.FilePath = value

    def add_association(self, i_parameter: "Parameter", i_sheet_column: str) -> None:
        return self.design_table.AddAssociation(i_parameter.com_object, i_sheet_column)

    def add_new_row(self) -> None:
        return self.design_table.AddNewRow()

    def cell_as_string(self, i_row: int, i_column: int) -> str:
        return self.design_table.CellAsString(i_row, i_column)

    def remove_association(self, i_sheet_column: str) -> None:
        return self.design_table.RemoveAssociation(i_sheet_column)

    def synchronize(self) -> None:
        return self.design_table.Synchronize()

    def __repr__(self):
        return f'DesignTable(name="{self.name}")'
