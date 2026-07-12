const contactButton = document.getElementById("contactButton");
const contactMessage = document.getElementById("contactMessage");

contactButton.addEventListener("click", () => {
  contactMessage.textContent =
    "Bạn có thể liên hệ với tôi qua email: your-email@example.com";
});
