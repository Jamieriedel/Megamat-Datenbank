import sqlite3

# Verbindung zur Datenbank herstellen
conn = sqlite3.connect('megamat.db')

# Cursor-Objekt erstellen
cursor = conn.cursor()

# Benutzer/in wählt aus, welche Aktion durchgeführt werden soll
aktion = input("Was möchten Sie tun? (1=Suche, 2=Auslagern/Einlagern, 3=Neues Werkzeug anlegen): ")

# Suchabfrage
if aktion == "1":
    suche_werkzeug = input("Bitte geben Sie den Werkzeugnamen ein, nach dem gesucht werden soll: ")
    suche_werkzeug = suche_werkzeug.lower()
    cursor.execute("SELECT * FROM werkzeuge WHERE LOWER(werkzeugname) LIKE ?", ('%' + suche_werkzeug + '%',))  # Datenbanknamen in Kleinbuchstaben umwandeln
    ergebnisse = cursor.fetchall()
    if len(ergebnisse) > 0:
        print("Es wurden", len(ergebnisse), "Ergebnisse gefunden:")
        for row in ergebnisse:
            print("ID:", row[0])
            print("Werkzeugname:", row[1])
            print("Position:", row[2])
            print("Mitarbeiter:", row[3])
            print()
    else:
        print("Das Werkzeug wurde nicht gefunden.")

# Aktualisierung der Position
elif aktion == "2":
    werkzeug_name = input("Bitte geben Sie den Namen des Werkzeugs ein, das ausgelagert oder eingelagert werden soll: ")
    werkzeug_name = werkzeug_name.lower()  
    neue_position = input("Bitte geben Sie die neue Position des Werkzeugs ein: ")
    if neue_position.lower() == "megamat":
        position_megamat = input("Bitte geben Sie den Ort ein in dem das Werkzeug eingelagert wird: ")
        cursor.execute("UPDATE werkzeuge SET position = ?, mitarbeiter = ? WHERE LOWER(werkzeugname) = ?", (position_megamat, 0, werkzeug_name))
    else:
        neuer_mitarbeiter = input("Bitte geben Sie den Namen des Mitarbeiters ein, der das Werkzeug jetzt hat: ")
        cursor.execute("UPDATE werkzeuge SET position = ?, mitarbeiter = ? WHERE LOWER(werkzeugname) = ?", (neue_position, neuer_mitarbeiter, werkzeug_name))
    conn.commit()
    if cursor.rowcount == 0:
        print("Das Werkzeug wurde nicht gefunden.")
    else:
        print("Das Ort des Werkzeugs wurde aktualisiert.")

# Neues Werkzeug hinzufügen
elif aktion == "3":
    werkzeugname = input("Bitte geben Sie den Namen des neuen Werkzeugs ein: ")
    position = input("Bitte geben Sie die Position des neuen Werkzeugs ein: ")
    mitarbeiter = input("Bitte geben Sie den Namen des Mitarbeiters ein, der das neue Werkzeug hat: ")
    cursor.execute("INSERT INTO werkzeuge (werkzeugname, position, mitarbeiter) VALUES (?, ?, ?)", (werkzeugname.lower(), position, mitarbeiter))
    conn.commit()
    print("Das neue Werkzeug wurde hinzugefügt.")

# Fehlermeldung bei ungültiger Eingabe
else:
    print("Ungültige Eingabe. Bitte wählen Sie 1, 2 oder 3.")

# Verbindung zur Datenbank schließen
conn.close()
