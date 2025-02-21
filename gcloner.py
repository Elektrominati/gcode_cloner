import re



from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json  # JSON-Daten aus JavaScript
    print("Empfangene Daten:", data)
    clone_code()
    return jsonify({"message": "Daten erhalten", "received": data})

if __name__ == '__main__':
    app.run(port=5000)
    receive_data()
    
def clone_code():
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


