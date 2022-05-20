from pytia.framework.system_interfaces.any_object import AnyObject
from pytia.framework.cat_types.general import cat_variant


class Hyperlink(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hyperlink = com_object

    def add_url(self, i_url: str) -> None:
        return self.hyperlink.AddUrl(i_url)

    def count_object(self) -> int:
        return self.hyperlink.CountObject()

    def item_object(self, i_index: cat_variant) -> str:
        return self.hyperlink.ItemObject(i_index)

    def remove_object(self, i_index: cat_variant) -> None:
        return self.hyperlink.RemoveObject(i_index)

    def __repr__(self):
        return f'Hyperlink(name="{self.name}")'
