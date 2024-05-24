
if __name__ == "__main__":
    # Création d'une instance de Faculté
    fac_sciences = Faculte("scienceinfo")

    # Création d'une instance d'Étudiant
    etudiant1 = Etudiant("albert", "ndaliko", "4376")

    # Inscription de l'étudiant à la facult
    fac_sciences.inscrire_etudiant(etudiant1)

    # Affichage des informations de la faculté
    print(fac_sciences)  # Polymorphisme: