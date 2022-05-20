from pytia.framework.system_interfaces.any_object import AnyObject


class RenderingMaterial(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.rendering_material = com_object

    @property
    def adaptive_coeff(self) -> int:
        return self.rendering_material.AdaptiveCoeff

    @adaptive_coeff.setter
    def adaptive_coeff(self, value: int):
        self.rendering_material.AdaptiveCoeff = value

    @property
    def ambient_coefficient(self) -> float:
        return self.rendering_material.AmbientCoefficient

    @ambient_coefficient.setter
    def ambient_coefficient(self, value: float):
        self.rendering_material.AmbientCoefficient = value

    @property
    def bump(self) -> float:
        return self.rendering_material.Bump

    @bump.setter
    def bump(self, value: float):
        self.rendering_material.Bump = value

    @property
    def chessboard_joint_height(self) -> float:
        return self.rendering_material.ChessboardJointHeight

    @chessboard_joint_height.setter
    def chessboard_joint_height(self, value: float):
        self.rendering_material.ChessboardJointHeight = value

    @property
    def chessboard_joint_width(self) -> float:
        return self.rendering_material.ChessboardJointWidth

    @chessboard_joint_width.setter
    def chessboard_joint_width(self, value: float):
        self.rendering_material.ChessboardJointWidth = value

    @property
    def chessboard_offset(self) -> float:
        return self.rendering_material.ChessboardOffset

    @chessboard_offset.setter
    def chessboard_offset(self, value: float):
        self.rendering_material.ChessboardOffset = value

    @property
    def chessboard_tile_height(self) -> float:
        return self.rendering_material.ChessboardTileHeight

    @chessboard_tile_height.setter
    def chessboard_tile_height(self, value: float):
        self.rendering_material.ChessboardTileHeight = value

    @property
    def chessboard_tile_width(self) -> float:
        return self.rendering_material.ChessboardTileWidth

    @chessboard_tile_width.setter
    def chessboard_tile_width(self, value: float):
        self.rendering_material.ChessboardTileWidth = value

    @property
    def color_number(self) -> int:
        return self.rendering_material.ColorNumber

    @color_number.setter
    def color_number(self, value: int):
        self.rendering_material.ColorNumber = value

    @property
    def diffuse_coefficient(self) -> float:
        return self.rendering_material.DiffuseCoefficient

    @diffuse_coefficient.setter
    def diffuse_coefficient(self, value: float):
        self.rendering_material.DiffuseCoefficient = value

    @property
    def environment_image(self) -> str:
        return self.rendering_material.EnvironmentImage

    @environment_image.setter
    def environment_image(self, value: str):
        self.rendering_material.EnvironmentImage = value

    @property
    def flip_u(self) -> bool:
        return self.rendering_material.FlipU

    @flip_u.setter
    def flip_u(self, value: bool):
        self.rendering_material.FlipU = value

    @property
    def flip_v(self) -> bool:
        return self.rendering_material.FlipV

    @flip_v.setter
    def flip_v(self, value: bool):
        self.rendering_material.FlipV = value

    @property
    def mapping_type(self) -> int:
        return self.rendering_material.MappingType

    @mapping_type.setter
    def mapping_type(self, value: int):
        self.rendering_material.MappingType = value

    @property
    def orientation(self) -> float:
        return self.rendering_material.Orientation

    @orientation.setter
    def orientation(self, value: float):
        self.rendering_material.Orientation = value

    @property
    def position_u(self) -> float:
        return self.rendering_material.PositionU

    @position_u.setter
    def position_u(self, value: float):
        self.rendering_material.PositionU = value

    @property
    def position_v(self) -> float:
        return self.rendering_material.PositionV

    @position_v.setter
    def position_v(self, value: float):
        self.rendering_material.PositionV = value

    @property
    def preview_size(self) -> float:
        return self.rendering_material.PreviewSize

    @preview_size.setter
    def preview_size(self, value: float):
        self.rendering_material.PreviewSize = value

    @property
    def reflection_height(self) -> float:
        return self.rendering_material.ReflectionHeight

    @reflection_height.setter
    def reflection_height(self, value: float):
        self.rendering_material.ReflectionHeight = value

    @property
    def reflection_length(self) -> float:
        return self.rendering_material.ReflectionLength

    @reflection_length.setter
    def reflection_length(self, value: float):
        self.rendering_material.ReflectionLength = value

    @property
    def reflection_mode(self) -> int:
        return self.rendering_material.ReflectionMode

    @reflection_mode.setter
    def reflection_mode(self, value: int):
        self.rendering_material.ReflectionMode = value

    @property
    def reflectivity_coefficient(self) -> float:
        return self.rendering_material.ReflectivityCoefficient

    @reflectivity_coefficient.setter
    def reflectivity_coefficient(self, value: float):
        self.rendering_material.ReflectivityCoefficient = value

    @property
    def refraction_coefficient(self) -> float:
        return self.rendering_material.RefractionCoefficient

    @refraction_coefficient.setter
    def refraction_coefficient(self, value: float):
        self.rendering_material.RefractionCoefficient = value

    @property
    def repeat_u(self) -> bool:
        return self.rendering_material.RepeatU

    @repeat_u.setter
    def repeat_u(self, value: bool):
        self.rendering_material.RepeatU = value

    @property
    def repeat_v(self) -> bool:
        return self.rendering_material.RepeatV

    @repeat_v.setter
    def repeat_v(self, value: bool):
        self.rendering_material.RepeatV = value

    @property
    def scale_u(self) -> float:
        return self.rendering_material.ScaleU

    @scale_u.setter
    def scale_u(self, value: float):
        self.rendering_material.ScaleU = value

    @property
    def scale_v(self) -> float:
        return self.rendering_material.ScaleV

    @scale_v.setter
    def scale_v(self, value: float):
        self.rendering_material.ScaleV = value

    @property
    def specular_coefficient(self) -> float:
        return self.rendering_material.SpecularCoefficient

    @specular_coefficient.setter
    def specular_coefficient(self, value: float):
        self.rendering_material.SpecularCoefficient = value

    @property
    def specular_exponent(self) -> float:
        return self.rendering_material.SpecularExponent

    @specular_exponent.setter
    def specular_exponent(self, value: float):
        self.rendering_material.SpecularExponent = value

    @property
    def texture_amplitude(self) -> float:
        return self.rendering_material.TextureAmplitude

    @texture_amplitude.setter
    def texture_amplitude(self, value: float):
        self.rendering_material.TextureAmplitude = value

    @property
    def texture_complexity(self) -> int:
        return self.rendering_material.TextureComplexity

    @texture_complexity.setter
    def texture_complexity(self, value: int):
        self.rendering_material.TextureComplexity = value

    @property
    def texture_gain(self) -> float:
        return self.rendering_material.TextureGain

    @texture_gain.setter
    def texture_gain(self, value: float):
        self.rendering_material.TextureGain = value

    @property
    def texture_image(self) -> str:
        return self.rendering_material.TextureImage

    @texture_image.setter
    def texture_image(self, value: str):
        self.rendering_material.TextureImage = value

    @property
    def texture_perturbation(self) -> float:
        return self.rendering_material.TexturePerturbation

    @texture_perturbation.setter
    def texture_perturbation(self, value: float):
        self.rendering_material.TexturePerturbation = value

    @property
    def texture_turbulence(self) -> bool:
        return self.rendering_material.TextureTurbulence

    @texture_turbulence.setter
    def texture_turbulence(self, value: bool):
        self.rendering_material.TextureTurbulence = value

    @property
    def texture_type(self) -> int:
        return self.rendering_material.TextureType

    @texture_type.setter
    def texture_type(self, value: int):
        self.rendering_material.TextureType = value

    @property
    def texture_vein_amplitude(self) -> float:
        return self.rendering_material.TextureVeinAmplitude

    @texture_vein_amplitude.setter
    def texture_vein_amplitude(self, value: float):
        self.rendering_material.TextureVeinAmplitude = value

    @property
    def transparency_coefficient(self) -> float:
        return self.rendering_material.TransparencyCoefficient

    @transparency_coefficient.setter
    def transparency_coefficient(self, value: float):
        self.rendering_material.TransparencyCoefficient = value

    def get3_d_texture_color(
        self, i_color_index: int, o3_d_texture_color: tuple
    ) -> None:
        return self.rendering_material.Get3DTextureColor(
            i_color_index, o3_d_texture_color
        )

    def get3_d_texture_color_coefficient(
        self, i_color_index: int, o3_d_texture_color_coefficient: float
    ) -> None:
        return self.rendering_material.Get3DTextureColorCoefficient(
            i_color_index, o3_d_texture_color_coefficient
        )

    def get3_d_texture_orientation(self, o3_d_texture_orientation: tuple) -> None:
        return self.rendering_material.Get3DTextureOrientation(o3_d_texture_orientation)

    def get3_d_texture_position(self, o3_d_texture_position: tuple) -> None:
        return self.rendering_material.Get3DTexturePosition(o3_d_texture_position)

    def get3_d_texture_scale(self, o3_d_texture_scale: tuple) -> None:
        return self.rendering_material.Get3DTextureScale(o3_d_texture_scale)

    def get_ambient_color(self, o_ambient_color: tuple) -> None:
        return self.rendering_material.GetAmbientColor(o_ambient_color)

    def get_diffuse_color(self, o_diffuse_color: tuple) -> None:
        return self.rendering_material.GetDiffuseColor(o_diffuse_color)

    def get_specular_color(self, o_specular_color: tuple) -> None:
        return self.rendering_material.GetSpecularColor(o_specular_color)

    def get_transparency_color(self, o_transparency_color: tuple) -> None:
        return self.rendering_material.GetTransparencyColor(o_transparency_color)

    def put3_d_texture_color(
        self, i_color_index: int, i3_d_texture_color: tuple
    ) -> None:
        return self.rendering_material.Put3DTextureColor(
            i_color_index, i3_d_texture_color
        )

    def put3_d_texture_color_coefficient(
        self, i_color_index: int, i3_d_texture_color_coefficient: float
    ) -> None:
        return self.rendering_material.Put3DTextureColorCoefficient(
            i_color_index, i3_d_texture_color_coefficient
        )

    def put3_d_texture_orientation(self, i3_d_texture_orientation: tuple) -> None:
        return self.rendering_material.Put3DTextureOrientation(i3_d_texture_orientation)

    def put3_d_texture_position(self, i3_d_texture_position: tuple) -> None:
        return self.rendering_material.Put3DTexturePosition(i3_d_texture_position)

    def put3_d_texture_scale(self, i3_d_texture_scale: tuple) -> None:
        return self.rendering_material.Put3DTextureScale(i3_d_texture_scale)

    def put_ambient_color(self, i_ambient_color: tuple) -> None:
        return self.rendering_material.PutAmbientColor(i_ambient_color)

    def put_diffuse_color(self, i_diffuse_color: tuple) -> None:
        return self.rendering_material.PutDiffuseColor(i_diffuse_color)

    def put_specular_color(self, i_specular_color: tuple) -> None:
        return self.rendering_material.PutSpecularColor(i_specular_color)

    def put_transparency_color(self, i_transparency_color: tuple) -> None:
        return self.rendering_material.PutTransparencyColor(i_transparency_color)

    def __repr__(self):
        return f'RenderingMaterial(name="{ self.name }")'
