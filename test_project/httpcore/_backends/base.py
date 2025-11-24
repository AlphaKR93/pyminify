from __future__ import annotations
import ssl,time,typing
SOCKET_OPTION=typing.Union[typing.Tuple[int,int,int],typing.Tuple[int,int,typing.Union[bytes,bytearray]],typing.Tuple[int,int,None,int]]
class NetworkStream:
	def read(self,max_bytes:int,timeout:float|None=None):raise NotImplementedError
	def write(self,buffer:bytes,timeout:float|None=None):raise NotImplementedError
	def close(self):raise NotImplementedError
	def start_tls(self,ssl_context:ssl.SSLContext,server_hostname:str|None=None,timeout:float|None=None):raise NotImplementedError
	def get_extra_info(self,info:str):0
class NetworkBackend:
	def connect_tcp(self,host:str,port:int,timeout:float|None=None,local_address:str|None=None,socket_options:typing.Iterable[SOCKET_OPTION]|None=None):raise NotImplementedError
	def connect_unix_socket(self,path:str,timeout:float|None=None,socket_options:typing.Iterable[SOCKET_OPTION]|None=None):raise NotImplementedError
	def sleep(self,seconds:float):time.sleep(seconds)
class AsyncNetworkStream:
	async def read(self,max_bytes:int,timeout:float|None=None):raise NotImplementedError
	async def write(self,buffer:bytes,timeout:float|None=None):raise NotImplementedError
	async def aclose(self):raise NotImplementedError
	async def start_tls(self,ssl_context:ssl.SSLContext,server_hostname:str|None=None,timeout:float|None=None):raise NotImplementedError
	def get_extra_info(self,info:str):0
class AsyncNetworkBackend:
	async def connect_tcp(self,host:str,port:int,timeout:float|None=None,local_address:str|None=None,socket_options:typing.Iterable[SOCKET_OPTION]|None=None):raise NotImplementedError
	async def connect_unix_socket(self,path:str,timeout:float|None=None,socket_options:typing.Iterable[SOCKET_OPTION]|None=None):raise NotImplementedError
	async def sleep(self,seconds:float):raise NotImplementedError