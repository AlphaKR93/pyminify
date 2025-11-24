B=property
from typing import Union
from.F import d
from.H import A
from.K import y,g
from.k import J
class I(d):
	ONE_CHAR_PROB=.5
	def __init__(B):super().__init__();B.coding_sm=A(J);B._num_mb_chars=0;B.reset()
	def reset(A):super().reset();A.coding_sm.reset();A._num_mb_chars=0
	@B
	def charset_name(self):return'utf-8'
	@B
	def language(self):return''
	def feed(A,byte_str:Union[bytes,bytearray]):
		for C in byte_str:
			B=A.coding_sm.next_state(C)
			if B==y.ERROR:A._state=g.NOT_ME;break
			if B==y.ITS_ME:A._state=g.FOUND_IT;break
			if B==y.START:
				if A.coding_sm.get_current_charlen()>=2:A._num_mb_chars+=1
		if A.state==g.DETECTING:
			if A.get_confidence()>A.SHORTCUT_THRESHOLD:A._state=g.FOUND_IT
		return A.state
	def get_confidence(A):
		B=.99
		if A._num_mb_chars<6:B*=A.ONE_CHAR_PROB**A._num_mb_chars;return 1.-B
		return B