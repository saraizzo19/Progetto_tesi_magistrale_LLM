# Adattamento LLM al dominio IT (IT localization fine-tuning)

Questo repository contiene il codice, i dati e l'analisi sperimentale per un progetto di tesi magistrale incentrato sul trasferimento di dominio IT (information technology) in modelli linguistici di dimensioni ridotte (4B - 8B parametri). 

L'obiettivo è valutare l'efficacia del *supervised fine-tuning* (SFT) tramite protocolli LoRA (low-rank adaptation) per la localizzazione di interfacce software dall'inglese all'italiano, confrontando le architetture **Qwen 2.5** e **Google Gemma 3**.

## Struttura del repository

* `/data`: contiene i vettori testuali estratti durante le fasi di inferenza (Baseline Zero-Shot, Post-Tuning, Post-Ottimizzazione).
* `/notebooks`: script e Jupyter Notebooks utilizzati su Google Colab per l'addestramento (Unsloth) e l'estrazione testuale.
* `/results`: file di analisi qualitativa (Framework MQM-DQF) e quantitativa (SacreBLEU, COMET) delle performance dei modelli.
* `/python`: contiene gli script che sono stati utilizzati in locale su VS Code.

## Risultati principali
La ricerca dimostra che l'assorbimento di un dominio tecnico rigido è soggetto a severe *Scaling Laws*. I modelli da 4B parametri hanno manifestato fenomeni di *conversational override* (Gemma) e *underfitting formale* (Qwen), mentre il modello Qwen 8B ha gestito la terminologia IT con maggiore efficacia, sebbene abbia presentato fenomeni di *source language leakage* su termini ultra-specialistici.
