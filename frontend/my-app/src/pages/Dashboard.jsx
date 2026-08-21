import { useEffect, useState } from "react";
import api from "../services/api";

function Dashboard() {
  const [stats, setStats] = useState({
    total_companies: 0,
    total_industries: 0,
    total_countries: 0,
    average_companies_per_country: 0,
  });

  useEffect(() => {
    const fetchStats = async () => {
      try {
        const res = await api.get("/companies/statistics");
        console.log("Dashboard Data:", res.data);
        setStats(res.data);
      } catch (error) {
        console.error(error);
      }
    };

    fetchStats();
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>Dashboard</h1>

      <h3>Total Companies: {stats.total_companies}</h3>

      <h3>Total Industries: {stats.total_industries}</h3>

      <h3>Total Countries: {stats.total_countries}</h3>

      <h3>
        Average Companies Per Country:
        {" "}
        {stats.average_companies_per_country}
      </h3>
    </div>
  );
}

export default Dashboard;