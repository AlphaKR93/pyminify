Y='Algorithm supplied is not a supported cipher algorithm.'
X=False
W=issubclass
Q=len
N=TypeError
M=b''
L=ValueError
K=isinstance
H=None
G=int
E=bytes
import typing as F
from C import utils as I
from C.B import C,D,A,B
from C.D.D import ciphers as P,cmac as R,constant_time as S,hashes as T,hmac as U
from C.D.D.J import b
class O(I.Enum):CounterMode='ctr'
class J(I.Enum):BeforeFixed='before_fixed';AfterFixed='after_fixed';MiddleFixed='middle_fixed'
class V:
	def __init__(A,prf:F.Callable,mode:O,length:G,rlen:G,llen:F.Optional[G],location:J,break_location:F.Optional[G],label:F.Optional[E],context:F.Optional[E],fixed:F.Optional[E]):
		Q=fixed;P=rlen;F=location;E=llen;D=context;C=label;B=break_location;assert callable(prf)
		if not K(mode,O):raise N('mode must be of type Mode')
		if not K(F,J):raise N('location must be of type CounterLocation')
		if B is H and F is J.MiddleFixed:raise L('Please specify a break_location')
		if B is not H and F!=J.MiddleFixed:raise L('break_location is ignored when location is not CounterLocation.MiddleFixed')
		if B is not H and not K(B,G):raise N('break_location must be an integer')
		if B is not H and B<0:raise L('break_location must be a positive integer')
		if(C or D)and Q:raise L('When supplying fixed data, label and context are ignored.')
		if P is H or not A._valid_byte_length(P):raise L('rlen must be between 1 and 4')
		if E is H and Q is H:raise L('Please specify an llen')
		if E is not H and not K(E,G):raise N('llen must be an integer')
		if C is H:C=M
		if D is H:D=M
		I._check_bytes('label',C);I._check_bytes('context',D);A._prf=prf;A._mode=mode;A._length=length;A._rlen=P;A._llen=E;A._location=F;A._break_location=B;A._label=C;A._context=D;A._used=X;A._fixed_data=Q
	@staticmethod
	def _valid_byte_length(value:G):
		A=value
		if not K(A,G):raise N('value must be of type int')
		B=I.int_to_bytes(1,A)
		if not 1<=Q(B)<=4:return X
		return True
	def derive(A,key_material:E,prf_output_size:G):
		F=key_material
		if A._used:raise C
		I._check_byteslike('key_material',F);A._used=True;H=-(-A._length//prf_output_size);N=[M];P=I.int_to_bytes(1,A._rlen)
		if H>pow(2,Q(P)*8)-1:raise L('There are too many iterations.')
		B=A._generate_fixed_input()
		if A._location==J.BeforeFixed:D=M;E=B
		elif A._location==J.AfterFixed:D=B;E=M
		else:
			if K(A._break_location,G)and A._break_location>Q(B):raise L('break_location offset > len(fixed)')
			D=B[:A._break_location];E=B[A._break_location:]
		for R in range(1,H+1):O=A._prf(F);S=I.int_to_bytes(R,A._rlen);T=D+S+E;O.update(T);N.append(O.finalize())
		return M.join(N)[:A._length]
	def _generate_fixed_input(A):
		if A._fixed_data and K(A._fixed_data,E):return A._fixed_data
		B=I.int_to_bytes(A._length*8,A._llen);return M.join([A._label,b'\x00',A._context,B])
class Z(b):
	def __init__(C,algorithm:T.HashAlgorithm,mode:O,length:G,rlen:G,llen:F.Optional[G],location:J,label:F.Optional[E],context:F.Optional[E],fixed:F.Optional[E],backend:F.Any=H,*,break_location:F.Optional[G]=H):
		D=algorithm
		if not K(D,T.HashAlgorithm):raise A('Algorithm supplied is not a supported hash algorithm.',B.UNSUPPORTED_HASH)
		from C.D.B.A.B import Î
		if not Î.hmac_supported(D):raise A('Algorithm supplied is not a supported hmac algorithm.',B.UNSUPPORTED_HASH)
		C._algorithm=D;C._deriver=V(C._prf,mode,length,rlen,llen,location,break_location,label,context,fixed)
	def _prf(A,key_material:E):return U.HMAC(key_material,A._algorithm)
	def derive(A,key_material:E):return A._deriver.derive(key_material,A._algorithm.digest_size)
	def verify(A,key_material:E,expected_key:E):
		if not S.bytes_eq(A.derive(key_material),expected_key):raise D
class a(b):
	def __init__(C,algorithm,mode:O,length:G,rlen:G,llen:F.Optional[G],location:J,label:F.Optional[E],context:F.Optional[E],fixed:F.Optional[E],backend:F.Any=H,*,break_location:F.Optional[G]=H):
		D=algorithm
		if not W(D,P.BlockCipherAlgorithm)or not W(D,P.CipherAlgorithm):raise A(Y,B.UNSUPPORTED_CIPHER)
		C._algorithm=D;C._cipher=H;C._deriver=V(C._prf,mode,length,rlen,llen,location,break_location,label,context,fixed)
	def _prf(A,_:E):assert A._cipher is not H;return R.CMAC(A._cipher)
	def derive(C,key_material:E):
		D=key_material;C._cipher=C._algorithm(D);assert C._cipher is not H;from C.D.B.A.B import Î
		if not Î.cmac_algorithm_supported(C._cipher):raise A(Y,B.UNSUPPORTED_CIPHER)
		return C._deriver.derive(D,C._cipher.block_size//8)
	def verify(A,key_material:E,expected_key:E):
		if not S.bytes_eq(A.derive(key_material),expected_key):raise D