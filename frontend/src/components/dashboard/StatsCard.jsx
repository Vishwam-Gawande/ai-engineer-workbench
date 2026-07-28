export default function StatsCard({
  title,
  value,
  subtitle,
}) {
  return (
    <div
      style={{
        background: "white",
        borderRadius: "12px",
        padding: "24px",
        boxShadow: "0 2px 8px rgba(0,0,0,0.08)",
      }}
    >
      <h3>{title}</h3>

      <h1>{value}</h1>

      <p>{subtitle}</p>
    </div>
  );
}