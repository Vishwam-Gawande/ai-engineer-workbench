export default function StatusBadge({ status }) {
  const colors = {
    Success: "#16a34a",
    Running: "#2563eb",
    Failed: "#dc2626",
  };

  return (
    <span
      style={{
        background: colors[status] || "#6b7280",
        color: "white",
        padding: "4px 10px",
        borderRadius: "999px",
        fontSize: "12px",
        fontWeight: "600",
      }}
    >
      {status}
    </span>
  );
}