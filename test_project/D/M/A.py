from contextlib import AsyncExitStack as C
from F.V import Ê,Ò,Ñ,Send
class Õ:
	def __init__(A,app:Ê,context_name:str='fastapi_middleware_astack'):A.app=app;A.context_name=context_name
	async def __call__(A,scope:Ñ,receive:Ò,send:Send):
		B=scope
		async with C()as D:B[A.context_name]=D;await A.app(B,receive,send)