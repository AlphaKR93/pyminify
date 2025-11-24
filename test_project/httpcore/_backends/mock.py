import ssl,typing
from.._exceptions import ReadError
from.base import SOCKET_OPTION,AsyncNetworkBackend,AsyncNetworkStream,NetworkBackend,NetworkStream
class MockSSLObject:
	def __init__(self,http2:bool):self._http2=http2
	def selected_alpn_protocol(self):return'h2'if self._http2 else'http/1.1'
class MockStream(NetworkStream):
	def __init__(self,buffer:list[bytes],http2:bool=False):self._buffer=buffer;self._http2=http2;self._closed=False
	def read(self,max_bytes:int,timeout:float|None=None):
		if self._closed:raise ReadError('Connection closed')
		if not self._buffer:return b''
		return self._buffer.pop(0)
	def write(self,buffer:bytes,timeout:float|None=None):0
	def close(self):self._closed=True
	def start_tls(self,ssl_context:ssl.SSLContext,server_hostname:str|None=None,timeout:float|None=None):return self
	def get_extra_info(self,info:str):return MockSSLObject(http2=self._http2)if info=='ssl_object'else None
	def __repr__(self):return'<httpcore.MockStream>'
class MockBackend(NetworkBackend):
	def __init__(self,buffer:list[bytes],http2:bool=False):self._buffer=buffer;self._http2=http2
	def connect_tcp(self,host:str,port:int,timeout:float|None=None,local_address:str|None=None,socket_options:typing.Iterable[SOCKET_OPTION]|None=None):return MockStream(list(self._buffer),http2=self._http2)
	def connect_unix_socket(self,path:str,timeout:float|None=None,socket_options:typing.Iterable[SOCKET_OPTION]|None=None):return MockStream(list(self._buffer),http2=self._http2)
	def sleep(self,seconds:float):0
class AsyncMockStream(AsyncNetworkStream):
	def __init__(self,buffer:list[bytes],http2:bool=False):self._buffer=buffer;self._http2=http2;self._closed=False
	async def read(self,max_bytes:int,timeout:float|None=None):
		if self._closed:raise ReadError('Connection closed')
		if not self._buffer:return b''
		return self._buffer.pop(0)
	async def write(self,buffer:bytes,timeout:float|None=None):0
	async def aclose(self):self._closed=True
	async def start_tls(self,ssl_context:ssl.SSLContext,server_hostname:str|None=None,timeout:float|None=None):return self
	def get_extra_info(self,info:str):return MockSSLObject(http2=self._http2)if info=='ssl_object'else None
	def __repr__(self):return'<httpcore.AsyncMockStream>'
class AsyncMockBackend(AsyncNetworkBackend):
	def __init__(self,buffer:list[bytes],http2:bool=False):self._buffer=buffer;self._http2=http2
	async def connect_tcp(self,host:str,port:int,timeout:float|None=None,local_address:str|None=None,socket_options:typing.Iterable[SOCKET_OPTION]|None=None):return AsyncMockStream(list(self._buffer),http2=self._http2)
	async def connect_unix_socket(self,path:str,timeout:float|None=None,socket_options:typing.Iterable[SOCKET_OPTION]|None=None):return AsyncMockStream(list(self._buffer),http2=self._http2)
	async def sleep(self,seconds:float):0