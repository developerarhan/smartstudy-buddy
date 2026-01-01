const BASE_URL = "http://127.0.0.1:8000/api";

export const generateStudyPlan = async (payload) => {
  const response = await fetch(`${BASE_URL}/study-plan/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });

  if (!response.ok) {
    throw new Error("Failed to generate study plan");
  }

  return response.json();
};
