import MainLayout from "../../layouts/MainLayout";

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
    <MainLayout>
      <PageHeader
        title="Traces"
        description="Inspect AI execution traces and debug application behavior."
      />

      <TraceList>
        {traces.map((trace) => (
          <TraceCard
            key={trace.id}
            traceName={trace.trace_name}
            model={trace.model}
            latency={trace.latency}
            tokens={trace.tokens}
            cost={trace.cost}
            status={trace.status}
          />
        ))}
      </TraceList>
      <TraceTimeline />
    </MainLayout>
  );
}