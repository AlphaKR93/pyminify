ß='name and value must be bytes'
Þ='SSH DSA key support is deprecated and will be removed in a future release'
Ý='SSH DSA keys are deprecated and will be removed in a future release.'
Ü='password'
Û='Unsupported key type'
Ú=b'aes256-ctr'
y='Invalid data'
x=float
w=bytearray
q='big'
o=True
i=b''
e=False
b=property
Y=TypeError
U=len
O=None
K=isinstance
J=int
H=memoryview
G=ValueError
D=bytes
import binascii as j,enum,os,re,typing as E,warnings as p
from base64 import encodebytes as à
from dataclasses import dataclass as á
from C import utils as Z
from C.B import A
from C.D.D import hashes as c
from C.D.D.D import dsa as T,ec as P,ed25519 as V,padding as Â,rsa as S
from C.D.D.D import utils as Ã
from C.D.D.E import AEADDecryptionContext as â,Cipher as Ä,algorithms as r,modes as a
from C.D.D.N import F,C,N,B,I,L
try:from bcrypt import kdf as Å;ã=o
except ImportError:
	ã=e
	def Å(password:D,salt:D,desired_key_bytes:J,rounds:J,ignore_few_rounds:bool=e):raise A('Need bcrypt module')
Æ=b'ssh-ed25519'
k=b'ssh-rsa'
s=b'ssh-dss'
Ç=b'ecdsa-sha2-nistp256'
È=b'ecdsa-sha2-nistp384'
É=b'ecdsa-sha2-nistp521'
z=b'-cert-v01@openssh.com'
Ê=b'rsa-sha2-256'
ª=b'rsa-sha2-512'
ä=re.compile(b'\\A(\\S+)[ \\t]+(\\S+)')
µ=b'openssh-key-v1\x00'
Ë=b'-----BEGIN OPENSSH PRIVATE KEY-----'
Ì=b'-----END OPENSSH PRIVATE KEY-----'
Í=b'bcrypt'
º=b'none'
å=Ú
æ=16
ç=re.compile(Ë+b'(.*?)'+Ì,re.DOTALL)
Î=H(w(range(1,1+16)))
@á
class t:alg:E.Type[r.AES];key_len:J;mode:E.Union[E.Type[a.CTR],E.Type[a.CBC],E.Type[a.GCM]];block_len:J;iv_len:J;tag_len:E.Optional[J];is_aead:bool
f={Ú:t(alg=r.AES,key_len=32,mode=a.CTR,block_len=16,iv_len=16,tag_len=O,is_aead=e),b'aes256-cbc':t(alg=r.AES,key_len=32,mode=a.CBC,block_len=16,iv_len=16,tag_len=O,is_aead=e),b'aes256-gcm@openssh.com':t(alg=r.AES,key_len=32,mode=a.GCM,block_len=16,iv_len=12,tag_len=16,is_aead=o)}
Ï={'secp256r1':Ç,'secp384r1':È,'secp521r1':É}
def u(key:E.Union[v,d]):
	A=key
	if K(A,P.EllipticCurvePrivateKey):B=Ð(A.public_key())
	elif K(A,P.EllipticCurvePublicKey):B=Ð(A)
	elif K(A,(S.RSAPrivateKey,S.RSAPublicKey)):B=k
	elif K(A,(T.DSAPrivateKey,T.DSAPublicKey)):B=s
	elif K(A,(V.Ed25519PrivateKey,V.Ed25519PublicKey)):B=Æ
	else:raise G(Û)
	return B
def Ð(public_key:P.EllipticCurvePublicKey):
	A=public_key.curve
	if A.name not in Ï:raise G(f"Unsupported curve for ssh private key: {A.name!r}")
	return Ï[A.name]
def è(data:D,prefix:D=Ë+b'\n',suffix:D=Ì+b'\n'):return i.join([prefix,à(data),suffix])
def Ñ(data:D,block_len:J):
	if not data or U(data)%block_len!=0:raise G('Corrupt data: missing padding')
def X(data:D):
	if data:raise G('Corrupt data: unparsed data')
def Ò(ciphername:D,password:E.Optional[D],salt:D,rounds:J):
	B=password
	if not B:raise G('Key is password-protected.')
	A=f[ciphername];C=Å(B,salt,A.key_len+A.iv_len,rounds,o);return Ä(A.alg(C[:A.key_len]),A.mode(C[A.key_len:]))
def l(data:H):
	A=data
	if U(A)<4:raise G(y)
	return J.from_bytes(A[:4],byteorder=q),A[4:]
def À(data:H):
	A=data
	if U(A)<8:raise G(y)
	return J.from_bytes(A[:8],byteorder=q),A[8:]
def M(data:H):
	A=data;B,A=l(A)
	if B>U(A):raise G(y)
	return A[:B],A[B:]
def W(data:H):
	A=data;B,A=M(A)
	if B and B[0]>127:raise G(y)
	return J.from_bytes(B,q),A
def é(val:J):
	A=val
	if A<0:raise G('negative mpint not allowed')
	if not A:return i
	B=(A.bit_length()+8)//8;return Z.int_to_bytes(A,B)
class Q:
	flist:E.List[D]
	def __init__(A,init:E.Optional[E.List[D]]=O):
		A.flist=[]
		if init:A.flist.extend(init)
	def put_raw(A,val:D):A.flist.append(val)
	def put_u32(A,val:J):A.flist.append(val.to_bytes(length=4,byteorder=q))
	def put_u64(A,val:J):A.flist.append(val.to_bytes(length=8,byteorder=q))
	def put_sshstr(B,val:E.Union[D,Q]):
		A=val
		if K(A,(D,H,w)):B.put_u32(U(A));B.flist.append(A)
		else:B.put_u32(A.size());B.flist.extend(A.flist)
	def put_mpint(A,val:J):A.put_sshstr(é(val))
	def size(A):return sum(map(U,A.flist))
	def render(C,dstbuf:H,pos:J=0):
		A=pos
		for B in C.flist:D=U(B);E,A=A,A+D;dstbuf[E:A]=B
		return A
	def tobytes(A):B=H(w(A.size()));A.render(B);return B.tobytes()
class ê:
	def get_public(D,data:H):A=data;B,A=W(A);C,A=W(A);return(B,C),A
	def load_public(B,data:H):A=data;(C,D),A=B.get_public(A);E=S.RSAPublicNumbers(C,D);F=E.public_key();return F,A
	def load_private(N,data:H,pubfields):
		A=data;C,A=W(A);D,A=W(A);B,A=W(A);H,A=W(A);E,A=W(A);F,A=W(A)
		if(D,C)!=pubfields:raise G('Corrupt data: rsa field mismatch')
		I=S.rsa_crt_dmp1(B,E);J=S.rsa_crt_dmq1(B,F);K=S.RSAPublicNumbers(D,C);L=S.RSAPrivateNumbers(E,F,B,I,J,H,K);M=L.private_key();return M,A
	def encode_public(C,public_key:S.RSAPublicKey,f_pub:Q):A=f_pub;B=public_key.public_numbers();A.put_mpint(B.e);A.put_mpint(B.n)
	def encode_private(D,private_key:S.RSAPrivateKey,f_priv:Q):A=f_priv;B=private_key.private_numbers();C=B.public_numbers;A.put_mpint(C.n);A.put_mpint(C.e);A.put_mpint(B.d);A.put_mpint(B.iqmp);A.put_mpint(B.p);A.put_mpint(B.q)
class ë:
	def get_public(F,data:H):A=data;B,A=W(A);C,A=W(A);D,A=W(A);E,A=W(A);return(B,C,D,E),A
	def load_public(B,data:H):A=data;(D,E,F,G),A=B.get_public(A);H=T.DSAParameterNumbers(D,E,F);C=T.DSAPublicNumbers(G,H);B._validate(C);I=C.public_key();return I,A
	def load_private(B,data:H,pubfields):
		A=data;(C,D,E,F),A=B.get_public(A);I,A=W(A)
		if(C,D,E,F)!=pubfields:raise G('Corrupt data: dsa field mismatch')
		J=T.DSAParameterNumbers(C,D,E);H=T.DSAPublicNumbers(F,J);B._validate(H);K=T.DSAPrivateNumbers(I,H);L=K.private_key();return L,A
	def encode_public(D,public_key:T.DSAPublicKey,f_pub:Q):A=f_pub;B=public_key.public_numbers();C=B.parameter_numbers;D._validate(B);A.put_mpint(C.p);A.put_mpint(C.q);A.put_mpint(C.g);A.put_mpint(B.y)
	def encode_private(C,private_key:T.DSAPrivateKey,f_priv:Q):B=f_priv;A=private_key;C.encode_public(A.public_key(),B);B.put_mpint(A.private_numbers().x)
	def _validate(B,public_numbers:T.DSAPublicNumbers):
		A=public_numbers.parameter_numbers
		if A.p.bit_length()!=1024:raise G('SSH supports only 1024 bit DSA keys')
class Á:
	def __init__(A,ssh_curve_name:D,curve:P.EllipticCurve):A.ssh_curve_name=ssh_curve_name;A.curve=curve
	def get_public(D,data:H):
		A=data;B,A=M(A);C,A=M(A)
		if B!=D.ssh_curve_name:raise G('Curve name mismatch')
		if C[0]!=4:raise NotImplementedError('Need uncompressed point')
		return(B,C),A
	def load_public(B,data:H):A=data;(E,C),A=B.get_public(A);D=P.EllipticCurvePublicKey.from_encoded_point(B.curve,C.tobytes());return D,A
	def load_private(B,data:H,pubfields):
		A=data;(C,D),A=B.get_public(A);E,A=W(A)
		if(C,D)!=pubfields:raise G('Corrupt data: ecdsa field mismatch')
		F=P.derive_private_key(E,B.curve);return F,A
	def encode_public(B,public_key:P.EllipticCurvePublicKey,f_pub:Q):A=f_pub;C=public_key.public_bytes(F.X962,I.UncompressedPoint);A.put_sshstr(B.ssh_curve_name);A.put_sshstr(C)
	def encode_private(C,private_key:P.EllipticCurvePrivateKey,f_priv:Q):B=f_priv;A=private_key;D=A.public_key();E=A.private_numbers();C.encode_public(D,B);B.put_mpint(E.private_value)
class ì:
	def get_public(C,data:H):A=data;B,A=M(A);return(B,),A
	def load_public(B,data:H):A=data;(C,),A=B.get_public(A);D=V.Ed25519PublicKey.from_public_bytes(C.tobytes());return D,A
	def load_private(D,data:H,pubfields):
		A=data;(B,),A=D.get_public(A);C,A=M(A);E=C[:32];F=C[32:]
		if B!=F or(B,)!=pubfields:raise G('Corrupt data: ed25519 field mismatch')
		H=V.Ed25519PrivateKey.from_private_bytes(E);return H,A
	def encode_public(B,public_key:V.Ed25519PublicKey,f_pub:Q):A=public_key.public_bytes(F.Raw,I.Raw);f_pub.put_sshstr(A)
	def encode_private(E,private_key:V.Ed25519PrivateKey,f_priv:Q):C=f_priv;A=private_key;D=A.public_key();G=A.private_bytes(F.Raw,B.Raw,N());H=D.public_bytes(F.Raw,I.Raw);J=Q([G,H]);E.encode_public(D,C);C.put_sshstr(J)
Ó={k:ê(),s:ë(),Æ:ì(),Ç:Á(b'nistp256',P.SECP256R1()),È:Á(b'nistp384',P.SECP384R1()),É:Á(b'nistp521',P.SECP521R1())}
def g(key_type:D):
	B=key_type
	if not K(B,D):B=H(B).tobytes()
	if B in Ó:return Ó[B]
	raise A(f"Unsupported key type: {B!r}")
v=E.Union[P.EllipticCurvePrivateKey,S.RSAPrivateKey,T.DSAPrivateKey,V.Ed25519PrivateKey]
def í(data:D,password:E.Optional[D],backend:E.Any=O):
	a='Not OpenSSH private key format';J=password;B=data;Z._check_byteslike('data',B)
	if J is not O:Z._check_bytes(Ü,J)
	L=ç.search(B)
	if not L:raise G(a)
	b=L.start(1);c=L.end(1);B=j.a2b_base64(H(B)[b:c])
	if not B.startswith(µ):raise G(a)
	B=H(B)[U(µ):];R,B=M(B);N,B=M(B);d,B=M(B);e,B=l(B)
	if e!=1:raise G('Only one key supported')
	F,B=M(B);S,F=M(F);V=g(S);h,F=V.get_public(F);X(F)
	if(R,N)!=(º,º):
		E=R.tobytes()
		if E not in f:raise A(f"Unsupported cipher: {E!r}")
		if N!=Í:raise A(f"Unsupported KDF: {N!r}")
		P=f[E].block_len;i=f[E].tag_len;C,B=M(B)
		if f[E].is_aead:
			W=D(B)
			if U(W)!=i:raise G('Corrupt data: invalid tag length for cipher')
		else:X(B)
		Ñ(C,P);k,Q=M(d);m,Q=l(Q);X(Q);n=Ò(E,J,k.tobytes(),m);I=n.decryptor();C=H(I.update(C))
		if f[E].is_aead:assert K(I,â);X(I.finalize_with_tag(W))
		else:X(I.finalize())
	else:C,B=M(B);X(B);P=8;Ñ(C,P)
	o,C=l(C);q,C=l(C)
	if o!=q:raise G('Corrupt data: broken checksum')
	r,C=M(C)
	if r!=S:raise G('Corrupt data: key type mismatch')
	Y,C=V.load_private(C,h);s,C=M(C)
	if C!=Î[:U(C)]:raise G('Corrupt data: invalid padding')
	if K(Y,T.DSAPrivateKey):p.warn(Ý,Z.DeprecatedIn40,stacklevel=2)
	return Y
def ð(private_key:v,password:D,encryption_algorithm:C):
	J=encryption_algorithm;I=password;C=private_key;Z._check_bytes(Ü,I)
	if K(C,T.DSAPrivateKey):p.warn(Þ,Z.DeprecatedIn40,stacklevel=4)
	M=u(C);U=g(M);N=Q()
	if I:
		D=å;E=f[D].block_len;V=Í;P=æ
		if K(J,L)and J._kdf_rounds is not O:P=J._kdf_rounds
		W=os.urandom(16);N.put_sshstr(W);N.put_u32(P);R=Ò(D,I,W,P)
	else:D=V=º;E=8;R=O
	a=1;X=os.urandom(4);b=i;S=Q();S.put_sshstr(M);U.encode_public(C.public_key(),S);B=Q([X,X]);B.put_sshstr(M);U.encode_private(C,B);B.put_sshstr(b);B.put_raw(Î[:E-B.size()%E]);A=Q();A.put_raw(µ);A.put_sshstr(D);A.put_sshstr(V);A.put_sshstr(N);A.put_u32(a);A.put_sshstr(S);A.put_sshstr(B);c=B.size();F=A.size();G=H(w(F+E));A.render(G);Y=F-c
	if R is not O:R.encryptor().update_into(G[Y:F],G[Y:])
	return è(G[:F])
d=E.Union[P.EllipticCurvePublicKey,S.RSAPublicKey,T.DSAPublicKey,V.Ed25519PublicKey]
m=E.Union[P.EllipticCurvePublicKey,S.RSAPublicKey,V.Ed25519PublicKey]
class n(enum.Enum):USER=1;HOST=2
class h:
	def __init__(A,_nonce:H,_public_key:d,_serial:J,_cctype:J,_key_id:H,_valid_principals:E.List[D],_valid_after:J,_valid_before:J,_critical_options:E.Dict[D,D],_extensions:E.Dict[D,D],_sig_type:H,_sig_key:H,_inner_sig_type:H,_signature:H,_tbs_cert_body:H,_cert_key_type:D,_cert_body:H):
		A._nonce=_nonce;A._public_key=_public_key;A._serial=_serial
		try:A._type=n(_cctype)
		except G:raise G('Invalid certificate type')
		A._key_id=_key_id;A._valid_principals=_valid_principals;A._valid_after=_valid_after;A._valid_before=_valid_before;A._critical_options=_critical_options;A._extensions=_extensions;A._sig_type=_sig_type;A._sig_key=_sig_key;A._inner_sig_type=_inner_sig_type;A._signature=_signature;A._cert_key_type=_cert_key_type;A._cert_body=_cert_body;A._tbs_cert_body=_tbs_cert_body
	@b
	def nonce(self):return D(self._nonce)
	def public_key(A):return A._public_key
	@b
	def serial(self):return self._serial
	@b
	def type(self):return self._type
	@b
	def key_id(self):return D(self._key_id)
	@b
	def valid_principals(self):return self._valid_principals
	@b
	def valid_before(self):return self._valid_before
	@b
	def valid_after(self):return self._valid_after
	@b
	def critical_options(self):return self._critical_options
	@b
	def extensions(self):return self._extensions
	def signature_key(A):B=g(A._sig_type);C,D=B.load_public(A._sig_key);X(D);return C
	def public_bytes(A):return D(A._cert_key_type)+b' '+j.b2a_base64(D(A._cert_body),newline=e)
	def verify_cert_signature(A):
		B=A.signature_key()
		if K(B,V.Ed25519PublicKey):B.verify(D(A._signature),D(A._tbs_cert_body))
		elif K(B,P.EllipticCurvePublicKey):F,E=W(A._signature);G,E=W(E);X(E);H=Ã.encode_dss_signature(F,G);C=Ô(B.curve);B.verify(H,D(A._tbs_cert_body),P.ECDSA(C))
		else:
			assert K(B,S.RSAPublicKey)
			if A._inner_sig_type==k:C=c.SHA1()
			elif A._inner_sig_type==Ê:C=c.SHA256()
			else:assert A._inner_sig_type==ª;C=c.SHA512()
			B.verify(D(A._signature),D(A._tbs_cert_body),Â.PKCS1v15(),C)
def Ô(curve:P.EllipticCurve):
	A=curve
	if K(A,P.SECP256R1):return c.SHA256()
	elif K(A,P.SECP384R1):return c.SHA384()
	else:assert K(A,P.SECP521R1);return c.SHA512()
def Õ(data:D,_legacy_dsa_allowed=e):
	N=_legacy_dsa_allowed;Z._check_byteslike('data',data);I=ä.match(data)
	if not I:raise G('Invalid line format')
	C=O=I.group(1);S=I.group(2);F=e
	if C.endswith(z):F=o;C=C[:-U(z)]
	if C==s and not N:raise A("DSA keys aren't supported in SSH certificates")
	T=g(C)
	try:B=H(j.a2b_base64(S))
	except(Y,j.Error):raise G('Invalid format')
	if F:P=B
	V,B=M(B)
	if V!=O:raise G('Invalid key format')
	if F:W,B=M(B)
	Q,B=T.load_public(B)
	if F:
		a,B=À(B);b,B=l(B);c,B=M(B);J,B=M(B);R=[]
		while J:d,J=M(J);R.append(D(d))
		f,B=À(B);i,B=À(B);m,B=M(B);n=Ø(m);p,B=M(B);q=Ø(p);x,B=M(B);r,B=M(B);E,t=M(r)
		if E==s and not N:raise A("DSA signatures aren't supported in SSH certificates")
		u=P[:-U(B)];v,B=M(B);X(B);K,L=M(v)
		if E==k and K not in[Ê,ª,k]or E!=k and K!=E:raise G('Signature key type does not match')
		w,L=M(L);X(L);return h(W,Q,a,b,c,R,f,i,n,q,E,t,K,w,u,O,P)
	else:X(B);return Q
def Ö(data:D):return Õ(data)
def Ø(exts_opts:H):
	A=exts_opts;F={};H=O
	while A:
		I,A=M(A);B=D(I)
		if B in F:raise G('Duplicate name')
		if H is not O and B<H:raise G('Fields not lexically sorted')
		C,A=M(A)
		if U(C)>0:
			try:C,J=M(C)
			except G:p.warn('This certificate has an incorrect encoding for critical options or extensions. This will be an exception in cryptography 42',Z.DeprecatedIn41,stacklevel=4)
			else:
				if U(J)>0:raise G('Unexpected extra data after value')
		F[B]=D(C);H=B
	return F
def î(data:D,backend:E.Any=O):
	B=Õ(data,_legacy_dsa_allowed=o)
	if K(B,h):A=B.public_key()
	else:A=B
	if K(A,T.DSAPublicKey):p.warn(Ý,Z.DeprecatedIn40,stacklevel=2)
	return A
def ñ(public_key:d):
	A=public_key
	if K(A,T.DSAPublicKey):p.warn(Þ,Z.DeprecatedIn40,stacklevel=4)
	B=u(A);D=g(B);C=Q();C.put_sshstr(B);D.encode_public(A,C);E=j.b2a_base64(C.tobytes()).strip();return i.join([B,b' ',E])
Ù=E.Union[P.EllipticCurvePrivateKey,S.RSAPrivateKey,V.Ed25519PrivateKey]
ï=256
class R:
	def __init__(A,_public_key:E.Optional[m]=O,_serial:E.Optional[J]=O,_type:E.Optional[n]=O,_key_id:E.Optional[D]=O,_valid_principals:E.List[D]=[],_valid_for_all_principals:bool=e,_valid_before:E.Optional[J]=O,_valid_after:E.Optional[J]=O,_critical_options:E.List[E.Tuple[D,D]]=[],_extensions:E.List[E.Tuple[D,D]]=[]):A._public_key=_public_key;A._serial=_serial;A._type=_type;A._key_id=_key_id;A._valid_principals=_valid_principals;A._valid_for_all_principals=_valid_for_all_principals;A._valid_before=_valid_before;A._valid_after=_valid_after;A._critical_options=_critical_options;A._extensions=_extensions
	def public_key(A,public_key:m):
		B=public_key
		if not K(B,(P.EllipticCurvePublicKey,S.RSAPublicKey,V.Ed25519PublicKey)):raise Y(Û)
		if A._public_key is not O:raise G('public_key already set')
		return R(_public_key=B,_serial=A._serial,_type=A._type,_key_id=A._key_id,_valid_principals=A._valid_principals,_valid_for_all_principals=A._valid_for_all_principals,_valid_before=A._valid_before,_valid_after=A._valid_after,_critical_options=A._critical_options,_extensions=A._extensions)
	def serial(A,serial:J):
		B=serial
		if not K(B,J):raise Y('serial must be an integer')
		if not 0<=B<2**64:raise G('serial must be between 0 and 2**64')
		if A._serial is not O:raise G('serial already set')
		return R(_public_key=A._public_key,_serial=B,_type=A._type,_key_id=A._key_id,_valid_principals=A._valid_principals,_valid_for_all_principals=A._valid_for_all_principals,_valid_before=A._valid_before,_valid_after=A._valid_after,_critical_options=A._critical_options,_extensions=A._extensions)
	def type(A,type:n):
		if not K(type,n):raise Y('type must be an SSHCertificateType')
		if A._type is not O:raise G('type already set')
		return R(_public_key=A._public_key,_serial=A._serial,_type=type,_key_id=A._key_id,_valid_principals=A._valid_principals,_valid_for_all_principals=A._valid_for_all_principals,_valid_before=A._valid_before,_valid_after=A._valid_after,_critical_options=A._critical_options,_extensions=A._extensions)
	def key_id(A,key_id:D):
		B=key_id
		if not K(B,D):raise Y('key_id must be bytes')
		if A._key_id is not O:raise G('key_id already set')
		return R(_public_key=A._public_key,_serial=A._serial,_type=A._type,_key_id=B,_valid_principals=A._valid_principals,_valid_for_all_principals=A._valid_for_all_principals,_valid_before=A._valid_before,_valid_after=A._valid_after,_critical_options=A._critical_options,_extensions=A._extensions)
	def valid_principals(A,valid_principals:E.List[D]):
		B=valid_principals
		if A._valid_for_all_principals:raise G("Principals can't be set because the cert is valid for all principals")
		if not all(K(A,D)for A in B)or not B:raise Y("principals must be a list of bytes and can't be empty")
		if A._valid_principals:raise G('valid_principals already set')
		if U(B)>ï:raise G('Reached or exceeded the maximum number of valid_principals')
		return R(_public_key=A._public_key,_serial=A._serial,_type=A._type,_key_id=A._key_id,_valid_principals=B,_valid_for_all_principals=A._valid_for_all_principals,_valid_before=A._valid_before,_valid_after=A._valid_after,_critical_options=A._critical_options,_extensions=A._extensions)
	def valid_for_all_principals(A):
		if A._valid_principals:raise G("valid_principals already set, can't set valid_for_all_principals")
		if A._valid_for_all_principals:raise G('valid_for_all_principals already set')
		return R(_public_key=A._public_key,_serial=A._serial,_type=A._type,_key_id=A._key_id,_valid_principals=A._valid_principals,_valid_for_all_principals=o,_valid_before=A._valid_before,_valid_after=A._valid_after,_critical_options=A._critical_options,_extensions=A._extensions)
	def valid_before(A,valid_before:E.Union[J,x]):
		B=valid_before
		if not K(B,(J,x)):raise Y('valid_before must be an int or float')
		B=J(B)
		if B<0 or B>=2**64:raise G('valid_before must [0, 2**64)')
		if A._valid_before is not O:raise G('valid_before already set')
		return R(_public_key=A._public_key,_serial=A._serial,_type=A._type,_key_id=A._key_id,_valid_principals=A._valid_principals,_valid_for_all_principals=A._valid_for_all_principals,_valid_before=B,_valid_after=A._valid_after,_critical_options=A._critical_options,_extensions=A._extensions)
	def valid_after(A,valid_after:E.Union[J,x]):
		B=valid_after
		if not K(B,(J,x)):raise Y('valid_after must be an int or float')
		B=J(B)
		if B<0 or B>=2**64:raise G('valid_after must [0, 2**64)')
		if A._valid_after is not O:raise G('valid_after already set')
		return R(_public_key=A._public_key,_serial=A._serial,_type=A._type,_key_id=A._key_id,_valid_principals=A._valid_principals,_valid_for_all_principals=A._valid_for_all_principals,_valid_before=A._valid_before,_valid_after=B,_critical_options=A._critical_options,_extensions=A._extensions)
	def add_critical_option(A,name:D,value:D):
		C=value;B=name
		if not K(B,D)or not K(C,D):raise Y(ß)
		if B in[A for(A,B)in A._critical_options]:raise G('Duplicate critical option name')
		return R(_public_key=A._public_key,_serial=A._serial,_type=A._type,_key_id=A._key_id,_valid_principals=A._valid_principals,_valid_for_all_principals=A._valid_for_all_principals,_valid_before=A._valid_before,_valid_after=A._valid_after,_critical_options=A._critical_options+[(B,C)],_extensions=A._extensions)
	def add_extension(A,name:D,value:D):
		C=value;B=name
		if not K(B,D)or not K(C,D):raise Y(ß)
		if B in[A for(A,B)in A._extensions]:raise G('Duplicate extension name')
		return R(_public_key=A._public_key,_serial=A._serial,_type=A._type,_key_id=A._key_id,_valid_principals=A._valid_principals,_valid_for_all_principals=A._valid_for_all_principals,_valid_before=A._valid_before,_valid_after=A._valid_after,_critical_options=A._critical_options,_extensions=A._extensions+[(B,C)])
	def sign(A,private_key:Ù):
		D=private_key
		if not K(D,(P.EllipticCurvePrivateKey,S.RSAPrivateKey,V.Ed25519PrivateKey)):raise Y('Unsupported private key type')
		if A._public_key is O:raise G('public_key must be set')
		b=0 if A._serial is O else A._serial
		if A._type is O:raise G('type must be set')
		d=i if A._key_id is O else A._key_id
		if not A._valid_principals and not A._valid_for_all_principals:raise G('valid_principals must be set if valid_for_all_principals is False')
		if A._valid_before is O:raise G('valid_before must be set')
		if A._valid_after is O:raise G('valid_after must be set')
		if A._valid_after>A._valid_before:raise G('valid_after must be earlier than valid_before')
		A._critical_options.sort(key=lambda x:x[0]);A._extensions.sort(key=lambda x:x[0]);T=u(A._public_key);W=T+z;e=os.urandom(32);f=g(T);B=Q();B.put_sshstr(W);B.put_sshstr(e);f.encode_public(A._public_key,B);B.put_u64(b);B.put_u32(A._type.value);B.put_sshstr(d);X=Q()
		for k in A._valid_principals:X.put_sshstr(k)
		B.put_sshstr(X.tobytes());B.put_u64(A._valid_after);B.put_u64(A._valid_before);I=Q()
		for(M,F)in A._critical_options:
			I.put_sshstr(M)
			if U(F)>0:Z=Q();Z.put_sshstr(F);I.put_sshstr(Z.tobytes())
			else:I.put_sshstr(F)
		B.put_sshstr(I.tobytes());J=Q()
		for(M,F)in A._extensions:
			J.put_sshstr(M)
			if U(F)>0:a=Q();a.put_sshstr(F);J.put_sshstr(a.tobytes())
			else:J.put_sshstr(F)
		B.put_sshstr(J.tobytes());B.put_sshstr(i);L=u(D);l=g(L);N=Q();N.put_sshstr(L);l.encode_public(D.public_key(),N);B.put_sshstr(N.tobytes())
		if K(D,V.Ed25519PrivateKey):H=D.sign(B.tobytes());C=Q();C.put_sshstr(L);C.put_sshstr(H);B.put_sshstr(C.tobytes())
		elif K(D,P.EllipticCurvePrivateKey):m=Ô(D.curve);H=D.sign(B.tobytes(),P.ECDSA(m));n,o=Ã.decode_dss_signature(H);C=Q();C.put_sshstr(L);R=Q();R.put_mpint(n);R.put_mpint(o);C.put_sshstr(R.tobytes());B.put_sshstr(C.tobytes())
		else:assert K(D,S.RSAPrivateKey);C=Q();C.put_sshstr(ª);H=D.sign(B.tobytes(),Â.PKCS1v15(),c.SHA512());C.put_sshstr(H);B.put_sshstr(C.tobytes())
		p=j.b2a_base64(B.tobytes()).strip();return Ö(i.join([W,b' ',p]))