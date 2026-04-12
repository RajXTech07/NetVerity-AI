async function sendToBackend(data) {

  const response = await fetch("https://netverity-ai.onrender.com/recommend", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(data)
  });

// Ai response error handling
async function askAI(userMessage) {
    try {
        const response = await fetch("https://netverity-ai.onrender.com/ask-ai", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: userMessage })
        });

        const data = await response.json();
        return data.response;
    } catch (error) {
        console.error("AI Error:", error);
        return "Sorry, I'm having trouble connecting to my brain right now.";
    }
}

  if (!response.ok) {
    const err = await response.text();
    console.error("Backend Error:", err);
    alert("Backend error ❌");
    return null;
  }

  return await response.json();
}