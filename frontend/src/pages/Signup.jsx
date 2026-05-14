import { useState } from "react";
import API from "../api";
import { Link } from "react-router-dom";

function Signup() {

  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSignup = async () => {

    try {

      await API.post(
        `/auth/signup?name=${name}&email=${email}&password=${password}`
      );

      alert("Signup successful");

      setName("");
      setEmail("");
      setPassword("");

    } catch (error) {

      console.log(error);

      alert("Signup failed");
    } };

  return (

    <div style={containerStyle}>

      <div style={cardStyle}>

        <h2>Create Account</h2>

        <input
          style={inputStyle}
          placeholder="Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />

        <input
          style={inputStyle}
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
  <input
          style={inputStyle}
          placeholder="Password"
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />

        <button
          style={buttonStyle}
          onClick={handleSignup}
        >
          Signup
        </button>
<p style={{ textAlign: "center" }}>
  Already have an account?{" "}

  <Link to="/login">
    Login
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
  minHeight: "100vh",
  backgroundColor: "#f4f4f4"
};const cardStyle = {
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

export default Signup;