from pytia.framework.system_interfaces.any_object import AnyObject


class AnnotationSetTransformIntoAssemblySet(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.annotation_set_transform_into_assembly_set = com_object

    def transform(self, i_assemblyannotation_set_name: str) -> None:
        return self.annotation_set_transform_into_assembly_set.Transform(
            i_assemblyannotation_set_name
        )

    def __repr__(self):
        return f'AnnotationSetTransformIntoAssemblySet(name="{ self.name }")'
