# Classe faculté
class Faculte:
    def __init__(self, nom):
        self.nom = nom
        self.etudiants = []  # Liste pour stocker les étudiants inscrits

    # Méthode pour inscrire un étudiant
    def inscrire_etudiant(self, etudiant):
        self.etudiants.append(etudiant)  # Ajout de l'étudiant à la liste

    # Surcharge de la méthode __str__ pour afficher les informations de la faculté
    def __str__(self):
        return f"Faculté: {self.nom}, Étudiants inscrits: {[e.matricule for e in self.etudiants]}"
