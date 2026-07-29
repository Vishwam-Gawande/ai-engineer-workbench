import API_BASE_URL from "../api/client";

export async function getTraces() {
  const response = await fetch(`${API_BASE_URL}/traces/`);

  if (!response.ok) {
    throw new Error("Failed to fetch traces.");
  }

  return await response.json();
}

export async function getTrace(id) {
  const response = await fetch(`${API_BASE_URL}/traces/${id}`);

  if (!response.ok) {
    throw new Error("Failed to fetch trace.");
  }

  return await response.json();
}