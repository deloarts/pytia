from pytia.framework.system_interfaces.any_object import AnyObject


class HybridShape(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape = com_object

    @property
    def thickness(self) -> "HybridShape":
        return HybridShape(self.hybrid_shape.Thickness)

    def append_hybrid_shape(self, i_hybrid_shape: "HybridShape") -> None:
        return self.hybrid_shape.AppendHybridShape(i_hybrid_shape.com_object)

    def compute(self) -> None:
        return self.hybrid_shape.Compute()

    def __repr__(self):
        return f'HybridShape(name="{self.name}")'
