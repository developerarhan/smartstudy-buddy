const BASE_URL = "https://smartstudy-backend-1okw.onrender.com/api";

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
