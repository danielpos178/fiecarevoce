const sitePreference = document.documentElement.getAttribute("data-default-appearance") || "light";
const autoAppearance = document.documentElement.getAttribute("data-auto-appearance") !== "false";

function getStoredAppearance() {
  try {
    return localStorage.getItem("appearance");
  } catch (e) {
    return null;
  }
}

function setStoredAppearance(val) {
  try {
    if (val) {
      localStorage.setItem("appearance", val);
    } else {
      localStorage.removeItem("appearance");
    }
  } catch (e) {
    // Ignore private browsing storage quota / security errors
  }
}

function applyInitialTheme() {
  const userPreference = getStoredAppearance();
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
    if (!getStoredAppearance()) {
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
  const isDark = document.documentElement.classList.contains("dark");
  const meta = document.querySelector('meta[name="theme-color"]');
  if (meta) {
    meta.setAttribute("content", isDark ? "#121212" : "#ffffff");
  }
}

function initAppearanceSwitcher() {
  const switchers = document.querySelectorAll(
    "#appearance-switcher, #appearance-switcher-mobile, #appearance-switcher-drawer, [data-theme-switcher]"
  );

  const updateTooltips = (targetAppearance) => {
    const label = targetAppearance === "dark" ? "Switch to light mode" : "Switch to dark mode";
    switchers.forEach((btn) => {
      btn.setAttribute("aria-label", label);
      btn.setAttribute("title", label);
    });
  };

  updateMeta();
  updateTooltips(getTargetAppearance());

  const handleToggle = (e) => {
    if (e) {
      e.preventDefault();
      e.stopPropagation();
    }
    document.documentElement.classList.toggle("dark");
    const newAppearance = getTargetAppearance();
    setStoredAppearance(newAppearance);
    updateMeta();
    updateTooltips(newAppearance);
  };

  const handleResetToSystem = (event) => {
    event.preventDefault();
    setStoredAppearance(null);
    applyInitialTheme();
    updateMeta();
    updateTooltips(getTargetAppearance());
  };

  switchers.forEach((btn) => {
    if (btn.dataset.themeBound) return;
    btn.dataset.themeBound = "true";

    btn.addEventListener("click", handleToggle);
    btn.addEventListener("contextmenu", handleResetToSystem);
  });
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", initAppearanceSwitcher);
} else {
  initAppearanceSwitcher();
}

