export default function PageHeader({
  title,
  description,
}) {
  return (
    <div
      style={{
        marginBottom: "40px",
      }}
    >
      <h1
        style={{
          marginBottom: "8px",
          fontSize: "34px",
          color: "#111827",
        }}
      >
        {title}
      </h1>

      <p
        style={{
          margin: 0,
          color: "#6b7280",
          fontSize: "16px",
        }}
      >
        {description}
      </p>
    </div>
  );
}