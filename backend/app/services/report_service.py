from datetime import datetime, timezone
from app.models.schemas import Report
from app.services.analysis_engine import AnalysisEngine
from app.services.alert_engine import AlertEngine
from app.services.repository import SectorRepository


class ReportService:
    def __init__(self):
        self.repo = SectorRepository()
        self.analysis = AnalysisEngine()
        self.alerts = AlertEngine()

    def generate(self, sector_id: str) -> Report | None:
        sector = self.repo.get_sector(sector_id)
        if not sector:
            return None
        return Report(
            id=f"report-{sector.id}",
            sector_id=sector.id,
            title=f"Rapport sectoriel — {sector.name}",
            generated_at=datetime.now(timezone.utc).isoformat(),
            analysis=self.analysis.analyze(sector),
            benchmark=self.repo.benchmark(sector.id),
            alerts=self.alerts.evaluate(sector),
        )
