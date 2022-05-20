from typing import Iterator
from pytia.framework.exception_handling import CATIAApplicationException
from pytia.framework.in_interfaces.document import Document
from pytia.framework.in_interfaces.selected_element import SelectedElement
from pytia.framework.in_interfaces.vis_property_set import VisPropertySet
from pytia.framework.system_interfaces.any_object import AnyObject
from pytia.framework.cat_types.checking import check_type


class Selection(AnyObject):
    def __init__(self, com_object, child_object=SelectedElement):
        super().__init__(com_object)
        self.selection = com_object
        self.child_object = child_object

    @property
    def count(self) -> int:
        return self.selection.Count

    @property
    def count2(self) -> int:
        return self.selection.Count2

    @property
    def vis_properties(self) -> VisPropertySet:
        return VisPropertySet(self.selection.VisProperties)

    def add(self, i_object: AnyObject) -> None:
        return self.selection.Add(i_object.com_object)

    def clear(self) -> None:
        return self.selection.Clear()

    def copy(self) -> None:
        return self.selection.Copy()

    def cut(self) -> None:
        return self.selection.Cut()

    def delete(self) -> None:
        return self.selection.Delete()

    def filter_correspondence(self, i_filter_type: tuple) -> bool:
        return self.selection.FilterCorrespondence(i_filter_type)

    def find_object(self, i_object_type: str) -> AnyObject:
        return AnyObject(self.selection.FindObject(i_object_type))

    def indicate_or_select_element_2d(
        self,
        i_message: str,
        i_filter_type: tuple,
        i_object_selection_before_command_use_possibility: bool,
        i_tooltip: bool,
        i_triggering_on_mouse_move: bool,
        o_object_selected: bool,
        o_document_window_location: tuple,
    ) -> str:
        return self.selection.IndicateOrSelectElement2D(
            i_message,
            i_filter_type,
            i_object_selection_before_command_use_possibility,
            i_tooltip,
            i_triggering_on_mouse_move,
            o_object_selected,
            o_document_window_location,
        )

    def indicate_or_select_element_3d(
        self,
        i_planar_geometric_object: AnyObject,
        i_message: str,
        i_filter_type: tuple,
        i_object_selection_before_command_use_possibility: bool,
        i_tooltip: bool,
        i_triggering_on_mouse_move: bool,
        o_object_selected: bool,
        o_window_location_2d: tuple,
        o_window_location_3d: tuple,
    ) -> str:
        return self.selection.IndicateOrSelectElement3D(
            i_planar_geometric_object.com_object,
            i_message,
            i_filter_type,
            i_object_selection_before_command_use_possibility,
            i_tooltip,
            i_triggering_on_mouse_move,
            o_object_selected,
            o_window_location_2d,
            o_window_location_3d,
        )

    def item(self, i_index: int) -> SelectedElement:
        return SelectedElement(self.selection.Item(i_index))

    def item2(self, i_index: int) -> SelectedElement:
        return SelectedElement(self.selection.Item2(i_index))

    def items(self):
        items_list = []
        for i in range(self.com_object.Count):
            item = self.child_object(self.com_object.Item(i + 1))
            items_list.append(item)
        return items_list

    def paste(self) -> None:
        return self.selection.Paste()

    def paste_special(self, i_format: str) -> None:
        return self.selection.PasteSpecial(i_format)

    def remove(self, i_index):
        return self.selection.Remove(i_index)

    def remove2(self, i_index):
        return self.selection.Remove2(i_index)

    def search(self, i_string_bstr):
        try:
            return self.selection.Search(i_string_bstr)
        except Exception as e:
            raise CATIAApplicationException(
                f'The method Search failed with search string "{i_string_bstr}". Try changing your search string.'
            )

    def select_element2(
        self,
        i_filter_type: tuple,
        i_message: str,
        i_object_selection_before_command_use_possibility: bool,
    ) -> str:
        check_type(i_filter_type, tuple)
        return self.selection.SelectElement2(
            i_filter_type, i_message, i_object_selection_before_command_use_possibility
        )

    def select_element3(
        self,
        i_filter_type: tuple,
        i_message: str,
        i_object_selection_before_command_use_possibility: bool,
        i_multi_selection_mode: int,
        i_tooltip: bool,
    ) -> str:
        check_type(i_filter_type, tuple)
        return self.selection.SelectElement3(
            i_filter_type,
            i_message,
            i_object_selection_before_command_use_possibility,
            i_multi_selection_mode,
            i_tooltip,
        )

    def select_element4(
        self,
        i_filter_type: tuple,
        i_active_document_message: str,
        i_non_active_document_message: str,
        i_tooltip: bool,
        o_document: Document,
    ) -> str:
        check_type(i_filter_type, tuple)
        check_type(o_document, Document)
        return self.selection.SelectElement4(
            i_filter_type,
            i_active_document_message,
            i_non_active_document_message,
            i_tooltip,
            o_document.com_object,
        )

    def __len__(self):
        return self.count

    def __getitem__(self, n: int) -> SelectedElement:
        if (n + 1) > self.count:
            raise StopIteration
        return SelectedElement(self.selection.item(n + 1))

    def __iter__(self) -> Iterator[SelectedElement]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'Selection(name="{self.name}")'
