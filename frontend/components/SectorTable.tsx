import type { Sector } from '@/lib/api'

const trendStyle = { positive:'text-emerald-300 bg-emerald-500/10', stable:'text-blue-300 bg-blue-500/10', negative:'text-orange-300 bg-orange-500/10' }

export function SectorTable({ sectors, selected, onSelect }: { sectors:Sector[]; selected:string; onSelect:(id:string)=>void }) {
  return <div className="card overflow-hidden">
    <div className="border-b border-white/10 p-5"><h2 className="text-lg font-semibold">Secteurs prioritaires</h2></div>
    <div className="divide-y divide-white/10">
      {sectors.map(s => <button key={s.id} onClick={() => onSelect(s.id)} className={`w-full p-4 text-left transition hover:bg-white/5 ${selected===s.id?'bg-blue-500/10':''}`}>
        <div className="flex items-center justify-between gap-3">
          <div>
            <p className="font-medium">{s.name}</p>
            <p className="mt-1 line-clamp-1 text-sm text-slate-400">{s.description}</p>
          </div>
          <span className={`rounded-full px-3 py-1 text-xs ${trendStyle[s.trend]}`}>{s.trend}</span>
        </div>
        <div className="mt-3 grid grid-cols-3 gap-2 text-xs text-slate-400">
          <span>Croissance {s.growth_rate}%</span><span>Invest. {s.investment_score}/100</span><span>Risque {s.risk_score}/100</span>
        </div>
      </button>)}
    </div>
  </div>
}
