// app.js
function toggleModal() {
  const modal = document.getElementById("loginModal");
  if (modal.style.display === "flex") {
    modal.style.display = "none";
  } else {
    modal.style.display = "flex";
  }
}

window.onclick = function(event) {
  const modal = document.getElementById("loginModal");
  if (event.target === modal) {
    modal.style.display = "none";
  }
}

async function startTest() {
  document.getElementById("result").style.display = "none";
  
  const testAgainBtn = document.getElementById("testAgainBtn");
  if (testAgainBtn) {
    testAgainBtn.style.opacity = "0";
    setTimeout(() => {
      testAgainBtn.style.display = "none";
    }, 300);
  }

  // --- SENIOR DEV LOGIC: Scenario Randomizer ---
  // This picks a random network condition so the AI can show different scores
  const rand = Math.random();
  let dlRange, ulRange, pingVal, lossVal;

  if (rand > 0.66) { 
    // SCENARIO: Excellent (Fiber/5G)
    dlRange = 200 + Math.random() * 150; // 200-350 Mbps
    ulRange = 80 + Math.random() * 40;   // 80-120 Mbps
    pingVal = 5 + Math.random() * 10;    // 5-15 ms
    lossVal = 0;                         // 0% loss
  } else if (rand > 0.33) {
    // SCENARIO: Moderate (Standard Broadband)
    dlRange = 40 + Math.random() * 40;   // 40-80 Mbps
    ulRange = 10 + Math.random() * 15;   // 10-25 Mbps
    pingVal = 30 + Math.random() * 40;   // 30-70 ms
    lossVal = Math.floor(Math.random() * 2); // 0-1% loss
  } else {
    // SCENARIO: Poor (Congested/Weak Signal)
    dlRange = 2 + Math.random() * 8;     // 2-10 Mbps
    ulRange = 0.5 + Math.random() * 3;   // 0.5-3.5 Mbps
    pingVal = 120 + Math.random() * 200; // 120-320 ms
    lossVal = 3 + Math.floor(Math.random() * 5); // 3-8% loss
  }

  // --- Start Running the Visual Meter ---
  let download = await runMeter(dlRange, "Testing Download...");
  document.getElementById("download").innerText = download.toFixed(1);

  await delay(500);

  let upload = await runMeter(ulRange, "Testing Upload...");
  document.getElementById("upload").innerText = upload.toFixed(1);

  await delay(500);

  document.getElementById("phase").innerText = "Testing Ping...";
  let ping = pingVal;
  document.getElementById("ping").innerText = ping.toFixed(0);

  await delay(800);

  const data = {
    download: Math.floor(download),
    upload: Math.floor(upload),
    ping: Math.floor(ping),
    jitter: 5 + Math.floor(Math.random() * 5),
    users_connected: 10 + Math.floor(Math.random() * 30),
    signal_strength: -40 - Math.floor(Math.random() * 20),
    packet_loss: lossVal,
    time_of_day: getTimeOfDay(),
    location_type: "hotel"
  };

  console.log("Sending to AI:", data);

  try {
    const result = await sendToBackend(data);

    if (!result) return;

    console.log("AI Result:", result);

    document.getElementById("result").style.display = "flex";

    document.getElementById("score").innerText =
      "Score: " + (result.trust_score || "--");

    document.getElementById("status").innerText =
      result.status || "No status";

    document.getElementById("recommendation").innerText =
      result.recommendation || "No recommendation";

    document.getElementById("barFill").style.width =
      (result.trust_score || 0) + "%";

    document.getElementById("phase").innerText = "Completed ✅";

    if (testAgainBtn) {
      testAgainBtn.style.display = "inline-block";
      setTimeout(() => {
        testAgainBtn.style.opacity = "1";
      }, 50); 
    }

  } catch (error) {
    console.error("ERROR:", error);
    alert("Connection failed ❌");
  }
}