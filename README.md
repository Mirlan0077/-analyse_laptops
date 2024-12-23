Installation und Einrichtung

1.pip install -r requirements.txt
2.python manage.py makemigrations
python manage.py migrate
3.python manage.py runserver


Hauptfunktionen:

Datenmodell
Die Klasse Laptop speichert Laptop-Eigenschaften wie Prozessor, Arbeitsspeicher, Gewicht, Betriebssystem und andere Parameter.
Berechnung eines Laptop-Scores basierend auf Preis, Gewicht, Speicher und Akkulaufzeit.
CSV-Verarbeitung
Das Skript csv_processor.py dient zum Laden und Verarbeiten von Daten aus einer CSV-Datei.
Automatische Vervollständigung fehlender Werte und Umwandlung von Datentypen.
Speicherung der Daten in der Datenbank mit Transaktionen.
APIs
analyze_laptops: Gibt die Top-10 der besten und schlechtesten Laptops basierend auf dem Score zurück.
upload_csv_and_analyze: Lädt Daten aus einer CSV-Datei hoch, analysiert sie und gibt die Ergebnisse zurück.


Nutzung

APIs
1. Laptop-Analyse

URL: /analyze_laptops/
Methode: GET
Beschreibung: Gibt ein JSON mit den Top-10 der besten und schlechtesten Laptops basierend auf dem Score zurück.
2. CSV hochladen und analysieren

URL: /upload_csv_and_analyze/
Methode: POST
Beschreibung: Lädt Daten aus einer CSV-Datei hoch, analysiert sie und gibt ein JSON mit den Ergebnissen zurück.
