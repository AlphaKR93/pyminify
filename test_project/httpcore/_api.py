import contextlib,typing
from._models import URL,Extensions,HeaderTypes
from._sync.connection_pool import ConnectionPool
def request(method:bytes|str,url:URL|bytes|str,*,headers:HeaderTypes=None,content:bytes|typing.Iterator[bytes]|None=None,extensions:Extensions|None=None):
	with ConnectionPool()as pool:return pool.request(method=method,url=url,headers=headers,content=content,extensions=extensions)
@contextlib.contextmanager
def stream(method:bytes|str,url:URL|bytes|str,*,headers:HeaderTypes=None,content:bytes|typing.Iterator[bytes]|None=None,extensions:Extensions|None=None):
	with ConnectionPool()as pool:
		with pool.stream(method=method,url=url,headers=headers,content=content,extensions=extensions)as response:yield response