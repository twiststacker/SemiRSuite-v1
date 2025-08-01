const agents = [
  { name: 'Pilot', status: 'Idle', task: 'Awaiting input...' },
  { name: 'Copilot', status: 'Monitoring', task: 'Tracking metrics' },
  { name: 'Navigator', status: 'Routing', task: 'Optimizing paths' },
];

export default function AgentPanel() {
  return (
    <div className="bg-glass p-6 rounded-xl shadow-xl">
      <h2 className="text-2xl text-neon mb-6">🧠 Agent Orchestration</h2>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {agents.map((agent) => (
          <div
            key={agent.name}
            className="bg-gradient-to-br from-cyan-900 to-indigo-900 p-4 rounded-lg border border-cyan-500 shadow-lg hover:shadow-cyan-500/50 transition duration-300"
          >
            <h3 className="text-cyan-300 text-xl mb-2">{agent.name}</h3>
            <p className="text-slate-300">
              Status: <span className="text-green-400">{agent.status}</span>
            </p>
            <p className="text-slate-300">
              Task: <span className="text-yellow-300">{agent.task}</span>
            </p>
          </div>
        ))}
      </div>
    </div>
  );
}