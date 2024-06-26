from web.site import Site
class Dns :
    def __init__(self):
        sites = dict()
        self.set_sites(sites)

#Getteurs and Setteurs
	#sites
    def get_sites(self):
    	return self._sites
        
    def set_sites(self,sites):
    	self._sites=sites

    def add_site(self,site:Site,adresse:str):
        domaine = site.get_nom_domaine()
        keys = self.get_sites().keys()
        adresses_ip = list()
        if domaine in keys:
            adresses_ip = self.get_sites().get(domaine);
            adresses_ip.append(adresse)
        else:
            adresses_ip.append(adresse)
            self.get_sites().__setitem__(domaine,adresses_ip)
    
    def get_domaine_ip(self,domaine:str):
        adresses_ip = self.get_sites().get(domaine)
        return adresses_ip

    def stringify(self):
        string = "~~ DNS ~~\n";
        string += "Sites : "+str(self.get_sites())+"\n";
        return string; 