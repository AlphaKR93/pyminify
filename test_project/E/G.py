import sys
A=sys.version_info
C=A[0]==2
D=A[0]==3
B=False
try:B=True
except ImportError:pass
if B:0
else:0
U=str
str=str
bytes=bytes
ä=str,bytes
E=int,float
ê=int,