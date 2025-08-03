import { useState } from 'react'

export default function NarrationPanel() {
  const [topic, setTopic] = useState("")
  const [tone, setTone] = useState("neutral")
  const [script, setScript] = useState("")
  const [loading, setLoading] = useState(false)

  const handleGenerate = async () => {
    setLoading(true)
    const response = await fetch("/api/v1/generate-script", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ topic, tone })
    })
    const data = await response.json()
    setScript(data.script)
    setLoading(false)
  }

  return (
    <div className="bg-glass p-6 rounded-lg shadow-lg max-w-2xl mx-auto mt-12">
      <h2 className="text-2xl font-orbitron text-neon mb-4">🗣️ NarrationWeaver</h2>
      <input
        type="text"
        value={topic}
        onChange={(e) => setTopic(e.target.value)}
        placeholder="Enter a topic..."
        className="w-full p-2 mb-4 bg-black text-gray-200 border border-gray-700 rounded"
      />
      <select
        value={tone}
        onChange={(e) => setTone(e.target.value)}
        className="w-full p-2 mb-4 bg-black text-gray-200 border border-gray-700 rounded"
      >
        <option value="neutral">Neutral</option>
        <option value="uplifting">Uplifting</option>
        <option value="dramatic">Dramatic</option>
        <option value="informative">Informative</option>
      </select>
      <button
        onClick={handleGenerate}
        className="bg-neon text-black px-4 py-2 rounded hover:opacity-80"
      >
        {loading ? "Generating..." : "Generate Script"}
      </button>

      {script && (
        <div className="mt-6 bg-black bg-opacity-30 p-4 rounded text-gray-100 whitespace-pre-wrap">
          {script}
        </div>
      )}
    </div>
  )
}