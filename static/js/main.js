document.addEventListener("DOMContentLoaded", () => {
  const contactForm = document.getElementById("contactForm");
  const formStatus = document.getElementById("formStatus");

  if (contactForm && formStatus) {
    contactForm.addEventListener("submit", (event) => {
      event.preventDefault();

      if (!contactForm.checkValidity()) {
        contactForm.reportValidity();
        return;
      }

      formStatus.textContent =
        "Cảm ơn bạn đã liên hệ. " +
        "Chức năng gửi tin nhắn đang được hoàn thiện.";

      formStatus.classList.remove("d-none");
      contactForm.reset();
    });
  }

  const navbarElement = document.getElementById("mainNavbar");

  if (navbarElement && window.bootstrap) {
    const navbarLinks = navbarElement.querySelectorAll(".nav-link");

    navbarLinks.forEach((link) => {
      link.addEventListener("click", () => {
        if (!navbarElement.classList.contains("show")) {
          return;
        }

        const collapseInstance =
          window.bootstrap.Collapse.getOrCreateInstance(navbarElement);

        collapseInstance.hide();
      });
    });
  }
});
