import { useEffect, useState } from "react";
import api from "../services/api";

function Companies() {
  const [companies, setCompanies] = useState([]);

  const [companyName, setCompanyName] = useState("");
  const [industry, setIndustry] = useState("");
  const [country, setCountry] = useState("");

  const [editingId, setEditingId] = useState(null);

  const [searchTerm, setSearchTerm] = useState("");

  useEffect(() => {
    fetchCompanies();
  }, []);

  const fetchCompanies = async () => {
    try {
      const res = await api.get("/companies");
      setCompanies(res.data);
    } catch (error) {
      console.error(error);
    }
  };

  const searchCompanies = async () => {
    try {
      if (searchTerm.trim() === "") {
        fetchCompanies();
        return;
      }

      const res = await api.get(
        `/companies/search?company_name=${searchTerm}`
      );

      setCompanies(res.data);
    } catch (error) {
      console.error(error);
      alert("Search Failed");
    }
  };

  const addCompany = async () => {
    try {
      if (!companyName || !industry || !country) {
        alert("All fields are required");
        return;
      }

      await api.post("/companies", {
        company_name: companyName,
        industry,
        country,
      });

      setCompanyName("");
      setIndustry("");
      setCountry("");

      fetchCompanies();
    } catch (error) {
      console.error(error);
      alert("Add Company Failed");
    }
  };

  const editCompany = (company) => {
    setEditingId(company.id);
    setCompanyName(company.company_name);
    setIndustry(company.industry);
    setCountry(company.country);
  };

  const updateCompany = async () => {
    try {
      await api.put(`/companies/${editingId}`, {
        company_name: companyName,
        industry,
        country,
      });

      setEditingId(null);
      setCompanyName("");
      setIndustry("");
      setCountry("");

      fetchCompanies();
    } catch (error) {
      console.error(error);
      alert("Update Failed");
    }
  };

  const deleteCompany = async (id) => {
    try {
      await api.delete(`/companies/${id}`);
      fetchCompanies();
    } catch (error) {
      console.error(error);
      alert("Delete Failed");
    }
  };

  const exportCSV = () => {
    window.open(
      "http://127.0.0.1:8000/companies/export/csv",
      "_blank"
    );
  };

  const exportExcel = () => {
    window.open(
      "http://127.0.0.1:8000/companies/export/excel",
      "_blank"
    );
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>🏢 Companies Management</h1>

      <div
        style={{
          display: "flex",
          gap: "10px",
          marginBottom: "20px",
        }}
      >
        <button
          onClick={() => (window.location.href = "/dashboard")}
        >
          Dashboard
        </button>

        <button
          onClick={() => (window.location.href = "/companies")}
        >
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

      <h3>Total Companies: {companies.length}</h3>

      <hr />

      <h3>🔍 Search Company</h3>

      <input
        type="text"
        placeholder="Search Company"
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
        style={{ padding: "8px", width: "250px" }}
      />

      <button
        onClick={searchCompanies}
        style={{
          marginLeft: "10px",
          padding: "8px 15px",
        }}
      >
        Search
      </button>

      <button
        onClick={fetchCompanies}
        style={{
          marginLeft: "10px",
          padding: "8px 15px",
        }}
      >
        Show All
      </button>

      <hr />

      <button
        onClick={exportCSV}
        style={{
          backgroundColor: "#36A2EB",
          color: "white",
          padding: "10px",
          border: "none",
          marginRight: "10px",
          cursor: "pointer",
        }}
      >
        Export CSV
      </button>

      <button
        onClick={exportExcel}
        style={{
          backgroundColor: "#4CAF50",
          color: "white",
          padding: "10px",
          border: "none",
          cursor: "pointer",
        }}
      >
        Export Excel
      </button>

      <hr />

      <div
        style={{
          border: "1px solid #ddd",
          padding: "20px",
          borderRadius: "10px",
          marginBottom: "20px",
        }}
      >
        <h3>
          {editingId ? "✏️ Edit Company" : "➕ Add Company"}
        </h3>

        <input
          type="text"
          placeholder="Company Name"
          value={companyName}
          onChange={(e) => setCompanyName(e.target.value)}
          style={{
            width: "300px",
            padding: "10px",
          }}
        />

        <br />
        <br />

        <input
          type="text"
          placeholder="Industry"
          value={industry}
          onChange={(e) => setIndustry(e.target.value)}
          style={{
            width: "300px",
            padding: "10px",
          }}
        />

        <br />
        <br />

        <input
          type="text"
          placeholder="Country"
          value={country}
          onChange={(e) => setCountry(e.target.value)}
          style={{
            width: "300px",
            padding: "10px",
          }}
        />

        <br />
        <br />

        {editingId ? (
          <button
            onClick={updateCompany}
            style={{
              backgroundColor: "#FF9800",
              color: "white",
              padding: "10px 20px",
              border: "none",
              cursor: "pointer",
            }}
          >
            Update Company
          </button>
        ) : (
          <button
            onClick={addCompany}
            style={{
              backgroundColor: "#4CAF50",
              color: "white",
              padding: "10px 20px",
              border: "none",
              cursor: "pointer",
            }}
          >
            Add Company
          </button>
        )}
      </div>

      <table
        border="1"
        cellPadding="10"
        style={{
          width: "100%",
          borderCollapse: "collapse",
        }}
      >
        <thead>
          <tr
            style={{
              backgroundColor: "#36A2EB",
              color: "white",
            }}
          >
            <th>ID</th>
            <th>Company</th>
            <th>Industry</th>
            <th>Country</th>
            <th>Actions</th>
          </tr>
        </thead>

        <tbody>
          {companies.map((company) => (
            <tr key={company.id}>
              <td>{company.id}</td>
              <td>{company.company_name}</td>
              <td>{company.industry}</td>
              <td>{company.country}</td>

              <td>
                <button
                  onClick={() => editCompany(company)}
                  style={{
                    backgroundColor: "#4CAF50",
                    color: "white",
                    border: "none",
                    padding: "5px 10px",
                    marginRight: "10px",
                    cursor: "pointer",
                  }}
                >
                  Edit
                </button>

                <button
                  onClick={() => deleteCompany(company.id)}
                  style={{
                    backgroundColor: "#f44336",
                    color: "white",
                    border: "none",
                    padding: "5px 10px",
                    cursor: "pointer",
                  }}
                >
                  Delete
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Companies;