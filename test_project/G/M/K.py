J='strict'
I='utf-8'
H=BaseException
G=TypeError
E=type
D=isinstance
C=bytes
B=str
A=None
from types import TracebackType as L
def F(x:B|C,encoding:B|A=A,errors:B|A=A):
	F=errors;A=encoding
	if D(x,C):return x
	elif not D(x,B):raise G(f"not expecting type {E(x).__name__}")
	if A or F:return x.encode(A or I,errors=F or J)
	return x.encode()
def Ã(x:B|C,encoding:B|A=A,errors:B|A=A):
	F=errors;A=encoding
	if D(x,B):return x
	elif not D(x,C):raise G(f"not expecting type {E(x).__name__}")
	if A or F:return x.decode(A or I,errors=F or J)
	return x.decode()
def b(tp:E[H]|A,value:H,tb:L|A=A):
	B=value
	try:
		if B.__traceback__ is not tb:raise B.with_traceback(tb)
		raise B
	finally:B=A;tb=A