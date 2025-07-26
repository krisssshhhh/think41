
const API_BASE_URL = "http://localhost:8000";

export async function sendMessageToBot(userId, message) {
  const response = await fetch(`${API_BASE_URL}/api/chat`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      user_id: userId,
      message: message,
    }),
  });

  if (!response.ok) {
    const error = await response.json();
    throw new Error(error?.error || "API call failed");
  }

  return await response.json();
}