from network.server import Server
from network.dns import Dns
from web.site import Site
def main():
    presentation();
    # Dns
    dns = Dns();
    # Servers
    server = Server("Server 1","192.162.10.1",dns);
    server2 = Server("Server 2","192.162.10.2",dns);
    server3 = Server("Server 3","192.162.10.3",dns);
    

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
    
    print(server.stringify());
    print(server2.stringify());
    print(dns.stringify());
    import gui

def presentation():
    print("# Dans le cadre d'un projet S4 on ce programme permet de faire la simualation d'un reseau de site web \n# ou l'on va essayer d'expliquer l'algorythme de recherche de chemin\n\n");
main()