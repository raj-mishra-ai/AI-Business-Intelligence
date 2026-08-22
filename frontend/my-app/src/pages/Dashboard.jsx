import { useEffect, useState } from "react";
import api from "../services/api";

function Dashboard() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetchDashboard();
  }, []);

  const fetchDashboard = async () => {
    try {
      const res = await api.get("/companies/dashboard");
      setData(res.data);
    } catch (error) {
      console.error(error);
      alert("Dashboard Load Failed");
    }
  };

  if (!data) {
    return <h2>Loading...</h2>;
  }

  return (
    <div style={{ padding: "20px" }}>
      <h1>Business Dashboard</h1>

      <div style={{ display: "flex", gap: "20px", flexWrap: "wrap" }}>
        <div style={{ border: "1px solid #ccc", padding: "15px" }}>
          <h3>Total Companies</h3>
          <h2>{data.statistics.total_companies}</h2>
        </div>

        <div style={{ border: "1px solid #ccc", padding: "15px" }}>
          <h3>Total Industries</h3>
          <h2>{data.statistics.total_industries}</h2>
        </div>

        <div style={{ border: "1px solid #ccc", padding: "15px" }}>
          <h3>Total Countries</h3>
          <h2>{data.statistics.total_countries}</h2>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;