import os
import h5py
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

uri = os.environ['DB_URI']

# MongoDB Datenbank-Verbindung
client = MongoClient(uri)
db = client['rosen']
collection = db['big_data']

# Verzeichnis, in dem sich die .h5 Dateien befinden
directory = './data'


# Rekursive Funktion zum Durchlaufen der .h5 Datei
def traverse_group(group, path=''):
    data = {}
    for key, item in group.items():
        new_key = key.lower()  # Schlüssel in Kleinbuchstaben umwandeln
        if isinstance(item, h5py.Dataset):  # Prüfen, ob es sich um einen Datensatz handelt
            data[new_key] = item[()].tolist()  # Konvertieren in eine Liste für MongoDB
        elif isinstance(item, h5py.Group):  # Prüfen, ob es sich um eine Gruppe handelt
            data[new_key] = traverse_group(item, path + '/' + new_key)  # Rekursiver Aufruf
    return data


# Funktion zum Verarbeiten einer .h5 Datei
def process_h5_file(file_path):
    with h5py.File(file_path, 'r') as h5file:
        data = traverse_group(h5file)  # Start der Rekursion von der Wurzelgruppe
        collection.insert_one(data)  # Daten in MongoDB einfügen
        print(f'Daten aus {file_path} wurden erfolgreich in MongoDB gespeichert.')


# Durchlaufe alle .h5 Dateien im angegebenen Verzeichnis
for filename in os.listdir(directory):
    if filename.endswith('.h5'):
        process_h5_file(os.path.join(directory, filename))

print('Verarbeitung abgeschlossen.')
