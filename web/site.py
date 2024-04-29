class Site :
	def __init__(self,nom_domaine,adresse_ip = None):
		self.set_nom_domaine(nom_domaine)
		self.set_adresse_ip(adresse_ip)
#Getteurs and Setteurs
	#nom_domaine
	def get_nom_domaine(self):
		return self._nom_domaine

	def set_nom_domaine(self,nom_domaine):
		self._nom_domaine=nom_domaine

	#adresse_ip
	def get_adresse_ip(self):
		return self._adresse_ip

	def set_adresse_ip(self,adresse_ip):
		self._adresse_ip=adresse_ip

