export default function TraceTimeline() {
  const steps = [
    "Receive Request",
    "Retrieve Context",
    "Call LLM",
    "Generate Response",
    "Return Output",
  ];

  return (
    <div
      style={{
        background: "white",
        border: "1px solid #e5e7eb",
        borderRadius: "12px",
        padding: "20px",
        marginTop: "24px",
      }}
    >
      <h3
        style={{
          marginTop: 0,
          marginBottom: "20px",
        }}
      >
        Trace Timeline
      </h3>

      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: "12px",
          flexWrap: "wrap",
        }}
      >
        {steps.map((step, index) => (
          <div
            key={index}
            style={{
              flex: 1,
              minWidth: "120px",
              textAlign: "center",
            }}
          >
            <div
              style={{
                width: "40px",
                height: "40px",
                margin: "0 auto 10px",
                borderRadius: "50%",
                background: "#2563eb",
                color: "white",
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                fontWeight: "bold",
              }}
            >
              {index + 1}
            </div>

            <p
              style={{
                margin: 0,
                fontSize: "14px",
              }}
            >
              {step}
            </p>
          </div>
        ))}
      </div>
    </div>
  );
}