import random
import time
import os
os.system("cls" if os.name == "nt" else "clear")
def mode_aléatoire():
    aléatoire = ["Course", "Bataille"]
    return random.choice(aléatoire)
def condition_course():
    conditions = ["Standard", "Position Précise", "Battle Royale", "Position Moyenne", "Position Globale (Equipe)"]
    return random.choice(conditions)
def modificateur_course():
    modificateurs = ["Aucun", "Aucun", "Aucun", "Equipe", "Compo Spécifique", "Type de Véhicule", "Bots", "Objets", "Cylindrée"]
    return random.choice(modificateurs)
def mode_bataille():
    modes = ["Ballons", "Pièces", "Bob-ombs", "Traque sur Piste (Equipe)", "Capture de Soleil", "Bataille Aléatoire"]
    return random.choice(modes)
def condition_bataille():
    conditions = ["Standard", "Score (Equipe)", "Position Moyenne", "Battle Royale (Solo)"]
    return random.choice(conditions)
def modificateur_bataille():
    modificateurs = ["Aucun", "Aucun", "Aucun", "Equipe", "Compo Spécifique", "Type de Véhicule", "Bots", "Objets"]
    return random.choice(modificateurs)
def composition():
    véhicules = ["Kart Standard", "Kart Rétro", "Proto 8", "Nautomobile", "Chabriolet", "Mach-Célère", "Tubul R3", "Beat-Bolide", "Cavalkart", "Paracoccinelly", "Caravéloce", "Sneakart", "Propulsar", "Kart Or", "Mercedes GLA", "Mercedes W25 Flèche d'Argent", "Mercedes 300SL Roadster", "Blue Falcon", "Buggy Tanuki", "Intrépide", "Autorhino", "Magikart", "Koopa-Mobile", "Moto Standard", "Météore", "Sport GP", "Cybertrombe", "Flamboyante", "Méchabécane", "Scootinette", "Epervier", "Yoshimoto", "Destrier de Légende", "Scooter AC", "Quad Standard", "Quad Wiggler", "Quad Nounours", "Malécycle", "Kartoon", "Missile Tornade"]
    roues = ["Roue Standard", "Mastodonte", "Roller", "Classique", "Lisse", "Métal", "Bouton", "Hors-Piste", "Eponge", "Bois", "Coussin", "Standard Bleu", "Masto-Flammes", "Roller Azur", "Classique Rouge", "Cyber-Lisse", "Hors-Piste Rétro", "Roue Or", "Roues GLA", "Triforce", "Feuille", "Archéonique"]
    planeur = ["Aile Standard", "Aile Nuages", "Aile Wario", "Dendinaile", "Ombrelle Peach", "Parachute", "Parapente", "Aile Fleurie", "Bowser-Volant", "Planeur", "Parapente MKTV", "Aile Or", "Aile  Hylienne", "Aile en Papier", "Paravoile"]
    personnage = ["Mario", "Luigi", "Peach", "Daisy", "Harmonie", "Mario Tanuki", "Peach Chat", "Yoshi", "Toad", "Koopa", "Maskass", "Lakitu", "Toadette", "Roi Boo", "Bébé Mario", "Bébé Luigi", "Bébé Peach", "Bébé Daisy", "Bébé Harmonie", "Mario de Métal/Mario d'Or", "Peach d'Or Rose", "Wario", "Waluigi", "Donkey Kong", "Bowser", "Skelerex", "Bowser Jr.", "Bowser Skelet", "Lemmy", "Larry", "Wendy", "Ludwig", "Iggy", "Roy", "Morton", "Fille Inkling", "Garçon Inkling", "Link", "Villageois", "Villageoise", "Marie", "Mii"]
    compo = f"Composition Choisie : {random.choice(personnage)}, {random.choice(véhicules)}, {random.choice(roues)}, {random.choice(planeur)}."
    return compo
def type_véhicule():
    types = ["Kart", "Moto", "Quad", "Moto Inward", "Moto Outward", "Kart", "Kart", "Kart", "Moto", "Moto", "Moto", "Quad", "Quad"]
    return random.choice(types)
def bots():
    robots = ["Facile", "Moyen", "Difficile"]
    return random.choice(robots)
def position_précise():
    return random.randint(1, players)
def objets_course():
    objets = ["Explosif", "Personalisé"]
    return random.choice(objets)
def cylindrée():
    cylindrées = ["200cc", "Miroir"]
    return random.choice(cylindrées)
players = int(input("Nombre de participants (2-12) ? "))
mode = input("Choisir le mode (course [c], bataille [b], aléatoire [a]) ").lower()
if mode == "c":
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
