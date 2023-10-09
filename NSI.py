from random import *

couleurs = ['pique', 'coeur', 'carreau', 'trefle']
noms = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
valeur = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Valet': 11, 'Dame': 12, 'Roi': 13, 'As': 14}


class Carte:
    def __init__(self, nom, couleur):
        # Affectation des attributs nom et couleur avec contrôle.
        assert nom in noms  # vérifie que le nom fait bien partie de la liste
        assert couleur in couleurs  # vérifie que la couleur fait bien partie de la liste
        self.nom = nom
        self.couleur = couleur
        self.valeur = valeur[nom]

    ############## Définition des méthodes d’instances avec contrôle #######
    def setNom(self, nom):  # setter
        assert nom in noms
        self.nom = nom

    def getNom(self):  # getter
        return f"(le nom de la carte : {self.nom})"

    def getCouleur(self):  # getter
        return f"(la couleur de la carte : {self.couleur})"

    def getValeur(self):  # getter
        return f"(la valeur de la carte : {self.valeur})"

    def egalite(self, carte):
        '''Renvoie True si les cartes ont la même valeur, False sinon
        carte: Objet de type Carte'''
        if self.valeur == carte.valeur:
            return True
        else:
            return False

    def estSuperieureA(self, carte):
        '''Renvoie True si la valeur de self est supérieure à celle de carte,
        False sinon carte: Objet de type Carte'''
        if self.valeur > carte.valeur:
            return True
        else:
            return False

    def estInferieureA(self, carte):
        ''' Renvoie True si la valeur de self est inférieure à celle de carte,
        False sinon carte: Objet de type Carte '''
        if self.valeur < carte.valeur:
            return True
        else:
            return False


def testCarte():
    valetCoeur = Carte('Valet', 'coeur')
    print('Nom:', valetCoeur.getNom())
    print('Couleur:', valetCoeur.getCouleur())
    print('Valeur:', valetCoeur.getValeur())
    valetCoeur.setNom('Dame')
    print('Nom modifié:', valetCoeur.getNom())
    print('Valeur modifiée:', valetCoeur.getValeur())
    carreau2 = Carte('2', 'carreau')
    assert carreau2.egalite(valetCoeur) == False
    assert carreau2.estInferieureA(valetCoeur) == True
    # Essai des exceptions: cette instruction conduit à une erreur
    dameCarreau = Carte('Dame', 'COooEUR ')

class JeuCartes:
    def __init__(self, nbCartes=52):
        # Le jeu doit comporter 32 ou 52 cartes, effectuer un contrôle
        assert nbCartes == 52 or nbCartes == 32
        self.jeu = []  # self.jeu est une liste des self.nbCartes
        for j in range(0, len(couleurs)):
            for i in range(0, len(noms)):
                carte = Carte(noms[i], couleurs[j])  # Crée une carte
                self.jeu.append(carte)  # Ajoute la carte au jeu

    ################# Définition des méthodes d’instances #################
    def getTailleJeu(self):
        '''Fonction qui retourne le nombre de cartes du jeu
        Valeur retournée: type int'''
        return len(self.jeu)

    def getJeu(self):
        '''Renvoie la liste des cartes correspondant à l’attribut self.jeu'''
        return self.jeu

    def melanger(self):
        '''Mélange sur place les cartes de la liste des cartes associée au champ self.jeu'''
        shuffle(self.jeu)

    def distribuerCarte(self):
        '''Cette fonction permet de distribuer une carte à un joueur. Elle retourne la carte
        Valeur retournée: Objet de type Carte'''
        if self.jeu:
            return self.jeu.pop()
        else:
            print("Plus de cartes à distribuer.")
            return None

    def distribuerJeu(self, nbJoueurs, nbCartes):
        '''Cette méthode distribue nbCartes à chacun des nbJoueurs, vérifie que la distribution est possible
        Valeur retournée: une liste contenant les listes de cartes distribuées à chaque joueur'''
        global jeu_joueur
        jeu_joueur = []

        for i in range(0, nbJoueurs):
            main = []
            for j in range(0, nbCartes):
                carte = self.distribuerCarte()
                if carte:
                    main.append(carte)
            jeu_joueur.append(main)

        return jeu_joueur
        
# Dans l’éditeur  PYTHON : fichier  jeucartes.py
#################  Test de la  classe  JeuCartes  #######
def  testJeuCartes ():
    jeu52 = JeuCartes (52)
    jeu52.melanger ()
    L=jeu52.getJeu ()
    carte= L[2] # le 3e carte
    print('Nom:', carte.getNom ())
    print('Couleur:', carte.getCouleur ())
    print('Valeur:', carte.getValeur ())
    # Distribution  de 4 cartes à 3 joueurs
    distribution_4j_13c = jeu52.distribuerJeu (4,13)
    for i in range (4):
        print('Joueur ', i+1, ':')
        listeCartes = distribution_4j_13c[i]
        for c in  listeCartes:
            print(c.getNom (), 'de', c.getCouleur ())            
liste_nom = []
n=0
class Joueur:
    def __init__(self, nom):
        global liste_nom
        assert nom not in liste_nom
        self.Nom = nom
        liste_nom.append(self.Nom)
        self.nbCartes = 0
        self.main = []
        self.victoire = 0

    def setMain(self, distribution):
        global n
        print(distribution)
        self.main = distribution
        n = n + 1

    def getNom(self):
        return self.Nom

    def getNbCartes(self):
        self.nbCartes = len(self.main)
        return self.nbCartes

    def printMain(self):
        print(f"(voici la main de : {self.Nom})")
        for i in self.main:
            print(f"({i.getNom()} de {i.getCouleur()})")

    def jouerCarte(self):
        global carte
        if len(self.main) > 0:
            carte = self.main[len(self.main) - 1]
            self.main.pop(len(self.main) - 1)
            return carte
        else:
            return None

    def insererCarte(self, carte):
        self.main.append(carte)

def testJoueur():
    joueur1 = Joueur('Toto')
    joueur2 = Joueur('Dupont')
    jeu52 = JeuCartes(52)
    jeu52.melanger()
    distribution_2j_6c = jeu52.distribuerJeu(2, 6)
    joueur1.setMain(distribution_2j_6c[0])
    print(joueur1.getNom(), ' a ', joueur1.getNbCartes(), ' cartes ')
    joueur1.printMain()
    carteJouee = joueur1.jouerCarte()
    print(joueur1.getNom(), ' a ', joueur1.getNbCartes(), ' cartes ')
    joueur1.printMain()
    joueur1.insererCarte(carteJouee)
    print(joueur1.getNom(), ' a ', joueur1.getNbCartes(), ' cartes ')
    joueur1.printMain()
    
class bataille:
    def __init__(self):
        
    


"""La classe bataille doit instancier un jeu de cartes,
deux joueurs et implémanter les méthodes tour et
jouer (qui devront effectuer les affichages attendus par l’affiche situé un peu plus loin).
Proposer un jeude test pour cette classe.
Vous devrez ensuite écrire le programme principal pour lancer une partie de bataille.
Vous devrez définir le nombre de tours qui seront effectués dans ce jeu."""