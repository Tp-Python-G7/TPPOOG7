#PROGRAMME SIMULANT UNE APPLICATION QUI GERE UN COMPTE BANCAIRE
#coding:utf-8
class Banque:
    def __init__(self,nomBanque,adresseBanque):       
        self.nomBanque=nomBanque
        self.adresseBanque=adresseBanque
        nomBanque=nomBanque("B.A.C",52-41)
        return"Banque:nom {0},dresse{1}".format(self.nom,self.adresse)

compte = {}


class Client:        
    def __init__(self, nom, prenom, init_solde=0):#Notre methode constructeur
        """Déclaration des attributs"""
Banque.__init__(self,nom,prenom,numeroCompte)
        self.nom = nom
        self.prenom = prenom
        self.solde=init_solde
        self.numeroCompte = 123456
        # self.balance=0 #on ne connait pas la balance,alors on ne déclare pas
        # self.lieuVersement=lieuVersement

        
    # def _set_lieuVersement(self,nouveauVersement):
    #     lieuVersement=property(_get_lieuVersement)
    # def _repr_(self):
print("client:nom({}),prenom({}),numeroCompte({}),lieuVersement({}),balance({})").format(self.nom,self.prenom,self.nimeroCompte,self.lieuVersement,self.balance)
        
    def retrait(self, montant):
        if montant > self.solde:
            return False
        self.solde -= montant
        return True
classCompte : 
    def__init__(self,compteIndividus,compteJoint) : 
    Client.__init__(self,compteIndividu,compteJoint,compteTitre)
    self.compteIndividus=compteIndividu
    Self.compteJoint=compteJoint
    self.compteAterme=compteAterme
    Self.compteTitre=compteTitre
    return"compteIndividu{0},compteJoint{1},compte à terme{2},compteTitre{3}".format(Self.compteIndivudus,self.compteJoint,self.compteTitre,self.compteAterme)
    self.compteAterme=compteTitre

class Controleurs(Banque):
    def __init__(self,nom,matricule):
        self.nom=nom
        self.matricule=matricule
        return "controleur{0},matricule{1}".format(self.nom,self.matricule)
        controleur=controleur("Mahamat Idriss",123-456)
        Banque.__init__(self,nom)#qui fait l'appel au constructeur de la classe mére
        self.matricule=matricule
        #Gestionnaire est aussi recruté de la banque
        
class Gestionnaires(Banque):
    def __init__(self,nom,tel,email):
        self.nom= nom
        self.tel= tel
        self.email= email
        return "gestionnaire{0},nimero telephone{1},compte email{2}".format(self.nom,self.tel,self.email)
        gestionnaire=gestionnaire("Mahamat Ahmat",+10000000000,m@email.com)
Banque.__init__(self,nom,email)#qui fait l'appel au constructeur de la classe mére
        self.tel=tel
        
class Guichetieres(Banque):
     def __init__(self,nomGuichetiere,prenomGuichetiere,poste): 
        self.nom= nomGuichetiere
        self.prenom= prenomGuichetiere
        self.poste= poste
        return "Guichetier:nom{0},prenom{1},poste{2}".format(self.nom,self.prenom,self.poste)
        guichetier=guichetier("Ousmanou","Amadou",12)
        Banque.__init__(self,nomGuichetuier,prenomGuichetier)
self.poste= poste
          
class GestionversementClients(Guichetieres):
      def __init__(self,versementSimple,versementConfrére):  
        self.versementSimple=versementSimple
        self.versementConfrére=versementConfrére
        return "GestionClients:versementsimple{0},versementconfrére{1}".format(self.versermentSimple,self.versementConfrére)
        GestionversementClients=GestionversementClients("")
        Guichetieres.__init__(self,versementSimple)
self.versementConfrére=versementConfrére
            
class Retrait(Guichetieres):
    def __init__(self,gestionRetrait,gestionRetraitchek): 
        self.gestionRetrait=gestionRetrait
        self.gestionRetraitchek=gestionRetraitchek-montant
        return"Retrait:gestionRetrait{0},gestionRetraitchek{1}".format(self.gestionRetrait,self.gestionRetraitchek)
        Retrait=Retrait("")
        Guichetieres.__init__(self,gestionRetrait)
        self.gestionRetraitchek=gestionRetraitchek
class Virement(Guichetieres):
    def __init__(self,virementEpargné,virementCourant): 
        self.virementEpargné=virementEpargné
        self.virementCourant=virementCourant
        serlf.virementMultiple=virementMultiple
        return"Virement:virement epargné{0},virement courant{1},virement multiple{2}".format(self.virementEpargné,self.virementCourant,self.virementMultiple)
        virement=virement("")
        Guichetiers.__init__(self,virementEpargné,viermentCourant)
        self.virementMultiple=virementMultiple
        
class OperationInternationale(Guichetieres):
    def __init__(self,compasation)self.compasation=compasation
        self.dette=dette
        return"operationInternationale:compasation{0},dette{1}".format(self.copasation,self.dette)
        OperationInternationale=OperationInternationale("")
        Guichetieres.__init__(self,copasation,dette)
        self.dette=dette

    

 #programmme principal         

# seul la fonctionnalité client a été devéloppée
def menu():
    print('\t\tMENU')
print('1 - Connexion en tant que Client')
    print('2 - Connexion en tant que Gestionnaire')
    print('3 - Connexion en tant que Guichetier')
    print()

def menu_client():
    print()
    print('\t \tMENU CLIENT')
    print('1  - Effectuer un virement')
    print('2  - Effectuer un retrait')
    print()
# Cas d'un seul client dans la base de données
client = Client("Inconnu", "Inconnu", 40000)

continuer = 'oui'
while continuer == 'oui':
menu()
    reponse=input("Entrez votre choix : ")
    if reponse == '1':
        menu_client()
        rep_client = input("Entrez votre choix : ")
        if rep_client == '2':
            montant = input("Entrez le montant de retrait : ")
            if client.retrait(int(montant)):
                print('Le retrait de {} a été effectué'.format(montant))
                print('Votre nouveau solde est : {} \n'.format(client.solde))
            else:
                print('Le montant est trop grand')
        else:
            print('La fonctionnalité reste à developper !')
      else:
        print('Cette fonctionnalité n\'a pas été devéloppée')

    continuer=input("Voulez vous continuer ? (oui/non) : ")
    
       
        
  
    
           
       
            
    
             
              
  
                  
   
