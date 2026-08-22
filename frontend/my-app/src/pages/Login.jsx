import { useState } from "react";
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
    <div
      style={{
        height: "100vh",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        background: "#ffffff",
      }}
    >
      <div
        style={{
          width: "400px",
          padding: "30px",
          background: "white",
          borderRadius: "12px",
          boxShadow: "0 0 20px rgba(61, 2, 2, 0.1)",
        }}
      >
        <h1 
        style={{
             textAlign: "center",
             fontSize:"32px",
             marginbottom:"10px",
            }}
            >
          AI Business Intelligence
        </h1>

        <p style={{ textAlign: "center" }}>
          Login to continue
        </p>

        <input
          type="email"
          placeholder="Enter Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          style={{
            width: "100%",
            padding: "10px",
            marginTop: "10px",
          }}
        />

        <br />
        <br />

        <input
          type="password"
          placeholder="Enter Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          style={{
            width: "100%",
            padding: "10px",
          }}
        />

        <br />
        <br />

        <button
          onClick={loginUser}
          style={{
            width: "100%",
            padding: "12px",
            cursor: "pointer",
          }}
        >
          Login
        </button>

        <p
          style={{
            textAlign: "center",
            marginTop: "15px",
          }}
        >
          Don't have an account?
          <a href="/register"> Register</a>
        </p>
      </div>
    </div>
  );
}

export default Login;