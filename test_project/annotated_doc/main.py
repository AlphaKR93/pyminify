class Doc:
	def __init__(self,documentation:str):self.documentation=documentation
	def __repr__(self):return f"Doc({self.documentation!r})"
	def __hash__(self):return hash(self.documentation)
	def __eq__(self,other:object):
		if not isinstance(other,Doc):return NotImplemented
		return self.documentation==other.documentation