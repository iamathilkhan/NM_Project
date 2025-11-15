// Weather Dashboard JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Toggle temperature unit
    const toggleUnitBtn = document.getElementById('toggle-unit');
    if (toggleUnitBtn) {
        toggleUnitBtn.addEventListener('click', function() {
            fetch('/toggle_unit', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                }
            })
            .then(response => response.json())
            .then(data => {
                location.reload();
            })
            .catch(error => {
                console.error('Error toggling unit:', error);
            });
        });
    }

    // Add loading states to search button
    const searchButton = document.querySelector('button[type="submit"]');
    if (searchButton) {
        const originalText = searchButton.innerHTML;
        searchButton.addEventListener('click', function() {
            this.innerHTML = 'Searching...';
            this.disabled = true;
            // Re-enable after 2 seconds (in case of slow response)
            setTimeout(() => {
                this.innerHTML = originalText;
                this.disabled = false;
            }, 2000);
        });
    }

    // Smooth scroll for better UX
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // Add elegant fade-in animation to weather cards
    const weatherCards = document.querySelectorAll('.bg-white');
    weatherCards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(30px)';
        setTimeout(() => {
            card.style.transition = 'opacity 0.8s cubic-bezier(0.4, 0, 0.2, 1), transform 0.8s cubic-bezier(0.4, 0, 0.2, 1)';
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, index * 200);
    });

    // Add subtle hover effects to forecast cards
    const forecastCards = document.querySelectorAll('.bg-gradient-to-b');
    forecastCards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            card.style.transform = 'translateY(-4px)';
            card.style.boxShadow = '0 8px 25px rgba(0, 0, 0, 0.15)';
        });
        card.addEventListener('mouseleave', () => {
            card.style.transform = 'translateY(0)';
            card.style.boxShadow = '0 2px 4px rgba(0, 0, 0, 0.1)';
        });
    });
});
