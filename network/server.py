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
		lisaisons = list();
		sites = list();

		self.set_nom_server(nom_server);
		self.set_adresse_ip(adresse_ip);
		self.set_sites(sites);
		self.set_lisaisons(lisaisons);
		self.set_etat(etat);
		self.set_dns(dns);

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

	def set_sites(self,sites:list):
		self._sites=sites;
  
	def add_site(self , site:str):
		self.get_sites().append(site);
		self.get_dns().add_site(site,self.get_adresse_ip());


	#lisaisons
	def get_lisaisons(self):
		return self._lisaisons

	def set_lisaisons(self,lisaisons:list):
		self._lisaisons=lisaisons

	def add_liaison(self,server,temps_reponse):
		liaison = Liaison((self,server),temps_reponse,True);
		self.get_lisaisons().append(liaison);
		server.get_lisaisons().append(liaison);


	#etat
	def get_etat(self):
		return self._etat

	def set_etat(self,etat:bool):
		self._etat=etat
	
	def shutdown(self):
		self.set_etat(False);
  
	def start(self):
		self.set_etat(True);
  
	#DNS
	def get_dns(self):
		return self._dns

	def set_dns(self,dns:Dns):
		self._dns=dns

	def stringify(self):
		string = "Server Name : "+self.get_nom_server()+"\n";
		string += "Adresse Ip : "+self.get_adresse_ip()+"\n";
		string += "Actif : "+str(self.get_etat())+"\n";
		string += "Sites : "+str(self.get_sites())+"\n";
		string += "Liaisons :";
		for li in self.get_lisaisons():
			string += "\n\t"+li.stringify();
		return string;

	def simple_string(self):
		string = self.get_nom_server()+" ["+self.get_adresse_ip()+"]("+str(self.get_etat())+")";
		return string; 