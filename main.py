from network.server import Server
from network.dns import Dns
from web.site import Site
from gui.application import Application
from algo import dijkstra
def main():
    presentation()
    # Dns
    dns = Dns();
    server_list = list()
    liaisons = list()
    # Servers
    
    app = Application(dns,server_list,liaisons)
    app.run()
    

def primary_test():
    # Dns
    dns = Dns();
    server_list = list()
    # Servers
    server = Server("Server 1","192.162.10.1",dns);
    server2 = Server("Server 2","192.162.10.2",dns);
    server3 = Server("Server 3","192.162.10.3",dns);
    
    server_list.append(server)
    server_list.append(server2)
    server_list.append(server3)
    

    # Liaisons
    server.add_liaison(server2,"15");
    server.add_liaison(server3,"25");

    # Sites
    server.add_site("www.facebook.com");
    server.add_site("www.youtube.com");
    server.add_site("www.facebook.fr");
    server.add_site("www.facebook.en");

    server2.add_site("www.facebook.com");
    server2.add_site("www.youtube.com");




def presentation():
    print("# Dans le cadre d'un projet S4 on ce programme permet de faire la simualation d'un reseau de site web \n# ou l'on va essayer d'expliquer l'algorythme de recherche de chemin\n\n");
main()