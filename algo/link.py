from .node import Node

class NodeLink :
	def __init__(self,link_value:int,next_node:Node):
		self.set_link_value(link_value)
		self.set_next_node(next_node)
#Getteurs and Setteurs
	#link_value
	def get_link_value(self):
		return self._link_value

	def set_link_value(self,link_value):
		self._link_value=link_value

	#next_node
	def get_next_node(self):
		return self._next_node

	def set_next_node(self,next_node):
		self._next_node=next_node
