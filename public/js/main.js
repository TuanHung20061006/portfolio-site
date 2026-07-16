document.addEventListener("DOMContentLoaded", function () {
  setupMobileNavbar();
  setupContactForm();
});

function setupMobileNavbar() {
  const navLinks = document.querySelectorAll(".navbar-nav .nav-link");

  navLinks.forEach((link) => {
    link.addEventListener("click", function () {
      const navbarCollapse = document.querySelector(".navbar-collapse");

      if (navbarCollapse && navbarCollapse.classList.contains("show")) {
        bootstrap.Collapse.getOrCreateInstance(navbarCollapse).hide();
      }
    });
  });
}

function setupContactForm() {
  const contactForm = document.getElementById("contactForm");

  if (!contactForm) {
    return;
  }

  const formStatus = document.getElementById("formStatus");
  let submitButton = document.getElementById("submitButton");
  const submitButtonText = document.getElementById("submitButtonText");
  const submitSpinner = document.getElementById("submitSpinner");

  if (!formStatus) {
    return;
  }

  if (!submitButton) {
    submitButton = contactForm.querySelector('button[type="submit"]');
  }

  const defaultSubmitText = submitButtonText
    ? submitButtonText.textContent
    : submitButton
      ? submitButton.textContent
      : "";

  contactForm.addEventListener("submit", async function (event) {
    event.preventDefault();

    if (!contactForm.checkValidity()) {
      contactForm.reportValidity();
      return;
    }

    setSubmittingState(true);
    hideStatus();

    const formData = new FormData(contactForm);

    try {
      const response = await fetch(contactForm.action, {
        method: "POST",
        body: formData,
        headers: {
          Accept: "application/json",
        },
      });

      const result = await response.json();

      if (response.ok) {
        showStatus("Tin nhắn của bạn đã được gửi thành công!", "success");

        contactForm.reset();
      } else {
        showStatus(getFormspreeError(result), "danger");
      }
    } catch (error) {
      console.error("Lỗi gửi biểu mẫu:", error);

      showStatus("Không thể kết nối đến máy chủ. Vui lòng thử lại.", "danger");
    } finally {
      setSubmittingState(false);
    }
  });

  function setSubmittingState(isSubmitting) {
    if (submitButton) {
      submitButton.disabled = isSubmitting;
    }

    if (submitSpinner) {
      submitSpinner.classList.toggle("d-none", !isSubmitting);
    }

    if (submitButtonText) {
      submitButtonText.textContent = isSubmitting
        ? "Đang gửi..."
        : defaultSubmitText;
    } else if (submitButton) {
      submitButton.textContent = isSubmitting
        ? "Đang gửi..."
        : defaultSubmitText;
    }
  }

  function showStatus(message, type) {
    formStatus.textContent = message;
    formStatus.className = `alert alert-${type}`;
  }

  function hideStatus() {
    formStatus.textContent = "";
    formStatus.className = "alert d-none";
  }

  function getFormspreeError(result) {
    if (
      result.errors &&
      Array.isArray(result.errors) &&
      result.errors.length > 0
    ) {
      return result.errors.map((error) => error.message).join(" ");
    }

    return "Không thể gửi tin nhắn. Vui lòng thử lại.";
  }
}
