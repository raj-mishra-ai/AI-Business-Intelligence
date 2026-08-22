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
      await api.post("/companies", {
        company_name: companyName,
        industry: industry,
        country: country,
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
        industry: industry,
        country: country,
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
      <h1>Companies Page</h1>

      <button
  onClick={() => {
    localStorage.removeItem("token");
    window.location.href = "/login";
  }}
>
  Logout
</button>

      <h3>Total Companies: {companies.length}</h3>

      <hr />

      <h3>Search Company</h3>

      <input
        type="text"
        placeholder="Search Company"
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
      />

      <button
        onClick={searchCompanies}
        style={{ marginLeft: "10px" }}
      >
        Search
      </button>

      <button
        onClick={fetchCompanies}
        style={{ marginLeft: "10px" }}
      >
        Show All
      </button>

      <hr />

      <button onClick={exportCSV}>
        Export CSV
      </button>

      <button
        onClick={exportExcel}
        style={{ marginLeft: "10px" }}
      >
        Export Excel
      </button>

      <hr />

      <h3>{editingId ? "Edit Company" : "Add Company"}</h3>

      <input
        type="text"
        placeholder="Company Name"
        value={companyName}
        onChange={(e) => setCompanyName(e.target.value)}
      />

      <br />
      <br />

      <input
        type="text"
        placeholder="Industry"
        value={industry}
        onChange={(e) => setIndustry(e.target.value)}
      />

      <br />
      <br />

      <input
        type="text"
        placeholder="Country"
        value={country}
        onChange={(e) => setCountry(e.target.value)}
      />

      <br />
      <br />

      {editingId ? (
        <button onClick={updateCompany}>
          Update Company
        </button>
      ) : (
        <button onClick={addCompany}>
          Add Company
        </button>
      )}

      <hr />

      {companies.map((company) => (
        <div key={company.id}>
          <p>
            <b>{company.company_name}</b> | {company.industry} |{" "}
            {company.country}

            <button
              onClick={() => editCompany(company)}
              style={{ marginLeft: "10px" }}
            >
              Edit
            </button>

            <button
              onClick={() => deleteCompany(company.id)}
              style={{ marginLeft: "10px" }}
            >
              Delete
            </button>
          </p>
        </div>
      ))}
    </div>
  );
}

export default Companies;