from pytia.framework.mec_mod_interfaces.face import Face


class CylindricalFace(Face):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.cylindrical_face = com_object

    def get_direction(self) -> tuple:
        vba_function_name = "get_direction"
        vba_code = """
        Public Function get_direction(cylindrical_face)
            Dim oDirection (2)
            cylindrical_face.GetDirection oDirection
            get_direction = oDirection
        End Function
        """
        system_service = self.application.system_service
        return system_service.evaluate(
            vba_code, 0, vba_function_name, [self.com_object]
        )

    def get_origin(self) -> tuple:
        vba_function_name = "get_origin"
        vba_code = """
        Public Function get_origin(cylindrical_face)
            Dim oOrigin (2)
            cylindrical_face.GetOrigin oOrigin
            get_origin = oOrigin
        End Function
        """
        system_service = self.application.system_service
        return system_service.evaluate(
            vba_code, 0, vba_function_name, [self.com_object]
        )

    def __repr__(self):
        return f'CylindricalFace(name="{self.name}")'
