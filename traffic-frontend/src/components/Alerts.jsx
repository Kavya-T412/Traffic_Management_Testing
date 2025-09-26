import { useState } from "react";
import { sendAmbulanceAlert } from "../services/api";

export default function Alerts() {
  const [hospital, setHospital] = useState("");
  const [message, setMessage] = useState("");
  const [status, setStatus] = useState("");

  const sendAlert = async () => {
    const res = await sendAmbulanceAlert(hospital, message);
    setStatus(res.message || "Error sending alert");
  };

  return (
    <div style={{ margin: "2rem" }}>
      <h3>🚑 Send Ambulance Alert</h3>
      <input
        placeholder="Hospital Name"
        value={hospital}
        onChange={(e) => setHospital(e.target.value)}
      />
      <input
        placeholder="Message"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />
      <button onClick={sendAlert}>Send Alert</button>
      <p>{status}</p>
    </div>
  );
}
