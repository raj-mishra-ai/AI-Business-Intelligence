import { useState } from "react";
import { Link } from "react-router-dom";
import api from "../services/api";


function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const loginUser = async () => {
    try {
      const formData = new URLSearchParams();

      formData.append("username", email);
      formData.append("password", password);

      const res = await api.post("/login", formData);

      localStorage.setItem(
        "access_token",
        res.data.access_token
      );

      alert("Login Successful");

      window.location.href = "/companies";
    } catch (error) {
      console.error(error);
      alert("Invalid Email or Password");
    }
  };

  return (
    <div className="login-container">

      


      

      <div className="login-card">

        <h1 className="logo">
          AI Business Intelligence
        </h1>

        <p className="subtitle">
          Smart Insights. Better Decisions.
        </p>

        <h2 className="welcome">
          Welcome Back 👋
        </h2>

        <input
          type="email"
          placeholder="Enter Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />

        <input
          type="password"
          placeholder="Enter Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />

        <button onClick={loginUser}>
          Login
        </button>

        <p className="register-text">
          Don't have an account?
          <Link to="/register"> Register</Link>
        </p>

      </div>

    </div>
  );
}

export default Login;