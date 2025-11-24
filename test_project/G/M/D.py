C=isinstance
A=AttributeError
import http.client as B
from email.errors import MultipartInvariantViolationDefect as G,StartBoundaryNotFoundDefect as H
from..H import W
def Ð(obj:object):
	B=obj
	try:return B.isclosed()
	except A:pass
	try:return B.closed
	except A:pass
	try:return B.fp is None
	except A:pass
	raise ValueError('Unable to determine whether fp is closed.')
def É(headers:B.HTTPMessage):
	A=headers
	if not C(A,B.HTTPMessage):raise TypeError(f"expected httplib.Message, got {type(A)}.")
	D=None
	if not A.is_multipart():
		E=A.get_payload()
		if C(E,(bytes,str)):D=E
	F=[A for A in A.defects if not C(A,(H,G))]
	if F or D:raise W(defects=F,unparsed_data=D)
def Ñ(response:B.HTTPResponse):A=response._method;return A.upper()=='HEAD'