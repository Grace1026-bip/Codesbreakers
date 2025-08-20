# Exercice 1 : Manipulation de listes

# notes = [12, 15, 8, 17, 9]
# print("Voici, les notes de l'étudiant X : ", notes)

# notes.append(14)
# print("Il a obtenu une nouvelle note de 14, qu'on a rajouté :", notes)

# notes.remove(8)
# print("Un prof a retranché sa cote qui était de 8 :", notes)

# notes.sort()
# print("On a triée ses notes en ordre croissant et ça a donné :", notes)

# # notes.sort(reverse=True)
# # print("On a triée ses notes en ordre décroissant et ça a donné :", notes)

# moy = sum(notes)/ len(notes)
# print("En tout, il a obtenu une moyenne de :", moy)

# Exercice 2 : Dictionnaire des étudiants

# etudiants = {"Alice" : 21,"Bob" : 22,"Charlie" : 20}
# print("Voici les candidats selectionnés et leurs âges : \n", etudiants)

# etudiants.update({"Alice": 22, "David": 23})
# print("Y a un nouveau candidats et on a modifié l'âge d'Alice qui vient de fêter son anniversaire\n", etudiants)
# del etudiants["Charlie"]
# print("Malheureusement Charlie vient d'être disqualifié :\n", etudiants)

# Exercice 3 : Ensemble de matières
# matiere_1 = {"math", "physique", "informatique"}
# matiere_2 = {"biologie", "informatique", "chimie"}

# for i in matiere_1 and matiere_2:
# 	if i in matiere_1 and matiere_2:
# 		print("La matière commune est: ", i)
# 	if i in matiere_1 :
# 		print("Les matières du premier ensemble sont: ", i)
# toutes = matiere_1.union(matiere_2)
# print("Toutes les matières sont :", toutes)
# uniques_m1 = matiere_1.difference(matiere_2)
# print("Matières uniquement dans matiere_1 :", uniques_m1)

# # Exercice 4 : Calcul de distance entre deux points
# import math
# def distance(p1, p2):
#     x1, y1 = p1
#     x2, y2 = p2
#     return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
# # Exemple
# print(distance((0, 0), (3, 4)))

# Exercice 5 : Gestion de produits
produits = [
    {"nom": "Stylo", "prix": 1500},
    {"nom": "Cahier", "prix": 2500},
    {"nom": "Livre", "prix": 7500}
]
print("Nos produits sont :", produits)

produits.append({"nom": "Règle", "prix": 1000})
print("Après ajout d'un produit :", produits)

total = sum(p["prix"] for p in produits)
print("Prix total des produits :", total, "FC")

print("Produits > 2000 FC :")
for p in produits:
    if p["prix"] > 2000:
        print(p)