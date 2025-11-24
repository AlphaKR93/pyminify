I=OSError
H=tuple
G=str
C=int
A=None
import socket as B,typing as E
from..H import D
from.I import Ð,Ó
x=E.Sequence[E.Tuple[C,C,E.Union[C,bytes]]]
def Ô(conn:F):return not conn.is_connected
def N(address:H[G,C],timeout:Ó=Ð,source_address:H[G,C]|A=A,socket_options:x|A=A):
	H=source_address;G=timeout;E,L=address
	if E.startswith('['):E=E.strip('[]')
	F=A;M=K()
	try:E.encode('idna')
	except UnicodeError:raise D(f"'{E}', label empty or too long")from A
	for N in B.getaddrinfo(E,L,M,B.SOCK_STREAM):
		O,P,Q,T,R=N;C=A
		try:
			C=B.socket(O,P,Q);J(C,socket_options)
			if G is not Ð:C.settimeout(G)
			if H:C.bind(H)
			C.connect(R);F=A;return C
		except I as S:
			F=S
			if C is not A:C.close()
	if F is not A:
		try:raise F
		finally:F=A
	else:raise I('getaddrinfo returns an empty list')
def J(sock:B.socket,options:x|A):
	B=options
	if B is A:return
	for C in B:sock.setsockopt(*C)
def K():
	A=B.AF_INET
	if M:A=B.AF_UNSPEC
	return A
def L(host:G):
	C=A;D=False
	if B.has_ipv6:
		try:C=B.socket(B.AF_INET6);C.bind((host,0));D=True
		except Exception:pass
	if C:C.close()
	return D
M=L('::1')