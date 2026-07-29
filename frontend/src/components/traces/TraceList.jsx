export default function TraceList({ children }) {
  return (
    <div
      style={{
        display: "grid",
        gap: "20px",
      }}
    >
      {children}
    </div>
  );
}