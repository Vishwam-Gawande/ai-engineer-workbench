export default function TraceList({
  children,
}) {
  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        gap: "20px",
        marginBottom: "40px",
      }}
    >
      {children}
    </div>
  );
}