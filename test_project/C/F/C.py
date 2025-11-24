Ü='oid must be an ObjectIdentifier'
Û='_signed_certificate_timestamps'
Ú='Every item in the signed_certificate_timestamps list must be a SignedCertificateTimestamp'
Ù='_distribution_points'
Ø='distribution_points must be a list of DistributionPoint objects'
Ö='_descriptions'
Õ='Every item in the descriptions list must be an AccessDescription'
Ô='crl_number must be an integer'
Ó=frozenset
Ò=Exception
r=True
q=classmethod
p=getattr
o=len
i='_general_names'
h=any
U=tuple
T=ValueError
R=all
Q=list
N=None
M=hash
L=NotImplemented
K=bytes
J=TypeError
H=property
G=str
F=int
D=bool
C=isinstance
import abc,datetime as j,hashlib,ipaddress as s,typing as B
from C import utils as t
from cryptography.hazmat.bindings._rust import asn1
from cryptography.hazmat.bindings._rust import x509 as P
from C.D.D import constant_time as Ý,serialization as W
from C.D.D.D.C import ð
from C.D.D.D.G import ó
from C.D.D.D.H import ò,ñ
from C.F.B import ë
from C.F.D import é,ä,â,ç,ã,ê,å,æ
from C.F.E import E
from C.F.G import î,í,ì,ï
a=B.TypeVar('ExtensionTypeVar',bound='ExtensionType',covariant=r)
def u(public_key:ñ):
	A=public_key
	if C(A,ó):B=A.public_bytes(W.Encoding.DER,W.PublicFormat.PKCS1)
	elif C(A,ð):B=A.public_bytes(W.Encoding.X962,W.PublicFormat.UncompressedPoint)
	else:D=A.public_bytes(W.Encoding.DER,W.PublicFormat.SubjectPublicKeyInfo);B=asn1.parse_spki_for_data(D)
	return hashlib.sha1(B).digest()
def V(field_name:G):
	A=field_name
	def B(self):return o(p(self,A))
	def C(self):return iter(p(self,A))
	def D(self,idx):return p(self,A)[idx]
	return B,C,D
class Þ(Ò):
	def __init__(A,msg:G,oid:ì):super().__init__(msg);A.oid=oid
class k(Ò):
	def __init__(A,msg:G,oid:ì):super().__init__(msg);A.oid=oid
class I(metaclass=abc.ABCMeta):
	oid:B.ClassVar[ì]
	def public_bytes(A):raise NotImplementedError('public_bytes is not implemented for extension type {!r}'.format(A))
class y:
	def __init__(A,extensions:B.Iterable[S[I]]):A._extensions=Q(extensions)
	def get_extension_for_oid(C,oid:ì):
		A=oid
		for B in C:
			if B.oid==A:return B
		raise k(f"No {A} extension was found",A)
	def get_extension_for_class(D,extclass:B.Type[a]):
		A=extclass
		if A is n:raise J("UnrecognizedExtension can't be used with get_extension_for_class because more than one instance of the class may be present.")
		for B in D:
			if C(B.value,A):return B
		raise k(f"No {A} extension was found",A.oid)
	__len__,__iter__,__getitem__=V('_extensions')
	def __repr__(A):return f"<Extensions({A._extensions})>"
class v(I):
	oid=í.CRL_NUMBER
	def __init__(B,crl_number:F):
		A=crl_number
		if not C(A,F):raise J(Ô)
		B._crl_number=A
	def __eq__(B,other:object):
		A=other
		if not C(A,v):return L
		return B.crl_number==A.crl_number
	def __hash__(A):return M(A.crl_number)
	def __repr__(A):return f"<CRLNumber({A.crl_number})>"
	@H
	def crl_number(self):return self._crl_number
	def public_bytes(A):return P.encode_extension_value(A)
class d(I):
	oid=í.AUTHORITY_KEY_IDENTIFIER
	def __init__(D,key_identifier:B.Optional[K],authority_cert_issuer:B.Optional[B.Iterable[â]],authority_cert_serial_number:B.Optional[F]):
		B=authority_cert_serial_number;A=authority_cert_issuer
		if(A is N)!=(B is N):raise T('authority_cert_issuer and authority_cert_serial_number must both be present or both None')
		if A is not N:
			A=Q(A)
			if not R(C(A,â)for A in A):raise J('authority_cert_issuer must be a list of GeneralName objects')
		if B is not N and not C(B,F):raise J('authority_cert_serial_number must be an integer')
		D._key_identifier=key_identifier;D._authority_cert_issuer=A;D._authority_cert_serial_number=B
	@q
	def from_issuer_public_key(cls,public_key:ò):A=u(public_key);return cls(key_identifier=A,authority_cert_issuer=N,authority_cert_serial_number=N)
	@q
	def from_issuer_subject_key_identifier(cls,ski:e):return cls(key_identifier=ski.digest,authority_cert_issuer=N,authority_cert_serial_number=N)
	def __repr__(A):return'<AuthorityKeyIdentifier(key_identifier={0.key_identifier!r}, authority_cert_issuer={0.authority_cert_issuer}, authority_cert_serial_number={0.authority_cert_serial_number})>'.format(A)
	def __eq__(B,other:object):
		A=other
		if not C(A,d):return L
		return B.key_identifier==A.key_identifier and B.authority_cert_issuer==A.authority_cert_issuer and B.authority_cert_serial_number==A.authority_cert_serial_number
	def __hash__(A):
		if A.authority_cert_issuer is N:B=N
		else:B=U(A.authority_cert_issuer)
		return M((A.key_identifier,B,A.authority_cert_serial_number))
	@H
	def key_identifier(self):return self._key_identifier
	@H
	def authority_cert_issuer(self):return self._authority_cert_issuer
	@H
	def authority_cert_serial_number(self):return self._authority_cert_serial_number
	def public_bytes(A):return P.encode_extension_value(A)
class e(I):
	oid=í.SUBJECT_KEY_IDENTIFIER
	def __init__(A,digest:K):A._digest=digest
	@q
	def from_public_key(cls,public_key:ñ):return cls(u(public_key))
	@H
	def digest(self):return self._digest
	@H
	def key_identifier(self):return self._digest
	def __repr__(A):return f"<SubjectKeyIdentifier(digest={A.digest!r})>"
	def __eq__(B,other:object):
		A=other
		if not C(A,e):return L
		return Ý.bytes_eq(B.digest,A.digest)
	def __hash__(A):return M(A.digest)
	def public_bytes(A):return P.encode_extension_value(A)
class w(I):
	oid=í.AUTHORITY_INFORMATION_ACCESS
	def __init__(B,descriptions:B.Iterable[X]):
		A=descriptions;A=Q(A)
		if not R(C(A,X)for A in A):raise J(Õ)
		B._descriptions=A
	__len__,__iter__,__getitem__=V(Ö)
	def __repr__(A):return f"<AuthorityInformationAccess({A._descriptions})>"
	def __eq__(B,other:object):
		A=other
		if not C(A,w):return L
		return B._descriptions==A._descriptions
	def __hash__(A):return M(U(A._descriptions))
	def public_bytes(A):return P.encode_extension_value(A)
class x(I):
	oid=í.SUBJECT_INFORMATION_ACCESS
	def __init__(B,descriptions:B.Iterable[X]):
		A=descriptions;A=Q(A)
		if not R(C(A,X)for A in A):raise J(Õ)
		B._descriptions=A
	__len__,__iter__,__getitem__=V(Ö)
	def __repr__(A):return f"<SubjectInformationAccess({A._descriptions})>"
	def __eq__(B,other:object):
		A=other
		if not C(A,x):return L
		return B._descriptions==A._descriptions
	def __hash__(A):return M(U(A._descriptions))
	def public_bytes(A):return P.encode_extension_value(A)
class X:
	def __init__(A,access_method:ì,access_location:â):
		D=access_location;B=access_method
		if not C(B,ì):raise J('access_method must be an ObjectIdentifier')
		if not C(D,â):raise J('access_location must be a GeneralName')
		A._access_method=B;A._access_location=D
	def __repr__(A):return'<AccessDescription(access_method={0.access_method}, access_location={0.access_location})>'.format(A)
	def __eq__(B,other:object):
		A=other
		if not C(A,X):return L
		return B.access_method==A.access_method and B.access_location==A.access_location
	def __hash__(A):return M((A.access_method,A.access_location))
	@H
	def access_method(self):return self._access_method
	@H
	def access_location(self):return self._access_location
class z(I):
	oid=í.BASIC_CONSTRAINTS
	def __init__(B,ca:D,path_length:B.Optional[F]):
		A=path_length
		if not C(ca,D):raise J('ca must be a boolean value')
		if A is not N and not ca:raise T('path_length must be None when ca is False')
		if A is not N and(not C(A,F)or A<0):raise J('path_length must be a non-negative integer or None')
		B._ca=ca;B._path_length=A
	@H
	def ca(self):return self._ca
	@H
	def path_length(self):return self._path_length
	def __repr__(A):return'<BasicConstraints(ca={0.ca}, path_length={0.path_length})>'.format(A)
	def __eq__(B,other:object):
		A=other
		if not C(A,z):return L
		return B.ca==A.ca and B.path_length==A.path_length
	def __hash__(A):return M((A.ca,A.path_length))
	def public_bytes(A):return P.encode_extension_value(A)
class ª(I):
	oid=í.DELTA_CRL_INDICATOR
	def __init__(B,crl_number:F):
		A=crl_number
		if not C(A,F):raise J(Ô)
		B._crl_number=A
	@H
	def crl_number(self):return self._crl_number
	def __eq__(B,other:object):
		A=other
		if not C(A,ª):return L
		return B.crl_number==A.crl_number
	def __hash__(A):return M(A.crl_number)
	def __repr__(A):return f"<DeltaCRLIndicator(crl_number={A.crl_number})>"
	def public_bytes(A):return P.encode_extension_value(A)
class µ(I):
	oid=í.CRL_DISTRIBUTION_POINTS
	def __init__(B,distribution_points:B.Iterable[Y]):
		A=distribution_points;A=Q(A)
		if not R(C(A,Y)for A in A):raise J(Ø)
		B._distribution_points=A
	__len__,__iter__,__getitem__=V(Ù)
	def __repr__(A):return f"<CRLDistributionPoints({A._distribution_points})>"
	def __eq__(B,other:object):
		A=other
		if not C(A,µ):return L
		return B._distribution_points==A._distribution_points
	def __hash__(A):return M(U(A._distribution_points))
	def public_bytes(A):return P.encode_extension_value(A)
class º(I):
	oid=í.FRESHEST_CRL
	def __init__(B,distribution_points:B.Iterable[Y]):
		A=distribution_points;A=Q(A)
		if not R(C(A,Y)for A in A):raise J(Ø)
		B._distribution_points=A
	__len__,__iter__,__getitem__=V(Ù)
	def __repr__(A):return f"<FreshestCRL({A._distribution_points})>"
	def __eq__(B,other:object):
		A=other
		if not C(A,º):return L
		return B._distribution_points==A._distribution_points
	def __hash__(A):return M(U(A._distribution_points))
	def public_bytes(A):return P.encode_extension_value(A)
class Y:
	def __init__(G,full_name:B.Optional[B.Iterable[â]],relative_name:B.Optional[E],reasons:B.Optional[B.FrozenSet[O]],crl_issuer:B.Optional[B.Iterable[â]]):
		F=relative_name;D=crl_issuer;B=reasons;A=full_name
		if A and F:raise T('You cannot provide both full_name and relative_name, at least one must be None.')
		if not A and not F and not D:raise T('Either full_name, relative_name or crl_issuer must be provided.')
		if A is not N:
			A=Q(A)
			if not R(C(A,â)for A in A):raise J('full_name must be a list of GeneralName objects')
		if F:
			if not C(F,E):raise J('relative_name must be a RelativeDistinguishedName')
		if D is not N:
			D=Q(D)
			if not R(C(A,â)for A in D):raise J('crl_issuer must be None or a list of general names')
		if B and(not C(B,Ó)or not R(C(A,O)for A in B)):raise J('reasons must be None or frozenset of ReasonFlags')
		if B and(O.unspecified in B or O.remove_from_crl in B):raise T('unspecified and remove_from_crl are not valid reasons in a DistributionPoint')
		G._full_name=A;G._relative_name=F;G._reasons=B;G._crl_issuer=D
	def __repr__(A):return'<DistributionPoint(full_name={0.full_name}, relative_name={0.relative_name}, reasons={0.reasons}, crl_issuer={0.crl_issuer})>'.format(A)
	def __eq__(B,other:object):
		A=other
		if not C(A,Y):return L
		return B.full_name==A.full_name and B.relative_name==A.relative_name and B.reasons==A.reasons and B.crl_issuer==A.crl_issuer
	def __hash__(A):
		if A.full_name is not N:C=U(A.full_name)
		else:C=N
		if A.crl_issuer is not N:D=U(A.crl_issuer)
		else:D=N
		return M((C,A.relative_name,A.reasons,D))
	@H
	def full_name(self):return self._full_name
	@H
	def relative_name(self):return self._relative_name
	@H
	def reasons(self):return self._reasons
	@H
	def crl_issuer(self):return self._crl_issuer
class O(t.Enum):unspecified='unspecified';key_compromise='keyCompromise';ca_compromise='cACompromise';affiliation_changed='affiliationChanged';superseded='superseded';cessation_of_operation='cessationOfOperation';certificate_hold='certificateHold';privilege_withdrawn='privilegeWithdrawn';aa_compromise='aACompromise';remove_from_crl='removeFromCRL'
ß={1:O.key_compromise,2:O.ca_compromise,3:O.affiliation_changed,4:O.superseded,5:O.cessation_of_operation,6:O.certificate_hold,7:O.privilege_withdrawn,8:O.aa_compromise}
à={O.key_compromise:1,O.ca_compromise:2,O.affiliation_changed:3,O.superseded:4,O.cessation_of_operation:5,O.certificate_hold:6,O.privilege_withdrawn:7,O.aa_compromise:8}
class À(I):
	oid=í.POLICY_CONSTRAINTS
	def __init__(D,require_explicit_policy:B.Optional[F],inhibit_policy_mapping:B.Optional[F]):
		B=inhibit_policy_mapping;A=require_explicit_policy
		if A is not N and not C(A,F):raise J('require_explicit_policy must be a non-negative integer or None')
		if B is not N and not C(B,F):raise J('inhibit_policy_mapping must be a non-negative integer or None')
		if B is N and A is N:raise T('At least one of require_explicit_policy and inhibit_policy_mapping must not be None')
		D._require_explicit_policy=A;D._inhibit_policy_mapping=B
	def __repr__(A):return'<PolicyConstraints(require_explicit_policy={0.require_explicit_policy}, inhibit_policy_mapping={0.inhibit_policy_mapping})>'.format(A)
	def __eq__(B,other:object):
		A=other
		if not C(A,À):return L
		return B.require_explicit_policy==A.require_explicit_policy and B.inhibit_policy_mapping==A.inhibit_policy_mapping
	def __hash__(A):return M((A.require_explicit_policy,A.inhibit_policy_mapping))
	@H
	def require_explicit_policy(self):return self._require_explicit_policy
	@H
	def inhibit_policy_mapping(self):return self._inhibit_policy_mapping
	def public_bytes(A):return P.encode_extension_value(A)
class Á(I):
	oid=í.CERTIFICATE_POLICIES
	def __init__(B,policies:B.Iterable[f]):
		A=policies;A=Q(A)
		if not R(C(A,f)for A in A):raise J('Every item in the policies list must be a PolicyInformation')
		B._policies=A
	__len__,__iter__,__getitem__=V('_policies')
	def __repr__(A):return f"<CertificatePolicies({A._policies})>"
	def __eq__(B,other:object):
		A=other
		if not C(A,Á):return L
		return B._policies==A._policies
	def __hash__(A):return M(U(A._policies))
	def public_bytes(A):return P.encode_extension_value(A)
class f:
	def __init__(B,policy_identifier:ì,policy_qualifiers:B.Optional[B.Iterable[B.Union[G,Z]]]):
		D=policy_identifier;A=policy_qualifiers
		if not C(D,ì):raise J('policy_identifier must be an ObjectIdentifier')
		B._policy_identifier=D
		if A is not N:
			A=Q(A)
			if not R(C(A,(G,Z))for A in A):raise J('policy_qualifiers must be a list of strings and/or UserNotice objects or None')
		B._policy_qualifiers=A
	def __repr__(A):return'<PolicyInformation(policy_identifier={0.policy_identifier}, policy_qualifiers={0.policy_qualifiers})>'.format(A)
	def __eq__(B,other:object):
		A=other
		if not C(A,f):return L
		return B.policy_identifier==A.policy_identifier and B.policy_qualifiers==A.policy_qualifiers
	def __hash__(A):
		if A.policy_qualifiers is not N:C=U(A.policy_qualifiers)
		else:C=N
		return M((A.policy_identifier,C))
	@H
	def policy_identifier(self):return self._policy_identifier
	@H
	def policy_qualifiers(self):return self._policy_qualifiers
class Z:
	def __init__(B,notice_reference:B.Optional[b],explicit_text:B.Optional[G]):
		A=notice_reference
		if A and not C(A,b):raise J('notice_reference must be None or a NoticeReference')
		B._notice_reference=A;B._explicit_text=explicit_text
	def __repr__(A):return'<UserNotice(notice_reference={0.notice_reference}, explicit_text={0.explicit_text!r})>'.format(A)
	def __eq__(B,other:object):
		A=other
		if not C(A,Z):return L
		return B.notice_reference==A.notice_reference and B.explicit_text==A.explicit_text
	def __hash__(A):return M((A.notice_reference,A.explicit_text))
	@H
	def notice_reference(self):return self._notice_reference
	@H
	def explicit_text(self):return self._explicit_text
class b:
	def __init__(B,organization:B.Optional[G],notice_numbers:B.Iterable[F]):
		A=notice_numbers;B._organization=organization;A=Q(A)
		if not R(C(A,F)for A in A):raise J('notice_numbers must be a list of integers')
		B._notice_numbers=A
	def __repr__(A):return'<NoticeReference(organization={0.organization!r}, notice_numbers={0.notice_numbers})>'.format(A)
	def __eq__(B,other:object):
		A=other
		if not C(A,b):return L
		return B.organization==A.organization and B.notice_numbers==A.notice_numbers
	def __hash__(A):return M((A.organization,U(A.notice_numbers)))
	@H
	def organization(self):return self._organization
	@H
	def notice_numbers(self):return self._notice_numbers
class Â(I):
	oid=í.EXTENDED_KEY_USAGE
	def __init__(B,usages:B.Iterable[ì]):
		A=usages;A=Q(A)
		if not R(C(A,ì)for A in A):raise J('Every item in the usages list must be an ObjectIdentifier')
		B._usages=A
	__len__,__iter__,__getitem__=V('_usages')
	def __repr__(A):return f"<ExtendedKeyUsage({A._usages})>"
	def __eq__(B,other:object):
		A=other
		if not C(A,Â):return L
		return B._usages==A._usages
	def __hash__(A):return M(U(A._usages))
	def public_bytes(A):return P.encode_extension_value(A)
class l(I):
	oid=í.OCSP_NO_CHECK
	def __eq__(A,other:object):
		if not C(other,l):return L
		return r
	def __hash__(A):return M(l)
	def __repr__(A):return'<OCSPNoCheck()>'
	def public_bytes(A):return P.encode_extension_value(A)
class m(I):
	oid=í.PRECERT_POISON
	def __eq__(A,other:object):
		if not C(other,m):return L
		return r
	def __hash__(A):return M(m)
	def __repr__(A):return'<PrecertPoison()>'
	def public_bytes(A):return P.encode_extension_value(A)
class Ã(I):
	oid=í.TLS_FEATURE
	def __init__(B,features:B.Iterable[g]):
		A=features;A=Q(A)
		if not R(C(A,g)for A in A)or o(A)==0:raise J('features must be a list of elements from the TLSFeatureType enum')
		B._features=A
	__len__,__iter__,__getitem__=V('_features')
	def __repr__(A):return f"<TLSFeature(features={A._features})>"
	def __eq__(B,other:object):
		A=other
		if not C(A,Ã):return L
		return B._features==A._features
	def __hash__(A):return M(U(A._features))
	def public_bytes(A):return P.encode_extension_value(A)
class g(t.Enum):status_request=5;status_request_v2=17
á={A.value:A for A in g}
class Ä(I):
	oid=í.INHIBIT_ANY_POLICY
	def __init__(B,skip_certs:F):
		A=skip_certs
		if not C(A,F):raise J('skip_certs must be an integer')
		if A<0:raise T('skip_certs must be a non-negative integer')
		B._skip_certs=A
	def __repr__(A):return f"<InhibitAnyPolicy(skip_certs={A.skip_certs})>"
	def __eq__(B,other:object):
		A=other
		if not C(A,Ä):return L
		return B.skip_certs==A.skip_certs
	def __hash__(A):return M(A.skip_certs)
	@H
	def skip_certs(self):return self._skip_certs
	def public_bytes(A):return P.encode_extension_value(A)
class Å(I):
	oid=í.KEY_USAGE
	def __init__(A,digital_signature:D,content_commitment:D,key_encipherment:D,data_encipherment:D,key_agreement:D,key_cert_sign:D,crl_sign:D,encipher_only:D,decipher_only:D):
		D=decipher_only;C=encipher_only;B=key_agreement
		if not B and(C or D):raise T('encipher_only and decipher_only can only be true when key_agreement is true')
		A._digital_signature=digital_signature;A._content_commitment=content_commitment;A._key_encipherment=key_encipherment;A._data_encipherment=data_encipherment;A._key_agreement=B;A._key_cert_sign=key_cert_sign;A._crl_sign=crl_sign;A._encipher_only=C;A._decipher_only=D
	@H
	def digital_signature(self):return self._digital_signature
	@H
	def content_commitment(self):return self._content_commitment
	@H
	def key_encipherment(self):return self._key_encipherment
	@H
	def data_encipherment(self):return self._data_encipherment
	@H
	def key_agreement(self):return self._key_agreement
	@H
	def key_cert_sign(self):return self._key_cert_sign
	@H
	def crl_sign(self):return self._crl_sign
	@H
	def encipher_only(self):
		if not self.key_agreement:raise T('encipher_only is undefined unless key_agreement is true')
		else:return self._encipher_only
	@H
	def decipher_only(self):
		if not self.key_agreement:raise T('decipher_only is undefined unless key_agreement is true')
		else:return self._decipher_only
	def __repr__(A):
		D=False
		try:B=A.encipher_only;C=A.decipher_only
		except T:B=D;C=D
		return'<KeyUsage(digital_signature={0.digital_signature}, content_commitment={0.content_commitment}, key_encipherment={0.key_encipherment}, data_encipherment={0.data_encipherment}, key_agreement={0.key_agreement}, key_cert_sign={0.key_cert_sign}, crl_sign={0.crl_sign}, encipher_only={1}, decipher_only={2})>'.format(A,B,C)
	def __eq__(B,other:object):
		A=other
		if not C(A,Å):return L
		return B.digital_signature==A.digital_signature and B.content_commitment==A.content_commitment and B.key_encipherment==A.key_encipherment and B.data_encipherment==A.data_encipherment and B.key_agreement==A.key_agreement and B.key_cert_sign==A.key_cert_sign and B.crl_sign==A.crl_sign and B._encipher_only==A._encipher_only and B._decipher_only==A._decipher_only
	def __hash__(A):return M((A.digital_signature,A.content_commitment,A.key_encipherment,A.data_encipherment,A.key_agreement,A.key_cert_sign,A.crl_sign,A._encipher_only,A._decipher_only))
	def public_bytes(A):return P.encode_extension_value(A)
class Æ(I):
	oid=í.NAME_CONSTRAINTS
	def __init__(D,permitted_subtrees:B.Optional[B.Iterable[â]],excluded_subtrees:B.Optional[B.Iterable[â]]):
		B=excluded_subtrees;A=permitted_subtrees
		if A is not N:
			A=Q(A)
			if not A:raise T('permitted_subtrees must be a non-empty list or None')
			if not R(C(A,â)for A in A):raise J('permitted_subtrees must be a list of GeneralName objects or None')
			D._validate_tree(A)
		if B is not N:
			B=Q(B)
			if not B:raise T('excluded_subtrees must be a non-empty list or None')
			if not R(C(A,â)for A in B):raise J('excluded_subtrees must be a list of GeneralName objects or None')
			D._validate_tree(B)
		if A is N and B is N:raise T('At least one of permitted_subtrees and excluded_subtrees must not be None')
		D._permitted_subtrees=A;D._excluded_subtrees=B
	def __eq__(B,other:object):
		A=other
		if not C(A,Æ):return L
		return B.excluded_subtrees==A.excluded_subtrees and B.permitted_subtrees==A.permitted_subtrees
	def _validate_tree(A,tree:B.Iterable[â]):A._validate_ip_name(tree);A._validate_dns_name(tree)
	def _validate_ip_name(A,tree:B.Iterable[â]):
		if h(C(A,ç)and not C(A.value,(s.IPv4Network,s.IPv6Network))for A in tree):raise J('IPAddress name constraints must be an IPv4Network or IPv6Network object')
	def _validate_dns_name(A,tree:B.Iterable[â]):
		if h(C(A,ä)and'*'in A.value for A in tree):raise T("DNSName name constraints must not contain the '*' wildcard character")
	def __repr__(A):return'<NameConstraints(permitted_subtrees={0.permitted_subtrees}, excluded_subtrees={0.excluded_subtrees})>'.format(A)
	def __hash__(A):
		if A.permitted_subtrees is not N:C=U(A.permitted_subtrees)
		else:C=N
		if A.excluded_subtrees is not N:D=U(A.excluded_subtrees)
		else:D=N
		return M((C,D))
	@H
	def permitted_subtrees(self):return self._permitted_subtrees
	@H
	def excluded_subtrees(self):return self._excluded_subtrees
	def public_bytes(A):return P.encode_extension_value(A)
class S(B.Generic[a]):
	def __init__(A,oid:ì,critical:D,value:a):
		B=critical
		if not C(oid,ì):raise J('oid argument must be an ObjectIdentifier instance.')
		if not C(B,D):raise J('critical must be a boolean value')
		A._oid=oid;A._critical=B;A._value=value
	@H
	def oid(self):return self._oid
	@H
	def critical(self):return self._critical
	@H
	def value(self):return self._value
	def __repr__(A):return'<Extension(oid={0.oid}, critical={0.critical}, value={0.value})>'.format(A)
	def __eq__(B,other:object):
		A=other
		if not C(A,S):return L
		return B.oid==A.oid and B.critical==A.critical and B.value==A.value
	def __hash__(A):return M((A.oid,A.critical,A.value))
class c:
	def __init__(B,general_names:B.Iterable[â]):
		A=general_names;A=Q(A)
		if not R(C(A,â)for A in A):raise J('Every item in the general_names list must be an object conforming to the GeneralName interface')
		B._general_names=A
	__len__,__iter__,__getitem__=V(i)
	@B.overload
	def get_values_for_type(self,type:B.Union[B.Type[ä],B.Type[æ],B.Type[å]]):0
	@B.overload
	def get_values_for_type(self,type:B.Type[é]):0
	@B.overload
	def get_values_for_type(self,type:B.Type[ê]):0
	@B.overload
	def get_values_for_type(self,type:B.Type[ç]):0
	@B.overload
	def get_values_for_type(self,type:B.Type[ã]):0
	def get_values_for_type(B,type:B.Union[B.Type[ä],B.Type[é],B.Type[ç],B.Type[ã],B.Type[å],B.Type[ê],B.Type[æ]]):
		A=(A for A in B if C(A,type))
		if type!=ã:return[A.value for A in A]
		return Q(A)
	def __repr__(A):return f"<GeneralNames({A._general_names})>"
	def __eq__(B,other:object):
		A=other
		if not C(A,c):return L
		return B._general_names==A._general_names
	def __hash__(A):return M(U(A._general_names))
class Ç(I):
	oid=í.SUBJECT_ALTERNATIVE_NAME
	def __init__(A,general_names:B.Iterable[â]):A._general_names=c(general_names)
	__len__,__iter__,__getitem__=V(i)
	@B.overload
	def get_values_for_type(self,type:B.Union[B.Type[ä],B.Type[æ],B.Type[å]]):0
	@B.overload
	def get_values_for_type(self,type:B.Type[é]):0
	@B.overload
	def get_values_for_type(self,type:B.Type[ê]):0
	@B.overload
	def get_values_for_type(self,type:B.Type[ç]):0
	@B.overload
	def get_values_for_type(self,type:B.Type[ã]):0
	def get_values_for_type(A,type:B.Union[B.Type[ä],B.Type[é],B.Type[ç],B.Type[ã],B.Type[å],B.Type[ê],B.Type[æ]]):return A._general_names.get_values_for_type(type)
	def __repr__(A):return f"<SubjectAlternativeName({A._general_names})>"
	def __eq__(B,other:object):
		A=other
		if not C(A,Ç):return L
		return B._general_names==A._general_names
	def __hash__(A):return M(A._general_names)
	def public_bytes(A):return P.encode_extension_value(A)
class È(I):
	oid=í.ISSUER_ALTERNATIVE_NAME
	def __init__(A,general_names:B.Iterable[â]):A._general_names=c(general_names)
	__len__,__iter__,__getitem__=V(i)
	@B.overload
	def get_values_for_type(self,type:B.Union[B.Type[ä],B.Type[æ],B.Type[å]]):0
	@B.overload
	def get_values_for_type(self,type:B.Type[é]):0
	@B.overload
	def get_values_for_type(self,type:B.Type[ê]):0
	@B.overload
	def get_values_for_type(self,type:B.Type[ç]):0
	@B.overload
	def get_values_for_type(self,type:B.Type[ã]):0
	def get_values_for_type(A,type:B.Union[B.Type[ä],B.Type[é],B.Type[ç],B.Type[ã],B.Type[å],B.Type[ê],B.Type[æ]]):return A._general_names.get_values_for_type(type)
	def __repr__(A):return f"<IssuerAlternativeName({A._general_names})>"
	def __eq__(B,other:object):
		A=other
		if not C(A,È):return L
		return B._general_names==A._general_names
	def __hash__(A):return M(A._general_names)
	def public_bytes(A):return P.encode_extension_value(A)
class É(I):
	oid=î.CERTIFICATE_ISSUER
	def __init__(A,general_names:B.Iterable[â]):A._general_names=c(general_names)
	__len__,__iter__,__getitem__=V(i)
	@B.overload
	def get_values_for_type(self,type:B.Union[B.Type[ä],B.Type[æ],B.Type[å]]):0
	@B.overload
	def get_values_for_type(self,type:B.Type[é]):0
	@B.overload
	def get_values_for_type(self,type:B.Type[ê]):0
	@B.overload
	def get_values_for_type(self,type:B.Type[ç]):0
	@B.overload
	def get_values_for_type(self,type:B.Type[ã]):0
	def get_values_for_type(A,type:B.Union[B.Type[ä],B.Type[é],B.Type[ç],B.Type[ã],B.Type[å],B.Type[ê],B.Type[æ]]):return A._general_names.get_values_for_type(type)
	def __repr__(A):return f"<CertificateIssuer({A._general_names})>"
	def __eq__(B,other:object):
		A=other
		if not C(A,É):return L
		return B._general_names==A._general_names
	def __hash__(A):return M(A._general_names)
	def public_bytes(A):return P.encode_extension_value(A)
class Ê(I):
	oid=î.CRL_REASON
	def __init__(B,reason:O):
		A=reason
		if not C(A,O):raise J('reason must be an element from ReasonFlags')
		B._reason=A
	def __repr__(A):return f"<CRLReason(reason={A._reason})>"
	def __eq__(B,other:object):
		A=other
		if not C(A,Ê):return L
		return B.reason==A.reason
	def __hash__(A):return M(A.reason)
	@H
	def reason(self):return self._reason
	def public_bytes(A):return P.encode_extension_value(A)
class Ë(I):
	oid=î.INVALIDITY_DATE
	def __init__(B,invalidity_date:j.datetime):
		A=invalidity_date
		if not C(A,j.datetime):raise J('invalidity_date must be a datetime.datetime')
		B._invalidity_date=A
	def __repr__(A):return'<InvalidityDate(invalidity_date={})>'.format(A._invalidity_date)
	def __eq__(B,other:object):
		A=other
		if not C(A,Ë):return L
		return B.invalidity_date==A.invalidity_date
	def __hash__(A):return M(A.invalidity_date)
	@H
	def invalidity_date(self):return self._invalidity_date
	def public_bytes(A):return P.encode_extension_value(A)
class Ì(I):
	oid=í.PRECERT_SIGNED_CERTIFICATE_TIMESTAMPS
	def __init__(B,signed_certificate_timestamps:B.Iterable[ë]):
		A=signed_certificate_timestamps;A=Q(A)
		if not R(C(A,ë)for A in A):raise J(Ú)
		B._signed_certificate_timestamps=A
	__len__,__iter__,__getitem__=V(Û)
	def __repr__(A):return'<PrecertificateSignedCertificateTimestamps({})>'.format(Q(A))
	def __hash__(A):return M(U(A._signed_certificate_timestamps))
	def __eq__(B,other:object):
		A=other
		if not C(A,Ì):return L
		return B._signed_certificate_timestamps==A._signed_certificate_timestamps
	def public_bytes(A):return P.encode_extension_value(A)
class Í(I):
	oid=í.SIGNED_CERTIFICATE_TIMESTAMPS
	def __init__(B,signed_certificate_timestamps:B.Iterable[ë]):
		A=signed_certificate_timestamps;A=Q(A)
		if not R(C(A,ë)for A in A):raise J(Ú)
		B._signed_certificate_timestamps=A
	__len__,__iter__,__getitem__=V(Û)
	def __repr__(A):return f"<SignedCertificateTimestamps({Q(A)})>"
	def __hash__(A):return M(U(A._signed_certificate_timestamps))
	def __eq__(B,other:object):
		A=other
		if not C(A,Í):return L
		return B._signed_certificate_timestamps==A._signed_certificate_timestamps
	def public_bytes(A):return P.encode_extension_value(A)
class Î(I):
	oid=ï.NONCE
	def __init__(B,nonce:K):
		A=nonce
		if not C(A,K):raise J('nonce must be bytes')
		B._nonce=A
	def __eq__(B,other:object):
		A=other
		if not C(A,Î):return L
		return B.nonce==A.nonce
	def __hash__(A):return M(A.nonce)
	def __repr__(A):return f"<OCSPNonce(nonce={A.nonce!r})>"
	@H
	def nonce(self):return self._nonce
	def public_bytes(A):return P.encode_extension_value(A)
class Ï(I):
	oid=ï.ACCEPTABLE_RESPONSES
	def __init__(B,responses:B.Iterable[ì]):
		A=responses;A=Q(A)
		if h(not C(A,ì)for A in A):raise J('All responses must be ObjectIdentifiers')
		B._responses=A
	def __eq__(B,other:object):
		A=other
		if not C(A,Ï):return L
		return B._responses==A._responses
	def __hash__(A):return M(U(A._responses))
	def __repr__(A):return f"<OCSPAcceptableResponses(responses={A._responses})>"
	def __iter__(A):return iter(A._responses)
	def public_bytes(A):return P.encode_extension_value(A)
class Ð(I):
	oid=í.ISSUING_DISTRIBUTION_POINT
	def __init__(B,full_name:B.Optional[B.Iterable[â]],relative_name:B.Optional[E],only_contains_user_certs:D,only_contains_ca_certs:D,only_some_reasons:B.Optional[B.FrozenSet[O]],indirect_crl:D,only_contains_attribute_certs:D):
		K=relative_name;I=only_contains_attribute_certs;H=indirect_crl;G=only_contains_ca_certs;F=only_contains_user_certs;E=full_name;A=only_some_reasons
		if E is not N:E=Q(E)
		if A and(not C(A,Ó)or not R(C(A,O)for A in A)):raise J('only_some_reasons must be None or frozenset of ReasonFlags')
		if A and(O.unspecified in A or O.remove_from_crl in A):raise T('unspecified and remove_from_crl are not valid reasons in an IssuingDistributionPoint')
		if not(C(F,D)and C(G,D)and C(H,D)and C(I,D)):raise J('only_contains_user_certs, only_contains_ca_certs, indirect_crl and only_contains_attribute_certs must all be boolean.')
		L=[F,G,H,I]
		if o([A for A in L if A])>1:raise T('Only one of the following can be set to True: only_contains_user_certs, only_contains_ca_certs, indirect_crl, only_contains_attribute_certs')
		if not h([F,G,H,I,E,K,A]):raise T('Cannot create empty extension: if only_contains_user_certs, only_contains_ca_certs, indirect_crl, and only_contains_attribute_certs are all False, then either full_name, relative_name, or only_some_reasons must have a value.')
		B._only_contains_user_certs=F;B._only_contains_ca_certs=G;B._indirect_crl=H;B._only_contains_attribute_certs=I;B._only_some_reasons=A;B._full_name=E;B._relative_name=K
	def __repr__(A):return'<IssuingDistributionPoint(full_name={0.full_name}, relative_name={0.relative_name}, only_contains_user_certs={0.only_contains_user_certs}, only_contains_ca_certs={0.only_contains_ca_certs}, only_some_reasons={0.only_some_reasons}, indirect_crl={0.indirect_crl}, only_contains_attribute_certs={0.only_contains_attribute_certs})>'.format(A)
	def __eq__(B,other:object):
		A=other
		if not C(A,Ð):return L
		return B.full_name==A.full_name and B.relative_name==A.relative_name and B.only_contains_user_certs==A.only_contains_user_certs and B.only_contains_ca_certs==A.only_contains_ca_certs and B.only_some_reasons==A.only_some_reasons and B.indirect_crl==A.indirect_crl and B.only_contains_attribute_certs==A.only_contains_attribute_certs
	def __hash__(A):return M((A.full_name,A.relative_name,A.only_contains_user_certs,A.only_contains_ca_certs,A.only_some_reasons,A.indirect_crl,A.only_contains_attribute_certs))
	@H
	def full_name(self):return self._full_name
	@H
	def relative_name(self):return self._relative_name
	@H
	def only_contains_user_certs(self):return self._only_contains_user_certs
	@H
	def only_contains_ca_certs(self):return self._only_contains_ca_certs
	@H
	def only_some_reasons(self):return self._only_some_reasons
	@H
	def indirect_crl(self):return self._indirect_crl
	@H
	def only_contains_attribute_certs(self):return self._only_contains_attribute_certs
	def public_bytes(A):return P.encode_extension_value(A)
class Ñ(I):
	oid=í.MS_CERTIFICATE_TEMPLATE
	def __init__(A,template_id:ì,major_version:B.Optional[F],minor_version:B.Optional[F]):
		E=template_id;D=minor_version;B=major_version
		if not C(E,ì):raise J(Ü)
		A._template_id=E
		if B is not N and not C(B,F)or D is not N and not C(D,F):raise J('major_version and minor_version must be integers or None')
		A._major_version=B;A._minor_version=D
	@H
	def template_id(self):return self._template_id
	@H
	def major_version(self):return self._major_version
	@H
	def minor_version(self):return self._minor_version
	def __repr__(A):return f"<MSCertificateTemplate(template_id={A.template_id}, major_version={A.major_version}, minor_version={A.minor_version})>"
	def __eq__(B,other:object):
		A=other
		if not C(A,Ñ):return L
		return B.template_id==A.template_id and B.major_version==A.major_version and B.minor_version==A.minor_version
	def __hash__(A):return M((A.template_id,A.major_version,A.minor_version))
	def public_bytes(A):return P.encode_extension_value(A)
class n(I):
	def __init__(A,oid:ì,value:K):
		if not C(oid,ì):raise J(Ü)
		A._oid=oid;A._value=value
	@H
	def oid(self):return self._oid
	@H
	def value(self):return self._value
	def __repr__(A):return'<UnrecognizedExtension(oid={0.oid}, value={0.value!r})>'.format(A)
	def __eq__(B,other:object):
		A=other
		if not C(A,n):return L
		return B.oid==A.oid and B.value==A.value
	def __hash__(A):return M((A.oid,A.value))
	def public_bytes(A):return A.value