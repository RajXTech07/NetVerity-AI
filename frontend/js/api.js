async function sendToBackend(data) {

  const response = await fetch("https://netverity-ai.onrender.com/recommend", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(data)
  });

  if (!response.ok) {
    const err = await response.text();
    console.error("Backend Error:", err);
    alert("Backend error ❌");
    return null;
  }

  return await response.json();
}