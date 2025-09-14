import "./App.css";

function App() {
  return (
    <div>
      {/* Navbar */}
      <nav className="navbar">
        <h2 className="logo">SafeSign</h2>
        <ul className="nav-links">
          <li>Home</li>
          <li>Features</li>
          <li>Contact</li>
        </ul>
      </nav>

      {/* Hero Section */}
      <section className="hero">
        <h1>Welcome to SafeSign</h1>
        <p>Your solution for amazing experiences.</p>
        <button className="cta-btn">Get Started</button>
      </section>

      {/* Features */}
      <section className="features">
        <div className="feature-card">🚀 Fast</div>
        <div className="feature-card">🔒 Secure</div>
        <div className="feature-card">⚡ Easy to Use</div>
      </section>

      {/* Footer */}
      <footer>
        <p>© 2025 SafeSign. All rights reserved.</p>
      </footer>
    </div>
  );
}

export default App;





