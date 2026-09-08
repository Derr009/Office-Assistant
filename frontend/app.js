const form = document.querySelector("#ask-form");
const questionInput = document.querySelector("#question");
const employeeInput = document.querySelector("#employee-id");
const messages = document.querySelector("#messages");
const sendButton = form.querySelector("button[type=submit]");

function addMessage(role, text, label) {
  const article = document.createElement("article");
  article.className = `message ${role}-message`;
  article.innerHTML = role === "assistant"
    ? `<div class="avatar">DT</div><div class="message-body"><span class="message-label">${label}</span><p></p><time>Just now</time></div>`
    : `<div class="message-body"><span class="message-label">You</span><p></p><time>Just now</time></div>`;
  article.querySelector("p").textContent = text;
  messages.appendChild(article);
  article.scrollIntoView({ behavior: "smooth", block: "nearest" });
  return article;
}

function setLoading(isLoading) {
  sendButton.disabled = isLoading;
  sendButton.querySelector("span:first-child").textContent = isLoading ? "Thinking" : "Send";
}

async function askQuestion(question) {
  const trimmedQuestion = question.trim();
  if (!trimmedQuestion) return;

  addMessage("user", trimmedQuestion);
  questionInput.value = "";
  questionInput.style.height = "auto";
  setLoading(true);
  const loadingMessage = addMessage("assistant", "Looking through the policy library...", "DT Assistant");
  loadingMessage.classList.add("loading");

  try {
    const response = await fetch("/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        question: trimmedQuestion,
        employee_id: employeeInput.value.trim() || null
      })
    });
    if (!response.ok) throw new Error("The assistant could not answer right now.");
    const data = await response.json();
    loadingMessage.remove();
    addMessage("assistant", data.answer || "I couldn't find an answer.", "DT Assistant");
  } catch (error) {
    loadingMessage.remove();
    addMessage("assistant", error.message, "Connection issue");
  } finally {
    setLoading(false);
    questionInput.focus();
  }
}

form.addEventListener("submit", (event) => {
  event.preventDefault();
  askQuestion(questionInput.value);
});

document.querySelectorAll("[data-question]").forEach((button) => {
  button.addEventListener("click", () => {
    questionInput.value = button.dataset.question;
    questionInput.focus();
  });
});

questionInput.addEventListener("input", () => {
  questionInput.style.height = "auto";
  questionInput.style.height = `${Math.min(questionInput.scrollHeight, 110)}px`;
});
