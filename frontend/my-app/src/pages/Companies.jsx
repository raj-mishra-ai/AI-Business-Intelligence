import { useEffect, useState } from "react";
import api from "../services/api";

function Companies() {
  const [companies, setCompanies] = useState([]);

  const [companyName, setCompanyName] = useState("");
  const [industry, setIndustry] = useState("");
  const [country, setCountry] = useState("");

  const [editingId, setEditingId] = useState(null);
  const [isEditing, setIsEditing] = useState(false);

  const fetchCompanies = async () => {
    try {
      const res = await api.get("/companies");
      console.log("Companies Data:", res.data);
      setCompanies(res.data);
    } catch (error) {
      console.error("Fetch Error:", error);
    }
  };

  useEffect(() => {
    fetchCompanies();
  }, []);

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
    setIsEditing(true);

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

      setCompanyName("");
      setIndustry("");
      setCountry("");

      setEditingId(null);
      setIsEditing(false);

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

  return (
    <div style={{ padding: "20px" }}>
      <h1>Company Management</h1>

      <p>Total Companies: {companies.length}</p>

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

      {isEditing ? (
        <button onClick={updateCompany}>
          Update Company
        </button>
      ) : (
        <button onClick={addCompany}>
          Add Company
        </button>
      )}

      <hr />

      {companies.length === 0 ? (
        <p>No Companies Found</p>
      ) : (
        companies.map((company) => (
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
        ))
      )}
    </div>
  );
}

export default Companies;