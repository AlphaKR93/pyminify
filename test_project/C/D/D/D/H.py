import typing as B
from C import utils as A
from C.D.D.D import dh,dsa as C,ec as D,ed448 as E,ed25519 as G,rsa as H,x448 as I,x25519 as J
F=B.Union[dh.DHPublicKey,C.DSAPublicKey,H.RSAPublicKey,D.EllipticCurvePublicKey,G.Ed25519PublicKey,E.Ed448PublicKey,J.X25519PublicKey,I.X448PublicKey]
K=F
A.deprecated(K,__name__,'Use PublicKeyTypes instead',A.DeprecatedIn40,name='PUBLIC_KEY_TYPES')
c=B.Union[dh.DHPrivateKey,G.Ed25519PrivateKey,E.Ed448PrivateKey,H.RSAPrivateKey,C.DSAPrivateKey,D.EllipticCurvePrivateKey,J.X25519PrivateKey,I.X448PrivateKey]
L=c
A.deprecated(L,__name__,'Use PrivateKeyTypes instead',A.DeprecatedIn40,name='PRIVATE_KEY_TYPES')
q=B.Union[G.Ed25519PrivateKey,E.Ed448PrivateKey,H.RSAPrivateKey,C.DSAPrivateKey,D.EllipticCurvePrivateKey]
M=q
A.deprecated(M,__name__,'Use CertificateIssuerPrivateKeyTypes instead',A.DeprecatedIn40,name='CERTIFICATE_PRIVATE_KEY_TYPES')
ò=B.Union[C.DSAPublicKey,H.RSAPublicKey,D.EllipticCurvePublicKey,G.Ed25519PublicKey,E.Ed448PublicKey]
N=ò
A.deprecated(N,__name__,'Use CertificateIssuerPublicKeyTypes instead',A.DeprecatedIn40,name='CERTIFICATE_ISSUER_PUBLIC_KEY_TYPES')
ñ=B.Union[C.DSAPublicKey,H.RSAPublicKey,D.EllipticCurvePublicKey,G.Ed25519PublicKey,E.Ed448PublicKey,J.X25519PublicKey,I.X448PublicKey]
O=ñ
A.deprecated(O,__name__,'Use CertificatePublicKeyTypes instead',A.DeprecatedIn40,name='CERTIFICATE_PUBLIC_KEY_TYPES')