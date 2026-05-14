import { Link } from "react-router-dom";
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import API from "../api";

function Login() {

  const navigate = useNavigate();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async () => {

    try {

      const response = await API.post(
        `/auth/login?email=${email}&password=${password}`
      );

      localStorage.setItem(
        "token",
        response.data.access_token
      );

      alert("Login successful");
      navigate("/");

    } catch (error) {

      console.log(error);

      alert("Login failed");
    }
  };

  return (

    <div style={containerStyle}>

      <div style={cardStyle}>

        <h1 style={{ marginBottom: "20px" }}>
          Team Task Manager
        </h1>

        <h2>Login</h2>

        <input
          style={inputStyle}
          placeholder="Email"
          onChange={(e) => setEmail(e.target.value)}
        /><input
          style={inputStyle}
          placeholder="Password"
          type="password"
          onChange={(e) => setPassword(e.target.value)}
        />

        <button
          style={buttonStyle}
          onClick={handleLogin}
        >
          Login
        </button>
<p style={{ textAlign: "center" }}>
  Don't have an account?{" "}

  <Link to="/signup">
    Signup
  </Link>
</p>
      </div>

    </div>
  );
}

const containerStyle = {
  display: "flex",
  justifyContent: "center",
  alignItems: "center",
  height: "100vh",
  backgroundColor: "#f4f4f4"
};
const cardStyle = {
  backgroundColor: "white",
  padding: "40px",
  borderRadius: "12px",
  boxShadow: "0px 0px 10px rgba(0,0,0,0.1)",
  width: "350px",
  display: "flex",
  flexDirection: "column",
  gap: "15px"
};

const inputStyle = {
  padding: "12px",
  borderRadius: "8px",
  border: "1px solid gray"
};

const buttonStyle = {
  padding: "12px",
  borderRadius: "8px",
  border: "none",
  backgroundColor: "#222",
  color: "white",
  cursor: "pointer",
  fontWeight: "bold"
};

export default Login;