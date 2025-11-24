A=str
from typing import Optional as B
def D(authorization_header_value:B[A]):
	A=authorization_header_value
	if not A:return'',''
	B,D,C=A.partition(' ');return B,C