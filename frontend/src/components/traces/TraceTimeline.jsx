import Card from "../ui/Card";

const steps = [
  "Receive Request",
  "Retrieve Context",
  "Call LLM",
  "Generate Response",
  "Return Output",
];

export default function TraceTimeline() {
  return (
    <Card>
      <h2
        style={{
          marginTop: 0,
          marginBottom: "24px",
        }}
      >
        Trace Timeline
      </h2>

      {steps.map((step, index) => (
        <div
          key={step}
          style={{
            display: "flex",
            alignItems: "center",
            marginBottom: "18px",
          }}
        >
          <div
            style={{
              width: "34px",
              height: "34px",
              borderRadius: "50%",
              background: "#2563eb",
              color: "white",
              display: "grid",
              placeItems: "center",
              marginRight: "18px",
              fontWeight: 700,
            }}
          >
            {index + 1}
          </div>

          <div>{step}</div>
        </div>
      ))}
    </Card>
  );
}