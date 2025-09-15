<<<<<<< HEAD
import { useState } from "react";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [extractedText, setExtractedText] = useState("");
  const [simplifiedText, setSimplifiedText] = useState("");

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) {
      alert("Please select a file first");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch("http://127.0.0.1:8000/uploadfile", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();
      console.log(data); // extracted_text and simplified_text

      // Save to state to display in UI
      setExtractedText(data.extracted_text);
      setSimplifiedText(data.simplified_text);
    } catch (error) {
      console.error("Upload error:", error);
    }
  };

=======
import "./App.css";

function App() {
>>>>>>> aa166ea661b14646fd3ff2d7a94066c76e2c0679
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
<<<<<<< HEAD

        {/* File Upload */}
        <input type="file" onChange={handleFileChange} />
        <button className="cta-btn" onClick={handleUpload}>
          Upload & Simplify
        </button>
      </section>

      {/* Display results */}
      {extractedText && (
        <section className="results">
          <h3>Extracted Text:</h3>
          <p>{extractedText}</p>

          <h3>Simplified Text:</h3>
          <p>{simplifiedText}</p>
        </section>
      )}

=======
        <button className="cta-btn">Get Started</button>
      </section>

>>>>>>> aa166ea661b14646fd3ff2d7a94066c76e2c0679
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

<<<<<<< HEAD
export default App;
=======
export default App;





>>>>>>> aa166ea661b14646fd3ff2d7a94066c76e2c0679
