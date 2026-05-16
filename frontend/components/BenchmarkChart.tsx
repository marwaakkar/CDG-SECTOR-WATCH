'use client'
import { ResponsiveContainer, BarChart, Bar, XAxis, YAxis, Tooltip, Legend } from 'recharts'
import type { Benchmark } from '@/lib/api'

export function BenchmarkChart({ data }: { data: Benchmark[] }) {
  return <div className="card p-5">
    <h2 className="mb-4 text-lg font-semibold">Benchmark Maroc vs international</h2>
    <div className="h-80">
      <ResponsiveContainer width="100%" height="100%">
        <BarChart data={data}>
          <XAxis dataKey="label" tick={{ fill: '#94a3b8', fontSize: 12 }} />
          <YAxis tick={{ fill: '#94a3b8', fontSize: 12 }} />
          <Tooltip contentStyle={{ background: '#0f172a', border: '1px solid rgba(255,255,255,.12)', borderRadius: 12 }} />
          <Legend />
          <Bar dataKey="morocco" name="Maroc" fill="#2563EB" radius={[6,6,0,0]} />
          <Bar dataKey="international_avg" name="Moy. internationale" fill="#C8A45D" radius={[6,6,0,0]} />
          <Bar dataKey="best_in_class" name="Best in class" fill="#64748B" radius={[6,6,0,0]} />
        </BarChart>
      </ResponsiveContainer>
    </div>
  </div>
}
