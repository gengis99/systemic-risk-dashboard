# systemic-risk-dashboard
Framework interattivo e replicabile per l’analisi del rischio sistemico nel sistema bancario italiano. 

# 📊 Analisi del Rischio Sistemico nel Sistema Bancario Italiano

Questo progetto sviluppa una **dashboard interattiva** per l'analisi del rischio sistemico nel sistema bancario italiano. Utilizzando **SRISK**, **CoVaR** e **ΔCoVaR**, la dashboard esplora le interconnessioni tra le principali banche italiane, consentendo di visualizzare il rischio sistemico e la propagazione di una crisi in tempo reale.

---

## 🎯 Obiettivi del progetto

- **Analizzare il rischio sistemico** delle banche italiane.
- Simulare il **fallimento** di una banca e osservare gli effetti sul sistema bancario.
- Fornire una visualizzazione interattiva e dinamica attraverso una **dashboard web**.
- **Monitorare il rischio** di ciascuna banca e le connessioni tra le principali banche italiane.

---

## 🧪 Metodologia

L'analisi si basa su:

- **SRISK**: Misura il rischio di fallimento di una banca durante un evento di stress economico.
- **CoVaR**: Misura l'impatto che una banca in crisi ha sul sistema bancario.
- **ΔCoVaR**: Differenza tra CoVaR e VaR di una banca, indicando il contributo sistemico.
- **Rete Interbancaria**: Costruzione di una rete basata sulla **correlazione** tra i ritorni azionari delle banche.
- Simulazioni del fallimento per osservare la propagazione del rischio nel sistema.

---

## 🛠️ Tecnologie utilizzate

- **Python 3.11**
  - Librerie principali: `pandas`, `numpy`, `statsmodels`, `networkx`, `plotly`, `dash`
- **Dash by Plotly**: Framework per la creazione della dashboard interattiva.
- **LaTeX**: Per la redazione del report finale.

---

## 📁 Struttura del repository
- app.py                # Codice principale della dashboard interattiva
- script.ipynb             # Script e analisi Python
- REPORT.PDF            # Report dettagliato scritto in LateX ed esportato in PDF

---

## 📊 Risultati principali

- **Ranking di sistemicità** delle banche italiane
- **Matrice ΔCoVaR** e **heatmap**
- **Rete interbancaria** basata su correlazioni tra le banche
- **Simulazioni di fallimento** delle banche
- **Grafici** interattivi per SRISK, CoVaR, e ΔCoVaR

---

## 🚀 Come eseguire la dashboard
---

**Note importanti:**
- Il comando `python app.py` deve essere eseguito nel terminale per avviare il server della dashboard.  
- La dashboard è accessibile localmente su **http://127.0.0.1:8050**.
- Assicurati di avere installato **tutte le dipendenze** e che il tuo ambiente virtuale sia attivo.

### 1. Creare un ambiente virtuale:
Assicurati di avere Python 3.11 o superiore installato. Esegui i seguenti comandi per creare un ambiente virtuale:

```bash
- python -m venv venv
- source venv/bin/activate   # Su Windows: venv\Scripts\activate
- Installa tutte le librerie necessarie eseguendo il comando: pip install -r
- Per eseguire la dashboard, usa il comando: python app.py
- La dashboard sarà disponibile al seguente indirizzo: http://127.0.0.1:8050
'''
