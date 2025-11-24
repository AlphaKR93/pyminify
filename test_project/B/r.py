E=float
D=property
B=bool
C=True
A=False
from typing import List as F,Union
from.F import d
from.K import g
class b(d):
	MIN_CHARS_FOR_DETECTION=20;EXPECTED_RATIO=.94
	def __init__(B):super().__init__();B.position=0;B.zeros_at_mod=[0]*4;B.nonzeros_at_mod=[0]*4;B._state=g.DETECTING;B.quad=[0,0,0,0];B.invalid_utf16be=A;B.invalid_utf16le=A;B.invalid_utf32be=A;B.invalid_utf32le=A;B.first_half_surrogate_pair_detected_16be=A;B.first_half_surrogate_pair_detected_16le=A;B.reset()
	def reset(B):super().reset();B.position=0;B.zeros_at_mod=[0]*4;B.nonzeros_at_mod=[0]*4;B._state=g.DETECTING;B.invalid_utf16be=A;B.invalid_utf16le=A;B.invalid_utf32be=A;B.invalid_utf32le=A;B.first_half_surrogate_pair_detected_16be=A;B.first_half_surrogate_pair_detected_16le=A;B.quad=[0,0,0,0]
	@D
	def charset_name(self):
		A=self
		if A.is_likely_utf32be():return'utf-32be'
		if A.is_likely_utf32le():return'utf-32le'
		if A.is_likely_utf16be():return'utf-16be'
		if A.is_likely_utf16le():return'utf-16le'
		return'utf-16'
	@D
	def language(self):return''
	def approx_32bit_chars(A):return max(1.,A.position/4.)
	def approx_16bit_chars(A):return max(1.,A.position/2.)
	def is_likely_utf32be(A):B=A.approx_32bit_chars();return B>=A.MIN_CHARS_FOR_DETECTION and(A.zeros_at_mod[0]/B>A.EXPECTED_RATIO and A.zeros_at_mod[1]/B>A.EXPECTED_RATIO and A.zeros_at_mod[2]/B>A.EXPECTED_RATIO and A.nonzeros_at_mod[3]/B>A.EXPECTED_RATIO and not A.invalid_utf32be)
	def is_likely_utf32le(A):B=A.approx_32bit_chars();return B>=A.MIN_CHARS_FOR_DETECTION and(A.nonzeros_at_mod[0]/B>A.EXPECTED_RATIO and A.zeros_at_mod[1]/B>A.EXPECTED_RATIO and A.zeros_at_mod[2]/B>A.EXPECTED_RATIO and A.zeros_at_mod[3]/B>A.EXPECTED_RATIO and not A.invalid_utf32le)
	def is_likely_utf16be(A):B=A.approx_16bit_chars();return B>=A.MIN_CHARS_FOR_DETECTION and((A.nonzeros_at_mod[1]+A.nonzeros_at_mod[3])/B>A.EXPECTED_RATIO and(A.zeros_at_mod[0]+A.zeros_at_mod[2])/B>A.EXPECTED_RATIO and not A.invalid_utf16be)
	def is_likely_utf16le(A):B=A.approx_16bit_chars();return B>=A.MIN_CHARS_FOR_DETECTION and((A.nonzeros_at_mod[0]+A.nonzeros_at_mod[2])/B>A.EXPECTED_RATIO and(A.zeros_at_mod[1]+A.zeros_at_mod[3])/B>A.EXPECTED_RATIO and not A.invalid_utf16le)
	def validate_utf32_characters(B,quad:F[int]):
		A=quad
		if A[0]!=0 or A[1]>16 or A[0]==0 and A[1]==0 and 216<=A[2]<=223:B.invalid_utf32be=C
		if A[3]!=0 or A[2]>16 or A[3]==0 and A[2]==0 and 216<=A[1]<=223:B.invalid_utf32le=C
	def validate_utf16_characters(B,pair:F[int]):
		D=pair
		if not B.first_half_surrogate_pair_detected_16be:
			if 216<=D[0]<=219:B.first_half_surrogate_pair_detected_16be=C
			elif 220<=D[0]<=223:B.invalid_utf16be=C
		elif 220<=D[0]<=223:B.first_half_surrogate_pair_detected_16be=A
		else:B.invalid_utf16be=C
		if not B.first_half_surrogate_pair_detected_16le:
			if 216<=D[1]<=219:B.first_half_surrogate_pair_detected_16le=C
			elif 220<=D[1]<=223:B.invalid_utf16le=C
		elif 220<=D[1]<=223:B.first_half_surrogate_pair_detected_16le=A
		else:B.invalid_utf16le=C
	def feed(A,byte_str:Union[bytes,bytearray]):
		for C in byte_str:
			B=A.position%4;A.quad[B]=C
			if B==3:A.validate_utf32_characters(A.quad);A.validate_utf16_characters(A.quad[0:2]);A.validate_utf16_characters(A.quad[2:4])
			if C==0:A.zeros_at_mod[B]+=1
			else:A.nonzeros_at_mod[B]+=1
			A.position+=1
		return A.state
	@D
	def state(self):
		A=self
		if A._state in{g.NOT_ME,g.FOUND_IT}:return A._state
		if A.get_confidence()>.8:A._state=g.FOUND_IT
		elif A.position>4*1024:A._state=g.NOT_ME
		return A._state
	def get_confidence(A):return .85 if A.is_likely_utf16le()or A.is_likely_utf16be()or A.is_likely_utf32le()or A.is_likely_utf32be()else .0