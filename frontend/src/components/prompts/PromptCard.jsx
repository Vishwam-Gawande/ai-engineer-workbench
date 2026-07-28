export default function PromptCard({
  name,
  version,
  model,
}) {
  return (
    <div
      style={{
        background: "white",
        borderRadius: "12px",
        padding: "20px",
        boxShadow: "0 2px 8px rgba(0,0,0,0.08)",
        border: "1px solid #e5e7eb",
      }}
    >
      <h3
        style={{
          margin: 0,
          marginBottom: "8px",
        }}
      >
        {name}
      </h3>

      <p
        style={{
          margin: "4px 0",
          color: "#6b7280",
        }}
      >
        Version: {version}
      </p>

      <p
        style={{
          margin: "4px 0",
          color: "#6b7280",
        }}
      >
        Model: {model}
      </p>
    </div>
  );
}