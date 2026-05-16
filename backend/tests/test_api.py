from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    r = client.get('/api/v1/health')
    assert r.status_code == 200
    assert r.json()['status'] == 'ok'


def test_sectors():
    r = client.get('/api/v1/sectors')
    assert r.status_code == 200
    assert len(r.json()) == 8


def test_report():
    r = client.get('/api/v1/reports/energie-renouvelables')
    assert r.status_code == 200
    assert r.json()['sector_id'] == 'energie-renouvelables'
