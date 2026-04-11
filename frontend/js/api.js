async function sendToBackend(data) {

  const response = await fetch("http://127.0.0.1:8000/recommend", {
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