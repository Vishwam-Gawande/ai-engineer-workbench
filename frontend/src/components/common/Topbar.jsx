import { colors } from "../../styles/theme";

export default function Topbar() {
  return (
    <header
      style={{
        height: "72px",
        background: colors.surface,
        borderBottom: `1px solid ${colors.border}`,
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
        padding: "0 32px",
      }}
    >
      <div>
        <h2
          style={{
            fontSize: "22px",
            margin: 0,
          }}
        >
          AI Engineer Workbench
        </h2>

        <div
          style={{
            color: colors.textSecondary,
            fontSize: "14px",
            marginTop: "4px",
          }}
        >
          Production AI Observability Platform
        </div>
      </div>

      <div
        style={{
          display: "flex",
          alignItems: "center",
          gap: "16px",
        }}
      >
        <div
          style={{
            width: "38px",
            height: "38px",
            borderRadius: "50%",
            background: "#2563eb",
            color: "white",
            display: "grid",
            placeItems: "center",
            fontWeight: 700,
          }}
        >
          VG
        </div>
      </div>
    </header>
  );
}