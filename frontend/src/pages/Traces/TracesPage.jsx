

import PageHeader from "../../components/ui/PageHeader";

import TraceList from "../../components/traces/TraceList";
import TraceCard from "../../components/traces/TraceCard";
import TraceTimeline from "../../components/traces/TraceTimeline";

import { useEffect, useState } from "react";

import {
  getTraces,
} from "../../services/traceService";

export default function TracesPage() {
  const [traces, setTraces] = useState([]);

  useEffect(() => {
    async function loadTraces() {
      const data = await getTraces();
      setTraces(data);
    }

    loadTraces();
  }, []);

  return (
  <>
    <PageHeader
      title="Traces"
      description="Inspect AI execution traces and debug application behavior."
    />

    <TraceList>
      {traces.map((trace) => (
        <TraceCard
          key={trace.id}
          traceName={trace.trace_name}
          model={trace.model_name}
          latency={trace.latency_ms}
          tokens={trace.total_tokens}
          cost={trace.total_cost}
          status={trace.status}
        />
      ))}
    </TraceList>

    <TraceTimeline />
  </>
);
}