from pydantic import BaseModel, Field
from typing import Literal


RiskLevel = Literal["low", "medium", "high", "critical"]
Trend = Literal["positive", "stable", "negative"]


class Sector(BaseModel):
    id: str
    name: str
    description: str
    priority: int
    trend: Trend
    growth_rate: float
    investment_score: int = Field(ge=0, le=100)
    risk_score: int = Field(ge=0, le=100)
    data_freshness_hours: int


class SectorAnalysis(BaseModel):
    sector_id: str
    executive_summary: str
    opportunities: list[str]
    risks: list[str]
    recommended_actions: list[str]
    confidence_score: int = Field(ge=0, le=100)


class BenchmarkItem(BaseModel):
    label: str
    morocco: float
    international_avg: float
    best_in_class: float
    unit: str


class Alert(BaseModel):
    id: str
    sector_id: str
    title: str
    message: str
    level: RiskLevel
    source: str
    created_at: str
    is_read: bool = False


class Document(BaseModel):
    id: str
    sector_id: str
    title: str
    source: str
    year: int
    tags: list[str]
    summary: str


class Report(BaseModel):
    id: str
    sector_id: str
    title: str
    generated_at: str
    analysis: SectorAnalysis
    benchmark: list[BenchmarkItem]
    alerts: list[Alert]
