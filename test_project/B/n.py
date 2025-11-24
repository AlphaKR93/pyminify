G=property
F=float
A=str
B=int
from typing import Dict as C,NamedTuple as H,Optional as D,Union
from.F import d
from.K import K,g,J
class I(H):charset_name:A;language:A;char_to_order_map:C[B,B];language_model:C[B,C[B,B]];typical_positive_ratio:F;keep_ascii_letters:bool;alphabet:A
class E(d):
	SAMPLE_SIZE=64;SB_ENOUGH_REL_THRESHOLD=1024;POSITIVE_SHORTCUT_THRESHOLD=.95;NEGATIVE_SHORTCUT_THRESHOLD=.05
	def __init__(A,model:I,is_reversed:bool=False,name_prober:D[d]=None):super().__init__();A._model=model;A._reversed=is_reversed;A._name_prober=name_prober;A._last_order=255;A._seq_counters=[];A._total_seqs=0;A._total_char=0;A._control_char=0;A._freq_char=0;A.reset()
	def reset(A):super().reset();A._last_order=255;A._seq_counters=[0]*J.get_num_categories();A._total_seqs=0;A._total_char=0;A._control_char=0;A._freq_char=0
	@G
	def charset_name(self):
		A=self
		if A._name_prober:return A._name_prober.charset_name
		return A._model.charset_name
	@G
	def language(self):
		A=self
		if A._name_prober:return A._name_prober.language
		return A._model.language
	def feed(A,byte_str:Union[bytes,bytearray]):
		B=byte_str
		if not A._model.keep_ascii_letters:B=A.filter_international_words(B)
		else:B=A.remove_xml_tags(B)
		if not B:return A.state
		H=A._model.char_to_order_map;E=A._model.language_model
		for I in B:
			C=H.get(I,K.UNDEFINED)
			if C<K.CONTROL:A._total_char+=1
			if C<A.SAMPLE_SIZE:
				A._freq_char+=1
				if A._last_order<A.SAMPLE_SIZE:
					A._total_seqs+=1
					if not A._reversed:F=E[A._last_order][C]
					else:F=E[C][A._last_order]
					A._seq_counters[F]+=1
			A._last_order=C
		G=A._model.charset_name
		if A.state==g.DETECTING:
			if A._total_seqs>A.SB_ENOUGH_REL_THRESHOLD:
				D=A.get_confidence()
				if D>A.POSITIVE_SHORTCUT_THRESHOLD:A.logger.debug('%s confidence = %s, we have a winner',G,D);A._state=g.FOUND_IT
				elif D<A.NEGATIVE_SHORTCUT_THRESHOLD:A.logger.debug('%s confidence = %s, below negative shortcut threshold %s',G,D,A.NEGATIVE_SHORTCUT_THRESHOLD);A._state=g.NOT_ME
		return A.state
	def get_confidence(A):
		B=.01
		if A._total_seqs>0:
			B=(A._seq_counters[J.POSITIVE]+.25*A._seq_counters[J.LIKELY])/A._total_seqs/A._model.typical_positive_ratio;B=B*(A._total_char-A._control_char)/A._total_char;B=B*A._freq_char/A._total_char
			if B>=1.:B=.99
		return B