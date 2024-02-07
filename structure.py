def transform_data(data):
    # Ermittle die Länge der Arrays und verwende die minimale Länge, um Indexfehler zu vermeiden
    min_length = min(len(v) for v in data.values() if isinstance(v, list))

    # Erstelle `measuring_points` basierend auf der minimalen Länge
    measuring_points = []
    for i in range(min_length):
        point = {key: data[key][i] if i < len(data[key]) else None for key in data if isinstance(data[key], list)}
        measuring_points.append(point)

    return measuring_points


def update_documents():
    for doc in collection.find():
        if 'data' in doc:
            # Transformiere die Daten
            new_measuring_points = transform_data(doc['data'])
            # Aktualisiere das Dokument mit den transformierten Daten unter dem neuen Schlüssel `measuring_points`
            collection.update_one({'_id': doc['_id']}, {'$set': {'measuring_points': new_measuring_points}})
            print(f'Dokument {doc["_id"]} wurde aktualisiert.')


update_documents()
print('Alle Dokumente wurden aktualisiert.')