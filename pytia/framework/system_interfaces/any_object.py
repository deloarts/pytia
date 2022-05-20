from typing import TYPE_CHECKING
from pytia.framework.base import Base

if TYPE_CHECKING:
    from pytia.framework.in_interfaces.application import Application
from pytia.framework.system_interfaces.cat_base_dispatch import CATBaseDispatch


class AnyObject(Base):
    def __init__(self, com_object):
        super().__init__()
        self.com_object = com_object

    @property
    def application(self) -> "Application":
        from pytia.framework.in_interfaces.application import Application

        return Application(self.com_object.Application)

    @property
    def name(self) -> str:
        return self.com_object.Name

    @name.setter
    def name(self, value: str):
        self.com_object.Name = value

    @property
    def parent(self) -> "AnyObject":
        return AnyObject(self.com_object.Parent)

    def get_item(self, id_name: str) -> "AnyObject":
        return AnyObject(self.com_object.GetItem(id_name))

    def get_item_dispatch(self, id_name: str) -> CATBaseDispatch:
        return self.com_object.GetItem(id_name)

    def __repr__(self):
        return f'AnyObject(name="{self.name}")'
