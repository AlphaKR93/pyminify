B='detail'
from D.I import L
from D.K import û,ü
from D.Z import I
from D.a import Û
from F.K import Ú
from F.N import Y
from F.O import H,C
from F.S import D
async def Ð(request:Y,exc:Ú):
	A=exc;D=getattr(A,'headers',None)
	if not I(A.status_code):return C(status_code=A.status_code,headers=D)
	return H({B:A.detail},status_code=A.status_code,headers=D)
async def Ó(request:Y,exc:û):return H(status_code=422,content={B:L(exc.errors())})
async def Ô(websocket:Û,exc:ü):await websocket.close(code=D,reason=L(exc.errors()))