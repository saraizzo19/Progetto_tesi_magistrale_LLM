from openai import OpenAI
import time
import re

# 1. Configurazione del client API locale (LM Studio)
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

# 2. Configurazione dei file di I/O
file_input = 'test_en.txt'
file_output = 'baseline_gemma3_12b.txt'

# 3. Prompt di sistema (System Prompt)
system_prompt = "You are a professional translator. Translate the following English text into Italian. Provide only the translation, without any notes, explanations, or introductory text."

print(f"Avvio dell'inferenza standard su Gemma 3 12B. Il risultato sarà salvato in: {file_output}")

traduzioni = []

# Lettura del dataset sorgente
with open(file_input, 'r', encoding='utf-8') as f:
    frasi_en = f.readlines()

# Esecuzione dell'inferenza iterativa
for i, frase in enumerate(frasi_en):
    frase = frase.strip()
    if not frase:
        continue
        
    print(f"Elaborazione segmento {i+1}/{len(frasi_en)}...")
    
    try:
        # 4. Chiamata API Chat standard
        response = client.chat.completions.create(
            model="local-model",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": frase}
            ],
            temperature=0.1, 
            max_tokens=100
        )
        
        # Estrazione e pulizia dell'output
        risposta_grezza = response.choices[0].message.content.strip()
        traduzione_pulita = re.sub(r'<think>.*?</think>', '', risposta_grezza, flags=re.DOTALL).strip()
        traduzioni.append(traduzione_pulita)
        
    except Exception as e:
        print(f"Errore computazionale nel segmento {i+1}: {e}")
        traduzioni.append("ERRORE_DI_TRADUZIONE")
        
# Scrittura dei risultati su disco
with open(file_output, 'w', encoding='utf-8') as f:
    for t in traduzioni:
        f.write(f"{t}\n")

print("\nOperazione completata con successo. File esportato.")