from D import Õ
from A import D
C=Õ(prefix='/router')
@C.get('')
async def A():return{'message':await D()}