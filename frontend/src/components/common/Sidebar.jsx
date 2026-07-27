import { Link } from "react-router-dom";

export default function Sidebar() {
  return (
    <aside
      style={{
        width: "240px",
        background: "#111827",
        color: "white",
        padding: "24px",
      }}
    >
      <h2>Workbench</h2>

      <nav
        style={{
          display: "flex",
          flexDirection: "column",
          gap: "16px",
          marginTop: "32px",
        }}
      >
        <Link to="/dashboard">Dashboard</Link>

        <Link to="/traces">Traces</Link>

        <Link to="/prompts">Prompts</Link>

        <Link to="/experiments">Experiments</Link>

        <Link to="/settings">Settings</Link>
      </nav>
    </aside>
  );
}