import axios from "axios";

const api = axios.create({
  baseURL: "https://ai-business-intelligence-api.onrender.com",
});

export default api;