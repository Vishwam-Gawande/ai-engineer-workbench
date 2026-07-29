import StatusBadge from "./StatusBadge";

export default function TraceCard({
  traceName,
  model,
  latency,
  tokens,
  cost,
  status,
}) {
  return (
    <div
      style={{
        background: "white",
        borderRadius: "12px",
        padding: "20px",
        border: "1px solid #e5e7eb",
        boxShadow: "0 2px 8px rgba(0,0,0,0.08)",
      }}
    >
      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          marginBottom: "12px",
        }}
      >
        <h3
          style={{
            margin: 0,
          }}
        >
          {traceName}
        </h3>

        <StatusBadge status={status} />
      </div>

      <p>Model: {model}</p>

      <p>Latency: {latency}</p>

      <p>Tokens: {tokens}</p>

      <p>Cost: {cost}</p>
    </div>
  );
}