import { useEffect, useState } from "react";
import api from "../services/api";

function Companies() {
  const [companies, setCompanies] = useState([]);

  const [companyName, setCompanyName] = useState("");
  const [industry, setIndustry] = useState("");
  const [country, setCountry] = useState("");

  const fetchCompanies = () => {
    api
      .get("/companies")
      .then((res) => setCompanies(res.data))
      .catch((err) => console.error(err));
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
      alert("Company already exists or request failed");
    }
  };

  const deleteCompany = async (id) => {
    try {
      await api.delete(`/companies/${id}`);
      fetchCompanies();
    } catch (error) {
      console.error(error);
      alert("Delete failed");
    }
  };

  return (
    <div>
      <h1>Companies</h1>

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

      <button onClick={addCompany}>
        Add Company
      </button>

      <hr />

      {companies.map((company) => (
        <div key={company.id}>
          <p>
            {company.company_name} | {company.industry} | {company.country}

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