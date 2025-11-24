from os import getenv as B
from fastapi import FastAPI
from vercel.cache import AsyncRuntimeCache as C
from.A import J
if __debug__ and B('PYCHARM_DEBUG','0')=='1':import pydevd_pycharm as D;D.settrace('localhost',port=8399,stdout_to_server=True,stderr_to_server=True)
E=C()
A=FastAPI()
A.mount('/v0',J)
@A.get('/')
async def H():await E.get('test');return{'success':'Hello, world!'}
F=A
G=F
I=G
app=I