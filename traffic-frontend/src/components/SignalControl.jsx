import { useState } from "react";
import { updateSignal } from "../services/api";

export default function SignalControl() {
  const [status, setStatus] = useState("");

  const handleSignal = async (color, duration) => {
    const res = await updateSignal(color, duration);
    setStatus(res.message || "Error updating signal");
  };

  return (
    <div style={{ margin: "2rem" }}>
      <h3>Control Traffic Signal</h3>
      <button onClick={() => handleSignal("RED", 30)}>🔴 Red (30s)</button>
      <button onClick={() => handleSignal("YELLOW", 10)}>🟡 Yellow (10s)</button>
      <button onClick={() => handleSignal("GREEN", 30)}>🟢 Green (30s)</button>
      <p>{status}</p>
    </div>
  );
}
