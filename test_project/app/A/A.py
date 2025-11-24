from D import Æ
from.B import C
D=Æ(version='0')
D.include_router(C)
@D.get('')
async def A():return{'version':'0'}