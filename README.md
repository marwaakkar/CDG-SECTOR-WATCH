# CDG Sector Watch — Plateforme d’Analyse Sectorielle & Veille Stratégique

MVP complet inspiré du cahier de conception CDG Capital : centralisation de données sectorielles, analyse automatique, benchmarking, dossiers intelligents, alertes et reporting.

## Stack

- **Backend** : Python 3.11, FastAPI, Pydantic, Uvicorn
- **Frontend** : Next.js 14, TypeScript, Tailwind CSS, Recharts
- **Data/IA MVP** : données mockées, scoring sectoriel, synthèse heuristique, détection d’alertes
- **Infra** : Docker Compose, PostgreSQL, Redis prêts pour extension

## Fonctionnalités MVP

- Dashboard sectoriel avec KPIs globaux
- Liste des 8 secteurs prioritaires
- Analyse sectorielle automatique
- Benchmark national/international
- Dossiers sectoriels intelligents avec historique documentaire
- Alertes et signaux faibles
- Génération de rapport JSON côté API
- UI moderne en dark/light style institutionnel

## Démarrage rapide sans Docker

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

API docs : http://localhost:8000/docs

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Interface : http://localhost:3000

## Démarrage avec Docker

```bash
docker compose up --build
```

- Frontend : http://localhost:3000
- Backend : http://localhost:8000
- Docs API : http://localhost:8000/docs

## Structure

```text
cdg-sector-watch/
├── backend/
│   ├── app/
│   │   ├── api/              # Routes FastAPI
│   │   ├── core/             # Configuration
│   │   ├── data/             # Données seed MVP
│   │   ├── models/           # Schémas Pydantic
│   │   ├── services/         # Logique métier / IA MVP
│   │   └── main.py
│   ├── tests/
│   └── requirements.txt
├── frontend/
│   ├── app/
│   ├── components/
│   ├── lib/
│   └── package.json
├── docs/
│   ├── ARCHITECTURE.md
│   ├── API.md
│   └── ROADMAP.md
├── docker-compose.yml
└── .env.example
```

## Notes importantes

Ce projet est un MVP pédagogique/prototype : il utilise des données simulées pour démontrer le produit. Les connecteurs réels HCP, Bank Al-Maghrib, AMMC, World Bank, IMF, Bloomberg/Refinitiv doivent être activés progressivement selon les accès disponibles.
