# Valutazione Quantitativa dei Modelli

Di seguito sono riportate le metriche automatizzate (COMET, SacreBLEU, chrF) registrate per i modelli analizzati. Viene confrontata l'inferenza Zero-Shot (Baseline) con quella successiva al Supervised Fine-Tuning tramite protocollo LoRA.

| Modello | Metrica | Baseline (Zero-Shot) | Post-Tuning (LoRA) | Delta (Δ) |
| :--- | :--- | :--- | :--- | :--- |
| **Qwen 4B** | COMET | 0.6001 | 0.5861 | -0.0140 |
| **Qwen 4B** | BLEU | 12.18 | 11.94 | -0.24 |
| **Qwen 4B** | chrF | 29.26 | 28.06 | -1.21 |
| **Gemma 3 4B** | COMET | 0.5964 | 0.3999 | -0.1965 |
| **Gemma 3 4B** | BLEU | 11.08 | 0.15 | -10.92 |
| **Gemma 3 4B** | chrF | 28.51 | 9.52 | -19.00 |
| **Gemma 3n E4B** | COMET | 0.6029 | 0.3752 | -0.2277 |
| **Gemma 3n E4B** | BLEU | 12.68 | 0.29 | -12.39 |
| **Gemma 3n E4B** | chrF | 29.12 | 9.15 | -19.96 |
| **Qwen 3 8B** | COMET | 0.5954 | 0.3818 | -0.2136 |
| **Qwen 3 8B** | BLEU | 12.41 | 0.17 | -12.24 |
| **Qwen 3 8B** | chrF | 29.26 | 10.24 | -19.01 |
