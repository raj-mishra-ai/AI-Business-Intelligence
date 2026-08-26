import { useEffect, useState } from "react";
import api from "../services/api";

function BusinessReport() {
  const [report, setReport] = useState(null);

  useEffect(() => {
    fetchReport();
  }, []);

  const fetchReport = async () => {
    try {
      const res = await api.get("/companies/reports/business");

      console.log("Business Report:", res.data);

      setReport(res.data);
    } catch (error) {
      console.error(error);
      alert("Report Load Failed");
    }
  };

  if (!report) {
    return <h2>Loading Report...</h2>;
  }

  return (
    <div style={{ padding: "20px" }}>
      <h1>📈 Business Report</h1>

      <pre>
        {JSON.stringify(report, null, 2)}
      </pre>
    </div>
  );
}

export default BusinessReport;