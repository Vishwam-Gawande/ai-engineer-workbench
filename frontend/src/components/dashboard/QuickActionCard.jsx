export default function QuickActionCard({ title }) {
  return (
    <div
      style={{
        background: "white",
        borderRadius: "12px",
        padding: "20px",
        cursor: "pointer",
      }}
    >
      <h3>{title}</h3>
    </div>
  );
}