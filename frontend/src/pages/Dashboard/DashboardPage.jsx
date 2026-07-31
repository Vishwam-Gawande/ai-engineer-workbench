import { useEffect, useState } from "react";

import PageHeader from "../../components/ui/PageHeader";

import StatsCard from "../../components/dashboard/StatsCard";
import ActivityCard from "../../components/dashboard/ActivityCard";
import QuickActionCard from "../../components/dashboard/QuickActionCard";
import SectionTitle from "../../components/dashboard/SectionTitle";

import { getDashboardStats } from "../../services/dashboardService";

const recentActivities = [
  "Trace completed successfully.",
  "Prompt updated.",
  "Evaluation finished.",
];

const quickActions = [
  "New Prompt",
  "View Traces",
  "Run Evaluation",
];

export default function DashboardPage() {
  const [stats, setStats] = useState([]);

  useEffect(() => {
    async function loadDashboard() {
      const data = await getDashboardStats();

      setStats([
        {
          title: "Traces",
          value: data.traceCount,
        },
        {
          title: "Cost",
          value: `$${data.totalCost.toFixed(3)}`,
        },
        {
          title: "Latency",
          value: `${data.averageLatency} ms`,
        },
        {
          title: "Success Rate",
          value: `${data.successRate}%`,
        },
      ]);
    }

    loadDashboard();
  }, []);

  return (
    <>
      <PageHeader
        title="Dashboard"
        description="Monitor your AI applications, traces, evaluations, and experiments."
      />

      <SectionTitle title="Overview" />

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(4, 1fr)",
          gap: "20px",
          marginBottom: "40px",
        }}
      >
        {stats.map((stat) => (
          <StatsCard
            key={stat.title}
            title={stat.title}
            value={stat.value}
          />
        ))}
      </div>

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "2fr 1fr",
          gap: "24px",
        }}
      >
        <div>
          <SectionTitle title="Recent Activity" />

          {recentActivities.map((activity) => (
            <ActivityCard
              key={activity}
              text={activity}
            />
          ))}
        </div>

        <div>
          <SectionTitle title="Quick Actions" />

          {quickActions.map((action) => (
            <QuickActionCard
              key={action}
              title={action}
            />
          ))}
        </div>
      </div>
    </>
  );
}