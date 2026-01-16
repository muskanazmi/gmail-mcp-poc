import { useState } from "react";
import React from "react";


const BACKEND_URL = import.meta.env.VITE_BACKEND_URL + "/chat";

export default function App() {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    setLoading(true);
    setResponse("");

    try {
      const res = await fetch(BACKEND_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message }),
      });

      const data = await res.json();
      setResponse(data.reply || JSON.stringify(data, null, 2));
    } catch (err) {
      setResponse("Error connecting to backend: " + err.message);
    }

    setLoading(false);
  };

  return (
    <div style={{ padding: 30 }}>
      <h2>Gmail MCP Chat (PoC)</h2>

      <textarea
        rows={4}
        style={{ width: "100%" }}
        placeholder="Ask something like: Search emails from supabase"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />

      <button onClick={sendMessage} disabled={loading}>
        {loading ? "Sending..." : "Send"}
      </button>

      <pre style={{ marginTop: 20 }}>{response}</pre>
    </div>
  );
}


// export default function App() {
//   return <h1>Hello Vite + React!</h1>;
// }
