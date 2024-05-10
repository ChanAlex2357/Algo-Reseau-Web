
class Liaison :
	def __init__(self,servers,temps_reponse:int,etat):
		self.set_servers(servers)
		self.set_temps_reponse(temps_reponse)
		self.set_etat(self.sync_etat())
		self.layout = None

	def sync_etat(self):
		etat=True
		for server in self.get_servers():
			if not server.get_etat():
				etat = False
		return etat
#Getteurs and Setteurs
	#servers
	def get_servers(self):
		return self._servers

	def set_servers(self,servers):
		self._servers=servers

	#temps_reponse
	def get_temps_reponse(self):
		return self._temps_reponse

	def set_temps_reponse(self,temps_reponse:int):
		self._temps_reponse=temps_reponse

	#etat
	def get_etat(self):
		return self._etat

	def set_etat(self,etat):
		self._etat=etat

	def stringify(self):
		string = self.get_servers()[0].simple_string()+f" <-- {self.get_temps_reponse()} --> "+self.get_servers()[1].simple_string()
		return string
	def set_layout(self , layout):
		self.layout = layout
	
	def get_layout(self):
		return self.layout

	'''Recuperer le server voisin lier par cette liaison
		ARGS
			server : le server qui veut connaitre son voisin
		Return 
			voisin si le voisin existe 
   			sinon None quand la source n'appartient pas a cette liaison 
  	'''
	def get_server_lier(self,server) :
		#  Considerer le premier server comme voisin
		voisin = self.get_servers()[0]
		if voisin.get_adresse_ip() == server.get_adresse_ip():
			# Prendre le deuxieme server comme voisin
			voisin = self.get_servers()[1]
		elif self.get_servers()[1].get_adresse_ip() != server.get_adresse_ip():
			# On ne peut pas prendre le premier comme voisin 
   			# si le deuxieme server n'est pas identique a la source donnee
			voisin = None
		return voisin
	def synch_liaisons(liaisons:list):
		for liaison in liaisons:
			liaison.sync_etat()