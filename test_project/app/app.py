from D import Æ
from.A import D
A=Æ()
A.mount('/v0',D)
@A.get('')
async def B():return{'success':'Hello, world!'}
C=A
app=C