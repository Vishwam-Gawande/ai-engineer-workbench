import PageHeader from "../../components/ui/PageHeader";

import StatsCard from "../../components/dashboard/StatsCard";
import ActivityCard from "../../components/dashboard/ActivityCard";
import QuickActionCard from "../../components/dashboard/QuickActionCard";
import SectionTitle from "../../components/dashboard/SectionTitle";

import {
  stats,
  recentActivities,
  quickActions,
} from "../../services/dashboardData";

export default function DashboardPage() {
  return (
    <>
      <PageHeader
        title="Dashboard"
        description="Monitor your AI applications, traces, evaluations, and experiments."
      />

      {/* Overview */}
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

      {/* Recent Activity + Quick Actions */}
      <div
        style={{
          display: "grid",
          gridTemplateColumns: "2fr 1fr",
          gap: "24px",
        }}
      >
        {/* Left Column */}
        <div>
          <SectionTitle title="Recent Activity" />

          {recentActivities.map((activity) => (
            <ActivityCard
              key={activity}
              text={activity}
            />
          ))}
        </div>

        {/* Right Column */}
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