document.addEventListener("DOMContentLoaded", function () {
    function createStars(numStars) {
        const body = document.body;

        for (let i = 0; i < numStars; i++) {
            const star = document.createElement("div");
            const size = Math.random() * 3 + 1;  // Taille entre 1px et 4px
            const x = Math.random() * window.innerWidth;
            const y = Math.random() * window.innerHeight;
            const duration = Math.random() * 3 + 2;  // Animation entre 2s et 5s

            star.classList.add("star");
            star.style.width = `${size}px`;
            star.style.height = `${size}px`;
            star.style.left = `${x}px`;
            star.style.top = `${y}px`;
            star.style.animation = `twinkle ${duration}s infinite alternate`;

            body.appendChild(star);
        }
    }

    createStars(100);  // Génère 100 étoiles
});
