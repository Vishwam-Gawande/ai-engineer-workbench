export default function PromptList({ children }) {
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