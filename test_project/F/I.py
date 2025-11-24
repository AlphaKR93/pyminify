y='Too many arguments.'
x='websocket'
w=TypeError
v=reversed
u=KeyError
t=getattr
q='wss'
p='https'
o='headers'
n=enumerate
m=iter
l=hasattr
h=sorted
g=dict
b='http'
a=False
Y=''
X=len
U=isinstance
S=bool
R=True
Q=bytes
P=tuple
O=int
K=property
F='latin-1'
E=list
C=None
A=str
from collections.abc import Iterable as ª,Mapping as L,MutableMapping as º,Sequence as j
from shlex import shlex
from typing import Any as B,BinaryIO as Á,NamedTuple as Â,TypeVar as r,cast as k
from urllib.parse import parse_qsl as c,urlencode as d,urlsplit as Ä
from F.F import Æ
from F.V import Ñ
class e(Â):host:A;port:O
M=r('_KeyType')
N=r('_CovariantValueType',covariant=R)
class W:
	def __init__(N,url:A=Y,scope:Ñ|C=C,**H:B):
		D=scope;A=url
		if D is not C:
			assert not A,'Cannot set both "url" and "scope".';assert not H,'Cannot set both "scope" and "**components".';E=D.get('scheme',b);J=D.get('server',C);G=D['path'];K=D.get('query_string',b'');I=C
			for(O,P)in D[o]:
				if O==b'host':I=P.decode(F);break
			if I is not C:A=f"{E}://{I}{G}"
			elif J is C:A=G
			else:
				L,M=J;Q={b:80,p:443,'ws':80,q:443}[E]
				if M==Q:A=f"{E}://{L}{G}"
				else:A=f"{E}://{L}:{M}{G}"
			if K:A+='?'+K.decode()
		elif H:assert not A,'Cannot set both "url" and "**components".';A=W(Y).replace(**H).components.geturl()
		N._url=A
	@K
	def components(self):
		A=self
		if not l(A,'_components'):A._components=Ä(A._url)
		return A._components
	@K
	def scheme(self):return self.components.scheme
	@K
	def netloc(self):return self.components.netloc
	@K
	def path(self):return self.components.path
	@K
	def query(self):return self.components.query
	@K
	def fragment(self):return self.components.fragment
	@K
	def username(self):return self.components.username
	@K
	def password(self):return self.components.password
	@K
	def hostname(self):return self.components.hostname
	@K
	def port(self):return self.components.port
	@K
	def is_secure(self):return self.scheme in(p,q)
	def replace(D,**A:B):
		N='port';M='hostname';L='password';K='username'
		if K in A or L in A or M in A or N in A:
			E=A.pop(M,C);G=A.pop(N,D.port);H=A.pop(K,D.username);I=A.pop(L,D.password)
			if E is C:
				F=D.netloc;O,O,E=F.rpartition('@')
				if E[-1]!=']':E=E.rsplit(':',1)[0]
			F=E
			if G is not C:F+=f":{G}"
			if H is not C:
				J=H
				if I is not C:J+=f":{I}"
				F=f"{J}@{F}"
			A['netloc']=F
		P=D.components._replace(**A);return D.__class__(P.geturl())
	def include_query_params(C,**E:B):D=f(c(C.query,keep_blank_values=R));D.update({A(B):A(C)for(B,C)in E.items()});F=d(D.multi_items());return C.replace(query=F)
	def replace_query_params(C,**D:B):E=d([(A(B),A(C))for(B,C)in D.items()]);return C.replace(query=E)
	def remove_query_params(D,keys:A|j[A]):
		B=keys
		if U(B,A):B=[B]
		E=f(c(D.query,keep_blank_values=R))
		for F in B:E.pop(F,C)
		G=d(E.multi_items());return D.replace(query=G)
	def __eq__(B,other:B):return A(B)==A(other)
	def __str__(A):return A._url
	def __repr__(B):
		C=A(B)
		if B.password:C=A(B.replace(password='********'))
		return f"{B.__class__.__name__}({repr(C)})"
class I(A):
	def __new__(B,path:A,protocol:A=Y,host:A=Y):assert protocol in(b,x,Y);return A.__new__(B,path)
	def __init__(A,path:A,protocol:A=Y,host:A=Y):A.protocol=protocol;A.host=host
	def make_absolute_url(C,base_url:A|W):
		B=base_url
		if U(B,A):B=W(B)
		if C.protocol:D={b:{R:p,a:b},x:{R:q,a:'ws'}}[C.protocol][B.is_secure]
		else:D=B.scheme
		E=C.host or B.netloc;F=B.path.rstrip('/')+A(C);return W(scheme=D,netloc=E,path=F)
class s:
	def __init__(A,value:A):A._value=value
	def __repr__(A):B=A.__class__.__name__;return f"{B}('**********')"
	def __str__(A):return A._value
	def __bool__(A):return S(A._value)
class Å(j[A]):
	def __init__(D,value:A|j[A]):
		B=value
		if U(B,A):C=shlex(B,posix=R);C.whitespace=',';C.whitespace_split=R;D._items=[A.strip()for A in C]
		else:D._items=E(B)
	def __len__(A):return X(A._items)
	def __getitem__(A,index:O|slice):return A._items[index]
	def __iter__(A):return m(A._items)
	def __repr__(A):B=A.__class__.__name__;C=[A for A in A];return f"{B}({C!r})"
	def __str__(A):return', '.join(repr(A)for A in A)
class T(L[M,N]):
	_dict:g[M,N]
	def __init__(F,*D:T[M,N]|L[M,N]|ª[P[M,N]],**G:B):
		assert X(D)<2,y;A=D[0]if D else[]
		if G:A=T(A).multi_items()+T(G).multi_items()
		if not A:C=[]
		elif l(A,'multi_items'):A=A;C=E(A.multi_items())
		elif l(A,'items'):A=A;C=E(A.items())
		else:A=A;C=E(A)
		F._dict={A:B for(A,B)in C};F._list=C
	def getlist(A,key:B):return[B for(A,B)in A._list if A==key]
	def keys(A):return A._dict.keys()
	def values(A):return A._dict.values()
	def items(A):return A._dict.items()
	def multi_items(A):return E(A._list)
	def __getitem__(A,key:M):return A._dict[key]
	def __contains__(A,key:B):return key in A._dict
	def __iter__(A):return m(A.keys())
	def __len__(A):return X(A._dict)
	def __eq__(A,other:B):
		B=other
		if not U(B,A.__class__):return a
		return h(A._list)==h(B._list)
	def __repr__(A):B=A.__class__.__name__;C=A.multi_items();return f"{B}({C!r})"
class f(T[B,B]):
	def __setitem__(A,key:B,value:B):A.setlist(key,[value])
	def __delitem__(A,key:B):A._list=[(A,B)for(A,B)in A._list if A!=key];del A._dict[key]
	def pop(A,key:B,default:B=C):A._list=[(A,B)for(A,B)in A._list if A!=key];return A._dict.pop(key,default)
	def popitem(A):B,C=A._dict.popitem();A._list=[(A,C)for(A,C)in A._list if A!=B];return B,C
	def poplist(A,key:B):B=[B for(A,B)in A._list if A==key];A.pop(key);return B
	def clear(A):A._dict.clear();A._list.clear()
	def setdefault(A,key:B,default:B=C):
		C=default;B=key
		if B not in A:A._dict[B]=C;A._list.append((B,C))
		return A[B]
	def setlist(A,key:B,values:E[B]):
		D=values;B=key
		if not D:A.pop(B,C)
		else:E=[(A,C)for(A,C)in A._list if A!=B];A._list=E+[(B,A)for A in D];A._dict[B]=D[-1]
	def append(A,key:B,value:B):B=value;A._list.append((key,B));A._dict[key]=B
	def update(A,*D:f|L[B,B]|E[P[B,B]],**F:B):C=f(*D,**F);G=[(A,B)for(A,B)in A._list if A not in C.keys()];A._list=G+C.multi_items();A._dict.update(C)
class Z(T[A,A]):
	def __init__(C,*D:T[B,B]|L[B,B]|E[P[B,B]]|A|Q,**H:B):
		assert X(D)<2,y;G=D[0]if D else[]
		if U(G,A):super().__init__(c(G,keep_blank_values=R),**H)
		elif U(G,Q):super().__init__(c(G.decode(F),keep_blank_values=R),**H)
		else:super().__init__(*D,**H)
		C._list=[(A(B),A(C))for(B,C)in C._list];C._dict={A(B):A(C)for(B,C)in C._dict.items()}
	def __str__(A):return d(A._list)
	def __repr__(B):C=B.__class__.__name__;D=A(B);return f"{C}({D!r})"
class G:
	def __init__(A,file:Á,*,size:O|C=C,filename:A|C=C,headers:D|C=C):A.filename=filename;A.file=file;A.size=size;A.headers=headers or D();A._max_mem_size=t(A.file,'_max_size',0)
	@K
	def content_type(self):return self.headers.get('content-type',C)
	@K
	def _in_memory(self):A=t(self.file,'_rolled',R);return not A
	def _will_roll(A,size_to_add:O):
		if not A._in_memory:return R
		B=A.file.tell()+size_to_add;return S(B>A._max_mem_size)if A._max_mem_size else a
	async def write(A,data:Q):
		B=data;D=X(B)
		if A.size is not C:A.size+=D
		if A._will_roll(D):await Æ(A.file.write,B)
		else:A.file.write(B)
	async def read(A,size:O=-1):
		if A._in_memory:return A.file.read(size)
		return await Æ(A.file.read,size)
	async def seek(A,offset:O):
		B=offset
		if A._in_memory:A.file.seek(B)
		else:await Æ(A.file.seek,B)
	async def close(A):
		if A._in_memory:A.file.close()
		else:await Æ(A.file.close)
	def __repr__(A):return f"{A.__class__.__name__}(filename={A.filename!r}, size={A.size!r}, headers={A.headers!r})"
class H(T[A,G|A]):
	def __init__(D,*B:H|L[A,A|G]|E[P[A,A|G]],**C:A|G):super().__init__(*B,**C)
	async def close(B):
		for(C,A)in B.multi_items():
			if U(A,G):await A.close()
class D(L[A,A]):
	def __init__(B,headers:L[A,A]|C=C,raw:E[P[Q,Q]]|C=C,scope:º[A,B]|C=C):
		G=headers;D=raw;A=scope;B._list=[]
		if G is not C:assert D is C,'Cannot set both "headers" and "raw".';assert A is C,'Cannot set both "headers" and "scope".';B._list=[(A.lower().encode(F),B.encode(F))for(A,B)in G.items()]
		elif D is not C:assert A is C,'Cannot set both "raw" and "scope".';B._list=D
		elif A is not C:B._list=A[o]=E(A[o])
	@K
	def raw(self):return E(self._list)
	def keys(A):return[A.decode(F)for(A,B)in A._list]
	def values(A):return[A.decode(F)for(B,A)in A._list]
	def items(A):return[(A.decode(F),B.decode(F))for(A,B)in A._list]
	def getlist(A,key:A):B=key.lower().encode(F);return[C.decode(F)for(A,C)in A._list if A==B]
	def mutablecopy(A):return J(raw=A._list[:])
	def __getitem__(A,key:A):
		B=key.lower().encode(F)
		for(C,D)in A._list:
			if C==B:return D.decode(F)
		raise u(key)
	def __contains__(A,key:B):
		B=key.lower().encode(F)
		for(C,D)in A._list:
			if C==B:return R
		return a
	def __iter__(A):return m(A.keys())
	def __len__(A):return X(A._list)
	def __eq__(B,other:B):
		A=other
		if not U(A,D):return a
		return h(B._list)==h(A._list)
	def __repr__(A):
		B=A.__class__.__name__;C=g(A.items())
		if X(C)==X(A):return f"{B}({C!r})"
		return f"{B}(raw={A.raw!r})"
class J(D):
	def __setitem__(B,key:A,value:A):
		D=key.lower().encode(F);G=value.encode(F);C=[]
		for(A,(H,I))in n(B._list):
			if H==D:C.append(A)
		for A in v(C[1:]):del B._list[A]
		if C:A=C[0];B._list[A]=D,G
		else:B._list.append((D,G))
	def __delitem__(B,key:A):
		D=key.lower().encode(F);C=[]
		for(A,(G,H))in n(B._list):
			if G==D:C.append(A)
		for A in v(C):del B._list[A]
	def __ior__(B,other:L[A,A]):
		A=other
		if not U(A,L):raise w(f"Expected a mapping but got {A.__class__.__name__}")
		B.update(A);return B
	def __or__(C,other:L[A,A]):
		A=other
		if not U(A,L):raise w(f"Expected a mapping but got {A.__class__.__name__}")
		B=C.mutablecopy();B.update(A);return B
	@K
	def raw(self):return self._list
	def setdefault(A,key:A,value:A):
		B=value;C=key.lower().encode(F);D=B.encode(F)
		for(H,(E,G))in n(A._list):
			if E==C:return G.decode(F)
		A._list.append((C,D));return B
	def update(A,other:L[A,A]):
		for(B,C)in other.items():A[B]=C
	def append(A,key:A,value:A):B=key.lower().encode(F);C=value.encode(F);A._list.append((B,C))
	def add_vary_header(B,vary:A):
		E='vary';A=vary;D=B.get(E)
		if D is not C:A=', '.join([D,A])
		B[E]=A
class V:
	_state:g[A,B]
	def __init__(B,state:g[A,B]|C=C):
		A=state
		if A is C:A={}
		super().__setattr__('_state',A)
	def __setattr__(A,key:B,value:B):A._state[key]=value
	def __getattr__(A,key:B):
		try:return A._state[key]
		except u:B="'{}' object has no attribute '{}'";raise AttributeError(B.format(A.__class__.__name__,key))
	def __delattr__(A,key:B):del A._state[key]