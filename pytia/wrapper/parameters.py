"""
    Wrapper module CATIA parameters.
"""
import functools
from typing import Any
from typing import List
from typing import Optional
from typing import Type

from pycatia.knowledge_interfaces.bool_param import BoolParam
from pycatia.knowledge_interfaces.dimension import Dimension
from pycatia.knowledge_interfaces.int_param import IntParam
from pycatia.knowledge_interfaces.parameter import Parameter
from pycatia.knowledge_interfaces.parameters import Parameters
from pycatia.knowledge_interfaces.real_param import RealParam
from pycatia.knowledge_interfaces.str_param import StrParam
from pycatia.mec_mod_interfaces.part import Part

from pytia.exceptions import PytiaParameterExistsError
from pytia.exceptions import PytiaParameterNotFoundError
from pytia.exceptions import PytiaParameterTypeError
from pytia.log import log

LENGTH = "LENGTH"
ANGLE = "ANGLE"
UNIT = {LENGTH: "mm", ANGLE: "deg"}


class PyPartParameters:
    """The wrapper class for CATIA Parameters and Dimensions (KnowledgeInterfaces Framework)"""

    def __init__(self, part: Part) -> None:
        """
        Inits the wrapper class for CATIA parameters.

        Args:
            part (Part): The part which contains the parameters.
        """
        self._part = part
        self._parameters = self._part.parameters

    def __call__(self) -> Parameters:
        return self._parameters

    def __repr__(self) -> str:
        return f"PyPartParameters({self._part.name})"

    @property
    def parameters(
        self,
    ) -> List[BoolParam | IntParam | RealParam | StrParam | Dimension]:
        """Returns a list of all parameters."""
        output = []
        for i in range(1, self._parameters.count + 1):
            output.append(self._parameters.item(i))
        return output

    @property
    def names(self) -> List[str]:
        """Returns a list all parameter names."""
        output = []
        for i in range(1, self._parameters.count + 1):
            output.append(self._parameters.item(i).name)
        return output

    @staticmethod
    def _unique(func):
        """Makes sure that no parameters with the same name are created."""

        @functools.wraps(func)
        def _unique_wrapper(self, name, *args, **kwargs):
            if self.exists(name=name):
                # We have to raise an exception when a parameter name matches any existing one.
                # The problem is, that CATIA doesn't warn the user when two parameters have the
                # same local name, instead the latter one will get a number as postfix, e.g.:
                #   First parameter local name: foo
                #   Second parameter local name: foo.1
                # Bad thing: We have no way of getting that postfixed local name, so when this
                # happens and we access the parameter by name (foo) later, we won't ever know which
                # parameter we get.
                raise PytiaParameterExistsError(
                    f"Failed creating parameter {name!r}: Already exists in {self._part.name!r}"
                )
            return func(self, name, *args, **kwargs)

        return _unique_wrapper

    def exists(self, name: str) -> bool:
        """
        Returns wether a parameter of the given name already exists in the part, or not.

        Args:
            name (str): The name of the parameter to check.

        Raises:
            AttributeError: Raised when the win32com client can't match the items value.

        Returns:
            bool: True if the parameter exists, otherwise False.
        """
        for i in range(1, self._parameters.count + 1):
            try:
                log.debug(
                    f"Checking parameter at index {i}: {self._parameters.item(i)}"
                )
                if self._parameters.item(i).name == name:
                    return True
            except AttributeError as e:
                log.exception(f"Attribute error from parameter index {i}: {e}")
        return False

    def get(
        self,
        name: str,
        of_type: Optional[Type[bool] | Type[int] | Type[float] | Type[str]] = None,
    ) -> BoolParam | IntParam | RealParam | StrParam | Dimension:
        """
        Returns a parameter with the given name.

        Args:
            name (str): The name of the parameter to retrieve.
            of_type (Optional[Type[bool]  |  Type[int]  |  Type[float]  |  Type[str]], optional): \
                The type of the parameter. Defaults to None. If None, no type checking will be used.

        Raises:
            PytiaParameterTypeError: Raised when the type of the parameter does not match.
            PytiaParameterNotFoundError: Raised when the parameter does not exist.

        Returns:
            BoolParam | IntParam | RealParam | StrParam | Dimension: _description_
        """
        if self.exists(name=name):
            native_value = self._parameters.item(name).value  # type: ignore
            parameter = Parameter(self._parameters.item(name).com_object).com_object

            # Return the parameter with its type
            if self.is_bool(parameter) and of_type in [bool, None]:
                log.debug(f"Parameter {name!r} is of type BoolParam.")
                return BoolParam(parameter)
            if self.is_int(parameter) and of_type in [int, None]:
                log.debug(f"Parameter {name!r} is of type IntParam.")
                return IntParam(parameter)
            if self.is_real(parameter) and of_type in [float, None]:
                log.debug(f"Parameter {name!r} is of type RealParam.")
                return RealParam(parameter)
            if self.is_dimension(parameter) and of_type in [float, None]:
                log.debug(f"Parameter {name!r} is of type Dimension.")
                return Dimension(parameter)
            if self.is_str(parameter) and of_type in [str, None]:
                log.debug(f"Parameter {name!r} is of type StrParam.")
                return StrParam(parameter)
            raise PytiaParameterTypeError(
                f"Parameter {name!r} has invalid type {type(native_value)!r}"
            )
        raise PytiaParameterNotFoundError(
            f"Parameter {name!r} not found in {self._part.name!r}"
        )

    @_unique
    def create_length(self, name: str, value: float) -> Dimension:
        """
        Creates a CATIA LENGTH parameter in millimeter with the given name and value.

        Args:
            name (str): The name of the length parameter.
            value (float): The value of the length parameter.

        Raises:
            PytiaParameterExistsError: Raised when a parameter with the given name already exists.

        Returns:
            Dimension: The length parameter as Dimension.
        """
        return self._create_dimension(name=name, value=value, param_type=LENGTH)

    @_unique
    def create_angle(self, name: str, value: float) -> Dimension:
        """
        Creates a CATIA ANGLE parameter in degrees with the given name and value.

        Args:
            name (str): The name of the angle parameter.
            value (float): The value of the angle parameter.

        Raises:
            PytiaParameterExistsError: Raised when a parameter with the given name already exists.

        Returns:
            Dimension: The angle parameter as Dimension.
        """
        return self._create_dimension(name=name, value=value, param_type=ANGLE)

    @_unique
    def create_bool(self, name: str, value: bool) -> BoolParam:
        """
        Creates a CATIA boolean parameter.

        Args:
            name (str): The name of the boolean parameter.
            value (float): The value of the boolean parameter.

        Raises:
            PytiaParameterExistsError: Raised when a parameter with the given name already exists.

        Returns:
            BoolParam: The boolean parameter.
        """
        parameter = self._parameters.create_boolean(name, value)
        parameter.rename(name)
        log.info(
            f"Created parameter {name!r} ({value}, BOOLEAN) in {self._part.name!r}"
        )
        return parameter

    @_unique
    def create_int(self, name: str, value: int) -> IntParam:
        """
        Creates a CATIA integer parameter.

        Args:
            name (str): The name of the integer parameter.
            value (float): The value of the integer parameter.

        Raises:
            PytiaParameterExistsError: Raised when a parameter with the given name already exists.

        Returns:
            IntParam: The integer parameter.
        """
        parameter = self._parameters.create_integer(name, value)
        parameter.rename(name)
        log.info(
            f"Created parameter {name!r} ({value}, INTEGER) in {self._part.name!r}"
        )
        return parameter

    @_unique
    def create_real(self, name: str, value: float) -> RealParam:
        """
        Creates a CATIA real parameter.

        Args:
            name (str): The name of the real parameter.
            value (float): The value of the real parameter.

        Raises:
            PytiaParameterExistsError: Raised when a parameter with the given name already exists.

        Returns:
            RealParam: The real parameter.
        """
        parameter = self._parameters.create_real(name, value)
        parameter.rename(name)
        log.info(f"Created parameter {name!r} ({value}, REAL) in {self._part.name!r}")
        return parameter

    @_unique
    def create_string(self, name: str, value: str) -> StrParam:
        """
        Creates a CATIA string parameter.

        Args:
            name (str): The name of the string parameter.
            value (float): The value of the string parameter.

        Raises:
            PytiaParameterExistsError: Raised when a parameter with the given name already exists.

        Returns:
            StrParam: The string parameter.
        """
        parameter = self._parameters.create_string(name, value)
        parameter.rename(name)
        log.info(f"Created parameter {name!r} ({value}, STRING) in {self._part.name!r}")
        return parameter

    @_unique
    def _create_dimension(self, name: str, value: Any, param_type: str) -> Dimension:
        """
        Creates a dimension parameter.

        Args:
            name (str): The name of the dimension parameter.
            value (Any): The value of the dimension parameter.
            param_type (str): The type of the dimension parameter (LENGTH or ANGLE).

        Raises:
            PytiaParameterExistsError: Raised when a parameter with the given name already exists.

        Returns:
            Dimension: The newly created dimension.
        """
        dimension = self._parameters.create_dimension(name, param_type, 0)
        dimension.rename(name)
        dimension.valuate_from_string(f"{value}{UNIT[param_type]}")
        # Use Parameter.Rename to set the Name.
        # This only applies to the name, the local name is set when creating the
        # parameter and cannot be changed later.
        log.info(
            f"Created dimension {name!r} ({value!r}, {param_type}, {UNIT[param_type]}) in {self._part.name!r}"
        )
        return dimension

    @staticmethod
    def is_dimension(parameter: Parameter) -> bool:
        """
        Returns True if the given parameter is of type Dimension.

        Args:
            parameter (Parameter): The parameter to check.

        Returns:
            bool: True if the given parameter is of type Dimension.
        """
        try:
            # Parameters of type Dimension and Real are both floats.
            # But only the Dimension parameter has a unit property.
            # To determine if we have a Dimension or a Real we try
            # to get the unit property. If it succeeds it's a Dimension.
            # pylint: disable=W0104
            parameter.unit.name  # type: ignore
            # pylint: enable=W0104
            return True
        except:  # pylint: disable=W0702
            return False

    @staticmethod
    def is_bool(parameter: Parameter) -> bool:
        """
        Returns True if the given parameter is of type BoolParam.

        Args:
            parameter (Parameter): The parameter to check.

        Returns:
            bool: True if the given parameter is of type BoolParam.
        """
        return isinstance(parameter.value, bool)  # type: ignore

    @staticmethod
    def is_int(parameter: Parameter) -> bool:
        """
        Returns True if the given parameter is of type IntParam.

        Args:
            parameter (Parameter): The parameter to check.

        Returns:
            bool: True if the given parameter is of type IntParam.
        """
        return isinstance(parameter.value, int)  # type: ignore

    @staticmethod
    def is_real(parameter: Parameter) -> bool:
        """
        Returns True if the given parameter is of type RealParam.

        Args:
            parameter (Parameter): The parameter to check.

        Returns:
            bool: True if the given parameter is of type RealParam.
        """
        try:
            # Parameters of type Dimension and Real are both floats.
            # But only the Dimension parameter has a unit property.
            # To determine if we have a Dimension or a Real we try
            # to get the unit property. If it fails it's a Real.
            # pylint: disable=W0104
            parameter.unit.name  # type: ignore
            # pylint: enable=W0104
            return False
        except:  # pylint: disable=W0702
            return isinstance(parameter.value, float)  # type: ignore

    @staticmethod
    def is_str(parameter: Parameter) -> bool:
        """
        Returns True if the given parameter is of type StrParam.

        Args:
            parameter (Parameter): The parameter to check.

        Returns:
            bool: True if the given parameter is of type StrParam.
        """
        return isinstance(parameter.value, str)  # type: ignore
