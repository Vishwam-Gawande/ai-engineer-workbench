export default function PromptToolbar() {
  return (
    <div
      style={{
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
        marginBottom: "24px",
      }}
    >
      <input
        type="text"
        placeholder="Search prompts..."
        style={{
          padding: "10px 14px",
          width: "300px",
          borderRadius: "8px",
          border: "1px solid #d1d5db",
        }}
      />

      <button
        style={{
          padding: "10px 18px",
          borderRadius: "8px",
          border: "none",
          background: "#2563eb",
          color: "white",
          cursor: "pointer",
        }}
      >
        + New Prompt
      </button>
    </div>
  );
}