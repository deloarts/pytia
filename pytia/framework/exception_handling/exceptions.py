class PYCATIABaseException(Exception):
    pass


class CATIAApplicationException(PYCATIABaseException):
    def __init__(self, message):
        self.message = message
