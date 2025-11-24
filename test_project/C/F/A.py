l='The last update date must be on or after 1950 January 1.'
k='Last update may only be set once.'
j='The serial number should not be more than 159 bits.'
f='The serial number may only be set once.'
e='Serial number must be of integral type.'
d='The issuer name may only be set once.'
c='The subject name may only be set once.'
b=slice
a=Exception
X='extension must be an ExtensionType'
W='Expecting x509.Name object.'
U=str
T='Expecting datetime object.'
Q=bool
M=TypeError
L=isinstance
K=int
J=bytes
G=property
F=ValueError
C=None
import abc as E,datetime as H,os,typing as B
from C import utils
from cryptography.hazmat.bindings._rust import x509 as N
from C.D.D import hashes as O,serialization as Y
from C.D.D.D import dsa,ec,ed448,ed25519 as m,padding as R,rsa,x448,x25519 as n
from C.D.D.D.H import q,ò,ñ
from C.F.C import S,y,I,V
from C.F.E import A,D
from C.F.G import ObjectIdentifier as P
g=H.datetime(1950,1,1)
Z=B.Union[O.SHA224,O.SHA256,O.SHA384,O.SHA512,O.SHA3_224,O.SHA3_256,O.SHA3_384,O.SHA3_512]
class đ(a):
	def __init__(A,msg:U,oid:P):super().__init__(msg);A.oid=oid
def h(extension:S[I],extensions:B.List[S[I]]):
	for A in extensions:
		if A.oid==extension.oid:raise F('This extension has already been set.')
def o(oid:P,attributes:B.List[B.Tuple[P,J,B.Optional[K]]]):
	for(A,B,B)in attributes:
		if A==oid:raise F('This attribute has already been set.')
def i(time:H.datetime):
	A=time
	if A.tzinfo is not C:B=A.utcoffset();B=B if B else H.timedelta();return A.replace(tzinfo=C)-B
	else:return A
class ď:
	def __init__(A,oid:P,value:J,_type:K=D.UTF8String.value):A._oid=oid;A._value=value;A._type=_type
	@G
	def oid(self):return self._oid
	@G
	def value(self):return self._value
	def __repr__(A):return f"<Attribute(oid={A.oid}, value={A.value!r})>"
	def __eq__(B,other:object):
		A=other
		if not L(A,ď):return NotImplemented
		return B.oid==A.oid and B.value==A.value and B._type==A._type
	def __hash__(A):return hash((A.oid,A.value,A._type))
class Ē:
	def __init__(A,attributes:B.Iterable[ď]):A._attributes=list(attributes)
	__len__,__iter__,__getitem__=V('_attributes')
	def __repr__(A):return f"<Attributes({A._attributes})>"
	def get_attribute_for_oid(C,oid:P):
		A=oid
		for B in C:
			if B.oid==A:return B
		raise đ(f"No {A} attribute was found",A)
class Đ(utils.Enum):v1=0;v3=2
class ē(a):
	def __init__(A,msg:U,parsed_version:K):super().__init__(msg);A.parsed_version=parsed_version
class Ċ(metaclass=E.ABCMeta):
	@E.abstractmethod
	def fingerprint(self,algorithm:O.HashAlgorithm):0
	@G
	@E.abstractmethod
	def serial_number(self):0
	@G
	@E.abstractmethod
	def version(self):0
	@E.abstractmethod
	def public_key(self):0
	@G
	@E.abstractmethod
	def not_valid_before(self):0
	@G
	@E.abstractmethod
	def not_valid_after(self):0
	@G
	@E.abstractmethod
	def issuer(self):0
	@G
	@E.abstractmethod
	def subject(self):0
	@G
	@E.abstractmethod
	def signature_hash_algorithm(self):0
	@G
	@E.abstractmethod
	def signature_algorithm_oid(self):0
	@G
	@E.abstractmethod
	def signature_algorithm_parameters(self):0
	@G
	@E.abstractmethod
	def extensions(self):0
	@G
	@E.abstractmethod
	def signature(self):0
	@G
	@E.abstractmethod
	def tbs_certificate_bytes(self):0
	@G
	@E.abstractmethod
	def tbs_precertificate_bytes(self):0
	@E.abstractmethod
	def __eq__(self,other:object):0
	@E.abstractmethod
	def __hash__(self):0
	@E.abstractmethod
	def public_bytes(self,encoding:Y.Encoding):0
	@E.abstractmethod
	def verify_directly_issued_by(self,issuer:Ċ):0
Ċ.register(N.Certificate)
class Ĉ(metaclass=E.ABCMeta):
	@G
	@E.abstractmethod
	def serial_number(self):0
	@G
	@E.abstractmethod
	def revocation_date(self):0
	@G
	@E.abstractmethod
	def extensions(self):0
Ĉ.register(N.RevokedCertificate)
class p(Ĉ):
	def __init__(A,serial_number:K,revocation_date:H.datetime,extensions:y):A._serial_number=serial_number;A._revocation_date=revocation_date;A._extensions=extensions
	@G
	def serial_number(self):return self._serial_number
	@G
	def revocation_date(self):return self._revocation_date
	@G
	def extensions(self):return self._extensions
class č(metaclass=E.ABCMeta):
	@E.abstractmethod
	def public_bytes(self,encoding:Y.Encoding):0
	@E.abstractmethod
	def fingerprint(self,algorithm:O.HashAlgorithm):0
	@E.abstractmethod
	def get_revoked_certificate_by_serial_number(self,serial_number:K):0
	@G
	@E.abstractmethod
	def signature_hash_algorithm(self):0
	@G
	@E.abstractmethod
	def signature_algorithm_oid(self):0
	@G
	@E.abstractmethod
	def issuer(self):0
	@G
	@E.abstractmethod
	def next_update(self):0
	@G
	@E.abstractmethod
	def last_update(self):0
	@G
	@E.abstractmethod
	def extensions(self):0
	@G
	@E.abstractmethod
	def signature(self):0
	@G
	@E.abstractmethod
	def tbs_certlist_bytes(self):0
	@E.abstractmethod
	def __eq__(self,other:object):0
	@E.abstractmethod
	def __len__(self):0
	@B.overload
	def __getitem__(self,idx:K):0
	@B.overload
	def __getitem__(self,idx:b):0
	@E.abstractmethod
	def __getitem__(self,idx:B.Union[K,b]):0
	@E.abstractmethod
	def __iter__(self):0
	@E.abstractmethod
	def is_signature_valid(self,public_key:ò):0
č.register(N.CertificateRevocationList)
class Ď(metaclass=E.ABCMeta):
	@E.abstractmethod
	def __eq__(self,other:object):0
	@E.abstractmethod
	def __hash__(self):0
	@E.abstractmethod
	def public_key(self):0
	@G
	@E.abstractmethod
	def subject(self):0
	@G
	@E.abstractmethod
	def signature_hash_algorithm(self):0
	@G
	@E.abstractmethod
	def signature_algorithm_oid(self):0
	@G
	@E.abstractmethod
	def extensions(self):0
	@G
	@E.abstractmethod
	def attributes(self):0
	@E.abstractmethod
	def public_bytes(self,encoding:Y.Encoding):0
	@G
	@E.abstractmethod
	def signature(self):0
	@G
	@E.abstractmethod
	def tbs_certrequest_bytes(self):0
	@G
	@E.abstractmethod
	def is_signature_valid(self):0
	@E.abstractmethod
	def get_attribute_for_oid(self,oid:P):0
Ď.register(N.CertificateSigningRequest)
def Ĕ(data:J,backend:B.Any=C):return N.load_pem_x509_certificate(data)
def ĕ(data:J):return N.load_pem_x509_certificates(data)
def Ė(data:J,backend:B.Any=C):return N.load_der_x509_certificate(data)
def ė(data:J,backend:B.Any=C):return N.load_pem_x509_csr(data)
def Ę(data:J,backend:B.Any=C):return N.load_der_x509_csr(data)
def ę(data:J,backend:B.Any=C):return N.load_pem_x509_crl(data)
def Ě(data:J,backend:B.Any=C):return N.load_der_x509_crl(data)
class ċ:
	def __init__(A,subject_name:B.Optional[A]=C,extensions:B.List[S[I]]=[],attributes:B.List[B.Tuple[P,J,B.Optional[K]]]=[]):A._subject_name=subject_name;A._extensions=extensions;A._attributes=attributes
	def subject_name(B,name:A):
		if not L(name,A):raise M(W)
		if B._subject_name is not C:raise F(c)
		return ċ(name,B._extensions,B._attributes)
	def add_extension(A,extval:I,critical:Q):
		B=extval
		if not L(B,I):raise M(X)
		C=S(B.oid,critical,B);h(C,A._extensions);return ċ(A._subject_name,A._extensions+[C],A._attributes)
	def add_attribute(A,oid:P,value:J,*,_tag:B.Optional[D]=C):
		F=value;E=oid;B=_tag
		if not L(E,P):raise M('oid must be an ObjectIdentifier')
		if not L(F,J):raise M('value must be bytes')
		if B is not C and not L(B,D):raise M('tag must be _ASN1Type')
		o(E,A._attributes)
		if B is not C:G=B.value
		else:G=C
		return ċ(A._subject_name,A._extensions,A._attributes+[(E,F,G)])
	def sign(A,private_key:q,algorithm:B.Optional[Z],backend:B.Any=C):
		if A._subject_name is C:raise F('A CertificateSigningRequest must have a subject')
		return N.create_x509_csr(A,private_key,algorithm)
class ć:
	_extensions:B.List[S[I]]
	def __init__(A,issuer_name:B.Optional[A]=C,subject_name:B.Optional[A]=C,public_key:B.Optional[ñ]=C,serial_number:B.Optional[K]=C,not_valid_before:B.Optional[H.datetime]=C,not_valid_after:B.Optional[H.datetime]=C,extensions:B.List[S[I]]=[]):A._version=Đ.v3;A._issuer_name=issuer_name;A._subject_name=subject_name;A._public_key=public_key;A._serial_number=serial_number;A._not_valid_before=not_valid_before;A._not_valid_after=not_valid_after;A._extensions=extensions
	def issuer_name(B,name:A):
		if not L(name,A):raise M(W)
		if B._issuer_name is not C:raise F(d)
		return ć(name,B._subject_name,B._public_key,B._serial_number,B._not_valid_before,B._not_valid_after,B._extensions)
	def subject_name(B,name:A):
		if not L(name,A):raise M(W)
		if B._subject_name is not C:raise F(c)
		return ć(B._issuer_name,name,B._public_key,B._serial_number,B._not_valid_before,B._not_valid_after,B._extensions)
	def public_key(A,key:ñ):
		if not L(key,(dsa.DSAPublicKey,rsa.RSAPublicKey,ec.EllipticCurvePublicKey,m.Ed25519PublicKey,ed448.Ed448PublicKey,n.X25519PublicKey,x448.X448PublicKey)):raise M('Expecting one of DSAPublicKey, RSAPublicKey, EllipticCurvePublicKey, Ed25519PublicKey, Ed448PublicKey, X25519PublicKey, or X448PublicKey.')
		if A._public_key is not C:raise F('The public key may only be set once.')
		return ć(A._issuer_name,A._subject_name,key,A._serial_number,A._not_valid_before,A._not_valid_after,A._extensions)
	def serial_number(A,number:K):
		B=number
		if not L(B,K):raise M(e)
		if A._serial_number is not C:raise F(f)
		if B<=0:raise F('The serial number should be positive.')
		if B.bit_length()>=160:raise F(j)
		return ć(A._issuer_name,A._subject_name,A._public_key,B,A._not_valid_before,A._not_valid_after,A._extensions)
	def not_valid_before(A,time:H.datetime):
		B=time
		if not L(B,H.datetime):raise M(T)
		if A._not_valid_before is not C:raise F('The not valid before may only be set once.')
		B=i(B)
		if B<g:raise F('The not valid before date must be on or after 1950 January 1).')
		if A._not_valid_after is not C and B>A._not_valid_after:raise F('The not valid before date must be before the not valid after date.')
		return ć(A._issuer_name,A._subject_name,A._public_key,A._serial_number,B,A._not_valid_after,A._extensions)
	def not_valid_after(A,time:H.datetime):
		B=time
		if not L(B,H.datetime):raise M(T)
		if A._not_valid_after is not C:raise F('The not valid after may only be set once.')
		B=i(B)
		if B<g:raise F('The not valid after date must be on or after 1950 January 1.')
		if A._not_valid_before is not C and B<A._not_valid_before:raise F('The not valid after date must be after the not valid before date.')
		return ć(A._issuer_name,A._subject_name,A._public_key,A._serial_number,A._not_valid_before,B,A._extensions)
	def add_extension(A,extval:I,critical:Q):
		B=extval
		if not L(B,I):raise M(X)
		C=S(B.oid,critical,B);h(C,A._extensions);return ć(A._issuer_name,A._subject_name,A._public_key,A._serial_number,A._not_valid_before,A._not_valid_after,A._extensions+[C])
	def sign(A,private_key:q,algorithm:B.Optional[Z],backend:B.Any=C,*,rsa_padding:B.Optional[B.Union[R.PSS,R.PKCS1v15]]=C):
		D=private_key;B=rsa_padding
		if A._subject_name is C:raise F('A certificate must have a subject name')
		if A._issuer_name is C:raise F('A certificate must have an issuer name')
		if A._serial_number is C:raise F('A certificate must have a serial number')
		if A._not_valid_before is C:raise F('A certificate must have a not valid before time')
		if A._not_valid_after is C:raise F('A certificate must have a not valid after time')
		if A._public_key is C:raise F('A certificate must have a public key')
		if B is not C:
			if not L(B,(R.PSS,R.PKCS1v15)):raise M('Padding must be PSS or PKCS1v15')
			if not L(D,rsa.RSAPrivateKey):raise M('Padding is only supported for RSA keys')
		return N.create_x509_certificate(A,D,algorithm,B)
class ĉ:
	_extensions:B.List[S[I]];_revoked_certificates:B.List[Ĉ]
	def __init__(A,issuer_name:B.Optional[A]=C,last_update:B.Optional[H.datetime]=C,next_update:B.Optional[H.datetime]=C,extensions:B.List[S[I]]=[],revoked_certificates:B.List[Ĉ]=[]):A._issuer_name=issuer_name;A._last_update=last_update;A._next_update=next_update;A._extensions=extensions;A._revoked_certificates=revoked_certificates
	def issuer_name(B,issuer_name:A):
		D=issuer_name
		if not L(D,A):raise M(W)
		if B._issuer_name is not C:raise F(d)
		return ĉ(D,B._last_update,B._next_update,B._extensions,B._revoked_certificates)
	def last_update(A,last_update:H.datetime):
		B=last_update
		if not L(B,H.datetime):raise M(T)
		if A._last_update is not C:raise F(k)
		B=i(B)
		if B<g:raise F(l)
		if A._next_update is not C and B>A._next_update:raise F('The last update date must be before the next update date.')
		return ĉ(A._issuer_name,B,A._next_update,A._extensions,A._revoked_certificates)
	def next_update(A,next_update:H.datetime):
		B=next_update
		if not L(B,H.datetime):raise M(T)
		if A._next_update is not C:raise F(k)
		B=i(B)
		if B<g:raise F(l)
		if A._last_update is not C and B<A._last_update:raise F('The next update date must be after the last update date.')
		return ĉ(A._issuer_name,A._last_update,B,A._extensions,A._revoked_certificates)
	def add_extension(A,extval:I,critical:Q):
		B=extval
		if not L(B,I):raise M(X)
		C=S(B.oid,critical,B);h(C,A._extensions);return ĉ(A._issuer_name,A._last_update,A._next_update,A._extensions+[C],A._revoked_certificates)
	def add_revoked_certificate(A,revoked_certificate:Ĉ):
		B=revoked_certificate
		if not L(B,Ĉ):raise M('Must be an instance of RevokedCertificate')
		return ĉ(A._issuer_name,A._last_update,A._next_update,A._extensions,A._revoked_certificates+[B])
	def sign(A,private_key:q,algorithm:B.Optional[Z],backend:B.Any=C):
		if A._issuer_name is C:raise F('A CRL must have an issuer name')
		if A._last_update is C:raise F('A CRL must have a last update time')
		if A._next_update is C:raise F('A CRL must have a next update time')
		return N.create_x509_crl(A,private_key,algorithm)
class Č:
	def __init__(A,serial_number:B.Optional[K]=C,revocation_date:B.Optional[H.datetime]=C,extensions:B.List[S[I]]=[]):A._serial_number=serial_number;A._revocation_date=revocation_date;A._extensions=extensions
	def serial_number(B,number:K):
		A=number
		if not L(A,K):raise M(e)
		if B._serial_number is not C:raise F(f)
		if A<=0:raise F('The serial number should be positive')
		if A.bit_length()>=160:raise F(j)
		return Č(A,B._revocation_date,B._extensions)
	def revocation_date(B,time:H.datetime):
		A=time
		if not L(A,H.datetime):raise M(T)
		if B._revocation_date is not C:raise F('The revocation date may only be set once.')
		A=i(A)
		if A<g:raise F('The revocation date must be on or after 1950 January 1.')
		return Č(B._serial_number,A,B._extensions)
	def add_extension(A,extval:I,critical:Q):
		B=extval
		if not L(B,I):raise M(X)
		C=S(B.oid,critical,B);h(C,A._extensions);return Č(A._serial_number,A._revocation_date,A._extensions+[C])
	def build(A,backend:B.Any=C):
		if A._serial_number is C:raise F('A revoked certificate must have a serial number')
		if A._revocation_date is C:raise F('A revoked certificate must have a revocation date')
		return p(A._serial_number,A._revocation_date,y(A._extensions))
def ě():return K.from_bytes(os.urandom(20),'big')>>1