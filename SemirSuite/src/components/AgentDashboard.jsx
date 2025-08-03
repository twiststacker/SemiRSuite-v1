import { useState } from 'react'

export default function AgentDashboard() {
  const [prompt, setPrompt] = useState("")
  const [ideas, setIdeas] = useState([])

  const handleGenerate = async () => {
    const response = await fetch("/api/v1/generate-ideas", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ prompt })
    })
    const data = await response.json()
    setIdeas(data.ideas)
  }

  return (
    <div className="bg-glass p-6 rounded-lg shadow-lg max-w-2xl mx-auto mb-12">
      <h2 className="text-2xl text-neon mb-4">🎯 IdeaForge Agent</h2>
      <input
        type="text"
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        placeholder="Enter a prompt..."
        className="w-full p-2 mb-4 bg-black text-gray-200 border border-gray-700 rounded"
      />
      <button
        onClick={handleGenerate}
        className="bg-neon px-4 py-2 rounded"
      >
        Generate Ideas
      </button>

      <ul className="mt-6 space-y-2">
        {ideas.map((idea, i) => (
          <li key={i} className="bg-black bg-opacity-30 p-2 rounded text-gray-100">
            {i + 1}. {idea}
          </li>
        ))}
      </ul>
    </div>
  )
}