'Low-level introspection utilities for [`typing`][] members.\n\nThe provided functions in this module check against both the [`typing`][] and [`typing_extensions`][]\nvariants, if they exists and are different.\n'
import collections.abc,contextlib,re,sys,typing
from textwrap import dedent
from types import GenericAlias
from typing import Any
import typing_extensions
from typing_extensions import LiteralString
_IS_PY310=sys.version_info[:2]==(3,10)
def _compile_identity_check_function(member:LiteralString,function_name:LiteralString):
	'Create a function checking that the function argument is the (unparameterized) typing `member`.\n\n    The function will make sure to check against both the `typing` and `typing_extensions`\n    variants as depending on the Python version, the `typing_extensions` variant might be different.\n    For instance, on Python 3.9:\n\n    ```pycon\n    >>> from typing import Literal as t_Literal\n    >>> from typing_extensions import Literal as te_Literal, get_origin\n\n    >>> t_Literal is te_Literal\n    False\n    >>> get_origin(t_Literal[1])\n    typing.Literal\n    >>> get_origin(te_Literal[1])\n    typing_extensions.Literal\n    ```\n    ';in_typing=hasattr(typing,member);in_typing_extensions=hasattr(typing_extensions,member)
	if in_typing and in_typing_extensions:
		if getattr(typing,member)is getattr(typing_extensions,member):check_code=f"obj is typing.{member}"
		else:check_code=f"obj is typing.{member} or obj is typing_extensions.{member}"
	elif in_typing and not in_typing_extensions:check_code=f"obj is typing.{member}"
	elif not in_typing and in_typing_extensions:check_code=f"obj is typing_extensions.{member}"
	else:check_code='False'
	func_code=dedent(f"\n    def {function_name}(obj: Any, /) -> bool:\n        return {check_code}\n    ");locals_={};globals_={'Any':Any,'typing':typing,'typing_extensions':typing_extensions};exec(func_code,globals_,locals_);return locals_[function_name]
def _compile_isinstance_check_function(member:LiteralString,function_name:LiteralString):
	'Create a function checking that the function is an instance of the typing `member`.\n\n    The function will make sure to check against both the `typing` and `typing_extensions`\n    variants as depending on the Python version, the `typing_extensions` variant might be different.\n    ';in_typing=hasattr(typing,member);in_typing_extensions=hasattr(typing_extensions,member)
	if in_typing and in_typing_extensions:
		if getattr(typing,member)is getattr(typing_extensions,member):check_code=f"isinstance(obj, typing.{member})"
		else:check_code=f"isinstance(obj, (typing.{member}, typing_extensions.{member}))"
	elif in_typing and not in_typing_extensions:check_code=f"isinstance(obj, typing.{member})"
	elif not in_typing and in_typing_extensions:check_code=f"isinstance(obj, typing_extensions.{member})"
	else:check_code='False'
	func_code=dedent(f"\n    def {function_name}(obj: Any, /) -> 'TypeIs[{member}]':\n        return {check_code}\n    ");locals_={};globals_={'Any':Any,'typing':typing,'typing_extensions':typing_extensions};exec(func_code,globals_,locals_);return locals_[function_name]
from types import NoneType
is_annotated=_compile_identity_check_function('Annotated','is_annotated')
is_annotated.__doc__='\nReturn whether the argument is the [`Annotated`][typing.Annotated] [special form][].\n\n```pycon\n>>> is_annotated(Annotated)\nTrue\n>>> is_annotated(Annotated[int, ...])\nFalse\n```\n'
is_any=_compile_identity_check_function('Any','is_any')
is_any.__doc__='\nReturn whether the argument is the [`Any`][typing.Any] [special form][].\n\n```pycon\n>>> is_any(Any)\nTrue\n```\n'
is_classvar=_compile_identity_check_function('ClassVar','is_classvar')
is_classvar.__doc__='\nReturn whether the argument is the [`ClassVar`][typing.ClassVar] [type qualifier][].\n\n```pycon\n>>> is_classvar(ClassVar)\nTrue\n>>> is_classvar(ClassVar[int])\n>>> False\n```\n'
is_concatenate=_compile_identity_check_function('Concatenate','is_concatenate')
is_concatenate.__doc__='\nReturn whether the argument is the [`Concatenate`][typing.Concatenate] [special form][].\n\n```pycon\n>>> is_concatenate(Concatenate)\nTrue\n>>> is_concatenate(Concatenate[int, P])\nFalse\n```\n'
is_final=_compile_identity_check_function('Final','is_final')
is_final.__doc__='\nReturn whether the argument is the [`Final`][typing.Final] [type qualifier][].\n\n```pycon\n>>> is_final(Final)\nTrue\n>>> is_final(Final[int])\nFalse\n```\n'
is_forwardref=_compile_isinstance_check_function('ForwardRef','is_forwardref')
is_forwardref.__doc__="\nReturn whether the argument is an instance of [`ForwardRef`][typing.ForwardRef].\n\n```pycon\n>>> is_forwardref(ForwardRef('T'))\nTrue\n```\n"
is_generic=_compile_identity_check_function('Generic','is_generic')
is_generic.__doc__='\nReturn whether the argument is the [`Generic`][typing.Generic] [special form][].\n\n```pycon\n>>> is_generic(Generic)\nTrue\n>>> is_generic(Generic[T])\nFalse\n```\n'
is_literal=_compile_identity_check_function('Literal','is_literal')
is_literal.__doc__='\nReturn whether the argument is the [`Literal`][typing.Literal] [special form][].\n\n```pycon\n>>> is_literal(Literal)\nTrue\n>>> is_literal(Literal["a"])\nFalse\n```\n'
is_paramspec=_compile_isinstance_check_function('ParamSpec','is_paramspec')
is_paramspec.__doc__="\nReturn whether the argument is an instance of [`ParamSpec`][typing.ParamSpec].\n\n```pycon\n>>> P = ParamSpec('P')\n>>> is_paramspec(P)\nTrue\n```\n"
is_typevar=_compile_isinstance_check_function('TypeVar','is_typevar')
is_typevar.__doc__="\nReturn whether the argument is an instance of [`TypeVar`][typing.TypeVar].\n\n```pycon\n>>> T = TypeVar('T')\n>>> is_typevar(T)\nTrue\n```\n"
is_typevartuple=_compile_isinstance_check_function('TypeVarTuple','is_typevartuple')
is_typevartuple.__doc__="\nReturn whether the argument is an instance of [`TypeVarTuple`][typing.TypeVarTuple].\n\n```pycon\n>>> Ts = TypeVarTuple('Ts')\n>>> is_typevartuple(Ts)\nTrue\n```\n"
is_union=_compile_identity_check_function('Union','is_union')
is_union.__doc__='\nReturn whether the argument is the [`Union`][typing.Union] [special form][].\n\nThis function can also be used to check for the [`Optional`][typing.Optional] [special form][],\nas at runtime, `Optional[int]` is equivalent to `Union[int, None]`.\n\n```pycon\n>>> is_union(Union)\nTrue\n>>> is_union(Union[int, str])\nFalse\n```\n\n!!! warning\n    This does not check for unions using the [new syntax][types-union] (e.g. `int | str`).\n'
def is_namedtuple(obj:Any):"Return whether the argument is a named tuple type.\n\n    This includes [`NamedTuple`][typing.NamedTuple] subclasses and classes created from the\n    [`collections.namedtuple`][] factory function.\n\n    ```pycon\n    >>> class User(NamedTuple):\n    ...     name: str\n    ...\n    >>> is_namedtuple(User)\n    True\n    >>> City = collections.namedtuple('City', [])\n    >>> is_namedtuple(City)\n    True\n    >>> is_namedtuple(NamedTuple)\n    False\n    ```\n    ";return isinstance(obj,type)and issubclass(obj,tuple)and hasattr(obj,'_fields')
is_literalstring=_compile_identity_check_function('LiteralString','is_literalstring')
is_literalstring.__doc__='\nReturn whether the argument is the [`LiteralString`][typing.LiteralString] [special form][].\n\n```pycon\n>>> is_literalstring(LiteralString)\nTrue\n```\n'
is_never=_compile_identity_check_function('Never','is_never')
is_never.__doc__='\nReturn whether the argument is the [`Never`][typing.Never] [special form][].\n\n```pycon\n>>> is_never(Never)\nTrue\n```\n'
is_newtype=_compile_isinstance_check_function('NewType','is_newtype')
is_newtype.__doc__='\nReturn whether the argument is a [`NewType`][typing.NewType].\n\n```pycon\n>>> UserId = NewType("UserId", int)\n>>> is_newtype(UserId)\nTrue\n```\n'
is_nodefault=_compile_identity_check_function('NoDefault','is_nodefault')
is_nodefault.__doc__='\nReturn whether the argument is the [`NoDefault`][typing.NoDefault] sentinel object.\n\n```pycon\n>>> is_nodefault(NoDefault)\nTrue\n```\n'
is_noextraitems=_compile_identity_check_function('NoExtraItems','is_noextraitems')
is_noextraitems.__doc__='\nReturn whether the argument is the `NoExtraItems` sentinel object.\n\n```pycon\n>>> is_noextraitems(NoExtraItems)\nTrue\n```\n'
is_noreturn=_compile_identity_check_function('NoReturn','is_noreturn')
is_noreturn.__doc__='\nReturn whether the argument is the [`NoReturn`][typing.NoReturn] [special form][].\n\n```pycon\n>>> is_noreturn(NoReturn)\nTrue\n>>> is_noreturn(Never)\nFalse\n```\n'
is_notrequired=_compile_identity_check_function('NotRequired','is_notrequired')
is_notrequired.__doc__='\nReturn whether the argument is the [`NotRequired`][typing.NotRequired] [special form][].\n\n```pycon\n>>> is_notrequired(NotRequired)\nTrue\n```\n'
is_paramspecargs=_compile_isinstance_check_function('ParamSpecArgs','is_paramspecargs')
is_paramspecargs.__doc__="\nReturn whether the argument is an instance of [`ParamSpecArgs`][typing.ParamSpecArgs].\n\n```pycon\n>>> P = ParamSpec('P')\n>>> is_paramspecargs(P.args)\nTrue\n```\n"
is_paramspeckwargs=_compile_isinstance_check_function('ParamSpecKwargs','is_paramspeckwargs')
is_paramspeckwargs.__doc__="\nReturn whether the argument is an instance of [`ParamSpecKwargs`][typing.ParamSpecKwargs].\n\n```pycon\n>>> P = ParamSpec('P')\n>>> is_paramspeckwargs(P.kwargs)\nTrue\n```\n"
is_readonly=_compile_identity_check_function('ReadOnly','is_readonly')
is_readonly.__doc__='\nReturn whether the argument is the [`ReadOnly`][typing.ReadOnly] [special form][].\n\n```pycon\n>>> is_readonly(ReadOnly)\nTrue\n```\n'
is_required=_compile_identity_check_function('Required','is_required')
is_required.__doc__='\nReturn whether the argument is the [`Required`][typing.Required] [special form][].\n\n```pycon\n>>> is_required(Required)\nTrue\n```\n'
is_self=_compile_identity_check_function('Self','is_self')
is_self.__doc__='\nReturn whether the argument is the [`Self`][typing.Self] [special form][].\n\n```pycon\n>>> is_self(Self)\nTrue\n```\n'
is_typealias=_compile_identity_check_function('TypeAlias','is_typealias')
is_typealias.__doc__='\nReturn whether the argument is the [`TypeAlias`][typing.TypeAlias] [special form][].\n\n```pycon\n>>> is_typealias(TypeAlias)\nTrue\n```\n'
is_typeguard=_compile_identity_check_function('TypeGuard','is_typeguard')
is_typeguard.__doc__='\nReturn whether the argument is the [`TypeGuard`][typing.TypeGuard] [special form][].\n\n```pycon\n>>> is_typeguard(TypeGuard)\nTrue\n```\n'
is_typeis=_compile_identity_check_function('TypeIs','is_typeis')
is_typeis.__doc__='\nReturn whether the argument is the [`TypeIs`][typing.TypeIs] [special form][].\n\n```pycon\n>>> is_typeis(TypeIs)\nTrue\n```\n'
_is_typealiastype_inner=_compile_isinstance_check_function('TypeAliasType','_is_typealiastype_inner')
if _IS_PY310:
	def is_typealiastype(obj:Any):return type(obj)is not GenericAlias and _is_typealiastype_inner(obj)
else:is_typealiastype=_compile_isinstance_check_function('TypeAliasType','is_typealiastype')
is_typealiastype.__doc__='\nReturn whether the argument is a [`TypeAliasType`][typing.TypeAliasType] instance.\n\n```pycon\n>>> type MyInt = int\n>>> is_typealiastype(MyInt)\nTrue\n>>> MyStr = TypeAliasType("MyStr", str)\n>>> is_typealiastype(MyStr):\nTrue\n>>> type MyList[T] = list[T]\n>>> is_typealiastype(MyList[int])\nFalse\n```\n'
is_unpack=_compile_identity_check_function('Unpack','is_unpack')
is_unpack.__doc__='\nReturn whether the argument is the [`Unpack`][typing.Unpack] [special form][].\n\n```pycon\n>>> is_unpack(Unpack)\nTrue\n>>> is_unpack(Unpack[Ts])\nFalse\n```\n'
def is_deprecated(obj:Any):return isinstance(obj,typing_extensions.deprecated)
is_deprecated.__doc__="\nReturn whether the argument is a [`deprecated`][warnings.deprecated] instance.\n\nThis also includes the [`typing_extensions` backport][typing_extensions.deprecated].\n\n```pycon\n>>> is_deprecated(warnings.deprecated('message'))\nTrue\n>>> is_deprecated(typing_extensions.deprecated('message'))\nTrue\n```\n"
DEPRECATED_ALIASES={typing.Hashable:collections.abc.Hashable,typing.Awaitable:collections.abc.Awaitable,typing.Coroutine:collections.abc.Coroutine,typing.AsyncIterable:collections.abc.AsyncIterable,typing.AsyncIterator:collections.abc.AsyncIterator,typing.Iterable:collections.abc.Iterable,typing.Iterator:collections.abc.Iterator,typing.Reversible:collections.abc.Reversible,typing.Sized:collections.abc.Sized,typing.Container:collections.abc.Container,typing.Collection:collections.abc.Collection,typing.Callable:collections.abc.Callable,typing.AbstractSet:collections.abc.Set,typing.MutableSet:collections.abc.MutableSet,typing.Mapping:collections.abc.Mapping,typing.MutableMapping:collections.abc.MutableMapping,typing.Sequence:collections.abc.Sequence,typing.MutableSequence:collections.abc.MutableSequence,typing.Tuple:tuple,typing.List:list,typing.Deque:collections.deque,typing.Set:set,typing.FrozenSet:frozenset,typing.MappingView:collections.abc.MappingView,typing.KeysView:collections.abc.KeysView,typing.ItemsView:collections.abc.ItemsView,typing.ValuesView:collections.abc.ValuesView,typing.Dict:dict,typing.DefaultDict:collections.defaultdict,typing.OrderedDict:collections.OrderedDict,typing.Counter:collections.Counter,typing.ChainMap:collections.ChainMap,typing.Generator:collections.abc.Generator,typing.AsyncGenerator:collections.abc.AsyncGenerator,typing.Type:type,typing.Pattern:re.Pattern,typing.Match:re.Match,typing.ContextManager:contextlib.AbstractContextManager,typing.AsyncContextManager:contextlib.AbstractAsyncContextManager}
'A mapping between the deprecated typing aliases to their replacement, as per [PEP 585](https://peps.python.org/pep-0585/).'
for(alias,target)in list(DEPRECATED_ALIASES.items()):
	if(te_alias:=getattr(typing_extensions,alias._name,None))is not None:DEPRECATED_ALIASES[te_alias]=target