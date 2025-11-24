from contextlib import asynccontextmanager as A
from typing import ContextManager as D,TypeVar as E
import anyio.to_thread
from anyio import CapacityLimiter as F
from F.F import Æ
B=E('_T')
@A
async def J(cm:D[B]):
	B=None;C=F(1)
	try:yield await Æ(cm.__enter__)
	except Exception as A:
		D=bool(await anyio.to_thread.run_sync(cm.__exit__,type(A),A,A.__traceback__,limiter=C))
		if not D:raise A
	else:await anyio.to_thread.run_sync(cm.__exit__,B,B,B,limiter=C)