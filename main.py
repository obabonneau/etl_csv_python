import csv

# Extraction du fichier de données csv dans une liste de dictionnaires
def extract():
    data = []
    with open('input.csv', mode='r') as file:
        csv_reader = csv.DictReader(file) # delimiter non renseigné mais par défaut ","
        for line in csv_reader:
            data.append(line)
    return data

# Transformation de la liste de dictionnaires dans une nouvelle liste de nouveaux dictionnaires
def transform(data_to_transform):
    data_to_load = []
    for data in data_to_transform:
        transformed_data = {}
        transformed_data["nom"] = data["nom"] # Copie simple d'un dictionnaire à l'autre
        data["heures_travaillees"] = int(data["heures_travaillees"]) * 15 # Opération sur les heures travaillées dans le 1er dictionnaire (Transformation en entier)
        transformed_data["salaire"] = str(data["heures_travaillees"]) # Copie du résultat d'un dictionnaire à l'autre (Transformation en chaine de caractères) 
        data_to_load.append(transformed_data)
    return data_to_load

# Chargement de la nouvelle liste de dictionnaires dans un nouveau fichier de données csv
def load(data_to_load):
    with open('output.csv', mode='w', newline="") as file: # newline="" pour retirer le saut de ligne
        entete = ['nom', 'salaire'] # Initialisation des valeurs de l'entete
        writer = csv.DictWriter(file, fieldnames=entete) # delimiter non renseigné mais par défaut "," 
        writer.writeheader() # Ecriture de l'entete
        for data in data_to_load:
            writer.writerow(data) # Ecriture des lignes

# Fonction principale
def main():
    data_to_transform = extract()
    data_to_load = transform(data_to_transform)
    load(data_to_load)

# Execution de la fonction main si exécuté
if __name__ == "__main__":
    main()