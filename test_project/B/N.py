B=property
E=None
from typing import Union
from.D import R
from.H import A
from.K import y,g
from.Y import H
from.i import J
from.k import I
class D(J):
	def __init__(B):super().__init__();B.coding_sm=A(I);B.distribution_analyzer=R();B.context_analyzer=H();B.reset()
	def reset(A):super().reset();A.context_analyzer.reset()
	@B
	def charset_name(self):return'EUC-JP'
	@B
	def language(self):return'Japanese'
	def feed(A,byte_str:Union[bytes,bytearray]):
		C=byte_str;assert A.coding_sm is not E;assert A.distribution_analyzer is not E
		for(B,G)in enumerate(C):
			F=A.coding_sm.next_state(G)
			if F==y.ERROR:A.logger.debug('%s %s prober hit error at byte %s',A.charset_name,A.language,B);A._state=g.NOT_ME;break
			if F==y.ITS_ME:A._state=g.FOUND_IT;break
			if F==y.START:
				D=A.coding_sm.get_current_charlen()
				if B==0:A._last_char[1]=G;A.context_analyzer.feed(A._last_char,D);A.distribution_analyzer.feed(A._last_char,D)
				else:A.context_analyzer.feed(C[B-1:B+1],D);A.distribution_analyzer.feed(C[B-1:B+1],D)
		A._last_char[0]=C[-1]
		if A.state==g.DETECTING:
			if A.context_analyzer.got_enough_data()and A.get_confidence()>A.SHORTCUT_THRESHOLD:A._state=g.FOUND_IT
		return A.state
	def get_confidence(A):assert A.distribution_analyzer is not E;B=A.context_analyzer.get_confidence();C=A.distribution_analyzer.get_confidence();return max(B,C)