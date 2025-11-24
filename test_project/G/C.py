N='Content-Type'
M=TypeError
I='headers'
H='body'
F=bytes
B=str
A=None
import json as O,typing as E
from urllib.parse import urlencode as L
from.A import C
from.B import D
from.J import K,R
J=E.Union[E.Sequence[E.Tuple[B,E.Union[B,F]]],E.Mapping[B,E.Union[B,F]]]
class G:
	_encode_url_methods={'DELETE','GET','HEAD','OPTIONS'}
	def __init__(A,headers:E.Mapping[B,B]|A=A):A.headers=headers or{}
	def urlopen(A,method:B,url:B,body:C|A=A,headers:E.Mapping[B,B]|A=A,encode_multipart:bool=True,multipart_boundary:B|A=A,**B:E.Any):raise NotImplementedError('Classes extending RequestMethods must implement their own ``urlopen`` method.')
	def request(F,method:B,url:B,body:C|A=A,fields:K|A=A,headers:E.Mapping[B,B]|A=A,json:E.Any|A=A,**J:E.Any):
		K=fields;I=json;G=body;D=method;C=headers;D=D.upper()
		if I is not A and G is not A:raise M("request got values for both 'body' and 'json' parameters which are mutually exclusive")
		if I is not A:
			if C is A:C=F.headers.copy()
			if not'content-type'in map(B.lower,C.keys()):C[N]='application/json'
			G=O.dumps(I,separators=(',',':'),ensure_ascii=False).encode('utf-8')
		if G is not A:J[H]=G
		if D in F._encode_url_methods:return F.request_encode_url(D,url,fields=K,headers=C,**J)
		else:return F.request_encode_body(D,url,fields=K,headers=C,**J)
	def request_encode_url(D,method:B,url:B,fields:J|A=A,headers:E.Mapping[B,B]|A=A,**H:B):
		F=fields;C=headers
		if C is A:C=D.headers
		G={I:C};G.update(H)
		if F:url+='?'+L(F)
		return D.urlopen(method,url,**G)
	def request_encode_body(O,method:B,url:B,fields:K|A=A,headers:E.Mapping[B,B]|A=A,encode_multipart:bool=True,multipart_boundary:B|A=A,**P:B):
		J=headers;G=fields
		if J is A:J=O.headers
		C={I:D(J)}
		if G:
			if H in P:raise M("request got values for both 'fields' and 'body', can only specify one.")
			if encode_multipart:K,Q=R(G,boundary=multipart_boundary)
			else:K,Q=L(G),'application/x-www-form-urlencoded'
			C[H]=K;C[I].setdefault(N,Q)
		C.update(P);return O.urlopen(method,url,**C)