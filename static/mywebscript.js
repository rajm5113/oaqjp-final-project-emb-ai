// Wait for page to fully load
document.addEventListener("DOMContentLoaded", function () {
    const resultCard = document.querySelector(".result-card");
    const form = document.querySelector("form");
    const input = document.querySelector("#text");
    const resetBtn = document.querySelector("#reset-btn");
    const submitBtn = document.querySelector("button[type='submit']");

    // Add animation to result card
    if (resultCard) {
        resultCard.classList.add("fade-in");
    }

    // Focus effect for input
    input.addEventListener("focus", () => {
        input.style.boxShadow = "0 0 10px #00c6ff";
    });

    input.addEventListener("blur", () => {
        input.style.boxShadow = "none";
    });

    // Reset button
    if (resetBtn) {
        resetBtn.addEventListener("click", () => {
            input.value = "";
            resultCard?.classList.remove("fade-in");
        });
    }

    // Loader animation on submit (optional)
    form.addEventListener("submit", () => {
        submitBtn.innerText = "Analyzing...";
        submitBtn.disabled = true;
    });
});
