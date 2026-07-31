import Card from "../ui/Card";
import { colors } from "../../styles/theme";

export default function StatsCard({
  title,
  value,
}) {
  return (
    <Card>
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          gap: "12px",
        }}
      >
        <span
          style={{
            color: colors.textSecondary,
            fontSize: "14px",
          }}
        >
          {title}
        </span>

        <h2
          style={{
            margin: 0,
            fontSize: "34px",
            fontWeight: 700,
          }}
        >
          {value}
        </h2>

        <span
          style={{
            color: "#16a34a",
            fontSize: "13px",
            fontWeight: 600,
          }}
        >
          ↑ Healthy
        </span>
      </div>
    </Card>
  );
}