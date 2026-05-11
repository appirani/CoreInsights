import { useState } from "react";
import axios from "axios";
import "../App.css";

function Analyzer() {
  const [input, setInput] = useState("");
  const [result, setResult] = useState("");
  const [chart, setChart] = useState("");

  const handleAnalyze = async () => {
    try {
      const res = await axios.post("http://127.0.0.1:5000/ask-data", {
        question: input,
      });

      if (res.data.response === "chart") {
        setChart("http://127.0.0.1:5000/chart");
        setResult("Chart generated:");
      } else {
        setResult(res.data.response);
        setChart("");
      }
    } catch (error) {
      setResult("Error connecting to backend");
    }
  };

  return (
    <div className="container">
      <h2>AI Data Analyst Dashboard</h2>

      <textarea
        rows="4"
        placeholder="Ask question about your data..."
        value={input}
        onChange={(e) => setInput(e.target.value)}
      />

      <button onClick={handleAnalyze}>Analyze</button>

      <h3>Result:</h3>
      <pre>{result}</pre>

      {chart && (
        <div>
          <h3>Chart:</h3>
          <img src={chart} alt="chart" width="600" />
        </div>
      )}
    </div>
  );
}

export default Analyzer;
