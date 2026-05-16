import type { Config } from 'tailwindcss'

const config: Config = {
  content: ['./app/**/*.{ts,tsx}', './components/**/*.{ts,tsx}', './lib/**/*.{ts,tsx}'],
  theme: {
    extend: {
      colors: {
        cdg: {
          navy: '#0B1220',
          blue: '#2563EB',
          gold: '#C8A45D',
          slate: '#64748B'
        }
      }
    }
  },
  plugins: []
}
export default config
