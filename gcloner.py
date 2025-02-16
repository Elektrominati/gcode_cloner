import re

# Datei einlesen
with open("Lampenclip.gcode", "r", encoding="utf-8") as file:
    text = file.read()

# Muster: Text ab erstem Semikolon bis zum ersten "; End of Gcode"
pattern = r";.*?(?=;End of Gcode)"

# Bereich extrahieren
match = re.search(pattern, text, re.DOTALL)

# Ausgabe
if match:
    bereich = match.group()
    print("🟢 Gefundener Textbereich:\n")
    #print(match.group().strip())
    # Text an die Datei anhängen
    with open("Lampenclip.gcode", "a", encoding="utf-8") as file:
        file.write("\n\n" + "electrominati" + "\n" + bereich)

    print("✅ Der Textbereich wurde erfolgreich an die Datei angehängt.")
else:
    print("❌ Kein passender Textbereich gefunden.")