S=False
K=bytearray
J=bytes
G=int
from typing import Union as H
from.B import Z,Y,X
from.O import C,B,A
from.Q import c,b,a
from.S import F,E,D
from.V import V,U,T
from.W import W
class I:
	ENOUGH_DATA_THRESHOLD=1024;SURE_YES=.99;SURE_NO=.01;MINIMUM_DATA_THRESHOLD=3
	def __init__(A):A._char_to_freq_order=tuple();A._table_size=0;A.typical_distribution_ratio=.0;A._done=S;A._total_chars=0;A._freq_chars=0;A.reset()
	def reset(A):A._done=S;A._total_chars=0;A._freq_chars=0
	def feed(A,char:H[J,K],char_len:G):
		if char_len==2:B=A.get_order(char)
		else:B=-1
		if B>=0:
			A._total_chars+=1
			if B<A._table_size:
				if 512>A._char_to_freq_order[B]:A._freq_chars+=1
	def get_confidence(A):
		if A._total_chars<=0 or A._freq_chars<=A.MINIMUM_DATA_THRESHOLD:return A.SURE_NO
		if A._total_chars!=A._freq_chars:
			B=A._freq_chars/((A._total_chars-A._freq_chars)*A.typical_distribution_ratio)
			if B<A.SURE_YES:return B
		return A.SURE_YES
	def got_enough_data(A):return A._total_chars>A.ENOUGH_DATA_THRESHOLD
	def get_order(A,_:H[J,K]):return-1
class M(I):
	def __init__(A):super().__init__();A._char_to_freq_order=c;A._table_size=b;A.typical_distribution_ratio=a
	def get_order(C,byte_str:H[J,K]):
		A=byte_str;B=A[0]
		if B>=196:return 94*(B-196)+A[1]-161
		return-1
class L(I):
	def __init__(D):super().__init__();D._char_to_freq_order=C;D._table_size=B;D.typical_distribution_ratio=A
	def get_order(C,byte_str:H[J,K]):
		A=byte_str;B=A[0]
		if B>=176:return 94*(B-176)+A[1]-161
		return-1
class N(I):
	def __init__(D):super().__init__();D._char_to_freq_order=C;D._table_size=B;D.typical_distribution_ratio=A
	def get_order(D,byte_str:H[J,K]):
		A=byte_str;B=A[0]
		if 136<=B<212:C=B*256+A[1];return W.get(C,-1)
		return-1
class O(I):
	def __init__(A):super().__init__();A._char_to_freq_order=F;A._table_size=E;A.typical_distribution_ratio=D
	def get_order(D,byte_str:H[J,K]):
		A=byte_str;B,C=A[0],A[1]
		if B>=176 and C>=161:return 94*(B-176)+C-161
		return-1
class P(I):
	def __init__(A):super().__init__();A._char_to_freq_order=Z;A._table_size=Y;A.typical_distribution_ratio=X
	def get_order(D,byte_str:H[J,K]):
		C=byte_str;A,B=C[0],C[1]
		if A>=164:
			if B>=161:return 157*(A-164)+B-161+63
			return 157*(A-164)+B-64
		return-1
class Q(I):
	def __init__(A):super().__init__();A._char_to_freq_order=V;A._table_size=U;A.typical_distribution_ratio=T
	def get_order(E,byte_str:H[J,K]):
		C=byte_str;B,D=C[0],C[1]
		if 129<=B<=159:A=188*(B-129)
		elif 224<=B<=239:A=188*(B-224+31)
		else:return-1
		A=A+D-64
		if D>127:A=-1
		return A
class R(I):
	def __init__(A):super().__init__();A._char_to_freq_order=V;A._table_size=U;A.typical_distribution_ratio=T
	def get_order(C,byte_str:H[J,K]):
		A=byte_str;B=A[0]
		if B>=160:return 94*(B-161)+A[1]-161
		return-1