export default function ActivityCard({ text }) {
  return (
    <div
      style={{
        background: "#ffffff",
        padding: "18px",
        marginBottom: "14px",
        borderRadius: "10px",
        border: "1px solid #e5e7eb",
        boxShadow: "0 2px 8px rgba(0,0,0,0.05)",
      }}
    >
      {text}
    </div>
  );
}