import API_BASE_URL from "../api/client";

export async function getPrompts() {
  const response = await fetch(`${API_BASE_URL}/prompts`);

  if (!response.ok) {
    throw new Error("Failed to fetch prompts.");
  }

  return await response.json();
}

export async function createPrompt(prompt) {
  const response = await fetch(`${API_BASE_URL}/prompts`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(prompt),
  });

  return await response.json();
}

export async function updatePrompt(id, prompt) {
  const response = await fetch(`${API_BASE_URL}/prompts/${id}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(prompt),
  });

  return await response.json();
}

export async function deletePrompt(id) {
  await fetch(`${API_BASE_URL}/prompts/${id}`, {
    method: "DELETE",
  });
}