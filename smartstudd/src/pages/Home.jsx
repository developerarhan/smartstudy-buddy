import { useEffect, useState } from "react";
import StudyForm from "../components/StudyForm";
import StudyPlan from "../components/StudyPlan";
import Loader from "../components/Loader";
import ThemeToggle from "../components/ThemeToggle";
import { generateStudyPlan } from "../services/api";

const Home = () => {
  const [loading, setLoading] = useState(false);
  const [studyPlan, setStudyPlan] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/health/")
      .then((res) => res.json())
      .then((data) => console.log("Backend says:", data))
      .catch((err) => console.error("Backend error:", err));
  }, []);

  const handleGeneratePlan = async (formData) => {
    try {
      setLoading(true);
      const data = await generateStudyPlan(formData);
      console.log("API RESPONSE:", data);

      setStudyPlan(data?.data?.plan || data?.plan || []);
    } catch (err) {
      alert("Failed to generate plan");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>🎯 SmartStudy Buddy</h1>
      <p>AI-powered study planner</p>

      <ThemeToggle />
      <StudyForm onSubmit={handleGeneratePlan} />

      {loading && <Loader />}
      {studyPlan && <StudyPlan plan={studyPlan} />}
    </div>
  );
};

export default Home;