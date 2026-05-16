from app.data.seeds import SECTORS, DOCUMENTS, BENCHMARKS
from app.models.schemas import Sector, Document, BenchmarkItem


class SectorRepository:
    def list_sectors(self) -> list[Sector]:
        return [Sector(**sector) for sector in SECTORS]

    def get_sector(self, sector_id: str) -> Sector | None:
        for sector in SECTORS:
            if sector["id"] == sector_id:
                return Sector(**sector)
        return None

    def documents(self, sector_id: str | None = None) -> list[Document]:
        docs = DOCUMENTS if sector_id is None else [doc for doc in DOCUMENTS if doc["sector_id"] == sector_id]
        return [Document(**doc) for doc in docs]

    def benchmark(self, sector_id: str) -> list[BenchmarkItem]:
        rows = BENCHMARKS.get(sector_id, BENCHMARKS["default"])
        return [BenchmarkItem(**row) for row in rows]
