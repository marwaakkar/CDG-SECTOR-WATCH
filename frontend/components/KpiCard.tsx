import { LucideIcon } from 'lucide-react'

export function KpiCard({ title, value, subtitle, icon: Icon }: { title:string; value:string|number; subtitle:string; icon:LucideIcon }) {
  return <div className="card p-5">
    <div className="flex items-center justify-between">
      <div>
        <p className="text-sm text-slate-400">{title}</p>
        <p className="mt-2 text-3xl font-semibold tracking-tight">{value}</p>
      </div>
      <div className="rounded-2xl bg-blue-500/10 p-3 text-blue-300"><Icon size={24}/></div>
    </div>
    <p className="mt-4 text-sm text-slate-500">{subtitle}</p>
  </div>
}
