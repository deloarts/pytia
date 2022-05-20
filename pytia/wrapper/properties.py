"""
    Wrapper module for CATIA properties.
"""

import functools
from typing import List

from pytia import __version__
from pytia.const import ENV_NO_PROPS, PROP_VERSION
from pytia.exceptions import PytiaPropertyExistsError, PytiaPropertyNotFoundError
from pytia.framework.knowledge_interfaces.parameters import Parameters
from pytia.framework.knowledge_interfaces.str_param import StrParam
from pytia.framework.product_structure_interfaces.product import Product
from pytia.log import log


class PyProperties:
    """The wrapper class for CATIA UserRefProperties. (ProductStructureInterfaces Framework)"""

    def __init__(self, product: Product) -> None:
        self._product = product
        self._user_ref_properties = self._product.user_ref_properties
        self.write_version()

    def __call__(self) -> Parameters:
        return self._user_ref_properties

    def __repr__(self) -> str:
        return f"PyProperties({self._product.name})"

    @property
    def properties(
        self,
    ) -> List[StrParam]:
        """Returns a list of all properties."""
        output = []
        for i in range(1, self._user_ref_properties.count + 1):
            output.append(self._user_ref_properties.item(i))
        return output

    @property
    def names(self) -> List[str]:
        """Returns a list all UserRefProperties names."""
        output = []
        for i in range(1, self._user_ref_properties.count + 1):
            output.append(self._user_ref_properties.item(i).name)
        return output

    @staticmethod
    def _unique(func):
        """
        Decorator that makes sure that no properties with the same name are created.

        Raises the PytiaPropertyExistsError if a property with the given name argument
        already exists.
        """

        @functools.wraps(func)
        def _unique_wrapper(self, name, *args, **kwargs):
            if self.exists(name=name):
                raise PytiaPropertyExistsError(
                    f"Failed creating property {name!r}: Already exists in {self._product.name!r}"
                )
            return func(self, name, *args, **kwargs)

        return _unique_wrapper

    def exists(self, name: str | List[str]) -> bool:
        """
        Returns True if a property of the given name already exists in the product.

        Returns True if all properties of the given list exists in the product.
        """

        def name_exists(name):
            for i in range(1, self._user_ref_properties.count + 1):
                if self._user_ref_properties.item(i).name == name:
                    return True
            return False

        if isinstance(name, str):
            return name_exists(name)

        return all(name_exists(n) for n in name)

    def get_by_name(self, name: str) -> StrParam:
        """
        Returns a UserRefProperty by its name.

        Raises the PytiaPropertyNotFound exception if the property does not exist.
        """
        if self.exists(name=name):
            return StrParam(self._user_ref_properties.item(name))

        raise PytiaPropertyNotFoundError(
            f"Property {name!r} not found in {self._product.name!r}"
        )

    def set_value(self, name: str, value: str) -> None:
        """
        Sets the value of an user ref property.

        Raises the PytiaPropertyNotFound exception if the property does not exist.
        """
        prop = self.get_by_name(name)
        prop.value = value

    @_unique
    def create(self, name: str, value: str = "") -> StrParam:
        """
        Creates a CATIA UserRefProperty of type STRING.

        Raises the PytiaPropertyExistsError if the property already exists.
        """
        parameter = self._user_ref_properties.create_string(name, value)
        parameter.rename(name)
        log.info(
            f"Created property {name!r} ({value}, STRING) in {self._product.name!r}"
        )
        return parameter

    def create_multi(
        self, names: List[str], skip_existing: bool = True
    ) -> List[StrParam]:
        """
        Creates all properties from the given list without a value.

        Raises the PytiaPropertyExistsError at least one property already exists, doesn't create
        any Property if the error is raised.

        Doesn't raise an error if skip_existing is True.
        """
        name_list = []
        props = []
        for name in names:
            if self.exists(name):
                if not skip_existing:
                    raise PytiaPropertyExistsError(
                        f"Failed creating property {name!r}: "
                        f"Already exists in {self._product.name!r}"
                    )
            else:
                name_list.append(name)

        for name in name_list:
            props.append(self.create(name=name))

        return props

    def write_version(self) -> None:
        """
        Writes the pytia version as user ref property.

        Omits this if the environment variable PYTIA_NO_PROPS is set to 1.
        """
        if ENV_NO_PROPS:
            log.info(
                f"Omitting creation of property {PROP_VERSION!r}:"
                f"{ENV_NO_PROPS!r} environment variable is set."
            )
        else:
            if self.exists(name=PROP_VERSION):
                self.set_value(name=PROP_VERSION, value=__version__)
            else:
                self.create(name=PROP_VERSION, value=__version__)
