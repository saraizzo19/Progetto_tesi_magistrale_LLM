# Valutazione Quantitativa dei Modelli

Di seguito sono riportate le metriche automatizzate (COMET, SacreBLEU, chrF) registrate per i modelli analizzati. Viene confrontata l'inferenza Zero-Shot (Baseline) con l'output successivo al Supervised Fine-Tuning standard (LoRA) e con la fase di Post-Ottimizzazione (variazione degli iperparametri).

| Modello | Metrica | Baseline (Zero-Shot) | Post-Tuning (Standard) | Post-Ottimizzazione |
| :--- | :--- | :--- | :--- | :--- |
| **Qwen 4B** | COMET | 0.6001 | 0.5861 | 0.4196 |
| **Qwen 4B** | BLEU | 12.18 | 11.94 | 0.18 |
| **Qwen 4B** | chrF | 29.26 | 28.06 | 12.24 |
| **Qwen 8B** | COMET | 0.5954 | 0.3818 | 0.5879 |
| **Qwen 8B** | BLEU | 12.41 | 0.17 | 11.84 |
| **Qwen 8B** | chrF | 29.26 | 10.24 | 28.67 |
| **Gemma 3 4B** | COMET | 0.5964 | 0.3999 | 0.4485 |
| **Gemma 3 4B** | BLEU | 11.08 | 0.15 | 0.16 |
| **Gemma 3 4B** | chrF | 28.51 | 9.52 | 12.24 |
| **Gemma E4B** | COMET | 0.6029 | 0.3752 | N/A |
| **Gemma E4B** | BLEU | 12.68 | 0.29 | N/A |
| **Gemma E4B** | chrF | 29.12 | 9.15 | N/A |
