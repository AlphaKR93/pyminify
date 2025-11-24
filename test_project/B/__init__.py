M=TypeError
D=False
C=bool
H=bytes
G=isinstance
E=bytearray
from typing import List as I,Union as F
from.E import c
from.F import d
from.K import i
from.m import B
from.q import L
from.t import A,__version__
def J(byte_str:F[H,E],should_rename_legacy:C=D):
	A=byte_str
	if not G(A,E):
		if not G(A,H):raise M(f"Expected object of type bytes or bytearray, got: {type(A)}")
		A=E(A)
	B=L(should_rename_legacy=should_rename_legacy);B.feed(A);return B.close()
def K(byte_str:F[H,E],ignore_threshold:C=D,should_rename_legacy:C=D):
	P='confidence';N=should_rename_legacy;F=byte_str
	if not G(F,E):
		if not G(F,H):raise M(f"Expected object of type bytes or bytearray, got: {type(F)}")
		F=E(F)
	A=L(should_rename_legacy=N);A.feed(F);A.close()
	if A.input_state==i.HIGH_BYTE:
		J=[];K=[]
		for C in A.charset_probers:
			if G(C,c):K.extend(A for A in C.probers)
			else:K.append(C)
		for C in K:
			if ignore_threshold or C.get_confidence()>A.MINIMUM_THRESHOLD:
				D=C.charset_name or'';O=D.lower()
				if O.startswith('iso-8859')and A.has_win_bytes:D=A.ISO_WIN_MAP.get(O,D)
				if N:D=A.LEGACY_MAP.get(D.lower(),D)
				J.append({'encoding':D,P:C.get_confidence(),'language':C.language})
		if len(J)>0:return sorted(J,key=lambda result:-result[P])
	return[A.result]