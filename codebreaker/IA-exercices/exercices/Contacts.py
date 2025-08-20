# Gestionnaire de Contacts en Python

contacts = {}

#Pour l'ajout d'un contact
def ajouter_contact():
    nom = input("Nom du contact : ")
    numero = input("Numéro de téléphone : ")
    email = input("Adresse email : ")

    contacts[nom] = {
        "numero": numero,
        "email": email,
    }
    print(f" 💾Contact '{nom}' ajouté avec succès !")

#Pour afficher tous les contacts
def afficher_contacts():
    if not contacts:
        print("Aucun contact enregistré.")
        return
    print("\n--- Liste des Contacts ---")
    for nom, infos in contacts.items():
        print(f"👤 {nom}")
        print(f"   📞 Numéro : {infos['numero']}")
        print(f"   📧 Email : {infos['email']}")

#Pour la echercher un contact par nom
def rechercher_contact():
    nom = input("Entrez le nom à rechercher : ")
    if nom in contacts:
        infos = contacts[nom]
        print(f"👤 {nom}")
        print(f"   📞 Numéro : {infos['numero']}")
        print(f"   📧 Email : {infos['email']}")
        print(f"   ✉️ Message : {infos['message']}")
    else:
        print("❌ Contact introuvable.")

#Pour modifier un contact
def modifier_contact():
    nom = input("Nom du contact à modifier : ")
    if nom in contacts:
        print("Que voulez-vous modifier ?")
        print("1. Numéro")
        print("2. Email")
        choix = input("Votre choix : ")

        if choix == "1":
            nouveau_numero = input("Nouveau numéro : ")
            contacts[nom]["numero"] = nouveau_numero
            print(" Numéro modifié avec succès !")
        elif choix == "2":
            nouvel_email = input("Nouvel email : ")
            contacts[nom]["email"] = nouvel_email
            print("✅ Email modifié avec succès !")
        else:
            print("❌Choix invalide.")
    else:
        print("❌ Contact introuvable.")

# Supprimer un contact
def supprimer_contact():
    nom = input("Nom du contact à supprimer : ")
    if nom in contacts:
        del contacts[nom]
        print(f"Contact '{nom}' supprimé avec succès !")
    else:
        print("❌ Contact introuvable.")

# Sauvegarder les contacts dans un fichier texte
def sauvegarder_contacts():
    with open("contacts.txt", "w") as f:
        for nom, infos in contacts.items():
            f.write(f"{nom} | {infos['numero']} | {infos['email']} | {infos['message']}\n")
    print("💾 Contacts sauvegardés dans 'contacts.txt'.")

# Menu principal
def menu():
    while True:
        print("\n=== Gestionnaire de Contacts ===")
        print("1. Ajouter un contact")
        print("2. Afficher tous les contacts")
        print("3. Rechercher un contact")
        print("4. Modifier un contact")
        print("5. Supprimer un contact")
        print("6. Sauvegarder les contacts")
        print("0. Quitter")

        choix = input("Votre choix : ")

        if choix == "1":
            ajouter_contact()
        elif choix == "2":
            afficher_contacts()
        elif choix == "3":
            rechercher_contact()
        elif choix == "4":
            modifier_contact()
        elif choix == "5":
            supprimer_contact()
        elif choix == "6":
            sauvegarder_contacts()
        elif choix == "0":
            print("👋 Au revoir !")
            break
        else:
            print("⚠️ Choix invalide, essayez encore.")

menu()