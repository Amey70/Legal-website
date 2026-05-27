import React, { useState } from "react";
import "./App.css";
import legalImg from "./assets/legalimage.jpg";
import Footer from "./Footer"; // ✅ Corrected path

function App() {
  const [darkMode, setDarkMode] = useState(false);

  return (
    <div className={darkMode ? "app dark" : "app"}>
      {/* Navbar */}
      <nav className="navbar">
        <div className="logo">Lexpopuli</div>

        <ul className="nav-links">
          <li><a href="#">Home</a></li>
          <li><a href="#">AI Legal Chatbot</a></li>
          <li><a href="#">Rights Visualizer</a></li>
          <li><a href="#">Document Simplifier</a></li>
        </ul>

        <div className="nav-buttons">
          <button className="dark-toggle" onClick={() => setDarkMode(!darkMode)}>
            {darkMode ? "☀️ Light" : "🌙 Dark"}
          </button>
          <button className="signin-btn">Sign In</button>
        </div>
      </nav>

      {/* Hero Section */}
      <section className="hero">
        <div className="hero-text">
          <h1>Simplifying Legal Knowledge for All Indians</h1>
          <p>
            LegalEase makes the justice system accessible through AI-powered
            tools, plain language explanations, and personalized guidance.
          </p>
          <div className="hero-buttons">
            <button className="primary-btn">Get Started Free</button>
            <button className="secondary-btn">Find Legal Help</button>
          </div>
        </div>
        <div className="hero-img">
          <img src={legalImg} alt="Legal illustration" />
        </div>
      </section>

      {/* ✅ Mission Section */}
      <section className="mission">
        <h2>Our Mission</h2>
        <p>
          We believe that legal knowledge should be accessible to everyone, not just those
          who can afford expensive lawyers. LegalEase uses AI and plain language to demystify
          the legal system, empowering citizens to understand and exercise their rights.
        </p>
      </section>

      {/* ✅ Footer */}
      <Footer />
    </div>
  );
}

export default App;
