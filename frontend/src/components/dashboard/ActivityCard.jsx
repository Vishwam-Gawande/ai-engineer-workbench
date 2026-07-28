export default function ActivityCard({ text }) {
  return (
    <div
      style={{
        background: "white",
        padding: "20px",
        borderRadius: "12px",
        marginBottom: "16px",
      }}
    >
      {text}
    </div>
  );
}