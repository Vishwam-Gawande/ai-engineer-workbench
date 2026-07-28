import { useEffect, useState } from "react";

import MainLayout from "../../layouts/MainLayout";

import PageHeader from "../../components/ui/PageHeader";

import PromptToolbar from "../../components/prompts/PromptToolbar";
import PromptList from "../../components/prompts/PromptList";
import PromptCard from "../../components/prompts/PromptCard";

import { getPrompts } from "../../services/promptService";

export default function PromptsPage() {
  const [prompts, setPrompts] = useState([]);

  useEffect(() => {
    async function loadPrompts() {
      const data = await getPrompts();
      setPrompts(data);
    }

    loadPrompts();
  }, []);

  return (
    <MainLayout>
      <PageHeader
        title="Prompts"
        description="Manage prompt templates and versions."
      />

      <PromptToolbar />

      <PromptList>
        {prompts.map((prompt) => (
          <PromptCard
            key={prompt.id}
            name={prompt.name}
            version={prompt.version}
            model={prompt.model}
          />
        ))}
      </PromptList>
    </MainLayout>
  );
}