from pytia.framework.system_interfaces.any_object import AnyObject


class SelectionSets(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.selection_sets = com_object

    def add_cso_into_selection_set(self, i_sel_set_name: str) -> None:
        return self.selection_sets.AddCSOIntoSelectionSet(i_sel_set_name)

    def create_selection_set(self, i_sel_set_name: str) -> None:
        return self.selection_sets.CreateSelectionSet(i_sel_set_name)

    def delete_selection_set(self, i_sel_set_name: str) -> None:
        return self.selection_sets.DeleteSelectionSet(i_sel_set_name)

    def get_list_of_selection_set(self, o_list_of_selection_set: tuple) -> None:
        return self.selection_sets.GetListOfSelectionSet(o_list_of_selection_set)

    def put_selection_set_into_cso(self, i_sel_set_name: str) -> None:
        return self.selection_sets.PutSelectionSetIntoCSO(i_sel_set_name)

    def rename_selection_set(
        self, i_old_sel_set_name: str, i_new_sel_set_name: str
    ) -> None:
        return self.selection_sets.RenameSelectionSet(
            i_old_sel_set_name, i_new_sel_set_name
        )

    def __repr__(self):
        return f'SelectionSets(name="{ self.name }")'
