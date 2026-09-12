function scrollToTop() {
  const scrollToTop = document.getElementById("scroll-to-top");
  if (!scrollToTop) return;
  if (window.scrollY > 300) {
    scrollToTop.classList.remove("translate-y-4", "opacity-0");
    scrollToTop.classList.add("translate-y-0", "opacity-100");
  } else {
    scrollToTop.classList.remove("translate-y-0", "opacity-100");
    scrollToTop.classList.add("translate-y-4", "opacity-0");
  }
}

window.addEventListener("scroll", scrollToTop, { passive: true });
window.addEventListener("load", scrollToTop);
