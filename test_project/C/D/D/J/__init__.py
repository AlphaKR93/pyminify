from __future__ import annotations
A=bytes
import abc as B
class b(metaclass=B.ABCMeta):
	@B.abstractmethod
	def derive(self,key_material:A):0
	@B.abstractmethod
	def verify(self,key_material:A,expected_key:A):0