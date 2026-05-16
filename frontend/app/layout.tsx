import './globals.css'
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'CDG Sector Watch',
  description: 'Plateforme d’analyse sectorielle et veille stratégique'
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return <html lang="fr"><body>{children}</body></html>
}
