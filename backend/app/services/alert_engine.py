from datetime import datetime, timezone
from app.models.schemas import Alert, Sector


class AlertEngine:
    def evaluate(self, sector: Sector) -> list[Alert]:
        alerts: list[Alert] = []
        now = datetime.now(timezone.utc).isoformat()
        if sector.risk_score >= 60:
            alerts.append(Alert(
                id=f"alert-risk-{sector.id}", sector_id=sector.id,
                title="Risque sectoriel élevé",
                message=f"Le score de risque du secteur {sector.name} atteint {sector.risk_score}/100.",
                level="high", source="Risk scoring engine", created_at=now,
            ))
        if sector.data_freshness_hours > 24:
            alerts.append(Alert(
                id=f"alert-freshness-{sector.id}", sector_id=sector.id,
                title="Données non fraîches",
                message="Le délai de mise à jour dépasse le seuil cible de 24h.",
                level="medium", source="Data quality monitor", created_at=now,
            ))
        if sector.trend == "negative":
            alerts.append(Alert(
                id=f"alert-trend-{sector.id}", sector_id=sector.id,
                title="Tendance négative détectée",
                message="Une tendance négative nécessite une revue analyste et un suivi renforcé.",
                level="medium", source="Trend detection", created_at=now,
            ))
        return alerts
