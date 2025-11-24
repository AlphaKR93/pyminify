import math,sys,types
from dataclasses import dataclass
from datetime import tzinfo
from typing import TYPE_CHECKING,Any,Callable,Iterator,Optional,SupportsFloat,SupportsIndex,TypeVar,Union
from typing import Protocol,runtime_checkable
from typing import Annotated,Literal
from types import EllipsisType
KW_ONLY={'kw_only':True}
SLOTS={'slots':True}
__version__='0.7.0'
T=TypeVar('T')
class SupportsGt(Protocol):
	def __gt__(self:T,__other:T):0
class SupportsGe(Protocol):
	def __ge__(self:T,__other:T):0
class SupportsLt(Protocol):
	def __lt__(self:T,__other:T):0
class SupportsLe(Protocol):
	def __le__(self:T,__other:T):0
class SupportsMod(Protocol):
	def __mod__(self:T,__other:T):0
class SupportsDiv(Protocol):
	def __div__(self:T,__other:T):0
class BaseMetadata:__slots__=()
@dataclass(frozen=True,**SLOTS)
class Gt(BaseMetadata):gt:SupportsGt
@dataclass(frozen=True,**SLOTS)
class Ge(BaseMetadata):ge:SupportsGe
@dataclass(frozen=True,**SLOTS)
class Lt(BaseMetadata):lt:SupportsLt
@dataclass(frozen=True,**SLOTS)
class Le(BaseMetadata):le:SupportsLe
@runtime_checkable
class GroupedMetadata(Protocol):
	@property
	def __is_annotated_types_grouped_metadata__(self):return True
	def __iter__(self):0
	__slots__=()
	def __init_subclass__(cls,*args:Any,**kwargs:Any):
		super().__init_subclass__(*args,**kwargs)
		if cls.__iter__ is GroupedMetadata.__iter__:raise TypeError("Can't subclass GroupedMetadata without implementing __iter__")
	def __iter__(self):raise NotImplementedError
@dataclass(frozen=True,**KW_ONLY,**SLOTS)
class Interval(GroupedMetadata):
	gt:Union[SupportsGt,None]=None;ge:Union[SupportsGe,None]=None;lt:Union[SupportsLt,None]=None;le:Union[SupportsLe,None]=None
	def __iter__(self):
		if self.gt is not None:yield Gt(self.gt)
		if self.ge is not None:yield Ge(self.ge)
		if self.lt is not None:yield Lt(self.lt)
		if self.le is not None:yield Le(self.le)
@dataclass(frozen=True,**SLOTS)
class MultipleOf(BaseMetadata):multiple_of:Union[SupportsDiv,SupportsMod]
@dataclass(frozen=True,**SLOTS)
class MinLen(BaseMetadata):min_length:Annotated[int,Ge(0)]
@dataclass(frozen=True,**SLOTS)
class MaxLen(BaseMetadata):max_length:Annotated[int,Ge(0)]
@dataclass(frozen=True,**SLOTS)
class Len(GroupedMetadata):
	min_length:Annotated[int,Ge(0)]=0;max_length:Optional[Annotated[int,Ge(0)]]=None
	def __iter__(self):
		if self.min_length>0:yield MinLen(self.min_length)
		if self.max_length is not None:yield MaxLen(self.max_length)
@dataclass(frozen=True,**SLOTS)
class Timezone(BaseMetadata):tz:Union[str,tzinfo,EllipsisType,None]
@dataclass(frozen=True,**SLOTS)
class Unit(BaseMetadata):unit:str
@dataclass(frozen=True,**SLOTS)
class Predicate(BaseMetadata):
	func:Callable[[Any],bool]
	def __repr__(self):
		if getattr(self.func,'__name__','<lambda>')=='<lambda>':return f"{self.__class__.__name__}({self.func!r})"
		if isinstance(self.func,(types.MethodType,types.BuiltinMethodType))and(namespace:=getattr(self.func.__self__,'__name__',None)):return f"{self.__class__.__name__}({namespace}.{self.func.__name__})"
		if isinstance(self.func,type(str.isascii)):return f"{self.__class__.__name__}({self.func.__qualname__})"
		return f"{self.__class__.__name__}({self.func.__name__})"
@dataclass
class Not:
	func:Callable[[Any],bool]
	def __call__(self,__v:Any):return not self.func(__v)
_StrType=TypeVar('_StrType',bound=str)
LowerCase=Annotated[_StrType,Predicate(str.islower)]
UpperCase=Annotated[_StrType,Predicate(str.isupper)]
IsDigit=Annotated[_StrType,Predicate(str.isdigit)]
IsDigits=IsDigit
IsAscii=Annotated[_StrType,Predicate(str.isascii)]
_NumericType=TypeVar('_NumericType',bound=Union[SupportsFloat,SupportsIndex])
IsFinite=Annotated[_NumericType,Predicate(math.isfinite)]
IsNotFinite=Annotated[_NumericType,Predicate(Not(math.isfinite))]
IsNan=Annotated[_NumericType,Predicate(math.isnan)]
IsNotNan=Annotated[_NumericType,Predicate(Not(math.isnan))]
IsInfinite=Annotated[_NumericType,Predicate(math.isinf)]
IsNotInfinite=Annotated[_NumericType,Predicate(Not(math.isinf))]
try:from typing_extensions import DocInfo,doc
except ImportError:
	@dataclass(frozen=True,**SLOTS)
	class DocInfo:documentation:str
	def doc(documentation:str):return DocInfo(documentation)