const API_URL = "http://127.0.0.1:5000/api"; // Flask backend

// Update traffic signal
export const updateSignal = async (signal, duration) => {
  const res = await fetch(`${API_URL}/traffic/update`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ signal, duration }),
  });
  return res.json();
};

// Send ambulance alert
export const sendAmbulanceAlert = async (hospital, message) => {
  const res = await fetch(`${API_URL}/ambulance/alert`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ hospital, message }),
  });
  return res.json();
};

// Report damaged road
// Report damaged road
export const reportDamage = async (location, description) => {
  const res = await fetch(`${API_URL}/damage/report`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ location, description }),
  });
  return res.json();
};
