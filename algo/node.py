from .link import NodeLink
class Node :
	def __init__( self, node_value:int = None , parent:Node = Node , node_links:list() = None ):
		self.set_node_value(node_value)
		self.set_parent(parent)
		self.set_node_links(node_links)
#Getteurs and Setteurs
	#node_value
	def get_node_value(self):
		return self._node_value

	def set_node_value(self,node_value):
		self._node_value=node_value

	#parent
	def get_parent(self):
		return self._parent

	def set_parent(self,parent):
		self._parent=parent

	#node_links
	def get_node_links(self):
		return self._node_links

	def set_node_links(self,node_links):
		self._node_links=node_links
