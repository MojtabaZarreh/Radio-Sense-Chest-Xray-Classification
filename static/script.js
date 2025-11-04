const uploadBtn = document.getElementById("uploadBtn");
const fileInput = document.getElementById("fileInput");
const preview = document.getElementById("preview");
const gradcamImg = document.getElementById("gradcam-img");
const resultSection = document.getElementById("result-section");
const placeholder = document.getElementById("placeholder");
const predClass = document.getElementById("pred-class");
const predSummary = document.getElementById("pred-summary");
const aiText = document.getElementById("ai-text");

uploadBtn.addEventListener("click", () => fileInput.click());

fileInput.addEventListener("change", async (e) => {
  const file = e.target.files[0];
  if (!file) return;

  const imgUrl = URL.createObjectURL(file);
  preview.src = imgUrl;
  preview.classList.remove("hidden");
  gradcamImg.classList.add("hidden");
  placeholder.classList.add("hidden");

  const formData = new FormData();
  formData.append("file", file);

  uploadBtn.textContent = "🧠 Analyzing...";
  uploadBtn.disabled = true;

  try {
    const res = await fetch("http://127.0.0.1:8000/predict", {
      method: "POST",
      body: formData,
    });

    const data = await res.json();

    setTimeout(() => {
      resultSection.classList.remove("hidden");
      predClass.textContent = data.class;
      predSummary.textContent = data.summary;

      gradcamImg.src = data.gradcam_url;
      gradcamImg.classList.remove("hidden");

      aiText.textContent = "";
      typeText(data.details, aiText);

      uploadBtn.textContent = "📤 Upload Another";
      uploadBtn.disabled = false;
    }, 5000); 
  } catch (err) {
    alert("❌ Error connecting to server.");
    uploadBtn.textContent = "📤 Try Again";
    uploadBtn.disabled = false;
  }
});

function typeText(text, element, speed = 25) {
  let i = 0;
  element.textContent = "";
  const interval = setInterval(() => {
    element.textContent += text.charAt(i);
    i++;
    if (i >= text.length) clearInterval(interval);
  }, speed);
}
