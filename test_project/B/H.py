B=int
import logging as C
from.I import D
from.K import y
class A:
	def __init__(A,sm:D):A._model=sm;A._curr_byte_pos=0;A._curr_char_len=0;A._curr_state=y.START;A.active=True;A.logger=C.getLogger(__name__);A.reset()
	def reset(A):A._curr_state=y.START
	def next_state(A,c:B):
		B=A._model['class_table'][c]
		if A._curr_state==y.START:A._curr_byte_pos=0;A._curr_char_len=A._model['char_len_table'][B]
		C=A._curr_state*A._model['class_factor']+B;A._curr_state=A._model['state_table'][C];A._curr_byte_pos+=1;return A._curr_state
	def get_current_charlen(A):return A._curr_char_len
	def get_coding_state_machine(A):return A._model['name']
	@property
	def language(self):return self._model['language']