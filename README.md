# Adattamento LLM al Dominio IT (IT Localization Fine-Tuning)

Questo repository contiene il codice, i dati e l'analisi sperimentale per un progetto di tesi magistrale incentrato sul trasferimento di dominio IT (Information Technology) in modelli linguistici di dimensioni ridotte (4B - 8B parametri). 

L'obiettivo è valutare l'efficacia del *Supervised Fine-Tuning* (SFT) tramite protocolli LoRA (Low-Rank Adaptation) per la localizzazione di interfacce software dall'inglese all'italiano, confrontando le architetture **Qwen 2.5** e **Google Gemma 3**.

## Struttura del Repository

* `/data`: Contiene i vettori testuali estratti durante le fasi di inferenza (Baseline Zero-Shot, Post-Tuning, Post-Ottimizzazione).
* `/notebooks`: Script e Jupyter Notebooks utilizzati su Google Colab per l'addestramento (Unsloth) e l'estrazione testuale.
* `/results`: File di analisi qualitativa (Framework MQM-DQF) e quantitativa (SacreBLEU, COMET) delle performance dei modelli.

## Risultati Principali
La ricerca dimostra che l'assorbimento di un dominio tecnico rigido è soggetto a severe *Scaling Laws*. I modelli da 4B parametri hanno manifestato fenomeni di *Conversational Override* (Gemma) e *Underfitting Formale* (Qwen), mentre il modello Qwen 8B ha gestito la terminologia IT con maggiore efficacia, sebbene abbia presentato fenomeni di *Source Language Leakage* su termini ultra-specialistici.
