import { getTraces } from "./traceService";

export async function getDashboardStats() {
  const traces = await getTraces();

  const traceCount = traces.length;

  const totalCost = traces.reduce(
    (sum, trace) => sum + trace.total_cost,
    0
  );

  const averageLatency =
    traces.length > 0
      ? Math.round(
          traces.reduce(
            (sum, trace) => sum + trace.latency_ms,
            0
          ) / traces.length
        )
      : 0;

  const successRate =
    traces.length > 0
      ? Math.round(
          traces.filter(
            (trace) => trace.status === "success"
          ).length /
            traces.length *
            100
        )
      : 0;

  return {
    traceCount,
    totalCost,
    averageLatency,
    successRate,
  };
}