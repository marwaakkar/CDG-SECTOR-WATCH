'use client'

import { useEffect, useMemo, useState } from 'react'
import { Activity, AlertTriangle, BarChart3, Database, FileText, TrendingUp } from 'lucide-react'
import { api, type Alert, type Analysis, type Benchmark, type Dashboard, type Sector } from '@/lib/api'
import { KpiCard } from '@/components/KpiCard'
import { SectorTable } from '@/components/SectorTable'
import { BenchmarkChart } from '@/components/BenchmarkChart'

export default function Page() {
  const [dashboard, setDashboard] = useState<Dashboard | null>(null)
  const [sectors, setSectors] = useState<Sector[]>([])
  const [alerts, setAlerts] = useState<Alert[]>([])
  const [selected, setSelected] = useState('energie-renouvelables')
  const [analysis, setAnalysis] = useState<Analysis | null>(null)
  const [benchmark, setBenchmark] = useState<Benchmark[]>([])

  useEffect(() => { api.dashboard().then(setDashboard); api.sectors().then(setSectors); api.alerts().then(setAlerts) }, [])
  useEffect(() => { api.analysis(selected).then(setAnalysis); api.benchmark(selected).then(setBenchmark) }, [selected])
  const selectedSector = useMemo(() => sectors.find(s => s.id === selected), [sectors, selected])

  return <main className="min-h-screen bg-[radial-gradient(circle_at_top_left,rgba(37,99,235,.25),transparent_35%),#020617]">
    <section className="mx-auto max-w-7xl px-6 py-8">
      <div className="mb-8 flex flex-col justify-between gap-4 md:flex-row md:items-end">
        <div>
          <p className="mb-3 inline-flex rounded-full border border-blue-400/30 bg-blue-500/10 px-3 py-1 text-sm text-blue-200">CDG Capital · Pôle Développement</p>
          <h1 className="text-4xl font-bold tracking-tight md:text-5xl">Sector Watch Intelligence</h1>
          <p className="mt-3 max-w-3xl text-slate-400">Plateforme MVP pour centraliser les données, automatiser l’analyse sectorielle, détecter les alertes et générer des rapports stratégiques.</p>
        </div>
        <a href="http://localhost:8000/docs" target="_blank" className="rounded-2xl bg-blue-600 px-5 py-3 font-medium text-white shadow-lg shadow-blue-900/30">Ouvrir l’API</a>
      </div>

      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
        <KpiCard title="Secteurs actifs" value={dashboard?.sector_count ?? '—'} subtitle="Périmètre initial CDG" icon={Database}/>
        <KpiCard title="Score investissement" value={dashboard?.avg_investment_score ?? '—'} subtitle="Moyenne tous secteurs" icon={TrendingUp}/>
        <KpiCard title="Score risque" value={dashboard?.avg_risk_score ?? '—'} subtitle="Surveillance consolidée" icon={Activity}/>
        <KpiCard title="Alertes actives" value={dashboard?.active_alerts ?? '—'} subtitle="Signaux faibles détectés" icon={AlertTriangle}/>
      </div>

      <div className="mt-6 grid gap-6 lg:grid-cols-[440px_1fr]">
        <SectorTable sectors={sectors} selected={selected} onSelect={setSelected}/>
        <div className="space-y-6">
          <div className="card p-6">
            <div className="mb-4 flex items-start justify-between gap-4">
              <div>
                <h2 className="text-2xl font-semibold">{selectedSector?.name ?? 'Analyse sectorielle'}</h2>
                <p className="mt-1 text-sm text-slate-400">Synthèse IA MVP · confiance {analysis?.confidence_score ?? '—'}%</p>
              </div>
              <FileText className="text-cdg-gold"/>
            </div>
            <p className="leading-7 text-slate-300">{analysis?.executive_summary ?? 'Chargement de la synthèse...'}</p>
            <div className="mt-6 grid gap-4 md:grid-cols-3">
              <Insight title="Opportunités" items={analysis?.opportunities}/>
              <Insight title="Risques" items={analysis?.risks}/>
              <Insight title="Actions recommandées" items={analysis?.recommended_actions}/>
            </div>
          </div>
          <BenchmarkChart data={benchmark}/>
        </div>
      </div>

      <div className="mt-6 card p-6">
        <h2 className="mb-4 text-lg font-semibold">Alertes & signaux</h2>
        <div className="grid gap-3 md:grid-cols-3">
          {alerts.slice(0,6).map(a => <div key={a.id} className="rounded-2xl border border-white/10 bg-black/20 p-4">
            <p className="text-sm uppercase tracking-wide text-orange-300">{a.level}</p>
            <h3 className="mt-1 font-semibold">{a.title}</h3>
            <p className="mt-2 text-sm text-slate-400">{a.message}</p>
          </div>)}
        </div>
      </div>
    </section>
  </main>
}

function Insight({ title, items }: { title:string; items?:string[] }) {
  return <div className="rounded-2xl border border-white/10 bg-white/[0.03] p-4">
    <h3 className="mb-3 font-medium text-blue-200">{title}</h3>
    <ul className="space-y-2 text-sm text-slate-400">{(items ?? []).map(item => <li key={item}>• {item}</li>)}</ul>
  </div>
}
