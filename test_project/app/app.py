from fastapi import Æ
from.A import D
A=Æ()
A.mount('/v0',D)
@A.get('/')
async def C():return{'success':'Hello, world!'}
B=A
E=B
app=E