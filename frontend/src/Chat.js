import React, { useState } from 'react';

function Chat() {
  const [messages, setMessages] = useState([]);
  const [userInput, setUserInput] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSend = async () => {
    if (!userInput) return;
    
    const userMessage = { sender: 'user', text: userInput };
    setMessages([...messages, userMessage]);
    setLoading(true);

    try {
      const response = await fetch("http://localhost:8000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ user_id: "default_user", message: userInput })
      });
      const data = await response.json();
      
      const botMessage = { sender: 'bot', text: data.response };
      setMessages(prev => [...prev, botMessage]);
    } catch (error) {
      console.error("Error sending message:", error);
    }
    
    setUserInput("");
    setLoading(false);
  };

  return (
    <div>
      <div style={{ border: "1px solid #ccc", padding: "1rem", height: "400px", overflowY: "scroll" }}>
        {messages.map((msg, idx) => (
          <div key={idx} style={{ margin: "0.5rem 0" }}>
            <strong>{msg.sender}:</strong> {msg.text}
          </div>
        ))}
        {loading && <div>Loading...</div>}
      </div>
      <input 
        type="text" 
        value={userInput} 
        onChange={e => setUserInput(e.target.value)} 
        placeholder="Type your message..."
      />
      <button onClick={handleSend}>Send</button>
    </div>
  );
}

export default Chat;
