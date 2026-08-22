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
      <button
  onClick={() => {
    localStorage.removeItem("token");
    window.location.href = "/login";
  }}
>
  Logout
</button>

      <hr />

      <h2>Statistics</h2>

      <p>
        <b>Total Companies:</b>{" "}
        {data.statistics.total_companies}
      </p>

      <p>
        <b>Total Industries:</b>{" "}
        {data.statistics.total_industries}
      </p>

      <p>
        <b>Total Countries:</b>{" "}
        {data.statistics.total_countries}
      </p>

      <p>
        <b>Average Companies Per Country:</b>{" "}
        {data.statistics.average_companies_per_country}
      </p>

      <hr />

      <h2>Industry Analytics</h2>

      {data.industry_analytics.map((item, index) => (
        <p key={index}>
          {item.industry} : {item.company_count}
        </p>
      ))}

      <hr />

      <h2>Country Analytics</h2>

      {data.country_analytics.map((item, index) => (
        <p key={index}>
          {item.country} : {item.company_count}
        </p>
      ))}
    </div>
  );
}

export default Dashboard;