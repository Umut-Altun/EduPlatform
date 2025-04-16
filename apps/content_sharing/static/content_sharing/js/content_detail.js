document.addEventListener('DOMContentLoaded', function() {
    // Like button functionality
    const likeButton = document.querySelector('.like-btn');
    
    if (likeButton) {
        likeButton.addEventListener('click', function() {
            const contentId = this.getAttribute('data-id');
            const likeCount = this.querySelector('.like-count');
            const likeIcon = this.querySelector('i');
            
            fetch(`/icerik-paylasimi/${contentId}/like/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken'),
                    'Content-Type': 'application/json'
                },
                credentials: 'same-origin'
            })
            .then(response => response.json())
            .then(data => {
                likeCount.textContent = data.likes_count;
                
                if (data.liked) {
                    this.setAttribute('data-liked', 'true');
                    likeIcon.classList.remove('far');
                    likeIcon.classList.add('fas');
                } else {
                    this.removeAttribute('data-liked');
                    likeIcon.classList.remove('fas');
                    likeIcon.classList.add('far');
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    }
    
    // File download tracking
    const downloadLink = document.querySelector('.download-link');
    
    if (downloadLink) {
        downloadLink.addEventListener('click', function() {
            // Optional: Track file downloads
            console.log('File downloaded');
        });
    }
    
    // Helper function to get CSRF token
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
}); 