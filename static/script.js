var TrandingSlider = new Swiper('.tranding-slider', {
    effect: 'coverflow',
    grabCursor: true,
    centeredSlides: true,
    loop: true,
    slidesPerView: 'auto',
    coverflowEffect: {
      rotate: 0,
      stretch: 0,
      depth: 100,
      modifier: 2.5,
    },
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
    },
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    }
  });



//  <script>
//   $(document).ready(function(){
//     $("#myCarousel").owlCarousel({
//       items: 3, // Number of cards shown in each slide
//       loop: true, // Continuously loop the carousel
//       margin: 20, // Space between cards
//       nav: true, // Show navigation buttons
//       navText: ["<i class='fas fa-chevron-left'></i>", "<i class='fas fa-chevron-right'></i>"], // Custom navigation icons
//       responsive: {
//         0: {
//           items: 1 // Number of cards shown in the carousel for smaller screens
//         },
//         768: {
//           items: 2 // Number of cards shown in the carousel for medium screens
//         },
//         992: {
//           items: 3 // Number of cards shown in the carousel for large screens
//         }
//       }
//     });
//   });
// </script> 
