from pytia.framework.system_interfaces.cat_base_unknown import CATBaseUnknown


class CATBaseDispatch(CATBaseUnknown):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return f"CatBaseDispatch()"
