from pytia.framework.system_interfaces.i_dispatch import IDispatch


class CATBaseUnknown(IDispatch):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return f"CatBaseUnknown()"
