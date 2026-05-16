# Architecture — CDG Sector Watch

## Modules

1. **Collecte & ingestion** : connecteurs API, scraping, RSS, fichiers.
2. **Analyse sectorielle** : scoring, classification, synthèse automatique.
3. **Benchmarking** : comparaison Maroc vs international.
4. **Dossiers intelligents** : documents sectoriels, historique, versioning.
5. **Alertes & signaux faibles** : règles métier, seuils, notifications.
6. **Interface & reporting** : dashboard, exports, rapports périodiques.

## Choix MVP

Le MVP garde une architecture propre mais remplace les composants coûteux par des services simulés :

- Données dans `backend/app/data/seeds.py`
- Analyse IA déterministe dans `AnalysisEngine`
- Alertes via règles dans `AlertEngine`
- Rapports JSON générés par `ReportService`

## Extensions prévues

- PostgreSQL + TimescaleDB pour stockage réel
- Elasticsearch / OpenSearch pour recherche documentaire
- Airflow pour orchestration ETL
- RAG avec LlamaIndex ou LangChain
- Exports PDF/Word
- Authentification RBAC
