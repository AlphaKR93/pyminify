F=bytes
E=ImportError
B=None
from typing import Any
from F.O import H
try:import ujson as D
except E:D=B
try:import orjson as A
except E:A=B
class G(H):
	def render(A,content:Any):assert D is not B,'ujson must be installed to use UJSONResponse';return D.dumps(content,ensure_ascii=False).encode('utf-8')
class I(H):
	def render(C,content:Any):assert A is not B,'orjson must be installed to use ORJSONResponse';return A.dumps(content,option=A.OPT_NON_STR_KEYS|A.OPT_SERIALIZE_NUMPY)