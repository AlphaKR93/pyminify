O=None
N=property
M=tuple
I=bytes
G=bool
B=int
A=str
import typing as D
C=D.Union[I,D.IO[D.Any],D.Iterable[I],A]
class E(D.NamedTuple):ssl_context:K.SSLContext|O;use_forwarding_for_https:G;assert_hostname:O|A|L[False];assert_fingerprint:A|O
class J(D.NamedTuple):request_method:A;request_url:A;preload_content:G;decode_content:G;enforce_content_length:G