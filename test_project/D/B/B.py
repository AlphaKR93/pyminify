H=isinstance
E=str
from typing import Any as B,Sequence as G,Tuple as F,Union
from.E import N,ValidationError as Q,create_model as X
J=X('Request')
def ÿ(errors:G[B]):
	C=[]
	for A in errors:
		if H(A,N):E=Q(errors=[A],model=J).errors();C.extend(E)
		elif H(A,list):C.extend(ÿ(A))
		else:C.append(A)
	return C
def K(*,errors:G[B],loc_prefix:F[Union[E,int],...]):A='loc';C=[{**err,A:loc_prefix+err.get(A,())}for err in ÿ(errors)];return C