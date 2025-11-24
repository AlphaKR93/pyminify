Q='big'
P=TypeError
G=ValueError
F=None
E=str
B=int
A=bytes
import base64 as I,binascii as L,os,time as K,typing as C
from C import utils
from C.B import T
from C.D.D import hashes as M,padding as N
from C.D.D.E import Y,algorithms as J,modes as O
from C.D.D.I import U
class D(Exception):0
R=60
class H:
	def __init__(B,key:C.Union[A,E],backend:C.Any=F):
		C='Fernet key must be 32 url-safe base64-encoded bytes.';A=key
		try:A=I.urlsafe_b64decode(A)
		except L.Error as D:raise G(C)from D
		if len(A)!=32:raise G(C)
		B._signing_key=A[:16];B._encryption_key=A[16:]
	@classmethod
	def generate_key(A):return I.urlsafe_b64encode(os.urandom(32))
	def encrypt(A,data:A):return A.encrypt_at_time(data,B(K.time()))
	def encrypt_at_time(A,data:A,current_time:B):B=os.urandom(16);return A._encrypt_from_parts(data,current_time,B)
	def _encrypt_from_parts(A,data:A,current_time:B,iv:A):utils._check_bytes('data',data);B=N.PKCS7(J.AES.block_size).padder();F=B.update(data)+B.finalize();C=Y(J.AES(A._encryption_key),O.CBC(iv)).encryptor();G=C.update(F)+C.finalize();D=b'\x80'+current_time.to_bytes(length=8,byteorder=Q)+iv+G;E=U(A._signing_key,M.SHA256());E.update(D);H=E.finalize();return I.urlsafe_b64encode(D+H)
	def decrypt(C,token:C.Union[A,E],ttl:C.Optional[B]=F):
		D,E=H._get_unverified_token_data(token)
		if ttl is F:A=F
		else:A=ttl,B(K.time())
		return C._decrypt_data(E,D,A)
	def decrypt_at_time(A,token:C.Union[A,E],ttl:B,current_time:B):
		if ttl is F:raise G('decrypt_at_time() can only be used with a non-None ttl')
		B,C=H._get_unverified_token_data(token);return A._decrypt_data(C,B,(ttl,current_time))
	def extract_timestamp(A,token:C.Union[A,E]):B,C=H._get_unverified_token_data(token);A._verify_signature(C);return B
	@staticmethod
	def _get_unverified_token_data(token:C.Union[A,E]):
		F=token
		if not isinstance(F,(E,A)):raise P('token must be bytes or str')
		try:C=I.urlsafe_b64decode(F)
		except(P,L.Error):raise D
		if not C or C[0]!=128:raise D
		if len(C)<9:raise D
		G=B.from_bytes(C[1:9],byteorder=Q);return G,C
	def _verify_signature(B,data:A):
		A=U(B._signing_key,M.SHA256());A.update(data[:-32])
		try:A.verify(data[-32:])
		except T:raise D
	def _decrypt_data(B,data:A,timestamp:B,time_info:C.Optional[C.Tuple[B,B]]):
		E=time_info;C=timestamp;A=data
		if E is not F:
			P,H=E
			if C+P<H:raise D
			if H+R<C:raise D
		B._verify_signature(A);Q=A[9:25];S=A[25:-32];I=Y(J.AES(B._encryption_key),O.CBC(Q)).decryptor();K=I.update(S)
		try:K+=I.finalize()
		except G:raise D
		L=N.PKCS7(J.AES.block_size).unpadder();M=L.update(K)
		try:M+=L.finalize()
		except G:raise D
		return M
class S:
	def __init__(B,fernets:C.Iterable[H]):
		A=fernets;A=list(A)
		if not A:raise G('MultiFernet requires at least one Fernet instance')
		B._fernets=A
	def encrypt(A,msg:A):return A.encrypt_at_time(msg,B(K.time()))
	def encrypt_at_time(A,msg:A,current_time:B):return A._fernets[0].encrypt_at_time(msg,current_time)
	def rotate(A,msg:C.Union[A,E]):
		B,C=H._get_unverified_token_data(msg)
		for E in A._fernets:
			try:G=E._decrypt_data(C,B,F);break
			except D:pass
		else:raise D
		I=os.urandom(16);return A._fernets[0]._encrypt_from_parts(G,B,I)
	def decrypt(A,msg:C.Union[A,E],ttl:C.Optional[B]=F):
		for B in A._fernets:
			try:return B.decrypt(msg,ttl)
			except D:pass
		raise D
	def decrypt_at_time(A,msg:C.Union[A,E],ttl:B,current_time:B):
		for B in A._fernets:
			try:return B.decrypt_at_time(msg,ttl,current_time)
			except D:pass
		raise D