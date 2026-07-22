from openai import OpenAI
import re

# 1. Connessione all'architettura locale
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

# 2. Configurazione I/O
file_input = 'test_en.txt'
file_output = 'post_tuning_qwen_4b_optm.txt'

# Il prompt DEVE rimanere identico allo Step 1
system_prompt = "You are a professional translator. Translate the following English text into Italian. Provide only the translation, without any notes, explanations, or introductory text."

print(f"Avvio estrazione Post-Tuning. Salvataggio in: {file_output}")
traduzioni = []

with open(file_input, 'r', encoding='utf-8') as f:
    frasi_en = f.readlines()

# 3. Ciclo di inferenza
for i, frase in enumerate(frasi_en):
    frase = frase.strip()
    if not frase:
        continue
        
    print(f"Elaborazione segmento {i+1}/{len(frasi_en)}...")
    
    try:
        response = client.chat.completions.create(
            model="local-model",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": frase}
            ],
            temperature=0.1, 
            max_tokens=100
        )
        
        risposta_grezza = response.choices[0].message.content.strip()
        traduzione_pulita = re.sub(r'<think>.*?</think>', '', risposta_grezza, flags=re.DOTALL).strip()
        traduzioni.append(traduzione_pulita)
        
    except Exception as e:
        print(f"Errore computazionale: {e}")
        traduzioni.append("ERRORE")
        
# 4. Esportazione
with open(file_output, 'w', encoding='utf-8') as f:
    for t in traduzioni:
        f.write(f"{t}\n")

print("\nEstrazione completata con successo.")