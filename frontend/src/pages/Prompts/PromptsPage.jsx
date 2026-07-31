import { useEffect, useState } from "react";



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
    <>
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
          />
        ))}
      </PromptList>
    </>
  );
}