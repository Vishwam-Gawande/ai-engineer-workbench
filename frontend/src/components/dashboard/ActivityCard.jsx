import Card from "../ui/Card";

export default function ActivityCard({
  text,
}) {
  return (
    <Card>
      <div
        style={{
          display: "flex",
          alignItems: "center",
          gap: "12px",
        }}
      >
        <div
          style={{
            width: 10,
            height: 10,
            borderRadius: "50%",
            background: "#16a34a",
          }}
        />

        <span>{text}</span>
      </div>
    </Card>
  );
}