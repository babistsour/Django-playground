
document.addEventListener('DOMContentLoaded', () => {
  const swiper = new Swiper(".swiper", {
    slidesPerView: 3,
    spaceBetween: 30,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
  })
})



document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll("img.skeleton-placeholder").forEach((img) => {
    img.addEventListener("load", () => {
      img.classList.remove("skeleton-placeholder")
    })
  })
})
