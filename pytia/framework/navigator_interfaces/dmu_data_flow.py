from pytia.framework.system_interfaces.any_object import AnyObject


class DMUDataFlow(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.dmu_data_flow = com_object

    def cache_export(self, i_directory: str, i_prefix: str, i_data: int) -> None:
        return self.dmu_data_flow.CacheExport(i_directory, i_prefix, i_data)

    def cache_import(self, i_directory: str) -> None:
        return self.dmu_data_flow.CacheImport(i_directory)

    def collapse(self) -> None:
        return self.dmu_data_flow.Collapse()

    def replace_by_cgr(self, i_directory: str, i_prefix: str) -> None:
        return self.dmu_data_flow.ReplaceByCGR(i_directory, i_prefix)

    def save_as_frozen(
        self, i_directory: str, i_prefix: str, i_data: int, i_cache: int
    ) -> None:
        return self.dmu_data_flow.SaveAsFrozen(i_directory, i_prefix, i_data, i_cache)

    def __repr__(self):
        return f'DmuDataFlow(name="{self.name}")'
