import Header from './components/Header'
import AgentDashboard from './components/AgentDashboard'
import NarrationPanel from './components/NarrationPanel'

export default function App() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-black via-gray-900 to-black text-gray-200 p-8">
      <Header />
      <AgentDashboard />
      <NarrationPanel />
    </div>
  )
}