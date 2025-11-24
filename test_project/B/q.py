Y='UTF-16'
X='ascii'
W='Windows-1254'
V='iso-8859-9'
U='iso-8859-1'
T=isinstance
P=.0
O='Windows-1252'
N=bytearray
M=property
J=1.
I=True
C=False
H=''
G=None
F='language'
E='confidence'
D='encoding'
import codecs as K,logging as Q,re
from typing import Union
from.E import c
from.K import i,h,g
from.L import Z
from.g import f
from.h import a
from.j import A
from.o import e
from.r import b
class L:
	MINIMUM_THRESHOLD=.2;HIGH_BYTE_DETECTOR=re.compile(b'[\x80-\xff]');ESC_DETECTOR=re.compile(b'(\x1b|~{)');WIN_BYTE_DETECTOR=re.compile(b'[\x80-\x9f]');ISO_WIN_MAP={U:O,'iso-8859-2':'Windows-1250','iso-8859-5':'Windows-1251','iso-8859-6':'Windows-1256','iso-8859-7':'Windows-1253','iso-8859-8':'Windows-1255',V:W,'iso-8859-13':'Windows-1257'};LEGACY_MAP={X:O,U:O,'tis-620':'ISO-8859-11',V:W,'gb2312':'GB18030','euc-kr':'CP949','utf-16le':Y}
	def __init__(A,lang_filter:h=h.ALL,should_rename_legacy:bool=C):A._esc_charset_prober=G;A._utf1632_prober=G;A._charset_probers=[];A.result={D:G,E:P,F:G};A.done=C;A._got_data=C;A._input_state=i.PURE_ASCII;A._last_char=b'';A.lang_filter=lang_filter;A.logger=Q.getLogger(__name__);A._has_win_bytes=C;A.should_rename_legacy=should_rename_legacy;A.reset()
	@M
	def input_state(self):return self._input_state
	@M
	def has_win_bytes(self):return self._has_win_bytes
	@M
	def charset_probers(self):return self._charset_probers
	def reset(A):
		A.result={D:G,E:P,F:G};A.done=C;A._got_data=C;A._has_win_bytes=C;A._input_state=i.PURE_ASCII;A._last_char=b''
		if A._esc_charset_prober:A._esc_charset_prober.reset()
		if A._utf1632_prober:A._utf1632_prober.reset()
		for B in A._charset_probers:B.reset()
	def feed(B,byte_str:Union[bytes,N]):
		C=byte_str
		if B.done:return
		if not C:return
		if not T(C,N):C=N(C)
		if not B._got_data:
			if C.startswith(K.BOM_UTF8):B.result={D:'UTF-8-SIG',E:J,F:H}
			elif C.startswith((K.BOM_UTF32_LE,K.BOM_UTF32_BE)):B.result={D:'UTF-32',E:J,F:H}
			elif C.startswith(b'\xfe\xff\x00\x00'):B.result={D:'X-ISO-10646-UCS-4-3412',E:J,F:H}
			elif C.startswith(b'\x00\x00\xff\xfe'):B.result={D:'X-ISO-10646-UCS-4-2143',E:J,F:H}
			elif C.startswith((K.BOM_LE,K.BOM_BE)):B.result={D:Y,E:J,F:H}
			B._got_data=I
			if B.result[D]is not G:B.done=I;return
		if B._input_state==i.PURE_ASCII:
			if B.HIGH_BYTE_DETECTOR.search(C):B._input_state=i.HIGH_BYTE
			elif B._input_state==i.PURE_ASCII and B.ESC_DETECTOR.search(B._last_char+C):B._input_state=i.ESC_ASCII
		B._last_char=C[-1:]
		if not B._utf1632_prober:B._utf1632_prober=b()
		if B._utf1632_prober.state==g.DETECTING:
			if B._utf1632_prober.feed(C)==g.FOUND_IT:B.result={D:B._utf1632_prober.charset_name,E:B._utf1632_prober.get_confidence(),F:H};B.done=I;return
		if B._input_state==i.ESC_ASCII:
			if not B._esc_charset_prober:B._esc_charset_prober=Z(B.lang_filter)
			if B._esc_charset_prober.feed(C)==g.FOUND_IT:B.result={D:B._esc_charset_prober.charset_name,E:B._esc_charset_prober.get_confidence(),F:B._esc_charset_prober.language};B.done=I
		elif B._input_state==i.HIGH_BYTE:
			if not B._charset_probers:
				B._charset_probers=[A(B.lang_filter)]
				if B.lang_filter&h.NON_CJK:B._charset_probers.append(e())
				B._charset_probers.append(f());B._charset_probers.append(a())
			for L in B._charset_probers:
				if L.feed(C)==g.FOUND_IT:B.result={D:L.charset_name,E:L.get_confidence(),F:L.language};B.done=I;break
			if B.WIN_BYTE_DETECTOR.search(C):B._has_win_bytes=I
	def close(A):
		R='%s %s confidence = %s'
		if A.done:return A.result
		A.done=I
		if not A._got_data:A.logger.debug('no data received!')
		elif A._input_state==i.PURE_ASCII:A.result={D:X,E:J,F:H}
		elif A._input_state==i.HIGH_BYTE:
			M=G;N=P;L=G
			for C in A._charset_probers:
				if not C:continue
				M=C.get_confidence()
				if M>N:N=M;L=C
			if L and N>A.MINIMUM_THRESHOLD:
				B=L.charset_name;assert B is not G;O=B.lower();S=L.get_confidence()
				if O.startswith('iso-8859'):
					if A._has_win_bytes:B=A.ISO_WIN_MAP.get(O,B)
				if A.should_rename_legacy:B=A.LEGACY_MAP.get((B or H).lower(),B)
				A.result={D:B,E:S,F:L.language}
		if A.logger.getEffectiveLevel()<=Q.DEBUG:
			if A.result[D]is G:
				A.logger.debug('no probers hit minimum threshold')
				for K in A._charset_probers:
					if not K:continue
					if T(K,c):
						for C in K.probers:A.logger.debug(R,C.charset_name,C.language,C.get_confidence())
					else:A.logger.debug(R,K.charset_name,K.language,K.get_confidence())
		return A.result