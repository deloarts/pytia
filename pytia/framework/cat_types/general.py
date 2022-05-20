from typing import TypeVar, Type
from pytia.framework.knowledge_interfaces.bool_param import BoolParam
from pytia.framework.knowledge_interfaces.int_param import IntParam
from pytia.framework.knowledge_interfaces.str_param import StrParam
from pytia.framework.knowledge_interfaces.real_param import RealParam

cat_variant = TypeVar("cat_variant", int, str)
list_str = TypeVar("list_str", list, str)
any_parameter = TypeVar("any_parameter", BoolParam, IntParam, StrParam, RealParam)
