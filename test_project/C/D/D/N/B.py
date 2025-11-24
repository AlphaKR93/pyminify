Q='Key must be RSA, DSA, EllipticCurve, ED25519, or ED448 private key, or None.'
P=NotImplemented
H=property
G=TypeError
F=bytes
C=None
B=isinstance
import typing as A
from C import x509 as E
from C.D.D import serialization as O
from C.D.D.C import K
from C.D.D.D import dsa as J,ec,ed448 as L,ed25519 as M,rsa as N
from C.D.D.D.H import c
a=A.Union[N.RSAPrivateKey,J.DSAPrivateKey,ec.EllipticCurvePrivateKey,M.Ed25519PrivateKey,L.Ed448PrivateKey]
class D:
	def __init__(D,cert:E.Certificate,friendly_name:A.Optional[F]):
		A=friendly_name
		if not B(cert,E.Certificate):raise G('Expecting x509.Certificate object')
		if A is not C and not B(A,F):raise G('friendly_name must be bytes or None')
		D._cert=cert;D._friendly_name=A
	@H
	def friendly_name(self):return self._friendly_name
	@H
	def certificate(self):return self._cert
	def __eq__(C,other:object):
		A=other
		if not B(A,D):return P
		return C.certificate==A.certificate and C.friendly_name==A.friendly_name
	def __hash__(A):return hash((A.certificate,A.friendly_name))
	def __repr__(A):return'<PKCS12Certificate({}, friendly_name={!r})>'.format(A.certificate,A.friendly_name)
class I:
	def __init__(A,key:A.Optional[c],cert:A.Optional[D],additional_certs:A.List[D]):
		H=additional_certs;F=cert;E=key
		if E is not C and not B(E,(N.RSAPrivateKey,J.DSAPrivateKey,ec.EllipticCurvePrivateKey,M.Ed25519PrivateKey,L.Ed448PrivateKey)):raise G(Q)
		if F is not C and not B(F,D):raise G('cert must be a PKCS12Certificate object or None')
		if not all(B(A,D)for A in H):raise G('all values in additional_certs must be PKCS12Certificate objects')
		A._key=E;A._cert=F;A._additional_certs=H
	@H
	def key(self):return self._key
	@H
	def cert(self):return self._cert
	@H
	def additional_certs(self):return self._additional_certs
	def __eq__(C,other:object):
		A=other
		if not B(A,I):return P
		return C.key==A.key and C.cert==A.cert and C.additional_certs==A.additional_certs
	def __hash__(A):return hash((A.key,A.cert,tuple(A.additional_certs)))
	def __repr__(A):B='<PKCS12KeyAndCertificates(key={}, cert={}, additional_certs={})>';return B.format(A.key,A.cert,A.additional_certs)
def R(data:F,password:A.Optional[F],backend:A.Any=C):from C.D.B.A.B import Î;return Î.load_key_and_certificates_from_pkcs12(data,password)
def S(data:F,password:A.Optional[F],backend:A.Any=C):from C.D.B.A.B import Î;return Î.load_pkcs12(data,password)
b=A.Union[E.Certificate,D]
def T(name:A.Optional[F],key:A.Optional[a],cert:A.Optional[E.Certificate],cas:A.Optional[A.Iterable[b]],encryption_algorithm:O.KeySerializationEncryption):
	I=encryption_algorithm;H=cert;F=key;A=cas
	if F is not C and not B(F,(N.RSAPrivateKey,J.DSAPrivateKey,ec.EllipticCurvePrivateKey,M.Ed25519PrivateKey,L.Ed448PrivateKey)):raise G(Q)
	if H is not C and not B(H,E.Certificate):raise G('cert must be a certificate or None')
	if A is not C:
		A=list(A)
		if not all(B(A,(E.Certificate,D))for A in A):raise G('all values in cas must be certificates')
	if not B(I,O.KeySerializationEncryption):raise G('Key encryption algorithm must be a KeySerializationEncryption instance')
	if F is C and H is C and not A:raise ValueError('You must supply at least one of key, cert, or cas')
	from C.D.B.A.B import Î;return Î.serialize_key_and_certificates_to_pkcs12(name,F,H,A,I)