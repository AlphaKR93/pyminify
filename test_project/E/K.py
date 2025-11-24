A=['response']
def s():return{A:[]for A in A}
def m(key,hooks,hook_data,**D):
	B=hook_data;A=hooks;A=A or{};A=A.get(key)
	if A:
		if hasattr(A,'__call__'):A=[A]
		for E in A:
			C=E(B,**D)
			if C is not None:B=C
	return B