R=b'\x00'
Q=b'\xa6YY\xa6'
N=b'\xa6\xa6\xa6\xa6\xa6\xa6\xa6\xa6'
L=reversed
M=int
J='The wrapping key must be a valid AES key length'
I=None
G='big'
F=ValueError
E=b''
D=range
B=len
A=bytes
import typing as C
from C.D.D.E import Y
from C.D.D.E.B import X
from C.D.D.E.D import Z
from C.D.D.G import W
def K(wrapping_key:A,a:A,r:C.List[A]):
	C=Y(X(wrapping_key),Z()).encryptor();F=B(r)
	for I in D(6):
		for A in D(F):H=C.update(a+r[A]);a=(M.from_bytes(H[:8],byteorder=G)^F*I+A+1).to_bytes(length=8,byteorder=G);r[A]=H[-8:]
	assert C.finalize()==E;return a+E.join(r)
def O(wrapping_key:A,key_to_wrap:A,backend:C.Any=I):
	C=wrapping_key;A=key_to_wrap
	if B(C)not in[16,24,32]:raise F(J)
	if B(A)<16:raise F('The key to wrap must be at least 16 bytes')
	if B(A)%8!=0:raise F('The key to wrap must be a multiple of 8 bytes')
	E=N;G=[A[B:B+8]for B in D(0,B(A),8)];return K(C,E,G)
def P(wrapping_key:A,a:A,r:C.List[A]):
	C=Y(X(wrapping_key),Z()).decryptor();F=B(r)
	for I in L(D(6)):
		for A in L(D(F)):J=(M.from_bytes(a,byteorder=G)^F*I+A+1).to_bytes(length=8,byteorder=G)+r[A];H=C.update(J);a=H[:8];r[A]=H[-8:]
	assert C.finalize()==E;return a,r
def S(wrapping_key:A,key_to_wrap:A,backend:C.Any=I):
	C=wrapping_key;A=key_to_wrap
	if B(C)not in[16,24,32]:raise F(J)
	H=Q+B(A).to_bytes(length=4,byteorder=G);L=(8-B(A)%8)%8;A=A+R*L
	if B(A)==8:I=Y(X(C),Z()).encryptor();M=I.update(H+A);assert I.finalize()==E;return M
	else:N=[A[B:B+8]for B in D(0,B(A),8)];return K(C,H,N)
def T(wrapping_key:A,wrapped_key:A,backend:C.Any=I):
	N=wrapping_key;A=wrapped_key
	if B(A)<16:raise H('Must be at least 16 bytes')
	if B(N)not in[16,24,32]:raise F(J)
	if B(A)==16:S=Y(X(N),Z()).decryptor();T=S.update(A);assert S.finalize()==E;O=T[:8];K=T[8:];L=1
	else:C=[A[B:B+8]for B in D(0,B(A),8)];V=C.pop(0);L=B(C);O,C=P(N,V,C);K=E.join(C)
	U=M.from_bytes(O[4:],byteorder=G);I=8*L-U
	if not W(O[:4],Q)or not 8*(L-1)<U<=8*L or I!=0 and not W(K[-I:],R*I):raise H()
	if I==0:return K
	else:return K[:-I]
def U(wrapping_key:A,wrapped_key:A,backend:C.Any=I):
	I=wrapping_key;A=wrapped_key
	if B(A)<24:raise H('Must be at least 24 bytes')
	if B(A)%8!=0:raise H('The wrapped key must be a multiple of 8 bytes')
	if B(I)not in[16,24,32]:raise F(J)
	K=N;C=[A[B:B+8]for B in D(0,B(A),8)];G=C.pop(0);G,C=P(I,G,C)
	if not W(G,K):raise H()
	return E.join(C)
class H(Exception):0