import { useEffect, useState } from "react";

export default function TimerDisplay() {
  const [timeLeft, setTimeLeft] = useState(30);
  const [signal, setSignal] = useState("RED");

  useEffect(() => {
    const timer = setInterval(() => {
      setTimeLeft((prev) => (prev > 0 ? prev - 1 : 0));
    }, 1000);
    return () => clearInterval(timer);
  }, []);

  return (
    <div style={{ textAlign: "center", margin: "2rem" }}>
      <h3>Current Signal: {signal}</h3>
      <h1 style={{ fontSize: "4rem" }}>{timeLeft}s</h1>
    </div>
  );
}
