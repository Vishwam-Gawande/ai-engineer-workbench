import { colors, radius } from "../../styles/theme";

export default function Button({ children }) {
  return (
    <button
      style={{
        background: colors.primary,
        color: "white",
        border: "none",
        padding: "12px 20px",
        borderRadius: radius.md,
        cursor: "pointer",
        fontWeight: 600,
      }}
    >
      {children}
    </button>
  );
}