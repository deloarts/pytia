from pytia.framework.system_interfaces.i_unknown import IUnknown


class IDispatch(IUnknown):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return f"IDispatch()"
