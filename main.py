import sqlite3

# Verbindung zur Datenbank herstellen
conn = sqlite3.connect('megamat.db')

# Cursor-Objekt erstellen
cursor = conn.cursor()

# Tabelle erstellen
cursor.execute('''CREATE TABLE werkzeuge
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   werkzeugname TEXT,
                   position TEXT,
                   mitarbeiter TEXT)''')

# Verbindung zur Datenbank schließen
conn.close()

