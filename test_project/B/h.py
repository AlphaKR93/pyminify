I=property
from typing import Union
from.F import d
from.K import g
J=4
N=0
A=1
D=2
E=3
C=4
H=5
B=6
G=7
F=8
K=9
L=A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,A,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,A,A,A,A,A,A,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,A,A,A,A,A,C,C,H,C,H,C,C,B,B,B,B,B,B,G,B,B,B,B,B,B,B,B,G,B,B,B,B,B,B,B,B,B,A,A,A,A,A,A,A,G,A,A,F,F,A,A,C,C,A,A,A,A,A,A,A,A,A,A,A,A,A,A,B,B,A,A,F,A,F,A,A,A,A,A,A,C,C,C,C,B,A,A,A,A,A,A,A,F,B,C,F,A,A,A,A,A,A,A,A,A,A,C,C,C,C,C,C,C,C,C,C,C,F,C,C,C,C,B,F,F,F,F,F,F,F,F,F,F
M=0,0,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,1,0,3,3,3,3,3,3,3,1,0,3,3,3,1,1,3,3,1,0,3,3,3,1,2,1,2,1,0,3,3,3,3,3,3,3,1,0,3,1,3,1,1,1,3,1,0,3,1,3,1,1,3,3,1,0,1,1,1,1,1,1,1,1
class a(d):
	def __init__(B):super().__init__();B._last_char_class=A;B._freq_counter=[];B.reset()
	def reset(B):B._last_char_class=A;B._freq_counter=[0]*J;B._freq_counter[2]=10;super().reset()
	@I
	def charset_name(self):return'MacRoman'
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