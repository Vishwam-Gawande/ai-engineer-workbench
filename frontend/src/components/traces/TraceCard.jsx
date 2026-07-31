import Card from "../ui/Card";

export default function TraceCard({
  traceName,
  model,
  latency,
  tokens,
  cost,
  status,
}) {
  const statusColor =
    status === "SUCCESS"
      ? "#16a34a"
      : "#dc2626";

  return (
    <Card>
      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
        }}
      >
        <div>
          <h3
            style={{
              margin: 0,
              fontSize: "18px",
            }}
          >
            {traceName}
          </h3>

          <p
            style={{
              margin: "8px 0",
              color: "#6b7280",
            }}
          >
            {model}
          </p>
        </div>

        <span
          style={{
            background: statusColor,
            color: "white",
            padding: "6px 12px",
            borderRadius: "20px",
            fontSize: "13px",
            fontWeight: 600,
          }}
        >
          {status}
        </span>
      </div>

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(3,1fr)",
          marginTop: "20px",
          gap: "20px",
        }}
      >
        <Metric
          title="Latency"
          value={`${latency} ms`}
        />

        <Metric
          title="Tokens"
          value={tokens}
        />

        <Metric
          title="Cost"
          value={`$${cost}`}
        />
      </div>
    </Card>
  );
}

function Metric({
  title,
  value,
}) {
  return (
    <div>
      <div
        style={{
          color: "#6b7280",
          fontSize: "13px",
        }}
      >
        {title}
      </div>

      <div
        style={{
          marginTop: "6px",
          fontWeight: 700,
          fontSize: "18px",
        }}
      >
        {value}
      </div>
    </div>
  );
}