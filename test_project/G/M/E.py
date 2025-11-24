S=isinstance
R=frozenset
Q=Exception
P=type
O=True
K=float
E=False
D=str
C=int
B=bool
A=None
import email as U,logging as X,random as Y,re,time as T,typing as N
from itertools import takewhile as Z
from types import TracebackType as a
from..H import F,H,M,I,L,J,G
from.K import b
V=X.getLogger(__name__)
class W(N.NamedTuple):method:D|A;url:D|A;error:Q|A;status:C|A;redirect_location:D|A
class Ï:
	DEFAULT_ALLOWED_METHODS=R(['HEAD','GET','PUT','DELETE','OPTIONS','TRACE']);RETRY_AFTER_STATUS_CODES=R([413,429,503]);DEFAULT_REMOVE_HEADERS_ON_REDIRECT=R(['Cookie','Authorization','Proxy-Authorization']);DEFAULT_BACKOFF_MAX=120;DEFAULT:N.ClassVar[Ï]
	def __init__(A,total:B|C|A=10,connect:C|A=A,read:C|A=A,redirect:B|C|A=A,status:C|A=A,other:C|A=A,allowed_methods:N.Collection[D]|A=DEFAULT_ALLOWED_METHODS,status_forcelist:N.Collection[C]|A=A,backoff_factor:K=0,backoff_max:K=DEFAULT_BACKOFF_MAX,raise_on_redirect:B=O,raise_on_status:B=O,history:tuple[W,...]|A=A,respect_retry_after_header:B=O,remove_headers_on_redirect:N.Collection[D]=DEFAULT_REMOVE_HEADERS_ON_REDIRECT,backoff_jitter:K=.0):
		D=raise_on_redirect;C=total;B=redirect;A.total=C;A.connect=connect;A.read=read;A.status=status;A.other=other
		if B is E or C is E:B=0;D=E
		A.redirect=B;A.status_forcelist=status_forcelist or set();A.allowed_methods=allowed_methods;A.backoff_factor=backoff_factor;A.backoff_max=backoff_max;A.raise_on_redirect=D;A.raise_on_status=raise_on_status;A.history=history or();A.respect_retry_after_header=respect_retry_after_header;A.remove_headers_on_redirect=R(A.lower()for A in remove_headers_on_redirect);A.backoff_jitter=backoff_jitter
	def new(A,**C:N.Any):B=dict(total=A.total,connect=A.connect,read=A.read,redirect=A.redirect,status=A.status,other=A.other,allowed_methods=A.allowed_methods,status_forcelist=A.status_forcelist,backoff_factor=A.backoff_factor,backoff_max=A.backoff_max,raise_on_redirect=A.raise_on_redirect,raise_on_status=A.raise_on_status,history=A.history,remove_headers_on_redirect=A.remove_headers_on_redirect,respect_retry_after_header=A.respect_retry_after_header,backoff_jitter=A.backoff_jitter);B.update(C);return P(A)(**B)
	@classmethod
	def from_int(E,retries:Ï|B|C|A,redirect:B|C|A=O,default:Ï|B|C|A=A):
		F=default;D=redirect;C=retries
		if C is A:C=F if F is not A else E.DEFAULT
		if S(C,Ï):return C
		D=B(D)and A;G=E(C,redirect=D);V.debug('Converted retries value: %r -> %r',C,G);return G
	def get_backoff_time(B):
		C=len(list(Z(lambda x:x.redirect_location is A,reversed(B.history))))
		if C<=1:return 0
		D=B.backoff_factor*2**(C-1)
		if B.backoff_jitter!=.0:D+=Y.random()*B.backoff_jitter
		return K(max(0,min(B.backoff_max,D)))
	def parse_retry_after(G,retry_after:D):
		D=retry_after
		if re.match('^\\s*[0-9]+\\s*$',D):B=C(D)
		else:
			E=U.utils.parsedate_tz(D)
			if E is A:raise H(f"Invalid Retry-After header: {D}")
			F=U.utils.mktime_tz(E);B=F-T.time()
		B=max(B,0);return B
	def get_retry_after(C,response:v):
		B=response.headers.get('Retry-After')
		if B is A:return
		return C.parse_retry_after(B)
	def sleep_for_retry(B,response:v):
		A=B.get_retry_after(response)
		if A:T.sleep(A);return O
		return E
	def _sleep_backoff(B):
		A=B.get_backoff_time()
		if A<=0:return
		T.sleep(A)
	def sleep(A,response:v|A=A):
		B=response
		if A.respect_retry_after_header and B:
			C=A.sleep_for_retry(B)
			if C:return
		A._sleep_backoff()
	def _is_connection_error(B,err:Q):
		A=err
		if S(A,L):A=A.original_error
		return S(A,F)
	def _is_read_error(A,err:Q):return S(err,(J,I))
	def _is_method_retryable(A,method:D):
		if A.allowed_methods and method.upper()not in A.allowed_methods:return E
		return O
	def is_retry(A,method:D,status_code:C,has_retry_after:B=E):
		C=status_code
		if not A._is_method_retryable(method):return E
		if A.status_forcelist and C in A.status_forcelist:return O
		return B(A.total and A.respect_retry_after_header and has_retry_after and C in A.RETRY_AFTER_STATUS_CODES)
	def is_exhausted(A):
		B=[A for A in(A.total,A.connect,A.read,A.redirect,A.status,A.other)if A]
		if not B:return E
		return min(B)<0
	def increment(C,method:D|A=A,url:D|A=A,response:v|A=A,error:Q|A=A,_pool:y|A=A,_stacktrace:a|A=A):
		L=_stacktrace;K=url;J=method;D=response;B=error
		if C.total is E and B:raise b(P(B),B,L)
		N=C.total
		if N is not A:N-=1
		F=C.connect;H=C.read;O=C.redirect;Q=C.status;R=C.other;I='unknown';S=A;U=A
		if B and C._is_connection_error(B):
			if F is E:raise b(P(B),B,L)
			elif F is not A:F-=1
		elif B and C._is_read_error(B):
			if H is E or J is A or not C._is_method_retryable(J):raise b(P(B),B,L)
			elif H is not A:H-=1
		elif B:
			if R is not A:R-=1
		elif D and D.get_redirect_location():
			if O is not A:O-=1
			I='too many redirects';X=D.get_redirect_location()
			if X:U=X
			S=D.status
		else:
			I=G.GENERIC_ERROR
			if D and D.status:
				if Q is not A:Q-=1
				I=G.SPECIFIC_ERROR.format(status_code=D.status);S=D.status
		Z=C.history+(W(J,K,B,S,U),);T=C.new(total=N,connect=F,read=H,redirect=O,status=Q,other=R,history=Z)
		if T.is_exhausted():Y=B or G(I);raise M(_pool,K,Y)from Y
		V.debug("Incremented Retry for (url='%s'): %r",K,T);return T
	def __repr__(A):return f"{P(A).__name__}(total={A.total}, connect={A.connect}, read={A.read}, redirect={A.redirect}, status={A.status})"
Ï.DEFAULT=Ï(3)