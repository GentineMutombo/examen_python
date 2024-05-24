from main import personne
# Classe étudiant héritant de Personne
class Etudiant(Personne):  # Héritage: Etudiant est une sorte de Personne
    def __init__(self, nom, prenom, matricule):
        super().__init__(nom, prenom)  # Appel du constructeur de la classe parent
        self.matricule = matricule  # Nouvel attribut spécifique aux étudiants