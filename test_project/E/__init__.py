S=ValueError
P=None
O=ImportError
M='.'
J=int
import warnings as L,G as Q
from.I import E
R=P
try:from B import __version__ as N
except O:N=P
def T(urllib3_version,chardet_version,charset_normalizer_version):
	F=charset_normalizer_version;E=chardet_version;D=urllib3_version;D=D.split(M);assert D!=['dev']
	if len(D)==2:D.append('0')
	A,B,C=D;A,B,C=J(A),J(B),J(C);assert A>=1
	if A==1:assert B>=21
	if E:A,B,C=E.split(M)[:3];A,B,C=J(A),J(B),J(C);assert(3,0,2)<=(A,B,C)<(6,0,0)
	elif F:A,B,C=F.split(M)[:3];A,B,C=J(A),J(B),J(C);assert(2,0,0)<=(A,B,C)<(4,0,0)
	else:raise Exception('You need either charset_normalizer or chardet installed')
def V(cryptography_version):
	A=cryptography_version
	try:A=list(map(J,A.split(M)))
	except S:return
	if A<[1,3,4]:B='Old version of cryptography ({}) may cause slowdown.'.format(A);L.warn(B,E)
try:T(Q.__version__,N,R)
except(AssertionError,S):L.warn("urllib3 ({}) or chardet ({})/charset_normalizer ({}) doesn't match a supported version!".format(Q.__version__,N,R),E)
try:
	try:import ssl
	except O:ssl=P
	if not getattr(ssl,'HAS_SNI',False):from G.G import pyopenssl as W;W.inject_into_urllib3();from C import __version__ as cryptography_version;V(cryptography_version)
except O:pass
from G.H import U
L.simplefilter('ignore',U)
import logging as X
from logging import NullHandler as Y
from.import packages,utils
from.A import __author__,__author_email__,__build__,__cake__,__copyright__,__description__,__license__,__title__,__url__,__version__
from.D import G,get,head,F,patch,post,put,C
from.I import ConnectionError,r,á,K,H,s,B,D,t,I
from.L import x,y,º
from.N import d,k
from.O import A
X.getLogger(__name__).addHandler(Y())
L.simplefilter('default',á,append=True)