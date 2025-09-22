import pytest
from ExDebug1 import environnement_optimal

#test unitaire pour la fonction environnement_optimal()
def test_environnement_optimal():
    #Arrange : préparer des variables d'entrées et le résultat attendu
    temperature = 25
    poussiere = "faible"
    humidite = 40
    resultat_attendu = "Tout est sous contrôle!"

    #Act: appeler la fonction à tester
    restltat_obtenu = environnement_optimal(temperature, poussiere, humidite)

    #Assert: vérifier le résultat
    assert resultat_attendu == restltat_obtenu

def test_environnement_optimal2():
    #Arrange : préparer des variables d'entrées et le résultat attendu
    temperature = 30
    poussiere = "faible"
    humidite = 40
    resultat_attendu = "Environnement non optimal"

    #Act: appeler la fonction à tester
    restltat_obtenu = environnement_optimal(temperature, poussiere, humidite)

    #Assert: vérifier le résultat
    assert resultat_attendu == restltat_obtenu

def test_environnement_optimal3():
    #Arrange : préparer des variables d'entrées et le résultat attendu
    temperature = 25
    poussiere = "faible"
    humidite = 20
    resultat_attendu = "Environnement non optimal"

    #Act: appeler la fonction à tester
    restltat_obtenu = environnement_optimal(temperature, poussiere, humidite)

    #Assert: vérifier le résultat
    assert resultat_attendu == restltat_obtenu

def test_environnement_optimal4():
    #Arrange : préparer des variables d'entrées et le résultat attendu
    temperature = 30
    poussiere = "moyen"
    humidite = 25
    resultat_attendu = "Environnement non optimal"

    #Act: appeler la fonction à tester
    restltat_obtenu = environnement_optimal(temperature, poussiere, humidite)

    #Assert: vérifier le résultat
    assert resultat_attendu == restltat_obtenu