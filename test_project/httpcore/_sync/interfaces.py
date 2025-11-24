import contextlib,typing
from.._models import URL,Extensions,HeaderTypes,Origin,Request,enforce_bytes,enforce_headers,enforce_url,include_request_headers
class RequestInterface:
	def request(self,method:bytes|str,url:URL|bytes|str,*,headers:HeaderTypes=None,content:bytes|typing.Iterator[bytes]|None=None,extensions:Extensions|None=None):
		method=enforce_bytes(method,name='method');url=enforce_url(url,name='url');headers=enforce_headers(headers,name='headers');headers=include_request_headers(headers,url=url,content=content);request=Request(method=method,url=url,headers=headers,content=content,extensions=extensions);response=self.handle_request(request)
		try:response.read()
		finally:response.close()
		return response
	@contextlib.contextmanager
	def stream(self,method:bytes|str,url:URL|bytes|str,*,headers:HeaderTypes=None,content:bytes|typing.Iterator[bytes]|None=None,extensions:Extensions|None=None):
		method=enforce_bytes(method,name='method');url=enforce_url(url,name='url');headers=enforce_headers(headers,name='headers');headers=include_request_headers(headers,url=url,content=content);request=Request(method=method,url=url,headers=headers,content=content,extensions=extensions);response=self.handle_request(request)
		try:yield response
		finally:response.close()
	def handle_request(self,request:Request):raise NotImplementedError
class ConnectionInterface(RequestInterface):
	def close(self):raise NotImplementedError
	def info(self):raise NotImplementedError
	def can_handle_request(self,origin:Origin):raise NotImplementedError
	def is_available(self):raise NotImplementedError
	def has_expired(self):raise NotImplementedError
	def is_idle(self):raise NotImplementedError
	def is_closed(self):raise NotImplementedError