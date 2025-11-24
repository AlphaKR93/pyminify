from cryptography.hazmat.bindings._rust import openssl as A
from C.D.D import hashes as B
U=A.hmac.HMAC
B.HashContext.register(U)