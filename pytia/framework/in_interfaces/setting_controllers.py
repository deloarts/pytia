from typing import Iterator
from pytia.framework.system_interfaces.collection import Collection
from pytia.framework.system_interfaces.setting_controller import SettingController


class SettingControllers(Collection):
    def __init__(self, com_object):
        super().__init__(com_object, child_object=SettingController)
        self.setting_controllers = com_object
        self.child_object = SettingController

    def item(self, i_index: str) -> SettingController:
        return SettingController(self.setting_controllers.Item(i_index))

    def __getitem__(self, n: int) -> SettingController:
        if (n + 1) > self.count:
            raise StopIteration
        return SettingController(self.setting_controllers.item(n + 1))

    def __iter__(self) -> Iterator[SettingController]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'SettingControllers(name="{self.name}")'
