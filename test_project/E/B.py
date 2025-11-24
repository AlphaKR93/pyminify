A='ascii'
B=isinstance
import re
from.G import U
C=re.compile(b'^[^:\\s][^:\\r\\n]*$')
D=re.compile('^[^:\\s][^:\\r\\n]*$')
E=re.compile(b'^\\S[^\\r\\n]*$|^$')
F=re.compile('^\\S[^\\r\\n]*$|^$')
ì=D,F
í=C,E
î={bytes:í,str:ì}
def ë(string,encoding=A):
	A=string
	if B(A,U):C=A
	else:C=A.decode(encoding)
	return C
def Z(u_string):
	C=u_string;assert B(C,str)
	try:C.encode(A);return True
	except UnicodeEncodeError:return False