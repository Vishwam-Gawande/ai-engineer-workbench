export default function QuickActionCard({ title }) {
  return (
    <button
      style={{
        width: "100%",
        padding: "18px",
        background: "#2563eb",
        color: "white",
        border: "none",
        borderRadius: "10px",
        cursor: "pointer",
        fontWeight: "600",
        fontSize: "15px",
      }}
    >
      {title}
    </button>
  );
}