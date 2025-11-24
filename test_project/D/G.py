b='binary'
a='string'
Y='format'
X='type'
U='UploadFile'
T=ValueError
S=bytes
P=bool
O=isinstance
N=int
M=str
I=classmethod
from typing import Any as A,BinaryIO as c,Callable as Q,Dict,Optional as K,Type as L,TypeVar as f,cast
from annotated_doc import Doc as B
from D.B import j,m
from F.I import D
from F.I import G
from typing_extensions import Annotated as C
class R(G):
	file:C[c,B('The standard Python file object (non-async).')];filename:C[K[M],B('The original file name.')];size:C[K[N],B('The size of the file in bytes.')];headers:C[D,B('The headers of the request.')];content_type:C[K[M],B('The content type of the request, from the headers.')]
	async def write(A,data:C[S,B('\n                The bytes to write to the file.\n                ')]):return await super().write(data)
	async def read(A,size:C[N,B('\n                The number of bytes to read from the file.\n                ')]=-1):return await super().read(size)
	async def seek(A,offset:C[N,B('\n                The position in bytes to seek to in the file.\n                ')]):return await super().seek(offset)
	async def close(A):return await super().close()
	@I
	def __get_validators__(cls:L[U]):yield cls.validate
	@I
	def validate(cls:L[U],v:A):
		if not O(v,G):raise T(f"Expected UploadFile, received: {type(v)}")
		return v
	@I
	def _validate(cls,__input_value:A,_:A):
		A=__input_value
		if not O(A,G):raise T(f"Expected UploadFile, received: {type(A)}")
		return A
	@I
	def __modify_schema__(cls,field_schema:Dict[M,A]):field_schema.update({X:a,Y:b})
	@I
	def __get_pydantic_json_schema__(cls,core_schema:j,handler:m):return{X:a,Y:b}
	@I
	def __get_pydantic_core_schema__(cls,source:L[A],handler:Q[[A],j]):from.B.F import k;return k(cls._validate)
class J:
	def __init__(A,value:A):A.value=value
	def __bool__(A):return P(A.value)
	def __eq__(A,o:object):return O(o,J)and o.value==A.value
E=f('DefaultType')
def F(value:E):return J(value)