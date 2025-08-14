document.addEventListener("DOMContentLoaded", function () {
  const loader = document.getElementById("loader");
  setTimeout(() => {
    loader.classList.add(
      "opacity-0",
      "pointer-events-none",
      "transition-opacity",
      "duration-500"
    );

    setTimeout(() => {
      loader.remove();
    }, 500);
  }, 300);
});
