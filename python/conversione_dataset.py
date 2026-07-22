import csv
import json
import os

# 1. Configurazione I/O
file_csv = 'train_bilingue.csv'
file_jsonl = 'train_bilingue.jsonl'

# 2. Iniezione del System Prompt (Vincolo strutturale per l'addestramento SFT)
system_prompt = "You are a professional translator. Translate the following English text into Italian. Provide only the translation, without any notes, explanations, or introductory text."

# 3. Mappatura esatta delle intestazioni del dataset
colonna_inglese = 'Inglese'
colonna_italiano = 'Italiano'
# La colonna 'Affidabilità' viene riconosciuta dall'ambiente ma esclusa dall'esportazione JSONL

print(f"Avvio estrazione dei vettori semantici da '{file_csv}'...")
dati_strutturati = []

try:
    # Apertura del file sorgente
    with open(file_csv, mode='r', encoding='utf-8-sig') as f_in:
        # L'utilizzo dello sniffer permette di rilevare automaticamente se il CSV 
        # utilizza la virgola o il punto e virgola come separatore di colonna.
        campione = f_in.read(1024)
        f_in.seek(0)
        separatore = csv.Sniffer().sniff(campione).delimiter
        
        lettore = csv.DictReader(f_in, delimiter=separatore)
        
        for numero_riga, riga in enumerate(lettore, start=1):
            # Estrazione e sanificazione dei dati
            frase_en = riga.get(colonna_inglese, "").strip()
            frase_it = riga.get(colonna_italiano, "").strip()

            # Salto iterativo per righe vuote o corrotte
            if not frase_en or not frase_it:
                continue

            # Assemblaggio del tensore formattato in ChatML
            conversazione = {
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": frase_en},
                    {"role": "assistant", "content": frase_it}
                ]
            }
            dati_strutturati.append(conversazione)

    # Scrittura formattata del file JSON Lines
    with open(file_jsonl, mode='w', encoding='utf-8') as f_out:
        for record in dati_strutturati:
            # Il parametro ensure_ascii=False conserva l'integrità della punteggiatura italiana
            f_out.write(json.dumps(record, ensure_ascii=False) + '\n')

    print("Procedura di ingegnerizzazione completata.")
    print(f"Esportato il file '{file_jsonl}' contenente {len(dati_strutturati)} segmenti di addestramento validi.")

except KeyError as e:
    print(f"ERRORE CRITICO: Parametro {e} non indicizzato nell'intestazione del file CSV.")
except FileNotFoundError:
    print(f"ERRORE CRITICO: Impossibile localizzare il file '{file_csv}' nella directory corrente ({os.getcwd()}).")
except Exception as e:
    print(f"Eccezione computazionale non gestita: {e}")