class Site :
	def __init__(self,nom_domaine,content = None):
		self.set_nom_domaine(nom_domaine)
		self.set_content(content)
#Getteurs and Setteurs
	#nom_domaine
	def get_nom_domaine(self):
		return self._nom_domaine

	def set_nom_domaine(self,nom_domaine):
		self._nom_domaine=nom_domaine

	#content
	def get_content(self):
		return self._content

	def set_content(self,content):
		self._content=content

	def stringify(self):
		return self.get_nom_domaine()