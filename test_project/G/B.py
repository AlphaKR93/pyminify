c='latin-1'
b='__getitem__'
a='keys'
Z=bytes
W=', '
V=NotImplemented
U=KeyError
Q=type
P=tuple
O=hasattr
L=int
K=False
J=bool
I=list
G=len
E=isinstance
C=None
A=str
import typing as B
from collections import OrderedDict as d
from enum import Enum,auto
from threading import RLock as X
F=B.TypeVar('_KT')
H=B.TypeVar('_VT')
M=B.TypeVar('_DT')
R=B.Union['HTTPHeaderDict',B.Mapping[A,A],B.Iterable[B.Tuple[A,A]],'HasGettableStringKeys']
class S(Enum):not_passed=auto()
def N(potential:object):
	C=potential
	if E(C,D):return C
	elif E(C,B.Mapping):return C
	elif E(C,B.Iterable):return C
	elif O(C,a)and O(C,b):return C
	else:return
class T(B.Generic[F,H],B.MutableMapping[F,H]):
	_container:B.OrderedDict[F,H];_maxsize:L;dispose_func:B.Callable[[H],C]|C;lock:X
	def __init__(A,maxsize:L=10,dispose_func:B.Callable[[H],C]|C=C):super().__init__();A._maxsize=maxsize;A.dispose_func=dispose_func;A._container=d();A.lock=X()
	def __getitem__(A,key:F):
		with A.lock:B=A._container.pop(key);A._container[key]=B;return B
	def __setitem__(A,key:F,value:H):
		E=value;B=key;D=C
		with A.lock:
			try:D=B,A._container.pop(B);A._container[B]=E
			except U:
				A._container[B]=E
				if G(A._container)>A._maxsize:D=A._container.popitem(last=K)
		if D is not C and A.dispose_func:H,F=D;A.dispose_func(F)
	def __delitem__(A,key:F):
		with A.lock:B=A._container.pop(key)
		if A.dispose_func:A.dispose_func(B)
	def __len__(A):
		with A.lock:return G(A._container)
	def __iter__(A):raise NotImplementedError('Iteration over this class is unlikely to be threadsafe.')
	def clear(A):
		with A.lock:B=I(A._container.values());A._container.clear()
		if A.dispose_func:
			for C in B:A.dispose_func(C)
	def keys(A):
		with A.lock:return set(A._container.keys())
class Y(B.Set[B.Tuple[A,A]]):
	_headers:D
	def __init__(A,headers:D):A._headers=headers
	def __len__(A):return G(I(A._headers.iteritems()))
	def __iter__(A):return A._headers.iteritems()
	def __contains__(F,item:object):
		B=item
		if E(B,P)and G(B)==2:
			C,D=B
			if E(C,A)and E(D,A):return F._headers._has_value_for_header(C,D)
		return K
class D(B.MutableMapping[A,A]):
	_container:B.MutableMapping[A,I[A]]
	def __init__(B,headers:R|C=C,**G:A):
		F=headers;super().__init__();B._container={}
		if F is not C:
			if E(F,D):B._copy_from(F)
			else:B.extend(F)
		if G:B.extend(G)
	def __setitem__(B,key:A,val:A):
		A=key
		if E(A,Z):A=A.decode(c)
		B._container[A.lower()]=[A,val]
	def __getitem__(A,key:A):B=A._container[key.lower()];return W.join(B[1:])
	def __delitem__(A,key:A):del A._container[key.lower()]
	def __contains__(B,key:object):
		if E(key,A):return key.lower()in B._container
		return K
	def setdefault(A,key:A,default:A=''):return super().setdefault(key,default)
	def __eq__(A,other:object):
		B=N(other)
		if B is C:return K
		else:D=Q(A)(B)
		return{A.lower():B for(A,B)in A.itermerged()}=={A.lower():B for(A,B)in D.itermerged()}
	def __ne__(A,other:object):return not A.__eq__(other)
	def __len__(A):return G(A._container)
	def __iter__(A):
		for B in A._container.values():yield B[0]
	def discard(A,key:A):
		try:del A[key]
		except U:pass
	def add(F,key:A,val:A,*,combine:J=K):
		C=val;A=key
		if E(A,Z):A=A.decode(c)
		H=A.lower();D=[A,C];B=F._container.setdefault(H,D)
		if D is not B:
			assert G(B)>=2
			if combine:B[-1]=B[-1]+W+C
			else:B.append(C)
	def extend(H,*I:R,**L:A):
		if G(I)>1:raise TypeError(f"extend() takes at most 1 positional arguments ({G(I)} given)")
		C=I[0]if G(I)>=1 else()
		if E(C,D):
			for(F,J)in C.iteritems():H.add(F,J)
		elif E(C,B.Mapping):
			for(F,J)in C.items():H.add(F,J)
		elif E(C,B.Iterable):
			C=C
			for(F,K)in C:H.add(F,K)
		elif O(C,a)and O(C,b):
			for F in C.keys():H.add(F,C[F])
		for(F,K)in L.items():H.add(F,K)
	@B.overload
	def getlist(self,key:A):0
	@B.overload
	def getlist(self,key:A,default:M):0
	def getlist(B,key:A,default:S|M=S.not_passed):
		A=default
		try:C=B._container[key.lower()]
		except U:
			if A is S.not_passed:return[]
			return A
		else:return C[1:]
	def _prepare_for_method_change(A):
		B=['Content-Encoding','Content-Language','Content-Location','Content-Type','Content-Length','Digest','Last-Modified']
		for C in B:A.discard(C)
		return A
	getheaders=getlist;getallmatchingheaders=getlist;iget=getlist;get_all=getlist
	def __repr__(A):return f"{Q(A).__name__}({dict(A.itermerged())})"
	def _copy_from(C,other:D):
		B=other
		for A in B:D=B.getlist(A);C._container[A.lower()]=[A,*D]
	def copy(A):B=Q(A)();B._copy_from(A);return B
	def iteritems(A):
		for C in A:
			B=A._container[C.lower()]
			for D in B[1:]:yield(B[0],D)
	def itermerged(A):
		for C in A:B=A._container[C.lower()];yield(B[0],W.join(B[1:]))
	def items(A):return Y(A)
	def _has_value_for_header(A,header_name:A,potential_value:A):
		B=header_name
		if B in A:return potential_value in A._container[B.lower()][1:]
		return K
	def __ior__(A,other:object):
		B=N(other)
		if B is C:return V
		A.extend(B);return A
	def __or__(D,other:object):
		A=N(other)
		if A is C:return V
		B=D.copy();B.extend(A);return B
	def __ror__(A,other:object):
		B=N(other)
		if B is C:return V
		D=Q(A)(B);D.extend(A);return D