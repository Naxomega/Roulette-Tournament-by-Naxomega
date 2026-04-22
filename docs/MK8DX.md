# Roulette Tournament

Tournoi dans lequel chaque round a des conditions de victoire aleatoirement définies.

Le programme permet de randomiser les règles afin d'éviter de les choisir au plouf-plouf

Vous avez simplement à ouvrir le programme, donner le nombre de participants, choisir le mode et c'est bon !

Plusieurs améliorations seront suseptibles d'apparaître au fur et à mesure, et je suis ouvert aux proposition (voir [ici](https://github.com/Naxomega/Roulette-Tournament?tab=readme-ov-file#d%C3%A9tails-suppl%C3%A9mentaires))

Le programme fonctionne actuellement sur Mario Kart 8 (Deluxe) (Le programme ignore les DLC de MK8DX, si vous ne les avez pas ce n'est pas un problème)

J'ajouterai, à l'avenir, un support pour Mario Kart World (Moins complet que MK8DX, dù à l'absence de nombreux modes bataille, ainsi que du 200cc)

Nous en sommes à la version 1.0.1, voici le changelog : Légers changements liés a un bug empêchant la "position précese" d'être choisie si un modificateur en 2 étapes (composition, type...) était actif, retrait de "position précise" en mode bataille, il sera réajouté dans le futur, pas d'inquiétude !

---

# COURSES

## Conditions de victoire

- Standard (Points)
- Position précise (1-12e)
- Battle Royale (Yoshis)
- Position moyenne (1-12e en moyenne sur les courses)
- Position globale (Equipe uniquement)

## Modificateurs

- Aucun
- Equipe
- Compo spécifique (un ou plusieurs éléments)
- Conduite assistée
- Type de véhicule (Kart, Quad, Moto I/O, Moto Inward, Moto Outward)
- Bots (Facile, Normal, Difficile)
- Objets (Explosif, Personnalisé)
- Cylindrée (Miroir, 200cc)

---

# BATAILLES

## Mode

- Mode Aleatoire
- Ballons
- Bob-ombs
- Traque sur la piste (Equipe est automatiquement activé)
- Soleil
- Pieces

## Conditions

- Standard (Points)
- Score (Equipe uniquement)
- Position moyenne (1-12e en moyenne sur toutes les batailles)
- Battle Royale (Solo uniquement)

## Modificateurs

- Aucun
- Equipe (activé pour traque sur piste)
- Compo spécifique (un ou plusieurs éléments)
- Conduite assistée
- Type de véhicule (Kart, Quad, Moto I/O, Moto Inward, Moto Outward)
- Bots (Facile, Normal, Difficile)
- Objets (Explosif, Personnalisé, Personnalisé par Equipe)

---

# INFOS SUPPLEMENTAIRES

## Condition "Position Précise"

L'objectif de cette position est de terminer la manche dans la position definie au début du round (2e, 4e...), les points du classement de round seront attribues de la méme manieére que le jeu de base.

Exemple :  
- Position définie : 15pts  
- 1 d'écart : 12pts  
- 2 d'écart : 10pts  

---

## Condition "Position Moyenne"

La Position finale des participants est calculée en faisant la moyenne de leurs positions au cours des différentes manches, qui est arrondie a l'entier inférieur.

Exemple :  
3e, 4e, 2e, 1er → 2.5e → 2e

---

## Condition "Position Globale"

La position de l'equipe est calculée en faisant la moyenne de la position de tous les participants.

Ces résultats s'additionnent et l'equipe qui a le moins de points (moins car c'est les positions, ou un chiffre moins élevé gagne : 1er > 4e) remporte la manche.

---

# Classement général

Une fois le classement des rounds fait, chaque personne remporte au classement general le nombre de points d'une course standard :

- 1er : 15pts  
- 2e : 12pts  
- etc.

Ces points sont définis par leur classement dans ce round (et de ces régles).

Pour ce qui concerne le mode en equipe :

- Membres de l'equipe gagnante : **10pts**
- Membres de l'equipe perdante : **5pts**

---

# Détails Supplémentaires

Vous souhaitez organiser un tournoi avec ce système, chouette, allez-y il n'y a pas de problême

Cependant, je vous demandrais de créditer : 

- Mon Pseudo (Naxoméga)

- Ma chaîne Twitch (twitch.com/naxomega)

Si vous avez quelques idées, de nouvelles règles, ou simplement des amélioration en général, n'hésitez pas à ouvrir un ticket (Issue) et j'y répondrais aussi vite que possible :)
