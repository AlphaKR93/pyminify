B=isinstance
A=bytes
import hmac
def W(a:A,b:A):
	if not B(a,A)or not B(b,A):raise TypeError('a and b must be bytes.')
	return hmac.compare_digest(a,b)