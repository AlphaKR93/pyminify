L='json'
K='validation'
H=False
F=None
E=property
C=bool
B=str
from typing import Any as A,Dict as I,Tuple as J,Union as D
from D.Y import x
from pydantic.fields import FieldInfo
from typing_extensions import Literal as G,Protocol as M
class ă(M):
	field_info:FieldInfo;name:B;mode:G[K,'serialization']=K;_version:G['v1','v2']='v1'
	@E
	def alias(self):0
	@E
	def required(self):0
	@E
	def default(self):0
	@E
	def type_(self):0
	def get_default(A):0
	def validate(A,value:A,values:I[B,A]={},*,loc:J[D[int,B],...]=()):0
	def serialize(A,value:A,*,mode:G[L,'python']=L,include:D[x,F]=F,exclude:D[x,F]=F,by_alias:C=True,exclude_unset:C=H,exclude_defaults:C=H,exclude_none:C=H):0