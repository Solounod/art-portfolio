document.addEventListener('DOMContentLoaded', () => {
    
    // 1. Buscamos la caja negra grande
    const lightboxBox = document.getElementById("zoomImgBox");

    if (lightboxBox) {
        const lightboxImg = document.getElementById("zoomImgDisplay");
        const closeBtn = document.getElementById("closeBtn");
        // Buscamos todas las fotos que tengan la clase js-zoom-trigger
        const thumbnails = document.querySelectorAll(".js-zoom-trigger");

        // --- ABRIR ---
        thumbnails.forEach(thumbnail => {
            thumbnail.addEventListener("click", function() {
                // Obtenemos la URL desde el atributo data
                const imgUrl = this.getAttribute("data-img-url");
                
                if (imgUrl) {
                    lightboxImg.setAttribute("src", imgUrl);
                    lightboxBox.classList.add("active"); // Usamos la clase active
                    document.body.style.overflow = 'hidden'; // Evitar scroll
                }
            });
        });

        // --- CERRAR ---
        const closeLightbox = () => {
            lightboxBox.classList.remove("active");
            document.body.style.overflow = 'auto'; // Reactivar scroll
            setTimeout(() => {
                lightboxImg.setAttribute("src", ""); 
            }, 300);
        };

        closeBtn.addEventListener("click", closeLightbox);
        
        // Cerrar al dar click fuera
        lightboxBox.addEventListener("click", (e) => {
            if (e.target === lightboxBox) {
                closeLightbox();
            }
        });

        // Cerrar con Escape
        document.addEventListener('keydown', function(e) {
            if (e.key === "Escape" && lightboxBox.classList.contains('active')) {
                closeLightbox();
            }
        });
    }
});