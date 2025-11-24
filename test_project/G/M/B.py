A=None
from.J import Url
def Â(proxy_url:Url|A=A,proxy_config:C|A=A,destination_scheme:str|A=A):
	D=proxy_config;C=proxy_url;B=False
	if C is A:return B
	if destination_scheme=='http':return B
	if C.scheme=='https'and D and D.use_forwarding_for_https:return B
	return True