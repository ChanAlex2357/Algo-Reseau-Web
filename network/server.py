from web.site import Site
from .dns import Dns
from network.liaison import Liaison
class Server():
	def __init__(
     self,
     nom_server:str,
     adresse_ip:str,
     dns:Dns = None
    ):
		etat:bool = True;
		lisaisons = list()
		sites = list()

		self.set_nom_server(nom_server);
		self.set_adresse_ip(adresse_ip);
		self.set_sites(sites);
		self.set_lisaisons(lisaisons);
		self.set_etat(etat);
		self.set_dns(dns);
		self.layout = None

		self.parent = None
		self.visited = False
		self.algo_value = None
	def __str__(self):
		return self.stringify()
#Getteurs and Setteurs
	#nom_server
	def get_nom_server(self):
		return self._nom_server;

	def set_nom_server(self,nom_server:str ):
		self._nom_server=nom_server;

	#adresse_ip
	def get_adresse_ip(self):
		return self._adresse_ip;

	def set_adresse_ip(self , adresse_ip:str):
		self._adresse_ip=adresse_ip;

	#sites
	def get_sites(self):
		return self._sites;

	def get_site(self,domaine:str):
		for site in self.get_sites():
			if site.get_nom_domaine() == domaine :
				return site
		return None

	def set_sites(self,sites:list):
		self._sites=sites;
  
	def add_site(self , site_domaine:str , content:str = None):
		for site_web in self.get_sites():
			if site_web.get_nom_domaine() == site_domaine:
				return None

		if content == None :
			content = f"<h1> Hello and welcome on {site_domaine} </h1>"

		site = Site(site_domaine,content)
		self.get_sites().append(site)
		self.get_dns().add_site(site,self.get_adresse_ip())
		return site


	#lisaisons
	def get_lisaisons(self):
		return self._lisaisons

	def set_lisaisons(self,lisaisons:list):
		self._lisaisons=lisaisons

	def get_liaison_with(self,server):
		for liaison in self.get_lisaisons():
			voisin = liaison.get_server_lier(self)
			if server.is_the_same(voisin):
				return liaison
		return None

	def add_liaison(self,server,temps_reponse):
		liaisons = self.get_lisaisons()
		ip = server.get_adresse_ip()
	
		for li in liaisons:
			ip1 = li.get_servers()[0].get_adresse_ip()
			ip2 = li.get_servers()[1].get_adresse_ip()
			if (ip1 == ip) and (ip2 == self.get_adresse_ip()):
				return None
			elif (ip1 == self.get_adresse_ip()) and (ip2 == ip):
				return None
  
		liaison = Liaison((self,server),temps_reponse,True);
		liaisons.append(liaison)
		server.get_lisaisons().append(liaison)
		return liaison

	#etat
	def get_etat(self):
		return self._etat

	def set_etat(self,etat:bool):
		self._etat=etat
	
	def shutdown(self):
		self.set_etat(False)
		Liaison.synch_liaisons(self.get_lisaisons())
  
	def start(self):
		self.set_etat(True)
		Liaison.synch_liaisons(self.get_lisaisons())
  
	#DNS
	def get_dns(self):
		return self._dns

	def set_dns(self,dns:Dns):
		self._dns=dns

	def stringify(self):
		string = "Server Name : "+self.get_nom_server()+"\n"
		string += "Adresse Ip : "+self.get_adresse_ip()+"\n"
		string += "Actif : "+str(self.get_etat())+"\n"
		# Afficher la liste des sites
		string += "Sites : "
		for site in self.get_sites():
			string += "\n\t"+site.stringify()
		# Afficher la liste des liaisons
		string += "\nLiaisons :"
		for li in self.get_lisaisons():
			string += "\n\t"+li.stringify()
		return string

	def simple_string(self):
		string = self.get_nom_server()+" ["+self.get_adresse_ip()+"]("+str(self.get_etat())+")";
		return string; 

	def set_layout(self , layout):
		self.layout = layout
	
	def get_layout(self):
		return self.layout
	
	def is_the_same(self,server):
		return self.get_adresse_ip() == server.get_adresse_ip()
