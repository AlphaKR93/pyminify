from._api import request,stream
from._async import AsyncConnectionInterface,AsyncConnectionPool,AsyncHTTP2Connection,AsyncHTTP11Connection,AsyncHTTPConnection,AsyncHTTPProxy,AsyncSOCKSProxy
from._backends.base import SOCKET_OPTION,AsyncNetworkBackend,AsyncNetworkStream,NetworkBackend,NetworkStream
from._backends.mock import AsyncMockBackend,AsyncMockStream,MockBackend,MockStream
from._backends.sync import SyncBackend
from._exceptions import ConnectError,ConnectionNotAvailable,ConnectTimeout,LocalProtocolError,NetworkError,PoolTimeout,ProtocolError,ProxyError,ReadError,ReadTimeout,RemoteProtocolError,TimeoutException,UnsupportedProtocol,WriteError,WriteTimeout
from._models import URL,Origin,Proxy,Request,Response
from._ssl import default_ssl_context
from._sync import ConnectionInterface,ConnectionPool,HTTP2Connection,HTTP11Connection,HTTPConnection,HTTPProxy,SOCKSProxy
try:from._backends.anyio import AnyIOBackend
except ImportError:
	class AnyIOBackend:
		def __init__(self,*args,**kwargs):msg="Attempted to use 'httpcore.AnyIOBackend' but 'anyio' is not installed.";raise RuntimeError(msg)
try:from._backends.trio import TrioBackend
except ImportError:
	class TrioBackend:
		def __init__(self,*args,**kwargs):msg="Attempted to use 'httpcore.TrioBackend' but 'trio' is not installed.";raise RuntimeError(msg)
__version__='1.0.9'
__locals=locals()
for __name in __all__:
	if not __name.startswith(('__','SOCKET_OPTION')):setattr(__locals[__name],'__module__','httpcore')