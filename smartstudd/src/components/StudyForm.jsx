import { useState } from "react";

const StudyForm = ({ onSubmit }) => {
  const [subject, setSubject] = useState("");
  const [deadline, setDeadline] = useState("");
  const [hours, setHours] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    onSubmit({
      subject,
      deadline,
      daily_hours: hours,
    });
  };

  return (
    <form onSubmit={handleSubmit} className="card">
      <h2>Create Your Study Plan</h2>

      <input
        type="text"
        placeholder="Subject (e.g. Operating Systems)"
        value={subject}
        onChange={(e) => setSubject(e.target.value)}
        required
      />

      <input
        type="date"
        value={deadline}
        onChange={(e) => setDeadline(e.target.value)}
        required
      />

      <input
        type="number"
        placeholder="Daily Study Hours"
        value={hours}
        onChange={(e) => setHours(e.target.value)}
        required
      />

      <button type="submit">Generate Plan 🚀</button>
    </form>
  );
};

export default StudyForm;
