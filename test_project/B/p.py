B=property
E=None
from typing import Union
from.D import Q
from.H import A
from.K import y,g
from.Y import G
from.i import J
from.k import O
class H(J):
	def __init__(B):super().__init__();B.coding_sm=A(O);B.distribution_analyzer=Q();B.context_analyzer=G();B.reset()
	def reset(A):super().reset();A.context_analyzer.reset()
	@B
	def charset_name(self):return self.context_analyzer.charset_name
	@B
	def language(self):return'Japanese'
	def feed(A,byte_str:Union[bytes,bytearray]):
		D=byte_str;assert A.coding_sm is not E;assert A.distribution_analyzer is not E
		for(C,G)in enumerate(D):
			F=A.coding_sm.next_state(G)
			if F==y.ERROR:A.logger.debug('%s %s prober hit error at byte %s',A.charset_name,A.language,C);A._state=g.NOT_ME;break
			if F==y.ITS_ME:A._state=g.FOUND_IT;break
			if F==y.START:
				B=A.coding_sm.get_current_charlen()
				if C==0:A._last_char[1]=G;A.context_analyzer.feed(A._last_char[2-B:],B);A.distribution_analyzer.feed(A._last_char,B)
				else:A.context_analyzer.feed(D[C+1-B:C+3-B],B);A.distribution_analyzer.feed(D[C-1:C+1],B)
		A._last_char[0]=D[-1]
		if A.state==g.DETECTING:
			if A.context_analyzer.got_enough_data()and A.get_confidence()>A.SHORTCUT_THRESHOLD:A._state=g.FOUND_IT
		return A.state
	def get_confidence(A):assert A.distribution_analyzer is not E;B=A.context_analyzer.get_confidence();C=A.distribution_analyzer.get_confidence();return max(B,C)