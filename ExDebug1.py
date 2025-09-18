def environnement_optimal(temp, poussiere, humidite):
    """
    Vérifie si l'environnement d'un ordinateur est optimal.

    Paramètres :
    - temp : température en °C (int ou float)
    - poussiere : niveau de poussière ("faible", "moyen", "élevé")
    - humidite : taux d’humidité en % (int ou float)

    Retour :
    - "Tout est sous contrôle!" si toutes les conditions sont respectées
    - "Environnement non optimal" sinon (après avoir affiché les problèmes détectés)
    """

    alerte = False

    # Vérification température
    if temp < 18:
        print("Température trop basse")
        alerte = True
    elif temp > 27:
        print("Température trop élevée")
        alerte = True

    # Vérification humidité
    if humidite <= 30:
        print("Humidité trop basse")
        alerte = True
    elif humidite >= 50:
        print("Humidité trop élevée")
        alerte = True

    # Vérification poussière
    if poussiere != "faible":
        print("Trop de poussière")
        alerte = True

    # Retour final
    if not alerte:
        return "Tout est sous contrôle!"
    else:
        return "Environnement non optimal"


if __name__ == "__main__":
    #print(environnement_optimal(25, "faible", 40))

    #créer 3 listes (temp, pousiere, humidité)
    #faire une boucle pour 3 ordinateurs
        #demander temp, poussiere, humidite
        #mettre les valeurs dans leurs listes

    # listes
    liste_temp = []
    liste_poussiere = []
    liste_humidite = []

    nb_ordinateurs = 3
    for i in range(nb_ordinateurs):
        #entrée de données
        temp = float(input("Entrez la température : "))
        poussiere = input("Entrez le niveau de poussière (faible, moyen, élevé) : ")
        humidite = float(input("Entrez l'humidité : "))
        print("-" * 30)

        #ajouter valeurs aux listes
        liste_temp.append(temp)
        liste_poussiere.append(poussiere)
        liste_humidite.append(humidite)

    #TODO: pour les 3 ordis
        #TODO: utiliser la fonction et afficher le résultat