import { useEffect, useState } from "react";
import api from "../services/api";

import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  ArcElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";

import { Bar, Pie } from "react-chartjs-2";

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  ArcElement,
  Title,
  Tooltip,
  Legend
);

function Dashboard() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetchDashboard();
  }, []);

  const fetchDashboard = async () => {
  try {
    const res = await api.get("/companies/dashboard");

    console.log("Dashboard Data:", res.data);

    setData(res.data);
  } catch (error) {
    console.error("Dashboard Error:", error);
    alert("Dashboard Load Failed");
  }
};

  if (!data) {
    return <h2>Loading...</h2>;
  }

  const industryData = {
    labels: data.industry_analytics.map(
      (item) => item.industry
    ),
    datasets: [
      {
        label: "Companies",
        data: data.industry_analytics.map(
          (item) => item.company_count
        ),
        backgroundColor: [
          "#FF6384",
          "#36A2EB",
          "#FFCE56",
          "#4BC0C0",
          "#9966FF",
          "#FF9F40",
        ],
      },
    ],
  };

  const countryData = {
    labels: data.country_analytics.map(
      (item) => item.country
    ),
    datasets: [
      {
        label: "Companies",
        data: data.country_analytics.map(
          (item) => item.company_count
        ),
        backgroundColor: [
          "#FF6384",
          "#36A2EB",
          "#FFCE56",
          "#4BC0C0",
          "#9966FF",
          "#FF9F40",
          "#8BC34A",
          "#E91E63",
        ],
      },
    ],
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1 style={{ textAlign: "center" }}>
        📊 Business Dashboard
      </h1>

      <div
  style={{
    display: "flex",
    gap: "15px",
    marginBottom: "20px",
  }}
>
  <button onClick={() => window.location.href = "/dashboard"}>
    Dashboard
  </button>

  <button onClick={() => window.location.href = "/companies"}>
    Companies
  </button>

  <button
    onClick={() => {
      localStorage.removeItem("access_token");
      window.location.href = "/login";
    }}
  >
    Logout
  </button>
</div>

      <div
        style={{
          display: "flex",
          gap: "20px",
          flexWrap: "wrap",
          marginTop: "20px",
        }}
      >
        <div
          style={{
            background: "#0098fd",
            color: "white",
            padding: "20px",
            borderRadius: "12px",
            minWidth: "220px",
            textAlign: "center",
          }}
        >
          <h3>Total Companies</h3>
          <h1>{data.statistics.total_companies}</h1>
        </div>

        <div
          style={{
            background: "#4BC0C0",
            color: "white",
            padding: "20px",
            borderRadius: "12px",
            minWidth: "220px",
            textAlign: "center",
          }}
        >
          <h3>Total Industries</h3>
          <h1>{data.statistics.total_industries}</h1>
        </div>

        <div
          style={{
            background: "#FF6384",
            color: "white",
            padding: "20px",
            borderRadius: "12px",
            minWidth: "220px",
            textAlign: "center",
          }}
        >
          <h3>Total Countries</h3>
          <h1>{data.statistics.total_countries}</h1>
        </div>
      </div>

      <hr style={{ margin: "30px 0" }} />

      <h2>📈 Industry Analytics</h2>

      <div
        style={{
          background: "#fff",
          padding: "20px",
          borderRadius: "12px",
          boxShadow: "0px 2px 10px rgba(0,0,0,0.1)",
        }}
      >
        <Bar data={industryData} />
      </div>

      <hr style={{ margin: "30px 0" }} />

      <h2>🌍 Country Analytics</h2>

      <div
        style={{
          width: "500px",
          background: "#fff",
          padding: "20px",
          borderRadius: "12px",
          boxShadow: "0px 2px 10px rgba(0,0,0,0.1)",
        }}
      >
        <Pie data={countryData} />
      </div>
    </div>
  );
}

export default Dashboard;