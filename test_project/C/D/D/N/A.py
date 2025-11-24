D=False
C=None
B=bytes
import typing as A
def E(data:B,password:A.Optional[B],backend:A.Any=C,*,unsafe_skip_rsa_key_validation:bool=D):from C.D.B.A.B import Î;return Î.load_pem_private_key(data,password,unsafe_skip_rsa_key_validation)
def G(data:B,backend:A.Any=C):from C.D.B.A.B import Î;return Î.load_pem_public_key(data)
def H(data:B,backend:A.Any=C):from C.D.B.A.B import Î;return Î.load_pem_parameters(data)
def J(data:B,password:A.Optional[B],backend:A.Any=C,*,unsafe_skip_rsa_key_validation:bool=D):from C.D.B.A.B import Î;return Î.load_der_private_key(data,password,unsafe_skip_rsa_key_validation)
def K(data:B,backend:A.Any=C):from C.D.B.A.B import Î;return Î.load_der_public_key(data)
def M(data:B,backend:A.Any=C):from C.D.B.A.B import Î;return Î.load_der_parameters(data)