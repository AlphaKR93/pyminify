try:from fastapi_cli.cli import main as A
except ImportError:A=None
def B():
	if not A:B='To use the fastapi command, please install "fastapi[standard]":\n\n\tpip install "fastapi[standard]"\n';print(B);raise RuntimeError(B)
	A()