L=Exception
I=str
G=None
from collections.abc import Awaitable as F,Callable as D,Mapping as M,MutableMapping as J
from contextlib import AbstractAsyncContextManager as K
from typing import Any as H,TypeVar as O
E=O('AppType')
Ñ=J[I,H]
Ì=J[I,H]
Ò=D[[],F[Ì]]
Send=D[[Ì],F[G]]
Ê=D[[Ñ,Ò,Send],F[G]]
P=D[[E],K[G]]
Q=D[[E],K[M[I,H]]]
B=P[E]|Q[E]
R=D[['Request',L],'Response | Awaitable[Response]']
S=D[['WebSocket',L],F[G]]
A=R|S