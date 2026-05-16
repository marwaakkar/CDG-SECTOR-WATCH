from fastapi import APIRouter, HTTPException
from app.models.schemas import Sector, SectorAnalysis, BenchmarkItem, Alert, Document, Report
from app.services.repository import SectorRepository
from app.services.analysis_engine import AnalysisEngine
from app.services.alert_engine import AlertEngine
from app.services.report_service import ReportService

router = APIRouter()
repo = SectorRepository()
analysis_engine = AnalysisEngine()
alert_engine = AlertEngine()
report_service = ReportService()


@router.get('/health')
def health():
    return {"status": "ok", "service": "cdg-sector-watch"}


@router.get('/dashboard')
def dashboard():
    sectors = repo.list_sectors()
    alerts = [a for s in sectors for a in alert_engine.evaluate(s)]
    return {
        "sector_count": len(sectors),
        "avg_investment_score": round(sum(s.investment_score for s in sectors) / len(sectors), 1),
        "avg_risk_score": round(sum(s.risk_score for s in sectors) / len(sectors), 1),
        "freshness_target_hours": 24,
        "active_alerts": len(alerts),
        "positive_trends": len([s for s in sectors if s.trend == 'positive']),
    }


@router.get('/sectors', response_model=list[Sector])
def list_sectors():
    return repo.list_sectors()


@router.get('/sectors/{sector_id}', response_model=Sector)
def get_sector(sector_id: str):
    sector = repo.get_sector(sector_id)
    if not sector:
        raise HTTPException(status_code=404, detail="Sector not found")
    return sector


@router.get('/sectors/{sector_id}/analysis', response_model=SectorAnalysis)
def analyze_sector(sector_id: str):
    sector = repo.get_sector(sector_id)
    if not sector:
        raise HTTPException(status_code=404, detail="Sector not found")
    return analysis_engine.analyze(sector)


@router.get('/sectors/{sector_id}/benchmark', response_model=list[BenchmarkItem])
def benchmark_sector(sector_id: str):
    if not repo.get_sector(sector_id):
        raise HTTPException(status_code=404, detail="Sector not found")
    return repo.benchmark(sector_id)


@router.get('/sectors/{sector_id}/documents', response_model=list[Document])
def documents(sector_id: str):
    if not repo.get_sector(sector_id):
        raise HTTPException(status_code=404, detail="Sector not found")
    return repo.documents(sector_id)


@router.get('/alerts', response_model=list[Alert])
def alerts():
    return [alert for sector in repo.list_sectors() for alert in alert_engine.evaluate(sector)]


@router.get('/reports/{sector_id}', response_model=Report)
def generate_report(sector_id: str):
    report = report_service.generate(sector_id)
    if not report:
        raise HTTPException(status_code=404, detail="Sector not found")
    return report
