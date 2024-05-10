class ServerPath :
	def __init__(self,server_depart,server_arrivee):
		self.set_server_depart(server_depart)
		self.set_server_arrivee(server_arrivee)
#Getteurs and Setteurs
	#server_depart
	def get_server_depart(self):
		return self._server_depart

	def set_server_depart(self,server_depart):
		self._server_depart=server_depart

	#server_arrivee
	def get_server_arrivee(self):
		return self._server_arrivee

	def set_server_arrivee(self,server_arrivee):
		self._server_arrivee=server_arrivee

