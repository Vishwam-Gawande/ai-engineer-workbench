import { NavLink } from "react-router-dom";
import { colors, spacing } from "../../styles/theme";

const links = [
  { name: "Dashboard", path: "/dashboard" },
  { name: "Traces", path: "/traces" },
  { name: "Prompts", path: "/prompts" },
  { name: "Experiments", path: "/experiments" },
  { name: "Settings", path: "/settings" },
];

export default function Sidebar() {
  return (
    <aside
      style={{
        width: "260px",
        background: colors.sidebar,
        color: "white",
        display: "flex",
        flexDirection: "column",
        justifyContent: "space-between",
        padding: spacing.xl,
      }}
    >
      <div>
        <h2
          style={{
            marginBottom: "40px",
            fontSize: "24px",
            fontWeight: 700,
          }}
        >
          AI Engineer
          <br />
          Workbench
        </h2>

        <nav
          style={{
            display: "flex",
            flexDirection: "column",
            gap: "10px",
          }}
        >
          {links.map((link) => (
            <NavLink
              key={link.path}
              to={link.path}
              style={({ isActive }) => ({
                padding: "12px 16px",
                borderRadius: "10px",
                textDecoration: "none",
                color: "white",
                background: isActive
                  ? "rgba(255,255,255,0.12)"
                  : "transparent",
                fontWeight: isActive ? 600 : 500,
                transition: "all .2s",
              })}
            >
              {link.name}
            </NavLink>
          ))}
        </nav>
      </div>

      <div
        style={{
          borderTop: "1px solid rgba(255,255,255,.15)",
          paddingTop: "20px",
          opacity: 0.8,
          fontSize: "14px",
        }}
      >
        v0.1.0
      </div>
    </aside>
  );
}