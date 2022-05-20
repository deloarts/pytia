from pytia.framework.system_interfaces.setting_controller import SettingController


class VrmlSettingAtt(SettingController):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.vrml_setting_att = com_object

    @property
    def export_edges(self) -> bool:
        return self.vrml_setting_att.ExportEdges

    @export_edges.setter
    def export_edges(self, value: bool):
        self.vrml_setting_att.ExportEdges = value

    @property
    def export_normals(self) -> bool:
        return self.vrml_setting_att.ExportNormals

    @export_normals.setter
    def export_normals(self, value: bool):
        self.vrml_setting_att.ExportNormals = value

    @property
    def export_texture(self) -> bool:
        return self.vrml_setting_att.ExportTexture

    @export_texture.setter
    def export_texture(self, value: bool):
        self.vrml_setting_att.ExportTexture = value

    @property
    def export_texture_file(self) -> int:
        return self.vrml_setting_att.ExportTextureFile

    @export_texture_file.setter
    def export_texture_file(self, value: int):
        self.vrml_setting_att.ExportTextureFile = value

    @property
    def export_texture_format(self) -> int:
        return self.vrml_setting_att.ExportTextureFormat

    @export_texture_format.setter
    def export_texture_format(self, value: int):
        self.vrml_setting_att.ExportTextureFormat = value

    @property
    def export_version(self) -> int:
        return self.vrml_setting_att.ExportVersion

    @export_version.setter
    def export_version(self, value: int):
        self.vrml_setting_att.ExportVersion = value

    @property
    def import_crease_angle(self) -> float:
        return self.vrml_setting_att.ImportCreaseAngle

    @import_crease_angle.setter
    def import_crease_angle(self, value: float):
        self.vrml_setting_att.ImportCreaseAngle = value

    @property
    def import_unit(self) -> int:
        return self.vrml_setting_att.ImportUnit

    @import_unit.setter
    def import_unit(self, value: int):
        self.vrml_setting_att.ImportUnit = value

    def get_export_background_color(self, io_r: int, io_g: int, io_b: int) -> None:
        return self.vrml_setting_att.GetExportBackgroundColor(io_r, io_g, io_b)

    def get_export_background_color_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.vrml_setting_att.GetExportBackgroundColorInfo(
            io_admin_level, io_locked
        )

    def get_export_edges_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.vrml_setting_att.GetExportEdgesInfo(io_admin_level, io_locked)

    def get_export_normals_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.vrml_setting_att.GetExportNormalsInfo(io_admin_level, io_locked)

    def get_export_texture_file_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.vrml_setting_att.GetExportTextureFileInfo(io_admin_level, io_locked)

    def get_export_texture_format_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.vrml_setting_att.GetExportTextureFormatInfo(
            io_admin_level, io_locked
        )

    def get_export_texture_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.vrml_setting_att.GetExportTextureInfo(io_admin_level, io_locked)

    def get_export_version_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.vrml_setting_att.GetExportVersionInfo(io_admin_level, io_locked)

    def get_import_crease_angle_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.vrml_setting_att.GetImportCreaseAngleInfo(io_admin_level, io_locked)

    def get_import_unit_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.vrml_setting_att.GetImportUnitInfo(io_admin_level, io_locked)

    def set_export_background_color(self, i_r: int, i_g: int, i_b: int) -> None:
        return self.vrml_setting_att.SetExportBackgroundColor(i_r, i_g, i_b)

    def set_export_background_color_lock(self, i_locked: bool) -> None:
        return self.vrml_setting_att.SetExportBackgroundColorLock(i_locked)

    def set_export_edges_lock(self, i_locked: bool) -> None:
        return self.vrml_setting_att.SetExportEdgesLock(i_locked)

    def set_export_normals_lock(self, i_locked: bool) -> None:
        return self.vrml_setting_att.SetExportNormalsLock(i_locked)

    def set_export_texture_file_lock(self, i_locked: bool) -> None:
        return self.vrml_setting_att.SetExportTextureFileLock(i_locked)

    def set_export_texture_format_lock(self, i_locked: bool) -> None:
        return self.vrml_setting_att.SetExportTextureFormatLock(i_locked)

    def set_export_texture_lock(self, i_locked: bool) -> None:
        return self.vrml_setting_att.SetExportTextureLock(i_locked)

    def set_export_version_lock(self, i_locked: bool) -> None:
        return self.vrml_setting_att.SetExportVersionLock(i_locked)

    def set_import_crease_angle_lock(self, i_locked: bool) -> None:
        return self.vrml_setting_att.SetImportCreaseAngleLock(i_locked)

    def set_import_unit_lock(self, i_locked: bool) -> None:
        return self.vrml_setting_att.SetImportUnitLock(i_locked)

    def __repr__(self):
        return f'VrmlSettingAtt(name="{self.name}")'
