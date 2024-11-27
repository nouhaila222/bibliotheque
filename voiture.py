class compteur:
    total_voitures = 0
    voitures_route = 0
    voitures_arret = 0
class voiture:
    def __init__(self,marque,modele,vitesse,moteur):
        self.marque=marque
        self.modele=modele
        self.vitesse=vitesse
        self.moteur=moteur
        compteur.total_voitures += 1
        compteur.voitures_arret += 1
    def accelerer(self):
            self.vitesse += 10
            print(self.vitesse)
            if self.vitesse >= 120:
                exit()
            
    def freiner(self):
            self.vitesse -= 10
            print(self.vitesse)
            if self.vitesse == 0:
                exit()
    def Afficher_vitesse(self):
        if self.vitesse > 0:
            etat = 'route'
            compteur.voitures_arret -= 1
            compteur.voitures_route += 1
        elif self.vitesse == 0:
            etat = 'arret'
            compteur.voitures_arret += 1
            compteur.voitures_route -= 1
        print(f"la vitesse actuelle de la voiture est {self.vitesse} et sa etat est en {etat} ")
print("Nombre total de voitures:", compteur.total_voitures)
print("Nombre de voitures en route:", compteur.voitures_route)
print("Nombre de voitures en arret:", compteur.voitures_arret)


v1=voiture('ferari',2018,90,'essence')
v1.accelerer()
v1.freiner()
v1.Afficher_vitesse()
print("Nombre total de voitures:", compteur.total_voitures)
print("Nombre de voitures en route:", compteur.voitures_route)
print("Nombre de voitures en arret:", compteur.voitures_arret)

v2=voiture('mercedice',2020,50,'diesel')
v2.accelerer()
v2.accelerer()
v2.accelerer()
v2.freiner()
v2.freiner()
v2.freiner()
v2.Afficher_vitesse()
print("Nombre total de voitures:", compteur.total_voitures)
print("Nombre de voitures en route:", compteur.voitures_route)
print("Nombre de voitures en arret:", compteur.voitures_arret)


v3=voiture('reuno',2019,20,'disel')
v3.accelerer()
v3.accelerer()
v3.accelerer()
#v3.freiner()
v3.Afficher_vitesse()
print("Nombre total de voitures:", compteur.total_voitures)
print("Nombre de voitures en route:", compteur.voitures_route)
print("Nombre de voitures en arret:", compteur.voitures_arret)