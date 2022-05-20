from pytia.framework.mec_mod_interfaces.factory import Factory
from pytia.framework.tps_interfaces.capture import Capture


class CaptureFactory(Factory):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.capture_factory = com_object

    def create_capture(self) -> Capture:
        return Capture(self.capture_factory.CreateCapture())

    def __repr__(self):
        return f'CaptureFactory(name="{ self.name }")'
