P='certificate must be a x509.Certificate'
K=None
J=TypeError
I=isinstance
E=ValueError
C=bytes
import email.base64mime,email.generator,email.message,email.policy,io,typing as A
from C import utils,x509 as B
from cryptography.hazmat.bindings._rust import pkcs7 as L
from C.D.D import hashes as D,serialization as F
from C.D.D.D import ec,rsa
from C.E import N
def R(data:C):from C.D.B.A.B import Î;return Î.load_pem_pkcs7_certificates(data)
def S(data:C):from C.D.B.A.B import Î;return Î.load_der_pkcs7_certificates(data)
def T(certs:A.List[B.Certificate],encoding:F.Encoding):return L.serialize_certificates(certs,encoding)
M=A.Union[D.SHA224,D.SHA256,D.SHA384,D.SHA512]
O=A.Union[rsa.RSAPrivateKey,ec.EllipticCurvePrivateKey]
class G(utils.Enum):Text='Add text/plain MIME type';Binary="Don't translate input data into canonical MIME format";DetachedSignature="Don't embed data in the PKCS7 structure";NoCapabilities="Don't embed SMIME capabilities";NoAttributes="Don't embed authenticatedAttributes";NoCerts="Don't embed signer certificate"
class H:
	def __init__(A,data:A.Optional[C]=K,signers:A.List[A.Tuple[B.Certificate,O,M]]=[],additional_certs:A.List[B.Certificate]=[]):A._data=data;A._signers=signers;A._additional_certs=additional_certs
	def set_data(A,data:C):
		N('data',data)
		if A._data is not K:raise E('data may only be set once')
		return H(data,A._signers)
	def add_signer(A,certificate:B.Certificate,private_key:O,hash_algorithm:M):
		F=hash_algorithm;E=private_key;C=certificate
		if not I(F,(D.SHA224,D.SHA256,D.SHA384,D.SHA512)):raise J('hash_algorithm must be one of hashes.SHA224, SHA256, SHA384, or SHA512')
		if not I(C,B.Certificate):raise J(P)
		if not I(E,(rsa.RSAPrivateKey,ec.EllipticCurvePrivateKey)):raise J('Only RSA & EC keys are supported at this time.')
		return H(A._data,A._signers+[(C,E,F)])
	def add_certificate(A,certificate:B.Certificate):
		C=certificate
		if not I(C,B.Certificate):raise J(P)
		return H(A._data,A._signers,A._additional_certs+[C])
	def sign(B,encoding:F.Encoding,options:A.Iterable[G],backend:A.Any=K):
		C=encoding;A=options
		if len(B._signers)==0:raise E('Must have at least one signer')
		if B._data is K:raise E('You must add data to sign')
		A=list(A)
		if not all(I(A,G)for A in A):raise E('options must be from the PKCS7Options enum')
		if C not in(F.Encoding.PEM,F.Encoding.DER,F.Encoding.SMIME):raise E('Must be PEM, DER, or SMIME from the Encoding enum')
		if G.Text in A and G.DetachedSignature not in A:raise E('When passing the Text option you must also pass DetachedSignature')
		if G.Text in A and C in(F.Encoding.DER,F.Encoding.PEM):raise E('The Text option is only available for SMIME serialization')
		if G.NoAttributes in A and G.NoCapabilities in A:raise E('NoAttributes is a superset of NoCapabilities. Do not pass both values.')
		return L.sign_and_serialize(B,C,A)
def U(data:C,signature:C,micalg:str,text_mode:bool):
	H='smime.p7s';G='application/x-pkcs7-signature';F='MIME-Version';D='Content-Type';A=email.message.Message();A.add_header(F,'1.0');A.add_header(D,'multipart/signed',protocol=G,micalg=micalg);A.preamble='This is an S/MIME signed message\n';C=Q();C.set_payload(data)
	if text_mode:C.add_header(D,'text/plain')
	A.attach(C);B=email.message.MIMEPart();B.add_header(D,G,name=H);B.add_header('Content-Transfer-Encoding','base64');B.add_header('Content-Disposition','attachment',filename=H);B.set_payload(email.base64mime.body_encode(signature,maxlinelen=65));del B[F];A.attach(B);E=io.BytesIO();I=email.generator.BytesGenerator(E,maxheaderlen=0,mangle_from_=False,policy=A.policy.clone(linesep='\r\n'));I.flatten(A);return E.getvalue()
class Q(email.message.MIMEPart):
	def _write_headers(A,generator):
		if list(A.raw_items()):generator._write_headers(A)