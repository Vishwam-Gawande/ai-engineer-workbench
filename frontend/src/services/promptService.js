import API_BASE_URL from "../api/client";

const API_KEY = import.meta.env.VITE_API_KEY;

export async function getPrompts() {
  const response = await fetch(`${API_BASE_URL}/prompts/`, {
    headers: {
      "X-API-Key": API_KEY,
    },
  });

  if (!response.ok) {
    throw new Error("Failed to fetch prompts.");
  }

  return await response.json();
}

export async function createPrompt(prompt) {
  const response = await fetch(`${API_BASE_URL}/prompts/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-API-Key": API_KEY,
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
      "X-API-Key": API_KEY,
    },
    body: JSON.stringify(prompt),
  });

  return await response.json();
}

export async function deletePrompt(id) {
  await fetch(`${API_BASE_URL}/prompts/${id}`, {
    method: "DELETE",
    headers: {
      "X-API-Key": API_KEY,
    },
  });
}