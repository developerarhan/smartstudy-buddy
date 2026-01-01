const StudyPlan = ({ plan }) => {
  return (
    <div className="card">
      <h2>Your Study Plan 📘</h2>

      {plan.map((day, index) => (
        <div key={index} className="plan-item">
          <strong>Day {index + 1}:</strong>
          <p>{day}</p>
        </div>
      ))}
    </div>
  );
};

export default StudyPlan;
