from __future__ import annotations
P=ImportError
M=int
J=bool
I=str
F=True
A=None
import logging as B,typing as L,warnings as E
from logging import NullHandler as N
from.import exceptions as G
from.A import C
from.B import D
from.D import __version__
from.F import Ë,w,z
from.J import K,R
from.K import O,Y,Z
from.L import v,x
from.M.C import V
from.M.E import Ï
from.M.I import Ò
try:import ssl as H
except P:pass
else:
	if not H.OPENSSL_VERSION.startswith('OpenSSL '):E.warn(f"urllib3 v2.0 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with {H.OPENSSL_VERSION!r}. See: https://github.com/urllib3/urllib3/issues/3020",G.NotOpenSSLWarning)
	elif H.OPENSSL_VERSION_INFO<(1,1,1):raise P(f"urllib3 v2.0 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with {H.OPENSSL_VERSION!r}. See: https://github.com/urllib3/urllib3/issues/2168")
try:import urllib3_secure_extra
except ModuleNotFoundError:pass
else:E.warn("'urllib3[secure]' extra is deprecated and will be removed in urllib3 v2.1.0. Read more in this issue: https://github.com/urllib3/urllib3/issues/2680",category=DeprecationWarning,stacklevel=2)
__author__='Andrey Petrov (andrey.petrov@shazow.net)'
__license__='MIT'
__version__=__version__
B.getLogger(__name__).addHandler(N())
def S(level:M=B.DEBUG):A=B.getLogger(__name__);C=B.StreamHandler();C.setFormatter(B.Formatter('%(asctime)s %(levelname)s %(message)s'));A.addHandler(C);A.setLevel(level);A.debug('Added a stderr logging handler to logger: %s',__name__);return C
del N
E.simplefilter('always',G.SecurityWarning,append=F)
E.simplefilter('default',G.InsecurePlatformWarning,append=F)
def T(category:type[Warning]=G.HTTPWarning):E.simplefilter('ignore',category)
Q=O()
def U(method:I,url:I,*,body:C|A=A,fields:K|A=A,headers:L.Mapping[I,I]|A=A,preload_content:J|A=F,decode_content:J|A=F,redirect:J|A=F,retries:Ï|J|M|A=A,timeout:Ò|float|M|A=3,json:L.Any|A=A):return Q.request(method,url,body=body,fields=fields,headers=headers,preload_content=preload_content,decode_content=decode_content,redirect=redirect,retries=retries,timeout=timeout,json=json)