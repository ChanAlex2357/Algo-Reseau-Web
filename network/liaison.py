class Liaison :
	def __init__(self,servers,temps_reponse,etat):
		self.set_servers(servers)
		self.set_temps_reponse(temps_reponse)
		self.set_etat(etat)
#Getteurs and Setteurs
	#servers
	def get_servers(self):
		return self._servers

	def set_servers(self,servers):
		self._servers=servers

	#temps_reponse
	def get_temps_reponse(self):
		return self._temps_reponse

	def set_temps_reponse(self,temps_reponse):
		self._temps_reponse=temps_reponse

	#etat
	def get_etat(self):
		return self._etat

	def set_etat(self,etat):
		self._etat=etat

	def stringify(self):
		string = self.get_servers()[0].simple_string()+" <-- "+self.get_temps_reponse()+" --> "+self.get_servers()[1].simple_string();
		return string;