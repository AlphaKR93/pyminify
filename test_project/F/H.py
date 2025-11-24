I=NotImplementedError
C=float
B=int
A=str
import math as H,uuid as D
from typing import Any,ClassVar as J,Generic as K,TypeVar as L
G=L('T')
class E(K[G]):
	regex:J[A]=''
	def convert(A,value:A):raise I
	def to_string(A,value:G):raise I
class M(E[A]):
	regex='[^/]+'
	def convert(A,value:A):return value
	def to_string(C,value:A):B=value;B=A(B);assert'/'not in B,'May not contain path separators';assert B,'Must not be empty';return B
class N(E[A]):
	regex='.*'
	def convert(B,value:A):return A(value)
	def to_string(B,value:A):return A(value)
class O(E[B]):
	regex='[0-9]+'
	def convert(A,value:A):return B(value)
	def to_string(D,value:B):C=value;C=B(C);assert C>=0,'Negative integers are not supported';return A(C)
class P(E[C]):
	regex='[0-9]+(\\.[0-9]+)?'
	def convert(A,value:A):return C(value)
	def to_string(B,value:C):A=value;A=C(A);assert A>=.0,'Negative floats are not supported';assert not H.isnan(A),'NaN values are not supported';assert not H.isinf(A),'Infinite values are not supported';return('%0.20f'%A).rstrip('0').rstrip('.')
class Q(E[D.UUID]):
	regex='[0-9a-fA-F]{8}-?[0-9a-fA-F]{4}-?[0-9a-fA-F]{4}-?[0-9a-fA-F]{4}-?[0-9a-fA-F]{12}'
	def convert(A,value:A):return D.UUID(value)
	def to_string(B,value:D.UUID):return A(value)
F={'str':M(),'path':N(),'int':O(),'float':P(),'uuid':Q()}
def R(key:A,convertor:E[Any]):F[key]=convertor