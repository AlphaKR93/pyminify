I=property
from typing import Union
from.F import d
from.K import g
J=4
H=0
A=1
B=2
C=3
D=4
F=5
E=6
G=7
K=8
L=A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,A,A,A,A,A,A,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,A,A,A,A,A,A,H,A,G,A,A,A,A,A,A,F,A,F,H,F,H,H,A,A,A,A,A,A,A,A,A,G,A,G,H,G,F,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,D,D,D,D,D,D,F,F,D,D,D,D,D,D,D,D,F,F,D,D,D,D,D,A,D,D,D,D,D,F,F,F,E,E,E,E,E,E,G,G,E,E,E,E,E,E,E,E,G,G,E,E,E,E,E,A,E,E,E,E,E,G,G,G
M=0,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,0,3,3,3,3,3,3,3,0,3,3,3,1,1,3,3,0,3,3,3,1,2,1,2,0,3,3,3,3,3,3,3,0,3,1,3,1,1,1,3,0,3,1,3,1,1,3,3
class f(d):
	def __init__(B):super().__init__();B._last_char_class=A;B._freq_counter=[];B.reset()
	def reset(B):B._last_char_class=A;B._freq_counter=[0]*J;super().reset()
	@I
	def charset_name(self):return'ISO-8859-1'
	@I
	def language(self):return''
	def feed(A,byte_str:Union[bytes,bytearray]):
		B=byte_str;B=A.remove_xml_tags(B)
		for E in B:
			C=L[E];D=M[A._last_char_class*K+C]
			if D==0:A._state=g.NOT_ME;break
			A._freq_counter[D]+=1;A._last_char_class=C
		return A.state
	def get_confidence(A):
		if A.state==g.NOT_ME:return .01
		C=sum(A._freq_counter);B=.0 if C<.01 else(A._freq_counter[3]-A._freq_counter[1]*2e1)/C;B=max(B,.0);B*=.73;return B