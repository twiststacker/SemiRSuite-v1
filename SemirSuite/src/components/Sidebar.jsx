export default function Sidebar() {
  return (
    <aside className="w-64 h-screen bg-glass p-6 flex flex-col gap-6">
      <h1 className="text-neon text-3xl">SemirSuite</h1>
      <nav className="flex flex-col gap-4 mt-4">
        {['Dashboard', 'Tools', 'Agents', 'Metrics'].map((item) => (
          <button key={item} className="hover:text-neon transition text-lg text-gray-300">
            {item}
          </button>
        ))}
      </nav>
    </aside>
  );
}