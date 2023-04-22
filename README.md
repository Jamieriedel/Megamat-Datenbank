# Megamat-Datenbank
Python Skript um mithilfe von SQL einen Megamat in einer SQLite Datenbank zu erstellen und anschließen Aktionen damit ausführen wie zum Beispiel das Ein- und Auslagern von Werkzeugen, den aktuellen Ort des Werkzeugs zu ermitteln oder ein neues Werkzeug hinzuzufügen. 

Vor ein paar Tagen ist der Megamat im Unternehmen in dem mein Vater arbeitet kaputt gegangen. Ein Megamat ist ein automatisch funktionierendes Lagersystem, in dem Werkzeuge und andere Materialien aufbewahrt werden. Mein Vater hatte mir erklärt, dass die Mitarbeiter oft stundenlang damit verbringen, nach den Werkzeugen zu suchen, die sie brauchen, weil sie nicht wissen, wo sie sich aktuell befinden.

Ich hatte mich gefragt, ob es nicht eine einfachere Möglichkeit gibt, die Lagerung und den Zugriff auf die Werkzeuge zu organisieren. Ich dachte, dass eine Datenbank hier helfen könnte, um die Positionen der Werkzeuge zu speichern und die Suche zu vereinfachen.

So kam ich auf die Idee, eine sehr einfache Version einer Datenbank für einen Megamat zu erstellen. Ich wollte, dass mein Vater und seine Mitarbeiter damit arbeiten können, ohne dass sie viel Zeit in die Einarbeitung in komplexe Datenbank-Tools investieren müssen.

Also habe ich eine Python-Datei geschrieben die main.py heißt welche die Datenbank für den Megamat erstellen würde. Sobald diese Datei ausgeführt wurde, kann man mit aktion.py simple Veränderungen oder Suchanfragen mit der Datenbank anstellen 
Diese wären zum Beispiel: 
 - neue Werkzeuge hinzuzufügen
 - die Positionen der Werkzeuge aktualisieren
 - nach dem Ort der Werkzeuge suchen
