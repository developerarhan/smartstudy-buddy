import "./StudyPlan.css";

const StudyPlan = ({ plan }) => {
  if (!Array.isArray(plan) || plan.length === 0) return null;

  return (
    <div className="study-plan-wrapper">
      <h2 className="plan-title">📘 Your AI-Generated Study Plan</h2>

      <div className="plan-grid">
        {plan.map((day) => (
          <div key={day.day} className="plan-card">
            <div className="plan-header">
              <span className="plan-day">Day {day.day}</span>
              <span className="plan-hours">⏱ {day.total_hours} hrs</span>
            </div>

            <h3 className="plan-topic">{day.title}</h3>

            <div className="plan-blocks">
              {day.blocks.map((block, idx) => (
                <div key={idx} className={`block ${block.type}`}>
                  <span className="block-time">{block.duration}h</span>
                  <span className="block-text">{block.topic}</span>
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default StudyPlan;