function delay(ms) {
  return new Promise(res => setTimeout(res, ms));
}

async function runMeter(targetSpeed, label) {

  document.getElementById("phase").innerText = label;

  let speed = 0;

  while (speed < targetSpeed) {
    speed += Math.random() * 5;
    document.getElementById("speed").innerText = speed.toFixed(1);
    await delay(50);
  }

  return speed;
}

function getTimeOfDay() {
  const hour = new Date().getHours();
  if (hour < 12) return "morning";
  if (hour < 18) return "afternoon";
  return "evening";
}