class Livre:
    """
        Permet de créer un livre avec son titre, auteur et année
    """"

    def __init__(self,nom,auteur,annee):
        self.nom = nom
        self.auteur = auteur
        self.annee = annee

    def __setattr__(self): 
        pass

    def __getattribute__(self):
        pass
        