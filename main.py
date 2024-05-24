# Classe de base pour toutes les personnes dans l'université
class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom  # Encapsulation: On cache les détails d'implémentation
        self.prenom = prenom