import tkinter as tk
from tkinter import messagebox

class FenetrePaiement(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Paiement")
        self.geometry("400x400")
        self.configure(bg="#FFFFFF")

        self.label_nom = tk.Label(self, text="Nom:")
        self.label_nom.pack()
        self.entry_nom = tk.Entry(self)
        self.entry_nom.pack()

        self.label_prenom = tk.Label(self, text="Prénom:")
        self.label_prenom.pack()
        self.entry_prenom = tk.Entry(self)
        self.entry_prenom.pack()

        self.label_telephone = tk.Label(self, text="Téléphone:")
        self.label_telephone.pack()
        self.entry_telephone = tk.Entry(self, validate="key", validatecommand=(self.register(self.valider_telephone), '%P'))
        self.entry_telephone.pack()

        self.label_adresse = tk.Label(self, text="Adresse:")
        self.label_adresse.pack()
        self.entry_adresse = tk.Entry(self)
        self.entry_adresse.pack()

        self.label_code_postal = tk.Label(self, text="Code Postal:")
        self.label_code_postal.pack()
        self.entry_code_postal = tk.Entry(self, validate="key", validatecommand=(self.register(self.valider_code_postal), '%P'))
        self.entry_code_postal.pack()

        self.label_ville = tk.Label(self, text="Ville:")
        self.label_ville.pack()
        self.entry_ville = tk.Entry(self)
        self.entry_ville.pack()

        self.label_numero_carte = tk.Label(self, text="Numéro de Carte:")
        self.label_numero_carte.pack()
        self.entry_numero_carte = tk.Entry(self, validate="key", validatecommand=(self.register(self.valider_numero_carte), '%P'))
        self.entry_numero_carte.pack()

        self.label_date_validite = tk.Label(self, text="Date de Validité (xx/xx):")
        self.label_date_validite.pack()
        self.entry_date_validite = tk.Entry(self, validate="key", validatecommand=(self.register(self.valider_date), '%P'))
        self.entry_date_validite.pack()

        self.label_cvv = tk.Label(self, text="CVV:")
        self.label_cvv.pack()
        self.entry_cvv = tk.Entry(self, validate="key", validatecommand=(self.register(self.valider_cvv), '%P'))
        self.entry_cvv.pack()

        self.btn_valider = tk.Button(self, text="Valider", command=self.valider_achat, state=tk.DISABLED)
        self.btn_valider.pack()

        self.btn_annuler = tk.Button(self, text="Annuler", command=self.annuler_achat)
        self.btn_annuler.pack()

        self.btn_retour = tk.Button(self, text="Retour à la commande", command=self.retour_commande)
        self.btn_retour.pack()

        self.parent = parent

        self.entry_nom.bind("<KeyRelease>", self.verifier_champs_obligatoires)
        self.entry_prenom.bind("<KeyRelease>", self.verifier_champs_obligatoires)
        self.entry_telephone.bind("<KeyRelease>", self.verifier_champs_obligatoires)
        self.entry_adresse.bind("<KeyRelease>", self.verifier_champs_obligatoires)
        self.entry_code_postal.bind("<KeyRelease>", self.verifier_champs_obligatoires)
        self.entry_ville.bind("<KeyRelease>", self.verifier_champs_obligatoires)
        self.entry_numero_carte.bind("<KeyRelease>", self.verifier_champs_obligatoires)
        self.entry_date_validite.bind("<KeyRelease>", self.verifier_champs_obligatoires)
        self.entry_cvv.bind("<KeyRelease>", self.verifier_champs_obligatoires)

    def valider_telephone(self, value):
        return value.isdigit() and len(value) <= 10

    def valider_code_postal(self, value):
        return value.isdigit() and len(value) <= 5

    def valider_numero_carte(self, value):
        return value.isdigit() and len(value) <= 16

    def valider_date(self, value):
        if len(value) <= 5:
            return all(char.isdigit() or char == '/' for char in value)
        return False



    def valider_cvv(self, value):
        return value.isdigit() and len(value) <= 3

    def verifier_champs_obligatoires(self, event=None):
        if (self.entry_nom.get() and self.entry_prenom.get() and self.entry_telephone.get() and
            self.entry_adresse.get() and self.entry_code_postal.get() and self.entry_ville.get() and
            self.entry_numero_carte.get() and self.entry_date_validite.get() and self.entry_cvv.get()):
            self.btn_valider.config(state=tk.NORMAL)
        else:
            self.btn_valider.config(state=tk.DISABLED)

    def valider_achat(self):
        messagebox.showinfo("Achat Confirmé", "Votre achat a été confirmé !")
        self.parent.panier.clear()
        self.parent.liste_panier.delete(0, tk.END)
        self.parent.calculer_sous_total()
        self.destroy()

    def annuler_achat(self):
        self.parent.panier.clear()
        self.parent.liste_panier.delete(0, tk.END)
        self.parent.calculer_sous_total()
        self.destroy()

    def retour_commande(self):
        self.destroy()

        
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Commande de plats")
        self.geometry("800x600")
        self.configure(bg="#FFFFFF")

        self.plats = [
            {"nom": "Pizza Margherita", "description": "Une délicieuse pizza avec une base de tomate, du fromage mozzarella et des feuilles de basilic frais.", "prix": 10},
            {"nom": "Hamburger Classique", "description": "Un hamburger juteux avec un steak de bœuf, de la laitue, des tomates et du fromage cheddar, servi avec des frites.", "prix": 8},
            {"nom": "Salade César", "description": "Une salade croustillante avec du poulet grillé, de la laitue romaine, des croûtons, du parmesan et une vinaigrette César.", "prix": 8},
            {"nom": "Tiramisu", "description": "Un dessert italien classique composé de couches de biscuits imbibés de café, de mascarpone crémeux et saupoudré de cacao.", "prix": 6}
        ]

        self.panier = []

        self.menu_frame = tk.Frame(self, bg="#FFFFFF")
        self.menu_frame.pack(side=tk.LEFT, fill=tk.BOTH, padx=20, pady=20)

        self.plat_frame = tk.Frame(self, bg="#F0F0F0")
        self.plat_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.label_menu = tk.Label(self.menu_frame, text="Menu:", font=("Helvetica", 18, "bold"), bg="#FFFFFF")
        self.label_menu.pack(pady=(0, 10))

        self.plats_buttons = []
        for plat in self.plats:
            button = tk.Button(self.menu_frame, text=f"{plat['nom']} - €{plat['prix']}", font=("Helvetica", 12), bg="#D3D3D3", bd=0, command=lambda p=plat: self.ajouter_au_panier(p))
            button.pack(pady=5, padx=20, fill=tk.X)
            self.plats_buttons.append(button)

        self.label_plat_nom = tk.Label(self.plat_frame, text="", font=("Helvetica", 18, "bold"), bg="#F0F0F0")
        self.label_plat_nom.pack(pady=(0, 10))

        self.label_plat_description = tk.Label(self.plat_frame, text="", font=("Helvetica", 12), bg="#F0F0F0", wraplength=300, justify=tk.LEFT)
        self.label_plat_description.pack(pady=(0, 10))

        self.label_plat_prix = tk.Label(self.plat_frame, text="", font=("Helvetica", 14, "bold"), bg="#F0F0F0")
        self.label_plat_prix.pack()

        self.panier_frame = tk.Frame(self, bg="#FFFFFF")
        self.panier_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, padx=20, pady=20)

        self.label_panier_titre = tk.Label(self.panier_frame, text="Contenu du Panier:", font=("Helvetica", 14, "bold"), bg="#FFFFFF")
        self.label_panier_titre.pack(pady=(10, 5))

        self.liste_panier = tk.Listbox(self.panier_frame, font=("Helvetica", 12), bg="white", width=50, height=10)
        self.liste_panier.pack(pady=(0, 10))

        self.btn_details_plat = tk.Button(self.panier_frame, text="Détails Plat", font=("Helvetica", 12), bg="#D3D3D3", bd=0, command=self.details_plat)
        self.btn_details_plat.pack(pady=5)

        self.btn_supprimer_plat = tk.Button(self.panier_frame, text="Supprimer Plat", font=("Helvetica", 12), bg="#D3D3D3", bd=0, command=self.supprimer_plat)
        self.btn_supprimer_plat.pack(pady=5)

        self.label_sous_total = tk.Label(self.panier_frame, text="Sous-Total:", font=("Helvetica", 14, "bold"), bg="#FFFFFF")
        self.label_sous_total.pack(pady=(10, 5))

        self.label_sous_total_prix = tk.Label(self.panier_frame, text="", font=("Helvetica", 14, "bold"), bg="#FFFFFF")
        self.label_sous_total_prix.pack()

        self.btn_confirmer_achat = tk.Button(self.panier_frame, text="Confirmer Achat", font=("Helvetica", 14, "bold"), bg="#D3D3D3", bd=0, command=self.ouvrir_fenetre_paiement)
        self.btn_confirmer_achat.pack(pady=10)

    def ajouter_au_panier(self, plat):
        self.panier.append(plat)
        self.liste_panier.insert(tk.END, plat["nom"])
        self.calculer_sous_total()

    def details_plat(self):
        selection = self.liste_panier.curselection()
        if selection:
            index = selection[0]
            plat = self.panier[index]
            messagebox.showinfo(f"Détails de {plat['nom']}", f"{plat['description']}\n\nPrix: €{plat['prix']}")
        else:
            messagebox.showerror("Erreur", "Veuillez sélectionner un plat dans le panier.")

    def supprimer_plat(self):
        selection = self.liste_panier.curselection()
        if selection:
            index = selection[0]
            self.liste_panier.delete(index)
            del self.panier[index]
            self.calculer_sous_total()
        else:
            messagebox.showerror("Erreur", "Veuillez sélectionner un plat dans le panier.")

    def calculer_sous_total(self):
        total = sum(plat["prix"] for plat in self.panier)
        self.label_sous_total_prix.config(text=f"€{total}")

    def ouvrir_fenetre_paiement(self):
        fenetre_paiement = FenetrePaiement(self)

if __name__ == "__main__":
    app = Application()
    app.mainloop()
