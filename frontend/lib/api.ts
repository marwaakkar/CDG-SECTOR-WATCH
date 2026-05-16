const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api/v1'

export type Sector = {
  id: string; name: string; description: string; priority: number; trend: 'positive'|'stable'|'negative';
  growth_rate: number; investment_score: number; risk_score: number; data_freshness_hours: number;
}
export type Dashboard = { sector_count:number; avg_investment_score:number; avg_risk_score:number; active_alerts:number; positive_trends:number; freshness_target_hours:number }
export type Alert = { id:string; sector_id:string; title:string; message:string; level:string; source:string; created_at:string }
export type Analysis = { sector_id:string; executive_summary:string; opportunities:string[]; risks:string[]; recommended_actions:string[]; confidence_score:number }
export type Benchmark = { label:string; morocco:number; international_avg:number; best_in_class:number; unit:string }

async function get<T>(path: string): Promise<T> {
  const res = await fetch(`${API_URL}${path}`, { cache: 'no-store' })
  if (!res.ok) throw new Error(`API error ${res.status}`)
  return res.json()
}

export const api = {
  dashboard: () => get<Dashboard>('/dashboard'),
  sectors: () => get<Sector[]>('/sectors'),
  alerts: () => get<Alert[]>('/alerts'),
  analysis: (id: string) => get<Analysis>(`/sectors/${id}/analysis`),
  benchmark: (id: string) => get<Benchmark[]>(`/sectors/${id}/benchmark`),
}
