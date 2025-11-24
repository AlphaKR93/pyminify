S='etag'
R=FileNotFoundError
O='/'
N=True
M=RuntimeError
L=list
K=False
J=bool
I=tuple
F=str
E=None
import errno,importlib.util,os as B,stat as G
from email.utils import parsedate as Q
from typing import Union
import anyio,anyio.to_thread
from F.B import A
from F.I import W,D
from F.K import Ú
from F.O import h,P,C
from F.V import Ò,Ñ,Send
H=Union[F,'os.PathLike[str]']
class T(C):
	NOT_MODIFIED_HEADERS='cache-control','content-location','date',S,'expires','vary'
	def __init__(B,headers:D):super().__init__(status_code=304,headers={A:C for(A,C)in headers.items()if A in B.NOT_MODIFIED_HEADERS})
class U:
	def __init__(A,*,directory:H|E=E,packages:L[F|I[F,F]]|E=E,html:J=K,check_dir:J=N,follow_symlink:J=K):
		D=packages;C=directory;A.directory=C;A.packages=D;A.all_directories=A.get_directories(C,D);A.html=html;A.config_checked=K;A.follow_symlink=follow_symlink
		if check_dir and C is not E and not B.path.isdir(C):raise M(f"Directory '{C}' does not exist")
	def get_directories(J,directory:H|E=E,packages:L[F|I[F,F]]|E=E):
		G=directory;C=[]
		if G is not E:C.append(G)
		for A in packages or[]:
			if isinstance(A,I):A,D=A
			else:D='statics'
			F=importlib.util.find_spec(A);assert F is not E,f"Package {A!r} could not be found.";assert F.origin is not E,f"Package {A!r} could not be found.";H=B.path.normpath(B.path.join(F.origin,'..',D));assert B.path.isdir(H),f"Directory '{D!r}' in package {A!r} could not be found.";C.append(H)
		return C
	async def __call__(A,scope:Ñ,receive:Ò,send:Send):
		B=scope;assert B['type']=='http'
		if not A.config_checked:await A.check_config();A.config_checked=N
		C=A.get_path(B);D=await A.get_response(C,B);await D(B,receive,send)
	def get_path(D,scope:Ñ):C=A(scope);return B.path.normpath(B.path.join(*C.split(O)))
	async def get_response(C,path:F,scope:Ñ):
		D=scope
		if D['method']not in('GET','HEAD'):raise Ú(status_code=405)
		try:F,A=await anyio.to_thread.run_sync(C.lookup_path,path)
		except PermissionError:raise Ú(status_code=401)
		except OSError as I:
			if I.errno==errno.ENAMETOOLONG:raise Ú(status_code=404)
			raise I
		if A and G.S_ISREG(A.st_mode):return C.file_response(F,A,D)
		elif A and G.S_ISDIR(A.st_mode)and C.html:
			J=B.path.join(path,'index.html');F,A=await anyio.to_thread.run_sync(C.lookup_path,J)
			if A is not E and G.S_ISREG(A.st_mode):
				if not D['path'].endswith(O):H=W(scope=D);H=H.replace(path=H.path+O);return P(url=H)
				return C.file_response(F,A,D)
		if C.html:
			F,A=await anyio.to_thread.run_sync(C.lookup_path,'404.html')
			if A and G.S_ISREG(A.st_mode):return h(F,stat_result=A,status_code=404)
		raise Ú(status_code=404)
	def lookup_path(D,path:F):
		for A in D.all_directories:
			G=B.path.join(A,path)
			if D.follow_symlink:C=B.path.abspath(G);A=B.path.abspath(A)
			else:C=B.path.realpath(G);A=B.path.realpath(A)
			if B.path.commonpath([C,A])!=F(A):continue
			try:return C,B.stat(C)
			except(R,NotADirectoryError):continue
		return'',E
	def file_response(B,full_path:H,stat_result:B.stat_result,scope:Ñ,status_code:int=200):
		C=D(scope=scope);A=h(full_path,status_code=status_code,stat_result=stat_result)
		if B.is_not_modified(A.headers,C):return T(A.headers)
		return A
	async def check_config(A):
		if A.directory is E:return
		try:C=await anyio.to_thread.run_sync(B.stat,A.directory)
		except R:raise M(f"StaticFiles directory '{A.directory}' does not exist.")
		if not(G.S_ISDIR(C.st_mode)or G.S_ISLNK(C.st_mode)):raise M(f"StaticFiles path '{A.directory}' is not a directory.")
	def is_not_modified(H,response_headers:D,request_headers:D):
		B=request_headers;A=response_headers
		if(F:=B.get('if-none-match')):G=A[S];return G in[A.strip(' W/')for A in F.split(',')]
		try:
			C=Q(B['if-modified-since']);D=Q(A['last-modified'])
			if C is not E and D is not E and C>=D:return N
		except KeyError:pass
		return K