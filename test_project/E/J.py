M=getattr
L=ImportError
H='Unknown'
E=''
B=None
A='version'
import json,platform as C,ssl,sys as D,idna,G as U
from.import __version__ as requests_version
I=B
try:import B as G
except L:G=B
try:from G.G import pyopenssl as J
except L:J=B;F=B;K=B
else:import C as K,OpenSSL as F
def V():
	F=C.python_implementation()
	if F=='CPython':B=C.python_version()
	elif F=='PyPy':
		B='{}.{}.{}'.format(D.pypy_version_info.major,D.pypy_version_info.minor,D.pypy_version_info.micro)
		if D.pypy_version_info.releaselevel!='final':B=E.join([B,D.pypy_version_info.releaselevel])
	elif F=='Jython':B=C.python_version()
	elif F=='IronPython':B=C.python_version()
	else:B=H
	return{'name':F,A:B}
def N():
	T='__version__';S='openssl_version';R='release';Q='system'
	try:D={Q:C.system(),R:C.release()}
	except OSError:D={Q:H,R:H}
	W=V();X={A:U.__version__};L={A:B};N={A:B}
	if I:L={A:I.__version__}
	if G:N={A:G.__version__}
	O={A:B,S:E}
	if F:O={A:F.__version__,S:f"{F.SSL.OPENSSL_VERSION_NUMBER:x}"}
	Y={A:M(K,T,E)};Z={A:M(idna,T,E)};P=ssl.OPENSSL_VERSION_NUMBER;a={A:f"{P:x}"if P is not B else E};return{'platform':D,'implementation':W,'system_ssl':a,'using_pyopenssl':J is not B,'using_charset_normalizer':False,'pyOpenSSL':O,'urllib3':X,'chardet':N,'charset_normalizer':L,'cryptography':Y,'idna':Z,'requests':{A:requests_version}}
def O():print(json.dumps(N(),sort_keys=True,indent=2))
if __name__=='__main__':O()