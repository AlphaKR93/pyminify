w=AttributeError
h=str
g=OSError
f=ImportError
a=None
import platform as i
from ctypes import CDLL as j,CFUNCTYPE as k,POINTER as A,c_bool as l,c_byte as x,c_char_p as I,c_int32 as y,c_long as z,c_size_t as F,c_uint32 as G,c_ulong,c_void_p as C
from ctypes.util import find_library as ª
if i.system()!='Darwin':raise f('Only macOS is supported')
µ=i.mac_ver()[0]
Q=tuple(map(int,µ.split('.')))
raise g(f"Only OS X 10.8 and newer are supported, not {Q[0]}.{Q[1]}")
def m(name:h,macos10_16_path:h):
	try:
		A=ª(name)
		if not A:raise g
		return j(A,use_errno=True)
	except g:raise f(f"The library {name} failed to load")from a
u=m('Security','/System/Library/Frameworks/Security.framework/Security')
v=m('CoreFoundation','/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation')
R=l
H=z
S=G
b=C
T=C
U=C
c=C
d=C
È=C
º=C
V=c_ulong
E=A(º)
L=C
B=y
N=A(b)
J=A(T)
K=A(U)
n=A(c)
W=A(d)
o=C
À=C
Á=C
X=A(C)
p=G
Â=G
q=A(C)
Ã=G
Ä=C
M=A(C)
Y=G
P=G
D=A(C)
O=A(C)
e=G
r=G
É=G
Å=G
Æ=G
Ç=G
try:
	u.SecItemImport.argtypes=[N,J,A(p),A(Â),Ã,A(Ä),M,A(K)];u.SecItemImport.restype=B;u.SecCertificateGetTypeID.argtypes=[];u.SecCertificateGetTypeID.restype=V;u.SecIdentityGetTypeID.argtypes=[];u.SecIdentityGetTypeID.restype=V;u.SecKeyGetTypeID.argtypes=[];u.SecKeyGetTypeID.restype=V;u.SecCertificateCreateWithData.argtypes=[L,N];u.SecCertificateCreateWithData.restype=X;u.SecCertificateCopyData.argtypes=[X];u.SecCertificateCopyData.restype=N;u.SecCopyErrorMessageString.argtypes=[B,C];u.SecCopyErrorMessageString.restype=J;u.SecIdentityCreateWithCertificate.argtypes=[E,X,A(q)];u.SecIdentityCreateWithCertificate.restype=B;u.SecKeychainCreate.argtypes=[I,G,C,R,C,A(M)];u.SecKeychainCreate.restype=B;u.SecKeychainDelete.argtypes=[M];u.SecKeychainDelete.restype=B;u.SecPKCS12Import.argtypes=[N,W,A(K)];u.SecPKCS12Import.restype=B;s=k(B,e,C,A(F));t=k(B,e,A(x),A(F));u.SSLSetIOFuncs.argtypes=[D,s,t];u.SSLSetIOFuncs.restype=B;u.SSLSetPeerID.argtypes=[D,I,F];u.SSLSetPeerID.restype=B;u.SSLSetCertificate.argtypes=[D,K];u.SSLSetCertificate.restype=B;u.SSLSetCertificateAuthorities.argtypes=[D,E,R];u.SSLSetCertificateAuthorities.restype=B;u.SSLSetConnection.argtypes=[D,e];u.SSLSetConnection.restype=B;u.SSLSetPeerDomainName.argtypes=[D,I,F];u.SSLSetPeerDomainName.restype=B;u.SSLHandshake.argtypes=[D];u.SSLHandshake.restype=B;u.SSLRead.argtypes=[D,I,F,A(F)];u.SSLRead.restype=B;u.SSLWrite.argtypes=[D,I,F,A(F)];u.SSLWrite.restype=B;u.SSLClose.argtypes=[D];u.SSLClose.restype=B;u.SSLGetNumberSupportedCiphers.argtypes=[D,A(F)];u.SSLGetNumberSupportedCiphers.restype=B;u.SSLGetSupportedCiphers.argtypes=[D,A(P),A(F)];u.SSLGetSupportedCiphers.restype=B;u.SSLSetEnabledCiphers.argtypes=[D,A(P),F];u.SSLSetEnabledCiphers.restype=B;u.SSLGetNumberEnabledCiphers.argtype=[D,A(F)];u.SSLGetNumberEnabledCiphers.restype=B;u.SSLGetEnabledCiphers.argtypes=[D,A(P),A(F)];u.SSLGetEnabledCiphers.restype=B;u.SSLGetNegotiatedCipher.argtypes=[D,A(P)];u.SSLGetNegotiatedCipher.restype=B;u.SSLGetNegotiatedProtocolVersion.argtypes=[D,A(Y)];u.SSLGetNegotiatedProtocolVersion.restype=B;u.SSLCopyPeerTrust.argtypes=[D,A(O)];u.SSLCopyPeerTrust.restype=B;u.SecTrustSetAnchorCertificates.argtypes=[O,K];u.SecTrustSetAnchorCertificates.restype=B;u.SecTrustSetAnchorCertificatesOnly.argstypes=[O,R];u.SecTrustSetAnchorCertificatesOnly.restype=B;u.SecTrustEvaluate.argtypes=[O,A(r)];u.SecTrustEvaluate.restype=B;u.SecTrustGetCertificateCount.argtypes=[O];u.SecTrustGetCertificateCount.restype=H;u.SecTrustGetCertificateAtIndex.argtypes=[O,H];u.SecTrustGetCertificateAtIndex.restype=X;u.SSLCreateContext.argtypes=[L,Å,Æ];u.SSLCreateContext.restype=D;u.SSLSetSessionOption.argtypes=[D,Ç,R];u.SSLSetSessionOption.restype=B;u.SSLSetProtocolVersionMin.argtypes=[D,Y];u.SSLSetProtocolVersionMin.restype=B;u.SSLSetProtocolVersionMax.argtypes=[D,Y];u.SSLSetProtocolVersionMax.restype=B
	try:u.SSLSetALPNProtocols.argtypes=[D,K];u.SSLSetALPNProtocols.restype=B
	except w:pass
	u.SecCopyErrorMessageString.argtypes=[B,C];u.SecCopyErrorMessageString.restype=J;u.SSLReadFunc=s;u.SSLWriteFunc=t;u.SSLContextRef=D;u.SSLProtocol=Y;u.SSLCipherSuite=P;u.SecIdentityRef=q;u.SecKeychainRef=M;u.SecTrustRef=O;u.SecTrustResultType=r;u.SecExternalFormat=p;u.OSStatus=B;u.kSecImportExportPassphrase=J.in_dll(u,'kSecImportExportPassphrase');u.kSecImportItemIdentity=J.in_dll(u,'kSecImportItemIdentity');v.CFRetain.argtypes=[E];v.CFRetain.restype=E;v.CFRelease.argtypes=[E];v.CFRelease.restype=a;v.CFGetTypeID.argtypes=[E];v.CFGetTypeID.restype=V;v.CFStringCreateWithCString.argtypes=[L,I,S];v.CFStringCreateWithCString.restype=J;v.CFStringGetCStringPtr.argtypes=[J,S];v.CFStringGetCStringPtr.restype=I;v.CFStringGetCString.argtypes=[J,I,H,S];v.CFStringGetCString.restype=l;v.CFDataCreate.argtypes=[L,I,H];v.CFDataCreate.restype=N;v.CFDataGetLength.argtypes=[N];v.CFDataGetLength.restype=H;v.CFDataGetBytePtr.argtypes=[N];v.CFDataGetBytePtr.restype=C;v.CFDictionaryCreate.argtypes=[L,A(E),A(E),H,À,Á];v.CFDictionaryCreate.restype=W;v.CFDictionaryGetValue.argtypes=[W,E];v.CFDictionaryGetValue.restype=E;v.CFArrayCreate.argtypes=[L,A(E),H,o];v.CFArrayCreate.restype=K;v.CFArrayCreateMutable.argtypes=[L,H,o];v.CFArrayCreateMutable.restype=n;v.CFArrayAppendValue.argtypes=[n,C];v.CFArrayAppendValue.restype=a;v.CFArrayGetCount.argtypes=[K];v.CFArrayGetCount.restype=H;v.CFArrayGetValueAtIndex.argtypes=[K,H];v.CFArrayGetValueAtIndex.restype=C;v.kCFAllocatorDefault=L.in_dll(v,'kCFAllocatorDefault');v.kCFTypeArrayCallBacks=C.in_dll(v,'kCFTypeArrayCallBacks');v.kCFTypeDictionaryKeyCallBacks=C.in_dll(v,'kCFTypeDictionaryKeyCallBacks');v.kCFTypeDictionaryValueCallBacks=C.in_dll(v,'kCFTypeDictionaryValueCallBacks');v.CFTypeRef=E;v.CFArrayRef=K;v.CFStringRef=J;v.CFDictionaryRef=W
except w:raise f('Error initializing ctypes')from a
class Z:kCFStringEncodingUTF8=S(134217984)