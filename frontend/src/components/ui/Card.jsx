import { colors, radius, shadow, spacing } from "../../styles/theme";

export default function Card({ children }) {
  return (
    <div
      style={{
        background: colors.surface,
        border: `1px solid ${colors.border}`,
        borderRadius: radius.lg,
        padding: spacing.lg,
        boxShadow: shadow.card,
      }}
    >
      {children}
    </div>
  );
}