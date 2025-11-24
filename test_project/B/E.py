B=property
C=None
from typing import Union
from.F import d
from.K import h,g
class c(d):
	def __init__(B,lang_filter:h=h.NONE):super().__init__(lang_filter=lang_filter);B._active_num=0;B.probers=[];B._best_guess_prober=C
	def reset(A):
		super().reset();A._active_num=0
		for B in A.probers:B.reset();B.active=True;A._active_num+=1
		A._best_guess_prober=C
	@B
	def charset_name(self):
		A=self
		if not A._best_guess_prober:
			A.get_confidence()
			if not A._best_guess_prober:return
		return A._best_guess_prober.charset_name
	@B
	def language(self):
		A=self
		if not A._best_guess_prober:
			A.get_confidence()
			if not A._best_guess_prober:return
		return A._best_guess_prober.language
	def feed(A,byte_str:Union[bytes,bytearray]):
		for B in A.probers:
			if not B.active:continue
			C=B.feed(byte_str)
			if not C:continue
			if C==g.FOUND_IT:A._best_guess_prober=B;A._state=g.FOUND_IT;return A.state
			if C==g.NOT_ME:
				B.active=False;A._active_num-=1
				if A._active_num<=0:A._state=g.NOT_ME;return A.state
		return A.state
	def get_confidence(A):
		F=A.state
		if F==g.FOUND_IT:return .99
		if F==g.NOT_ME:return .01
		D=.0;A._best_guess_prober=C
		for B in A.probers:
			if not B.active:A.logger.debug('%s not active',B.charset_name);continue
			E=B.get_confidence();A.logger.debug('%s %s confidence = %s',B.charset_name,B.language,E)
			if D<E:D=E;A._best_guess_prober=B
		if not A._best_guess_prober:return .0
		return D