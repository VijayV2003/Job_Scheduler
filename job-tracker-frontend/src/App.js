import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [resume, setResume] = useState(null);
  const [jobRole, setJobRole] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleResumeChange = (e) => {
    setResume(e.target.files[0]);
  };

  const handleJobRoleChange = (e) => {
    setJobRole(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError("");
    setResult(null);

    const formData = new FormData();
    formData.append("resume", resume);
    formData.append("job_role", jobRole);

    try {
      const response = await axios.post(
        "http://localhost:8010/process_resume/",
        formData,
        {
          headers: { "Content-Type": "multipart/form-data" },
        }
      );
      setResult(response.data);
    } catch (error) {
      console.error("Error:", error);
      setError("Failed to process resume. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <header className="header">
        <h1>AI Resume Matcher DEVOPS CLASS</h1>
        <p>Match your resume against top job roles and get insights!</p>
      </header>

      <div className="form-container">
        <form onSubmit={handleSubmit} className="form">
          {/* Resume Upload */}
          <div className="input-group">
            <label>upload your resumes (PDF):</label>
            <input type="file" accept=".pdf" onChange={handleResumeChange} required />
          </div>

          {/* Job Role Selection */}
          <div className="input-group">
            <label>Select Job Role:</label>
            <select value={jobRole} onChange={handleJobRoleChange} required>
              <option value="">-- Choose a Role --</option>
              <option value="Data Scientist">Data Scientist</option>
              <option value="Data Analyst">Data Analyst</option>
              <option value="Machine Learning Engineer">Machine Learning Engineer</option>
              <option value="AI Specialist">AI Specialist</option>
            </select>
          </div>

          {/* Submit Button */}
          <button type="submit" className="btn" disabled={loading}>
            {loading ? "Processing..." : "Submit"}
          </button>
        </form>

        {/* Error Message */}
        {error && <p className="error">{error}</p>}

        {/* Result Section */}
        {result && (
          <div className="results">
            <h2>Results for: {result.job_role}</h2>

            {/* Match Score */}
            <div className="score-box">
              Match Score: {result.similarity_score }%
            </div>

            {/* Matching Skills */}
            <div className="matching-box">
              <h3>Matching Skills:</h3>
              {result.matching_skills && result.matching_skills.length > 0 ? (
                <ul className="skills-list">
                  {result.matching_skills.map((skill, index) => (
                    <li key={index}>{skill}</li>
                  ))}
                </ul>
              ) : (
                <p>No matching skills found.</p>
              )}
            </div>

            {/* Missing Skills */}
            <div className="missing-box">
              <h3>Missing Skills:</h3>
              {result.missing_skills && result.missing_skills.length > 0 ? (
                <ul className="skills-list">
                  {result.missing_skills.map((skill, index) => (
                    <li key={index}>{skill}</li>
                  ))}
                </ul>
              ) : (
                <p>No missing skills!</p>
              )}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
