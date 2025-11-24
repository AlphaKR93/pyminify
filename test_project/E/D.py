A=None
from.import sessions as B
def C(method,url,**A):
	with B.Session()as C:return C.request(method=method,url=url,**A)
def get(url,params=A,**A):return C('get',url,params=params,**A)
def F(url,**A):return C('options',url,**A)
def head(url,**A):A.setdefault('allow_redirects',False);return C('head',url,**A)
def post(url,data=A,json=A,**A):return C('post',url,data=data,json=json,**A)
def put(url,data=A,**A):return C('put',url,data=data,**A)
def patch(url,data=A,**A):return C('patch',url,data=data,**A)
def G(url,**A):return C('delete',url,**A)