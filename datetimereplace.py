# Funktion zum Konvertieren von Timestamps zu datetime
def convert_to_datetime(timestamp):
    try:
        # Versuche, den Timestamp mit dateutil.parser zu parsen
        return parser.parse(timestamp)
    except (ValueError, TypeError):
        # Bei einem Fehler, gib den ursprünglichen Wert zurück oder handle den Fehler
        return timestamp


# Funktion zum Durchlaufen aller Dokumente und Aktualisieren der Timestamps
def update_timestamps():
    # Durchlaufe jedes Dokument in der Kollektion
    for doc in collection.find():
        # Annahme: Die Timestamps befinden sich im Feld 'data.timestamps', das eine Liste von Timestamps ist
        if 'data' in doc and 'timestamps' in doc['data']:
            # Initialisiere eine Liste für die aktualisierten Timestamps
            updated_timestamps = []
            # Durchlaufe die Liste der Timestamps und konvertiere jeden Timestamp
            for timestamp in doc['data']['timestamps']:
                updated_timestamp = convert_to_datetime(timestamp)
                if isinstance(updated_timestamp, datetime.datetime):
                    updated_timestamps.append(updated_timestamp)
                else:
                    # Füge den ursprünglichen Wert hinzu, wenn die Konvertierung fehlschlägt
                    updated_timestamps.append(timestamp)
            # Aktualisiere das Dokument mit den neuen Timestamps
            collection.update_one({'_id': doc['_id']}, {'$set': {'data.timestamps': updated_timestamps}})
            print(f'Dokument {doc["_id"]} aktualisiert.')


update_timestamps()
print('Alle Timestamps wurden aktualisiert.')