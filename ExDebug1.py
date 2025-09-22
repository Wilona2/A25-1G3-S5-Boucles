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
    #créer 3 listes (temp, pousiere, humidité)
    #faire une boucle pour chaque ordinateur
        #demander temp, poussiere, humidite
        #mettre les valeurs dans leurs listes

    #listes
    liste_temp = []
    liste_poussiere = []
    liste_humidite = []

    #demander le nombre d'ordinateurs
    nb_ordinateurs = 0
    try:
        while True:
            nb_ordinateurs = int(input("Nombre d'ordinateurs : "))
            break
    except ValueError:
        print("Erreur: veuillez entrer un nombre.")

    #initialiser valeurs
    temp = 0
    humidite = 0

    #entrée de données (temp/poussiere/humidite) + gestion d'exceptions
    for i in range(nb_ordinateurs):
        while True: #seulement accepter un nombre
            try:
                temp = float(input("Entrez la température : "))
                break
            except ValueError:
                print("Erreur: veuillez entrer un nombre.")
        while True: #seulement accepter l'un des trois choix. Sinon, recommencer
            poussiere = (str(input("Entrez le niveau de poussière (faible, moyen, élevé) : ")))
            poussiere = poussiere.lower()
            if poussiere == "faible" or "moyen" or "élevé":
                break
            else: print("Erreur: veuillez choisir l'une des trois options.")
        while True:
            try:
                humidite = float(input("Entrez l'humidité : "))
                break
            except ValueError:
                print("Erreur: veuillez entrer un nombre.")
        print("-"*30)

        #ajouter valeurs aux listes
        liste_temp.append(temp)
        liste_poussiere.append(poussiere)
        liste_humidite.append(humidite)

    #pour chaque ordi : utiliser la fonction et afficher le résultat
    indice = 0
    no_ordi = 1 #numero de l'ordi
    for i in range(nb_ordinateurs):
        print("*" * 30)
        print(f"** Ordinateur {no_ordi} :",
              environnement_optimal(liste_temp[indice], liste_poussiere[indice], liste_humidite[indice]))
        indice += 1
        no_ordi += 1