import { useState } from "react";
import { reportDamage } from "../services/api";

export default function ReportDamage() {
  const [location, setLocation] = useState("");
  const [description, setDescription] = useState("");
  const [status, setStatus] = useState("");

  const handleSubmit = async () => {
    const res = await reportDamage(location, description);
    setStatus(res.message || "Error reporting damage");
    setLocation("");
    setDescription("");
  };

  return (
    <div style={{ margin: "2rem" }}>
      <h3>🛠 Report Damaged Road</h3>
      <input
        placeholder="Enter Location"
        value={location}
        onChange={(e) => setLocation(e.target.value)}
      />
      <input
        placeholder="Enter Description"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
      />
      <button onClick={handleSubmit}>Submit Report</button>
      <p>{status}</p>
    </div>
  );
}
