document.addEventListener('DOMContentLoaded', function() {
    // Filter functionality
    const applyButton = document.getElementById('apply-filters');
    const categoryFilter = document.getElementById('category-filter');
    const typeFilter = document.getElementById('type-filter');
    const sortFilter = document.getElementById('sort-filter');
    const searchInput = document.getElementById('content-search');
    const tabButtons = document.querySelectorAll('.tab-btn');
    
    // URL'den aktif tab'ı al ve ayarla
    function setActiveTab() {
        const params = new URLSearchParams(window.location.search);
        const currentType = params.get('type') || '';
        
        tabButtons.forEach(btn => {
            const btnType = btn.getAttribute('data-type') || '';
            if (btnType === currentType) {
                btn.classList.add('active');
                if (typeFilter) typeFilter.value = currentType;
            } else {
                btn.classList.remove('active');
            }
        });
        
        // Eğer type parametresi yoksa veya boşsa, "Tüm İçerikler" tab'ını aktif yap
        if (!currentType) {
            const allContentsTab = document.querySelector('.tab-btn[data-type=""]');
            if (allContentsTab) {
                allContentsTab.classList.add('active');
                if (typeFilter) typeFilter.value = '';
            }
        }
    }
    
    // Sayfa yüklendiğinde aktif tab'ı ayarla
    setActiveTab();
    
    // Tab tıklama olayları
    tabButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const type = this.getAttribute('data-type') || '';
            
            // URL'yi güncelle
            const params = new URLSearchParams(window.location.search);
            if (type) {
                params.set('type', type);
            } else {
                params.delete('type');
            }
            
            // Sayfayı yenile
            window.location.href = window.location.pathname + '?' + params.toString();
        });
    });
    
    if (applyButton) {
        applyButton.addEventListener('click', function() {
            applyFilters();
        });
    }
    
    // Like functionality
    const likeButtons = document.querySelectorAll('.like-btn');
    
    likeButtons.forEach(button => {
        button.addEventListener('click', function() {
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
    });
    
    // Search functionality
    if (searchInput) {
        searchInput.addEventListener('keypress', function(e) {
            // Apply search filter when Enter key is pressed
            if (e.key === 'Enter') {
                applyFilters();
            }
        });
    }
    
    // Helper function to apply filters
    function applyFilters() {
        const params = new URLSearchParams(window.location.search);
        
        // Get filter values
        const category = categoryFilter ? categoryFilter.value : '';
        const type = typeFilter ? typeFilter.value : '';
        const sort = sortFilter ? sortFilter.value : '';
        const search = searchInput ? searchInput.value : '';
        
        // Update or remove parameters based on filter values
        if (category) {
            params.set('category', category);
        } else {
            params.delete('category');
        }
        
        if (type) {
            params.set('type', type);
        } else {
            params.delete('type');
        }
        
        if (sort) {
            params.set('sort', sort);
        } else {
            params.delete('sort');
        }
        
        if (search) {
            params.set('search', search);
        } else {
            params.delete('search');
        }
        
        // Redirect to filtered URL
        window.location.href = window.location.pathname + '?' + params.toString();
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
