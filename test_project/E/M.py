import sys as B,B as E
for D in('urllib3','idna'):
	locals()[D]=__import__(D)
	for A in list(B.modules):
		if A==D or A.startswith(f"{D}."):B.modules[f"requests.packages.{A}"]=B.modules[A]
C=E.__name__
for A in list(B.modules):
	if A==C or A.startswith(f"{C}."):C=C.replace(C,'chardet');B.modules[f"requests.packages.{C}"]=B.modules[A]