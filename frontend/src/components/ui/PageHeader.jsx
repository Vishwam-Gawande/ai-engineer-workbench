export default function PageHeader({ title, description }) {
  return (
    <header
      style={{
        marginBottom: "32px",
      }}
    >
      <h1
        style={{
          margin: 0,
          fontSize: "2rem",
        }}
      >
        {title}
      </h1>

      <p
        style={{
          marginTop: "8px",
          color: "#6b7280",
        }}
      >
        {description}
      </p>
    </header>
  );
}