import contextlib,typing
ExceptionMapping=typing.Mapping[typing.Type[Exception],typing.Type[Exception]]
@contextlib.contextmanager
def map_exceptions(map:ExceptionMapping):
	try:yield
	except Exception as exc:
		for(from_exc,to_exc)in map.items():
			if isinstance(exc,from_exc):raise to_exc(exc)from exc
		raise
class ConnectionNotAvailable(Exception):0
class ProxyError(Exception):0
class UnsupportedProtocol(Exception):0
class ProtocolError(Exception):0
class RemoteProtocolError(ProtocolError):0
class LocalProtocolError(ProtocolError):0
class TimeoutException(Exception):0
class PoolTimeout(TimeoutException):0
class ConnectTimeout(TimeoutException):0
class ReadTimeout(TimeoutException):0
class WriteTimeout(TimeoutException):0
class NetworkError(Exception):0
class ConnectError(NetworkError):0
class ReadError(NetworkError):0
class WriteError(NetworkError):0