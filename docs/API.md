# API MVP

Base URL : `http://localhost:8000/api/v1`

| Méthode | Endpoint | Rôle |
|---|---|---|
| GET | `/health` | Santé API |
| GET | `/dashboard` | KPIs consolidés |
| GET | `/sectors` | Liste des secteurs |
| GET | `/sectors/{id}` | Détail secteur |
| GET | `/sectors/{id}/analysis` | Synthèse automatique |
| GET | `/sectors/{id}/benchmark` | Benchmark |
| GET | `/sectors/{id}/documents` | Dossier documentaire |
| GET | `/alerts` | Alertes actives |
| GET | `/reports/{id}` | Rapport consolidé |
