import tkinter as tk

class Livre:
    def __init__(self, ISBN, titre, auteur, disponibilite):
        self.ISBN = ISBN
        self.titre = titre
        self.auteur = auteur
        self.disponibilite = disponibilite

    def emprunter(self):
        if self.disponibilite >= 1:
            print("Emprunter le livre")
            self.disponibilite -= 1
        else:
            print("Ce livre n'est pas disponible")

    def retourner(self):
        if self.disponibilite == 0:
            print("Le livre est retourne")
            self.disponibilite += 1

    def __str__(self):
        return f"ISBN: {self.ISBN}, Titre: {self.titre}, Auteur: {self.auteur}, Disponibilite: {self.disponibilite}"

class Membre:
    def __init__(self, nom, prenom, souscription):
        self.nom = nom
        self.prenom = prenom
        self.souscription = souscription
        self.livres_empruntes = ['python']

    def emprunter_livre(self, livre):
        if livre not in self.livres_empruntes:
            self.livres_empruntes.append(livre)
            return f"{livre} a ete emprunte par {self.nom} {self.prenom}"
        else:
            return f"{self.nom} {self.prenom} a deje emprunte {livre}."

    def retourner_livre(self, livre):
        if livre in self.livres_empruntes:
            self.livres_empruntes.remove(livre)
            return f"{livre} a ete retourne par {self.nom} {self.prenom}"
        else:
            return f"{self.nom} {self.prenom} n'a pas emprunte {livre}."

    def afficher_livre_empruntes(self):
        if self.livres_empruntes:
            result = f"Livres empruntes par {self.nom} {self.prenom}:\n"
            for livre in self.livres_empruntes:
                result += livre.titre + "\n"
            return result
        else:
            return f"Aucun livre emprunte par {self.nom} {self.prenom}"

class Biblioteque:
    def __init__(self):
        self.liste_livre = [Livre(1,'java','nouha',3)]

    def ajouter_livre(self, livre):
        self.liste_livre.append(livre)

    def supprime_livre(self, ISBN, titre, auteur, disponibilite):
        for livre in self.liste_livre:
            if (livre.ISBN == ISBN and livre.titre == titre and livre.auteur == auteur and livre.disponibilite == disponibilite):
                self.liste_livre.remove(livre)
                return "Le livre a ete supprime avec succes"
        return "Le livre n'a pas ete trouve dans la bibliotheque"

    def rechercher(self, titre):
        for livre in self.liste_livre:
            if livre.titre == titre:
                return livre
        #return None
        print("ce livre n'exist pas")

    def emprunter(self, titre):
        for livre in self.liste_livre:
            if livre.titre == titre:
                if livre.disponibilite >= 1:
                    livre.disponibilite -= 1
                    return "Le livre a ete emprunte"
                else:
                    return "Le livre n'est pas disponible pour l'emprunt"
        return "Ce livre n'est pas dans la bibliotheque"

    def retourner(self, titre):
        for livre in self.liste_livre:
            if livre.titre == titre:
                if livre.disponibilite == 0:
                    livre.disponibilite += 1
                    return "Le livre a ete retourne"
                else:
                    return "Le livre n'a pas ete emprunte"
        return "Ce livre n'est pas dans la bibliotheque"
bibliotheque=Biblioteque()
def emprunter_livre():
    livre = Livre(int(entry_ISBN.get()), entry_titre.get(), entry_auteur.get(), int(entry_disponibilite.get()))
    livre.emprunter()
    label_result.config(text=str(livre))

def retourner_livre():
    livre = Livre(int(entry_ISBN.get()), entry_titre.get(), entry_auteur.get(), int(entry_disponibilite.get()))
    livre.retourner()
    label_result.config(text=str(livre))

def emprunter_livre_membre():
    global m1
    livre = entry_livre.get()
    result = m1.emprunter_livre(livre)
    label_result.config(text=result)

def retourner_livre_membre():
    global m1
    livre = entry_livre.get()
    result = m1.retourner_livre(livre)
    label_result.config(text=result)

def afficher_livre():
    global m1
    result = m1.afficher_livre_empruntes()
    label_result.config(text=result)

def ajouter_livre_gui():
    ISBN = int(entry_ISBN.get())
    titre = entry_titre.get()
    auteur = entry_auteur.get()
    disponibilite = int(entry_disponibilite.get())
    livre = Livre(ISBN, titre, auteur, disponibilite)
    bibliotheque.ajouter_livre(livre)
    label_result.config(text="Le livre a ete ajoute avec succes")

def supprimer_livre_gui():
    ISBN = int(entry_ISBN.get())
    titre = entry_titre.get()
    auteur = entry_auteur.get()
    disponibilite = int(entry_disponibilite.get())
    result = bibliotheque.supprime_livre(ISBN, titre, auteur, disponibilite)
    label_result.config(text=result)

def rechercher_livre_gui():
    titre = entry_titre.get()
    livre = bibliotheque.rechercher(titre)
    if livre:
        label_result.config(text=f"Le livre existe:\nISBN: {livre.ISBN}, Titre: {livre.titre}, Auteur: {livre.auteur}, Disponibilite: {livre.disponibilite}")
    else:
        label_result.config(text="Ce livre n'existe pas dans la bibliotheque")

def emprunter_livre_gui():
    titre = entry_titre.get()
    result = bibliotheque.emprunter(titre)
    label_result.config(text=result)

def retourner_livre_gui():
    titre = entry_titre.get()
    result = bibliotheque.retourner(titre)
    label_result.config(text=result)

def creer_membre():
    global m1
    nom = entry_nom.get()
    prenom = entry_prenom.get()
    souscription = entry_souscription.get()
    m1 = Membre(nom, prenom, souscription)

    entry_nom.delete(0, tk.END)
    entry_prenom.delete(0, tk.END)
    entry_souscription.delete(0, tk.END)

    label_result.config(text=f"Membre {nom} {prenom} a ete cree avec succes.") 


root = tk.Tk()
root.title("Gestion de Bibliotheque")
root.geometry('400x700')

root.config(bg="#f0f0f0")  
root.option_add("*Font", "Arial 12") 
root.option_add("*Button.Background", "#007bff") 
root.option_add("*Button.Foreground", "white")  
root.option_add("*Button.Relief", "flat")  
root.option_add("*Button.BorderWidth", 1)  
root.option_add("*Button.Padding", 5)  

label_ISBN = tk.Label(root, text="ISBN:")
label_ISBN.grid(row=0, column=0, padx=5, pady=5)
label_titre = tk.Label(root, text="Titre:")
label_titre.grid(row=1, column=0, padx=5, pady=5)
label_auteur = tk.Label(root, text="Auteur:")
label_auteur.grid(row=2, column=0, padx=5, pady=5)
label_disponibilite = tk.Label(root, text="Disponibilite:")
label_disponibilite.grid(row=3, column=0, padx=5, pady=5)

entry_ISBN = tk.Entry(root)
entry_ISBN.grid(row=0, column=1, padx=5, pady=5)
entry_titre = tk.Entry(root)
entry_titre.grid(row=1, column=1, padx=5, pady=5)
entry_auteur = tk.Entry(root)
entry_auteur.grid(row=2, column=1, padx=5, pady=5)
entry_disponibilite = tk.Entry(root)
entry_disponibilite.grid(row=3, column=1, padx=5, pady=5)


button_ajouter_livre = tk.Button(root, text="Ajouter Livre", command=ajouter_livre_gui)
button_ajouter_livre.grid(row=4, columnspan=2, padx=5, pady=5)
button_supprimer_livre = tk.Button(root, text="Supprimer Livre", command=supprimer_livre_gui)
button_supprimer_livre.grid(row=5, columnspan=2, padx=5, pady=5)
button_rechercher_livre = tk.Button(root, text="Rechercher Livre", command=rechercher_livre_gui)
button_rechercher_livre.grid(row=6, columnspan=2, padx=5, pady=5)
button_emprunter_livre = tk.Button(root, text="Emprunter Livre", command=emprunter_livre_gui)
button_emprunter_livre.grid(row=7, columnspan=2, padx=5, pady=5)
button_rendre_livre = tk.Button(root, text="Retourner Livre", command=retourner_livre_gui)
button_rendre_livre.grid(row=8, columnspan=2, padx=5, pady=5)
button_afficher_livre = tk.Button(root, text="Afficher livre", command=afficher_livre)
button_afficher_livre.grid(row=9, columnspan=2, padx=5, pady=5)

label_nom = tk.Label(root, text="Nom:")
label_nom.grid(row=10, column=0, padx=5, pady=5)
label_prenom = tk.Label(root, text="Prénom:")
label_prenom.grid(row=11, column=0, padx=5, pady=5)
label_souscription = tk.Label(root, text="Souscription:")
label_souscription.grid(row=12, column=0, padx=5, pady=5)
label_livre = tk.Label(root, text="Livre:")
label_livre.grid(row=13, column=0, padx=5, pady=5)

entry_nom = tk.Entry(root)
entry_nom.grid(row=10, column=1, padx=5, pady=5)
entry_prenom = tk.Entry(root)
entry_prenom.grid(row=11, column=1, padx=5, pady=5)
entry_souscription = tk.Entry(root)
entry_souscription.grid(row=12, column=1, padx=5, pady=5)
entry_livre = tk.Entry(root)
entry_livre.grid(row=13, column=1, padx=5, pady=5)

button_emprunter_membre = tk.Button(root, text="Emprunter", command=emprunter_livre_membre)
button_emprunter_membre.grid(row=14, columnspan=2, padx=5, pady=5)
button_retourne_membre = tk.Button(root, text="Retourner", command=retourner_livre_membre)
button_retourne_membre.grid(row=15, columnspan=2, padx=5, pady=5)
button_afficher_livre = tk.Button(root, text="Afficher livre", command=afficher_livre)
button_afficher_livre.grid(row=16, columnspan=2, padx=5, pady=5)
button_creer_membre = tk.Button(root, text="Creer Membre", command=creer_membre)
button_creer_membre.grid(row=17, columnspan=2, padx=5, pady=5)

label_result = tk.Label(root, text="")
label_result.grid(row=18, columnspan=2, padx=5, pady=5)

root.mainloop()
