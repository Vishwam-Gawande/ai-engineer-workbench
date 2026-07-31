import Button from "../ui/Button";
import Card from "../ui/Card";

export default function QuickActionCard({
  title,
}) {
  return (
    <Card>
      <Button>
        {title}
      </Button>
    </Card>
  );
}