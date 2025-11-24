R=BaseException
Q=MemoryError
L='utf-8'
K=tuple
I='Unable to allocate memory!'
H=list
G=str
F=len
D=bytes
A=None
import base64 as J,ctypes as B,itertools as N,os,re,ssl as C,struct as O,tempfile as S,typing as P
from.A import Z,T,E,v,M,u
V=re.compile(b'-----BEGIN CERTIFICATE-----\n(.*?)\n-----END CERTIFICATE-----',re.DOTALL)
def W(bytestring:D):A=bytestring;return v.CFDataCreate(v.kCFAllocatorDefault,A,F(A))
def h(tuples:H[K[P.Any,P.Any]]):A=tuples;B=F(A);C=(A[0]for A in A);D=(A[1]for A in A);E=(v.CFTypeRef*B)(*C);G=(v.CFTypeRef*B)(*D);return v.CFDictionaryCreate(v.kCFAllocatorDefault,E,G,B,v.kCFTypeDictionaryKeyCallBacks,v.kCFTypeDictionaryValueCallBacks)
def X(py_bstr:D):A=B.c_char_p(py_bstr);C=v.CFStringCreateWithCString(v.kCFAllocatorDefault,A,Z.kCFStringEncodingUTF8);return C
def y(lst:H[D]):
	D=A
	try:
		D=v.CFArrayCreateMutable(v.kCFAllocatorDefault,0,B.byref(v.kCFTypeArrayCallBacks))
		if not D:raise Q(I)
		for F in lst:
			E=X(F)
			if not E:raise Q(I)
			try:v.CFArrayAppendValue(D,E)
			finally:v.CFRelease(E)
	except R as G:
		if D:v.CFRelease(D)
		raise C.SSLError(f"Unable to allocate array: {G}")from A
	return D
def Y(value:T):
	D=B.POINTER(B.c_void_p);C=v.CFStringGetCStringPtr(D,Z.kCFStringEncodingUTF8)
	if C is A:
		E=B.create_string_buffer(1024);F=v.CFStringGetCString(D,E,1024,Z.kCFStringEncodingUTF8)
		if not F:raise OSError('Error copying C string from CFStringRef')
		C=E.value
	if C is not A:C=C.decode(L)
	return C
def x(error:int,exception_class:type[R]|A=A):
	E=exception_class;D=error
	if D==0:return
	F=u.SecCopyErrorMessageString(D,A);B=Y(F);v.CFRelease(F)
	if B is A or B=='':B=f"OSStatus {D}"
	if E is A:E=C.SSLError
	raise E(B)
def z(pem_bundle:D):
	D=pem_bundle;D=D.replace(b'\r\n',b'\n');G=[J.b64decode(A.group(1))for A in V.finditer(D)]
	if not G:raise C.SSLError('No root certificates specified')
	A=v.CFArrayCreateMutable(v.kCFAllocatorDefault,0,B.byref(v.kCFTypeArrayCallBacks))
	if not A:raise C.SSLError(I)
	try:
		for H in G:
			E=W(H)
			if not E:raise C.SSLError(I)
			F=u.SecCertificateCreateWithData(v.kCFAllocatorDefault,E);v.CFRelease(E)
			if not F:raise C.SSLError('Unable to build cert object!')
			v.CFArrayAppendValue(A,F);v.CFRelease(F)
	except Exception:v.CFRelease(A);raise
	return A
def a(item:E):A=u.SecCertificateGetTypeID();return v.CFGetTypeID(item)==A
def e(item:E):A=u.SecIdentityGetTypeID();return v.CFGetTypeID(item)==A
def ª():C=os.urandom(40);H=J.b16encode(C[:8]).decode(L);D=J.b16encode(C[8:]);E=S.mkdtemp();I=os.path.join(E,H).encode(L);G=u.SecKeychainRef();K=u.SecKeychainCreate(I,F(D),D,False,A,B.byref(G));x(K);return G,E
def f(keychain:M,path:G):
	E=[];G=[];D=A
	with open(path,'rb')as J:H=J.read()
	try:
		I=v.CFDataCreate(v.kCFAllocatorDefault,H,F(H));D=v.CFArrayRef();K=u.SecItemImport(I,A,A,A,0,A,keychain,B.byref(D));x(K);L=v.CFArrayGetCount(D)
		for M in range(L):
			C=v.CFArrayGetValueAtIndex(D,M);C=v.CFTypeRef
			if a(C):v.CFRetain(C);E.append(C)
			elif e(C):v.CFRetain(C);G.append(C)
	finally:
		if D:v.CFRelease(D)
		v.CFRelease(I)
	return G,E
def µ(keychain:M,*I:G|A):
	E=keychain;C=[];D=[];J=(A for A in I if A)
	try:
		for K in J:L,M=f(E,K);D.extend(L);C.extend(M)
		if not D:F=u.SecIdentityRef();O=u.SecIdentityCreateWithCertificate(E,C[0],B.byref(F));x(O);D.append(F);v.CFRelease(C.pop(0))
		H=v.CFArrayCreateMutable(v.kCFAllocatorDefault,0,B.byref(v.kCFTypeArrayCallBacks))
		for P in N.chain(D,C):v.CFArrayAppendValue(H,P)
		return H
	finally:
		for Q in N.chain(D,C):v.CFRelease(Q)
g={'SSLv2':(0,2),'SSLv3':(3,0),'TLSv1':(3,1),'TLSv1.1':(3,2),'TLSv1.2':(3,3)}
def º(version:G):B,C=g[version];D=2;E=48;A=O.pack('>BB',D,E);G=F(A);H=21;I=O.pack('>BBBH',H,B,C,G)+A;return I
class w:kSSLSessionOptionBreakOnServerAuth=0;kSSLProtocol2=1;kSSLProtocol3=2;kTLSProtocol1=4;kTLSProtocol11=7;kTLSProtocol12=8;kTLSProtocol13=10;kTLSProtocolMaxSupported=999;kSSLClientSide=1;kSSLStreamType=0;kSecFormatPEMSequence=10;kSecTrustResultInvalid=0;kSecTrustResultProceed=1;kSecTrustResultDeny=3;kSecTrustResultUnspecified=4;kSecTrustResultRecoverableTrustFailure=5;kSecTrustResultFatalTrustFailure=6;kSecTrustResultOtherError=7;errSSLProtocol=-9800;errSSLWouldBlock=-9803;errSSLClosedGraceful=-9805;errSSLClosedNoNotify=-9816;errSSLClosedAbort=-9806;errSSLXCertChainInvalid=-9807;errSSLCrypto=-9809;errSSLInternal=-9810;errSSLCertExpired=-9814;errSSLCertNotYetValid=-9815;errSSLUnknownRootCert=-9812;errSSLNoRootCert=-9813;errSSLHostNameMismatch=-9843;errSSLPeerHandshakeFail=-9824;errSSLPeerUserCancelled=-9839;errSSLWeakPeerEphemeralDHKey=-9850;errSSLServerAuthCompleted=-9841;errSSLRecordOverflow=-9847;errSecVerifyFailed=-67808;errSecNoTrustSettings=-25263;errSecItemNotFound=-25300;errSecInvalidTrustSettings=-25262