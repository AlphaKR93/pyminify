B=property
E=None
D=str
from typing import Union
from.F import d
from.H import A
from.K import h,y,g
from.M import H,I,J,K
class Z(d):
	def __init__(B,lang_filter:h=h.NONE):
		super().__init__(lang_filter=lang_filter);B.coding_sm=[]
		if B.lang_filter&h.CHINESE_SIMPLIFIED:B.coding_sm.append(A(H));B.coding_sm.append(A(I))
		if B.lang_filter&h.JAPANESE:B.coding_sm.append(A(J))
		if B.lang_filter&h.KOREAN:B.coding_sm.append(A(K))
		B.active_sm_count=0;B._detected_charset=E;B._detected_language=E;B._state=g.DETECTING;B.reset()
	def reset(A):
		super().reset()
		for B in A.coding_sm:B.active=True;B.reset()
		A.active_sm_count=len(A.coding_sm);A._detected_charset=E;A._detected_language=E
	@B
	def charset_name(self):return self._detected_charset
	@B
	def language(self):return self._detected_language
	def get_confidence(A):return .99 if A._detected_charset else .0
	def feed(A,byte_str:Union[bytes,bytearray]):
		for D in byte_str:
			for B in A.coding_sm:
				if not B.active:continue
				C=B.next_state(D)
				if C==y.ERROR:
					B.active=False;A.active_sm_count-=1
					if A.active_sm_count<=0:A._state=g.NOT_ME;return A.state
				elif C==y.ITS_ME:A._state=g.FOUND_IT;A._detected_charset=B.get_coding_state_machine();A._detected_language=B.language;return A.state
		return A.state