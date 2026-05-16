from app.models.schemas import Sector, SectorAnalysis


class AnalysisEngine:
    """Moteur IA MVP : synthèse déterministe, remplaçable par RAG + LLM."""

    def analyze(self, sector: Sector) -> SectorAnalysis:
        if sector.trend == "positive":
            summary = f"Le secteur {sector.name} présente une dynamique favorable avec une croissance estimée à {sector.growth_rate}%. Le score d'investissement élevé indique un potentiel prioritaire pour les analyses CDG Capital."
            opportunities = [
                "Accélérer la veille sur les projets d'investissement structurants.",
                "Identifier les champions nationaux et les partenariats internationaux.",
                "Mettre en place un suivi mensuel des indicateurs de croissance.",
            ]
        elif sector.trend == "negative":
            summary = f"Le secteur {sector.name} montre des signaux de fragilité. Le niveau de risque nécessite une surveillance rapprochée et des scénarios de stress sectoriel."
            opportunities = [
                "Repérer les niches résilientes malgré le ralentissement sectoriel.",
                "Prioriser les données de terrain et indicateurs avancés.",
                "Définir des seuils d'alerte plus conservateurs.",
            ]
        else:
            summary = f"Le secteur {sector.name} reste stable avec une croissance modérée. La priorité est de suivre les ruptures réglementaires, financières et concurrentielles."
            opportunities = [
                "Comparer le secteur avec les benchmarks internationaux.",
                "Surveiller les annonces publiques et publications institutionnelles.",
                "Mettre à jour le dossier sectoriel à fréquence hebdomadaire.",
            ]

        risks = []
        if sector.risk_score >= 60:
            risks.append("Risque élevé : volatilité des prix, dépendance climatique ou pression réglementaire.")
        if sector.data_freshness_hours > 24:
            risks.append("Fraîcheur insuffisante des données : actualisation requise.")
        risks.append("Risque de qualité variable des sources si les connecteurs ne sont pas validés métier.")

        actions = [
            "Valider les sources clés avec les analystes métier.",
            "Générer un rapport sectoriel consolidé.",
            "Configurer des alertes sur les indicateurs critiques.",
        ]
        confidence = max(55, min(95, 100 - sector.risk_score // 2))
        return SectorAnalysis(
            sector_id=sector.id,
            executive_summary=summary,
            opportunities=opportunities,
            risks=risks,
            recommended_actions=actions,
            confidence_score=confidence,
        )
