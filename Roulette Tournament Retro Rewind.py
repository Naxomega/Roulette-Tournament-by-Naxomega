import random
import time
import os
os.system("cls" if os.name == "nt" else "clear")
def condition_course():
    conditions = ["Grand Prix", "Grand Prix", "Grand Prix", "Grand Prix", "Elimination", "Position Précise", "Position Moyenne", "Position Globale (Equipe)"]
    return random.choice(conditions)
def modificateur_course():
    modificateurs = ["Aucun", "2 Equipes", "Duo", "Trio", "Quatuor", "Compo Spécifique", "Type de Véhicule", "Type de Personnage", "Objets", "200cc", "Circuits", "Objets Rapides", "Nuage Shock", "Transmission", "Falling Items"]
    return random.choice(modificateurs)
def composition():
    poids = ["Léger", "Moyen", "Lourd"]
    choix = random.choice(poids)
    if choix == "Léger":
        véhicule = ["Kart Standard", "Moto Standard", "Auto-Pousse", "Doryphare", "Bill Bécane", "Mini-Mob", "Cheepmobile", "Mini-Monstre", "Blue Falcon", "Coin-Coin", "Kamekroiseur", "Jet Capsule"]
        perso = ["Bébé Mario", "Bébé Luigi", "Bébé Peach", "Bébé Daisy", "Toad", "Toadette", "Koopa", "Skelerex"]
    elif choix == "Moyen":
        véhicule = ["Kart Standard", "Moto Standard", "Nostalgia", "Cabriolaile", "Moto Mach", "Etincelle", "Super Bloups", "Carrosse Royal", "Intrépide II", "Cyclo Vroum", "Nitrocyclette", "Dauphine"]
        perso = ["Mario", "Luigi", "Peach", "Daisy", "Yoshi", "Birdo", "Diddy Kong", "Bowser Jr."]
    elif choix == "Lourd":
        véhicule = ["Kart Standard", "Moto Standard", "Buggy Brute", "Crache-Feu", "Bécane Bowser", "Wario Custom", "Kart Piranha", "Bolide Stellaire", "Turbo Flash", "Scoot Comète", "Torpille", "Propulsor"]
        perso = ["Wario", "Waluigi", "Donkey Kong", "Bowser", "Roi Boo", "Harmonie", "Funky Kong", "Bowser Skelet"]
    compo = f"Composition Choisie : {random.choice(perso)}, {random.choice(véhicule)}."
    return compo
def type_véhicule():
    types = ["Kart", "Moto"]
    return random.choice(types)
def type_perso():
    types_perso = ["Légers", "Moyens", "Lourds"]
    return random.choice(types_perso)
def position_précise():
    return random.randint(1, players-1)
def objets_course():
    objets = ["Aléatoire Géneral", "Obtention Aléatoire", "Mode Chaos", "Pluie d'Objets"]
    return random.choice(objets)
def Circuits():
    circuits = ["Vanilla", "Retro", "Custom"]
    return random.choice(circuits)
def Transmission():
    transmission = ["Inward", "Outward"]
    return random.choice(transmission)
players = int(input("Nombre de participants (2-12) ? "))
mode = "c"
if mode == "c":
    os.system("cls" if os.name == "nt" else "clear")
    print("Pour l'instant, uniquement le mode course est présent")
    time.sleep(0.5)
    condition_actuelle = condition_course()
    print("Condition de victoire :", condition_actuelle)
    modificateur_actuel = modificateur_course()
    print("Modificateur de course :", modificateur_actuel)
    if modificateur_actuel == "Compo Spécifique":
        time.sleep(0.5)
        print(composition())
    elif modificateur_actuel == "Type de Véhicule":
        time.sleep(0.5)
        print("Type de véhicule :", type_véhicule())
    elif modificateur_actuel == "Transmission":
        time.sleep(0.5)
        print("La transmission doit être réglée en ", Transmission())
    elif condition_actuelle == "Position Précise":
        time.sleep(0.5)
        print("Position précise :", position_précise())
    elif modificateur_actuel == "Objets":
        time.sleep(0.5)
        print("Type d'objets :", objets_course())
    elif modificateur_actuel == "Type de Personnage":
        time.sleep(0.5)
        print("Les personnages autorisés sont les personnages ", type_perso())

    


elif mode == "b":
    os.system("cls" if os.name == "nt" else "clear")
    print("Mode bataille sélectionné")
    time.sleep(0.5)
    mode_bataille_actuel = mode_bataille()
    print("Mode de bataille sélectionné :", mode_bataille_actuel)
    condition_bataille_actuelle = condition_bataille()
    print("Condition de victoire :", condition_bataille_actuelle)
    modificateur_bataille_actuel = modificateur_bataille()
    print("Modificateur de bataille :", modificateur_bataille_actuel)
    if modificateur_bataille_actuel == "Compo Spécifique":
        time.sleep(0.5)
        print(composition())
    elif modificateur_bataille_actuel == "Type de Véhicule":
        time.sleep(0.5)
        print("Type de véhicule :", type_véhicule())
    elif modificateur_bataille_actuel == "Bots":
        time.sleep(0.5)
        print("Paramètres des bots :", bots())
    elif modificateur_bataille_actuel == "Objets":
        time.sleep(0.5)
        print("Type d'objets :", objets_course())
    if condition_bataille_actuelle == "Position Précise":
        time.sleep(0.5)
        print("Position précise :", position_précise())
    


elif mode == "a":
    os.system("cls" if os.name == "nt" else "clear")
    print("Mode aléatoire sélectionné")
    mode_actuel =  mode_aléatoire()
    print("Mode sélectionné : ", mode_actuel)
    time.sleep(2)
    if mode_actuel == "Course":
        os.system("cls" if os.name == "nt" else "clear")
        print("Mode course sélectionné")
        time.sleep(0.5)
        condition_actuelle = condition_course()
        print("Condition de victoire :", condition_actuelle)
        modificateur_actuel = modificateur_course()
        print("Modificateur de course :", modificateur_actuel)
        if modificateur_actuel == "Compo Spécifique":
            time.sleep(0.5)
            print(composition())
        elif modificateur_actuel == "Type de Véhicule":
            time.sleep(0.5)
            print("Type de véhicule :", type_véhicule())
        elif modificateur_actuel == "Bots":
            time.sleep(0.5)
            print("Paramètres des bots :", bots())
        elif condition_actuelle == "Position Précise":
            time.sleep(0.5)
            print("Position précise :", position_précise())
        elif modificateur_actuel == "Objets":
            time.sleep(0.5)
            print("Type d'objets :", objets_course())
        elif modificateur_actuel == "Cylindrée":
            time.sleep(0.5)
            print("Cylindrée :", cylindrée())
    elif mode_actuel == "Bataille":
        os.system("cls" if os.name == "nt" else "clear")
        print("Mode bataille sélectionné")
        time.sleep(0.5)
        mode_bataille_actuel = mode_bataille()
        print("Mode de bataille sélectionné :", mode_bataille_actuel)
        condition_bataille_actuelle = condition_bataille()
        print("Condition de victoire :", condition_bataille_actuelle)
        modificateur_bataille_actuel = modificateur_bataille()
        print("Modificateur de bataille :", modificateur_bataille_actuel)
        if modificateur_bataille_actuel == "Compo Spécifique":
            time.sleep(0.5)
            print(composition())
        elif modificateur_bataille_actuel == "Type de Véhicule":
            time.sleep(0.5)
            print("Type de véhicule :", type_véhicule())
        elif modificateur_bataille_actuel == "Bots":
            time.sleep(0.5)
            print("Paramètres des bots :", bots())
        elif condition_bataille_actuelle == "Position Précise":
            time.sleep(0.5)
            print("Position précise :", position_précise())
        elif modificateur_bataille_actuel == "Objets":
            time.sleep(0.5)
            print("Type d'objets :", objets_course())

else:
    print("Mode non reconnu")
