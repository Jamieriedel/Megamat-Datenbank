# Megamat-Datenbank
---

Entwicklung eines Python-Skripts zur Erstellung eines Megamats in einer SQLite-Datenbank und zur Durchführung verschiedener Aktionen wie Ein- und Auslagern von Werkzeugen, Lokalisierung des aktuellen Standorts von Werkzeugen und Hinzufügen neuer Werkzeuge.

Hintergrundgeschichte:
Kürzlich ist im Unternehmen meines Vaters der Megamat ausgefallen. Ein Megamat ist ein automatisiertes Lagersystem, das Werkzeuge und andere Materialien verwaltet. Mein Vater erklärte mir, dass die Mitarbeiter oft viel Zeit damit verbringen, Werkzeuge zu suchen, da sie nicht wissen, wo sie sich befinden.

Das brachte mich dazu, über eine effizientere Möglichkeit zur Organisation der Werkzeuglagerung und -zugriffe nachzudenken. Ich kam zu dem Schluss, dass eine Datenbank dazu beitragen könnte, die Positionen der Werkzeuge zu verfolgen und die Suchzeit zu minimieren.
So kam ich auf die Idee, eine sehr einfache Version einer Datenbank für einen Megamat zu erstellen. Ich wollte, dass mein Vater und seine Mitarbeiter damit arbeiten können, ohne dass sie viel Zeit in die Einarbeitung in komplexe Datenbank-Tools investieren müssen.

Also habe ich eine Python-Datei geschrieben die main.py heißt welche die Datenbank für den Megamat erstellen würde. Sobald diese Datei ausgeführt wurde, kann man mit aktion.py simple Veränderungen oder Suchanfragen mit der Datenbank anstellen 
Diese wären zum Beispiel: 
 - neue Werkzeuge hinzuzufügen
 - die Positionen der Werkzeuge aktualisieren
 - nach dem Ort der Werkzeuge suchen
