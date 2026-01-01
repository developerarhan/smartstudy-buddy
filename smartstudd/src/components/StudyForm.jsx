import { useState } from "react";
import "./StudyForm.css";

const StudyForm = ({ onSubmit }) => {
  const [subject, setSubject] = useState("");
  const [hours, setHours] = useState("");
  const [days, setDays] = useState(7);

  const handleSubmit = (e) => {
    e.preventDefault();

    onSubmit({
      subject,
      hours_per_day: Number(hours),
      days: Number(days),
    });
  };

  return (
    <form onSubmit={handleSubmit} className="study-form">
      <div className="form-header">
        <h2>🎯 Create Your Study Plan</h2>
        <p>Let AI organize your learning efficiently</p>
      </div>

      <div className="form-group">
        <label>Subject</label>
        <input
          type="text"
          placeholder="e.g. Machine Learning"
          value={subject}
          onChange={(e) => setSubject(e.target.value)}
          required
        />
      </div>

      <div className="form-row">
        <div className="form-group">
          <label>Hours / Day</label>
          <input
            type="number"
            placeholder="2"
            value={hours}
            onChange={(e) => setHours(e.target.value)}
            required
          />
        </div>

        <div className="form-group">
          <label>Total Days</label>
          <input
            type="number"
            placeholder="7"
            value={days}
            onChange={(e) => setDays(e.target.value)}
            required
          />
        </div>
      </div>

      <button type="submit" className="submit-btn">
        🚀 Generate AI Plan
      </button>
    </form>
  );
};

export default StudyForm;