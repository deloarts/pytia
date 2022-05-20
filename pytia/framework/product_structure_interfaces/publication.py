from pytia.framework.system_interfaces.any_object import AnyObject


class Publication(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.publication = com_object

    @property
    def relay(self) -> "Publication":
        return self.publication.Relay

    @relay.setter
    def relay(self, publication: "Publication"):
        self.publication.Relay = publication.com_object

    @property
    def valuation(self) -> AnyObject:
        return AnyObject(self.publication.Valuation)

    @valuation.setter
    def valuation(self, value: AnyObject):
        self.publication.Valuation = value

    def __repr__(self):
        return f'Publication(name="{ self.name }")'
