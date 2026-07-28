export default function StatsCard({ title, value }) {
  return (
    <div
      style={{
        background: "#ffffff",
        borderRadius: "12px",
        padding: "24px",
        boxShadow: "0 2px 10px rgba(0,0,0,0.08)",
        border: "1px solid #e5e7eb",
      }}
    >
      <p
        style={{
          margin: 0,
          fontSize: "14px",
          color: "#6b7280",
        }}
      >
        {title}
      </p>

      <h2
        style={{
          marginTop: "12px",
          marginBottom: 0,
          fontSize: "30px",
          color: "#111827",
        }}
      >
        {value}
      </h2>
    </div>
  );
}