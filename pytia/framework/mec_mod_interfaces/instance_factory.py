from pytia.framework.mec_mod_interfaces.factory import Factory
from pytia.framework.system_interfaces.any_object import AnyObject


class InstanceFactory(Factory):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.instance_factory = com_object

    @property
    def instantiation_mode(self) -> str:
        return self.instance_factory.InstantiationMode

    @instantiation_mode.setter
    def instantiation_mode(self, value: str):
        self.instance_factory.InstantiationMode = value

    def add_instance(self, i_reference: AnyObject) -> AnyObject:
        return AnyObject(self.instance_factory.AddInstance(i_reference.com_object))

    def begin_instance_factory(
        self, i_name_of_reference: str, i_name_of_document: str
    ) -> None:
        return self.instance_factory.BeginInstanceFactory(
            i_name_of_reference, i_name_of_document
        )

    def begin_instantiate(self) -> None:
        return self.instance_factory.BeginInstantiate()

    def end_instance_factory(self) -> None:
        return self.instance_factory.EndInstanceFactory()

    def end_instantiate(self) -> None:
        return self.instance_factory.EndInstantiate()

    def get_parameter(self, i_name: str) -> AnyObject:
        return AnyObject(self.instance_factory.GetParameter(i_name))

    def instantiate(self) -> AnyObject:
        return AnyObject(self.instance_factory.Instantiate())

    def put_input_data(self, i_name: str, i_input: AnyObject) -> None:
        return self.instance_factory.PutInputData(i_name, i_input.com_object)

    def __repr__(self):
        return f'InstanceFactory(name="{self.name}")'
