import Navbar from "./components/Navbar";
import SignalControl from "./components/SignalControl";
import TimerDisplay from "./components/TimerDisplay";
import Alerts from "./components/Alerts";
import ReportDamage from "./components/ReportDamage"; // ✅ NEW

function App() {
  return (
    <div>
      <Navbar />
      <SignalControl />
      <TimerDisplay />
      <Alerts />
      <ReportDamage /> {/* ✅ NEW */}
    </div>
  );
}

export default App;
