from fastapi import Æ
from.A import D
A=Æ()
A.mount('/v0',D)
@A.get('/')
async def E():return{'success':'Hello, world!'}
B=A
C=B
F=C
app=F