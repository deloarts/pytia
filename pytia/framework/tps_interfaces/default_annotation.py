from pytia.framework.system_interfaces.any_object import AnyObject


class DefaultAnnotation(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.default_annotation = com_object

    @property
    def link_wi_geom_type(self) -> str:
        return self.default_annotation.LinkWiGeomType

    @property
    def search_algo_type(self) -> str:
        return self.default_annotation.SearchAlgoType

    def is_in_automatic_search_mode(self) -> bool:
        return self.default_annotation.IsInAutomaticSearchMode()

    def __repr__(self):
        return f'DefaultAnnotation(name="{ self.name }")'
