let isDarkMode = false;
toggleTheme();

// Inverted preview logic: when in light mode, show dark preview; when in dark mode, show light preview.
function setCardImage(imgElement, lightImage, darkImage) {
  imgElement.src = isDarkMode ? lightImage : darkImage;
}

async function loadWidgets() {
  try {
    // Adjusted path to widgets.json (one level up from docs/)
    const response = await fetch("js/widgets.json");
    const widgets = await response.json();
    const container = document.getElementById("widgets-container");
    container.innerHTML = "";
    widgets.forEach(widget => {
      const widgetElement = document.createElement("a");
      widgetElement.href = widget.link;
      widgetElement.target = "_blank";
      widgetElement.classList.add("widget");

      const card = document.createElement("div");
      card.classList.add("card");

      // Adjusted path to the previews folder (one level up from docs/)
      const lightImage = `previews/${widget.lightImage}`;
      const darkImage = `previews/${widget.darkImage}`;

      const imgElement = document.createElement("img");
      imgElement.dataset.light = lightImage;
      imgElement.dataset.dark = darkImage;
      setCardImage(imgElement, lightImage, darkImage);

      const cardBody = document.createElement("div");
      cardBody.classList.add("card-body");
      const title = document.createElement("h3");
      title.classList.add("card-title");
      title.textContent = widget.name;
      cardBody.appendChild(title);

      card.appendChild(imgElement);
      card.appendChild(cardBody);
      widgetElement.appendChild(card);
      container.appendChild(widgetElement);
    });
  } catch (error) {
    console.error("Error loading widgets:", error);
  }
}

function toggleTheme() {
  if (document.body.getAttribute("data-theme") === "dark") {
    document.body.removeAttribute("data-theme");
    isDarkMode = false;
  } else {
    document.body.setAttribute("data-theme", "dark");
    isDarkMode = true;
  }
  updateImages();
  const themeIcon = document.getElementById("theme-icon");
  const themeText = document.getElementById("theme-text");
  if (isDarkMode) {
    themeIcon.textContent = "light_mode";
    themeText.textContent = "Light Mode";
  } else {
    themeIcon.textContent = "dark_mode";
    themeText.textContent = "Dark Mode";
  }
}

function updateImages() {
  document.querySelectorAll(".widget img").forEach(img => {
    const lightImage = img.dataset.light;
    const darkImage = img.dataset.dark;
    setCardImage(img, lightImage, darkImage);
  });
}

// Fade-in/out scroll-to-top button
window.addEventListener("scroll", function () {
  const scrollBtn = document.getElementById("scroll-to-top");
  if (window.pageYOffset > 100) {
    scrollBtn.classList.add("visible");
  } else {
    scrollBtn.classList.remove("visible");
  }
});

// Smooth scroll to top on click
document.getElementById("scroll-to-top").addEventListener("click", function () {
  window.scrollTo({ top: 0, behavior: "smooth" });
});

loadWidgets();
