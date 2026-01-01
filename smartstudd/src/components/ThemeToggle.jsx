import { useEffect, useState } from "react";

const ThemeToggle = () => {
  const [darkMode, setDarkMode] = useState(
    localStorage.getItem("theme") === "dark"
  );

  useEffect(() => {
    document.body.classList.toggle("dark", darkMode);
    localStorage.setItem("theme", darkMode ? "dark" : "light");
  }, [darkMode]);

  return (
    <button
      onClick={() => setDarkMode(!darkMode)}
      style={{
        padding: "10px 16px",
        borderRadius: "999px",
        border: "none",
        background: darkMode ? "#818cf8" : "#6366f1",
        color: "#fff",
        fontWeight: 600,
        marginBottom: "20px",
      }}
    >
      {darkMode ? "🌙 Dark Mode" : "☀️ Light Mode"}
    </button>
  );
};

export default ThemeToggle;