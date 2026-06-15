(() => {
    const forms = document.querySelectorAll(".needs-validation");

    forms.forEach((form) => {
        form.addEventListener("submit", (event) => {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }

            form.classList.add("was-validated");
        });
    });

    const processingPage = document.querySelector("[data-result-url]");
    if (!processingPage) {
        return;
    }

    const resultUrl = processingPage.dataset.resultUrl;
    const progressBar = document.querySelector("[data-progress-bar]");
    const statuses = Array.from(document.querySelectorAll("[data-status-list] li"));
    const progressValues = [18, 46, 74, 100];
    let index = 0;

    const advance = () => {
        statuses.forEach((item, itemIndex) => {
            item.classList.toggle("active", itemIndex <= index);
        });

        if (progressBar) {
            progressBar.style.width = `${progressValues[index]}%`;
        }

        index += 1;
        if (index < statuses.length) {
            window.setTimeout(advance, 650);
        } else {
            window.setTimeout(() => {
                window.location.href = resultUrl;
            }, 700);
        }
    };

    window.setTimeout(advance, 500);
})();
