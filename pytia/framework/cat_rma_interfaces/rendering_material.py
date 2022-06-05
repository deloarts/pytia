from pytia.exceptions import PytiaApplicationError
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
        min_coeff = 1
        max_coeff = 8
        if not min_coeff <= value <= max_coeff:
            raise PytiaApplicationError(
                f"Adaptive coefficient must be between {min_coeff} and {max_coeff}, "
                f"but is {value}."
            )
        self.rendering_material.AdaptiveCoeff = value

    @property
    def ambient_coefficient(self) -> float:
        return self.rendering_material.AmbientCoefficient

    @ambient_coefficient.setter
    def ambient_coefficient(self, value: float):
        min_coeff = 0
        max_coeff = 1
        if not min_coeff <= value <= max_coeff:
            raise PytiaApplicationError(
                f"Ambient coefficient must be between {min_coeff} and {max_coeff}, "
                f"but is {value}."
            )
        self.rendering_material.AmbientCoefficient = value

    @property
    def bump(self) -> float:
        return self.rendering_material.Bump

    @bump.setter
    def bump(self, value: float):
        min_value = -10
        max_value = 10
        if not min_value <= value <= max_value:
            raise PytiaApplicationError(
                f"Bump must be between {min_value} and {max_value}, " f"but is {value}."
            )
        self.rendering_material.Bump = value

    @property
    def chessboard_joint_height(self) -> float:
        return self.rendering_material.ChessboardJointHeight

    @chessboard_joint_height.setter
    def chessboard_joint_height(self, value: float):
        min_height = 0
        max_height = 100
        if not min_height <= value <= max_height:
            raise PytiaApplicationError(
                f"Chessboard joint height must be between {min_height} and {max_height}, "
                f"but is {value}."
            )
        self.rendering_material.ChessboardJointHeight = value

    @property
    def chessboard_joint_width(self) -> float:
        return self.rendering_material.ChessboardJointWidth

    @chessboard_joint_width.setter
    def chessboard_joint_width(self, value: float):
        min_width = 0
        max_width = 100
        if not min_width <= value <= max_width:
            raise PytiaApplicationError(
                f"Chessboard joint width must be between {min_width} and {max_width}, "
                f"but is {value}."
            )
        self.rendering_material.ChessboardJointWidth = value

    @property
    def chessboard_offset(self) -> float:
        return self.rendering_material.ChessboardOffset

    @chessboard_offset.setter
    def chessboard_offset(self, value: float):
        min_offset = 0
        max_offset = 0.5
        if not min_offset <= value <= max_offset:
            raise PytiaApplicationError(
                f"Chessboard offset must be between {min_offset} and {max_offset}, "
                f"but is {value}."
            )
        self.rendering_material.ChessboardOffset = value

    @property
    def chessboard_tile_height(self) -> float:
        return self.rendering_material.ChessboardTileHeight

    @chessboard_tile_height.setter
    def chessboard_tile_height(self, value: float):
        min_height = 0
        max_height = 100
        if not min_height <= value <= max_height:
            raise PytiaApplicationError(
                f"Chessboard tile height must be between {min_height} and {max_height}, "
                f"but is {value}."
            )
        self.rendering_material.ChessboardTileHeight = value

    @property
    def chessboard_tile_width(self) -> float:
        return self.rendering_material.ChessboardTileWidth

    @chessboard_tile_width.setter
    def chessboard_tile_width(self, value: float):
        min_width = 0
        max_width = 100
        if not min_width <= value <= max_width:
            raise PytiaApplicationError(
                f"Chessboard tile width must be between {min_width} and {max_width}, "
                f"but is {value}."
            )
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
        min_coeff = 0
        max_coeff = 1
        if not min_coeff <= value <= max_coeff:
            raise PytiaApplicationError(
                f"Diffuse coefficient must be between {min_coeff} and {max_coeff}, "
                f"but is {value}."
            )
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
        min_mapping = 0
        max_mapping = 5
        if not min_mapping <= value <= max_mapping:
            raise PytiaApplicationError(
                f"Mapping type must be between {min_mapping} and {max_mapping}, "
                f"but is {value}."
            )
        self.rendering_material.MappingType = value

    @property
    def orientation(self) -> float:
        return self.rendering_material.Orientation

    @orientation.setter
    def orientation(self, value: float):
        min_orient = -360
        max_orient = 360
        if not min_orient <= value <= max_orient:
            raise PytiaApplicationError(
                f"Orientation must be between {min_orient} and {max_orient}, "
                f"but is {value}."
            )
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
        min_height = 0
        max_height = 1
        if not min_height <= value <= max_height:
            raise PytiaApplicationError(
                f"Reflection height must be between {min_height} and {max_height}, "
                f"but is {value}."
            )
        self.rendering_material.ReflectionHeight = value

    @property
    def reflection_length(self) -> float:
        return self.rendering_material.ReflectionLength

    @reflection_length.setter
    def reflection_length(self, value: float):
        min_length = 0
        max_length = 1
        if not min_length <= value <= max_length:
            raise PytiaApplicationError(
                f"Reflection length must be between {min_length} and {max_length}, "
                f"but is {value}."
            )
        self.rendering_material.ReflectionLength = value

    @property
    def reflection_mode(self) -> int:
        return self.rendering_material.ReflectionMode

    @reflection_mode.setter
    def reflection_mode(self, value: int):
        min_mode = 0
        max_mode = 4
        if not min_mode <= value <= max_mode:
            raise PytiaApplicationError(
                f"Reflection mode must be between {min_mode} and {max_mode}, "
                f"but is {value}."
            )
        self.rendering_material.ReflectionMode = value

    @property
    def reflectivity_coefficient(self) -> float:
        return self.rendering_material.ReflectivityCoefficient

    @reflectivity_coefficient.setter
    def reflectivity_coefficient(self, value: float):
        min_coeff = 0
        max_coeff = 4
        if not min_coeff <= value <= max_coeff:
            raise PytiaApplicationError(
                f"Reflectivity coefficient must be between {min_coeff} and {max_coeff}, "
                f"but is {value}."
            )
        self.rendering_material.ReflectivityCoefficient = value

    @property
    def refraction_coefficient(self) -> float:
        return self.rendering_material.RefractionCoefficient

    @refraction_coefficient.setter
    def refraction_coefficient(self, value: float):
        min_coeff = 1
        max_coeff = 2
        if not min_coeff <= value <= max_coeff:
            raise PytiaApplicationError(
                f"Refraction coefficient must be between {min_coeff} and {max_coeff}, "
                f"but is {value}."
            )
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
        min_scale = 0
        max_scale = 100
        if not min_scale <= value <= max_scale:
            raise PytiaApplicationError(
                f"Scale U must be between {min_scale} and {max_scale}, "
                f"but is {value}."
            )
        self.rendering_material.ScaleU = value

    @property
    def scale_v(self) -> float:
        return self.rendering_material.ScaleV

    @scale_v.setter
    def scale_v(self, value: float):
        min_scale = 0
        max_scale = 100
        if not min_scale <= value <= max_scale:
            raise PytiaApplicationError(
                f"Scale V must be between {min_scale} and {max_scale}, "
                f"but is {value}."
            )
        self.rendering_material.ScaleV = value

    @property
    def specular_coefficient(self) -> float:
        return self.rendering_material.SpecularCoefficient

    @specular_coefficient.setter
    def specular_coefficient(self, value: float):
        min_coeff = 0
        max_coeff = 1
        if not min_coeff <= value <= max_coeff:
            raise PytiaApplicationError(
                f"Specular coefficient must be between {min_coeff} and {max_coeff}, "
                f"but is {value}."
            )
        self.rendering_material.SpecularCoefficient = value

    @property
    def specular_exponent(self) -> float:
        return self.rendering_material.SpecularExponent

    @specular_exponent.setter
    def specular_exponent(self, value: float):
        min_expo = 0
        max_expo = 1
        if not min_expo <= value <= max_expo:
            raise PytiaApplicationError(
                f"Specular exponent must be between {min_expo} and {max_expo}, "
                f"but is {value}."
            )
        self.rendering_material.SpecularExponent = value

    @property
    def texture_amplitude(self) -> float:
        return self.rendering_material.TextureAmplitude

    @texture_amplitude.setter
    def texture_amplitude(self, value: float):
        min_amp = 0
        max_amp = 1
        if not min_amp <= value <= max_amp:
            raise PytiaApplicationError(
                f"Texture amplitude must be between {min_amp} and {max_amp}, "
                f"but is {value}."
            )
        self.rendering_material.TextureAmplitude = value

    @property
    def texture_complexity(self) -> int:
        return self.rendering_material.TextureComplexity

    @texture_complexity.setter
    def texture_complexity(self, value: int):
        min_cplx = 0
        max_cplx = 10
        if not min_cplx <= value <= max_cplx:
            raise PytiaApplicationError(
                f"Texture complexity must be between {min_cplx} and {max_cplx}, "
                f"but is {value}."
            )
        self.rendering_material.TextureComplexity = value

    @property
    def texture_gain(self) -> float:
        return self.rendering_material.TextureGain

    @texture_gain.setter
    def texture_gain(self, value: float):
        min_gain = 0
        max_gain = 2
        if not min_gain <= value <= max_gain:
            raise PytiaApplicationError(
                f"Texture gain must be between {min_gain} and {max_gain}, "
                f"but is {value}."
            )
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
        min_pet = 0
        max_pet = 10
        if not min_pet <= value <= max_pet:
            raise PytiaApplicationError(
                f"Texture perturbation must be between {min_pet} and {max_pet}, "
                f"but is {value}."
            )
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
        min_type = 0
        max_type = 6
        if not min_type <= value <= max_type:
            raise PytiaApplicationError(
                f"Texture type must be between {min_type} and {max_type}, "
                f"but is {value}."
            )
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
        min_coeff = 0
        max_coeff = 1
        if not min_coeff <= value <= max_coeff:
            raise PytiaApplicationError(
                f"Transparency coefficient must be between {min_coeff} and {max_coeff}, "
                f"but is {value}."
            )
        self.rendering_material.TransparencyCoefficient = value

    def get_3d_texture_color(
        self, i_color_index: int, o_3d_texture_color: tuple
    ) -> None:
        return self.rendering_material.Get3DTextureColor(
            i_color_index, o_3d_texture_color
        )

    def get_3d_texture_color_coefficient(
        self, i_color_index: int, o_3d_texture_color_coefficient: float
    ) -> None:
        return self.rendering_material.Get3DTextureColorCoefficient(
            i_color_index, o_3d_texture_color_coefficient
        )

    def get_3d_texture_orientation(self, o_3d_texture_orientation: tuple) -> None:
        return self.rendering_material.Get3DTextureOrientation(o_3d_texture_orientation)

    def get_3d_texture_position(self, o_3d_texture_position: tuple) -> None:
        return self.rendering_material.Get3DTexturePosition(o_3d_texture_position)

    def get_3d_texture_scale(self, o_3d_texture_scale: tuple) -> None:
        return self.rendering_material.Get3DTextureScale(o_3d_texture_scale)

    def get_ambient_color(self, o_ambient_color: tuple) -> None:
        return self.rendering_material.GetAmbientColor(o_ambient_color)

    def get_diffuse_color(self, o_diffuse_color: tuple) -> None:
        return self.rendering_material.GetDiffuseColor(o_diffuse_color)

    def get_specular_color(self, o_specular_color: tuple) -> None:
        return self.rendering_material.GetSpecularColor(o_specular_color)

    def get_transparency_color(self, o_transparency_color: tuple) -> None:
        return self.rendering_material.GetTransparencyColor(o_transparency_color)

    def put_3d_texture_color(
        self, i_color_index: int, i_3d_texture_color: tuple
    ) -> None:
        return self.rendering_material.Put3DTextureColor(
            i_color_index, i_3d_texture_color
        )

    def put_3d_texture_color_coefficient(
        self, i_color_index: int, i_3d_texture_color_coefficient: float
    ) -> None:
        return self.rendering_material.Put3DTextureColorCoefficient(
            i_color_index, i_3d_texture_color_coefficient
        )

    def put_3d_texture_orientation(self, i_3d_texture_orientation: tuple) -> None:
        return self.rendering_material.Put3DTextureOrientation(i_3d_texture_orientation)

    def put_3d_texture_position(self, i_3d_texture_position: tuple) -> None:
        return self.rendering_material.Put3DTexturePosition(i_3d_texture_position)

    def put_3d_texture_scale(self, i_3d_texture_scale: tuple) -> None:
        return self.rendering_material.Put3DTextureScale(i_3d_texture_scale)

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
