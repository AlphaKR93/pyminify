F=b'\x00\x00'
C=bytearray
B=None
from typing import Union
from.F import d
from.K import h,y,g
class J(d):
	def __init__(D,lang_filter:h=h.NONE):super().__init__(lang_filter=lang_filter);D.distribution_analyzer=B;D.coding_sm=B;D._last_char=C(F)
	def reset(A):
		super().reset()
		if A.coding_sm:A.coding_sm.reset()
		if A.distribution_analyzer:A.distribution_analyzer.reset()
		A._last_char=C(F)
	def feed(A,byte_str:Union[bytes,C]):
		D=byte_str;assert A.coding_sm is not B;assert A.distribution_analyzer is not B
		for(C,F)in enumerate(D):
			E=A.coding_sm.next_state(F)
			if E==y.ERROR:A.logger.debug('%s %s prober hit error at byte %s',A.charset_name,A.language,C);A._state=g.NOT_ME;break
			if E==y.ITS_ME:A._state=g.FOUND_IT;break
			if E==y.START:
				G=A.coding_sm.get_current_charlen()
				if C==0:A._last_char[1]=F;A.distribution_analyzer.feed(A._last_char,G)
				else:A.distribution_analyzer.feed(D[C-1:C+1],G)
		A._last_char[0]=D[-1]
		if A.state==g.DETECTING:
			if A.distribution_analyzer.got_enough_data()and A.get_confidence()>A.SHORTCUT_THRESHOLD:A._state=g.FOUND_IT
		return A.state
	def get_confidence(A):assert A.distribution_analyzer is not B;return A.distribution_analyzer.get_confidence()