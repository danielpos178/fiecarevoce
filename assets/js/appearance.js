const sitePreference = document.documentElement.getAttribute("data-default-appearance") || "light";
const autoAppearance = document.documentElement.getAttribute("data-auto-appearance") !== "false";

function applyInitialTheme() {
  const userPreference = localStorage.getItem("appearance");
  if (userPreference === "dark") {
    document.documentElement.classList.add("dark");
  } else if (userPreference === "light") {
    document.documentElement.classList.remove("dark");
  } else if (autoAppearance && window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches) {
    document.documentElement.classList.add("dark");
  } else if (sitePreference === "dark" && userPreference === null) {
    document.documentElement.classList.add("dark");
  } else {
    document.documentElement.classList.remove("dark");
  }
}

applyInitialTheme();

if (window.matchMedia) {
  window.matchMedia("(prefers-color-scheme: dark)").addEventListener("change", (event) => {
    if (!localStorage.getItem("appearance")) {
      if (event.matches) {
        document.documentElement.classList.add("dark");
      } else {
        document.documentElement.classList.remove("dark");
      }
      if (typeof updateMeta === "function") updateMeta();
    }
  });
}

function getTargetAppearance() {
  return document.documentElement.classList.contains("dark") ? "dark" : "light";
}

function updateMeta() {
  const elem = document.querySelector("body");
  if (elem) {
    const style = getComputedStyle(elem);
    const meta = document.querySelector('meta[name="theme-color"]');
    if (meta) {
      meta.setAttribute("content", style.backgroundColor);
    }
  }
}

function initAppearanceSwitcher() {
  const switcher = document.getElementById("appearance-switcher");
  const switcherMobile = document.getElementById("appearance-switcher-mobile");

  const updateTooltip = (targetAppearance) => {
    const label = targetAppearance === "dark" ? "Switch to light mode" : "Switch to dark mode";
    if (switcher) {
      switcher.setAttribute("aria-label", label);
      switcher.setAttribute("title", label);
    }
    if (switcherMobile) {
      switcherMobile.setAttribute("aria-label", label);
      switcherMobile.setAttribute("title", label);
    }
  };

  updateMeta();
  updateTooltip(getTargetAppearance());

  const handleToggle = () => {
    document.documentElement.classList.toggle("dark");
    const newAppearance = getTargetAppearance();
    localStorage.setItem("appearance", newAppearance);
    updateMeta();
    updateTooltip(newAppearance);
  };

  const handleResetToSystem = (event) => {
    event.preventDefault();
    localStorage.removeItem("appearance");
    applyInitialTheme();
    updateMeta();
    updateTooltip(getTargetAppearance());
  };

  if (switcher) {
    switcher.addEventListener("click", handleToggle);
    switcher.addEventListener("contextmenu", handleResetToSystem);
  }

  if (switcherMobile) {
    switcherMobile.addEventListener("click", handleToggle);
    switcherMobile.addEventListener("contextmenu", handleResetToSystem);
  }
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", initAppearanceSwitcher);
} else {
  initAppearanceSwitcher();
}

