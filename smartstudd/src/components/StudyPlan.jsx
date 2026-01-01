import "./StudyPlan.css";

const StudyPlan = ({ plan }) => {
  if (!Array.isArray(plan) || plan.length === 0) {
    return null;
  }

  return (
    <div className="study-plan-wrapper">
      <h2 className="plan-title">📘 Your Personalized Study Plan</h2>

      <div className="plan-grid">
        {plan.map((item) => (
          <div key={item.day} className="plan-card">
            <div className="plan-day">Day {item.day}</div>

            <h4 className="plan-topic">{item.topic}</h4>
            <p className="plan-hours">⏱ {item.hours} hours</p>

            <div className="badges">
              {item.revision && (
                <span className="badge revision">🔁 Revision</span>
              )}
              {item.practice && (
                <span className="badge practice">🧠 Practice</span>
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default StudyPlan;
