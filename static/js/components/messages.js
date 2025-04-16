document.addEventListener('DOMContentLoaded', function() {
    const messageContainer = document.getElementById('message-container');
    if (!messageContainer) return;

    // Mesajları otomatik kapatma ve animasyon ekleme
    function initializeMessage(messageBox) {
        const closeBtn = messageBox.querySelector('.message-close');
        
        // Kapatma butonu tıklama olayı
        closeBtn.addEventListener('click', () => removeMessage(messageBox));
        
        // Success mesajlarını otomatik kapatma
        if (messageBox.classList.contains('success')) {
            setTimeout(() => removeMessage(messageBox), 3000);
        }
    }

    // Mesajı kaldırma fonksiyonu
    function removeMessage(messageBox) {
        messageBox.classList.add('removing');
        messageBox.addEventListener('animationend', () => {
            messageBox.remove();
            
            // Eğer başka mesaj kalmadıysa container'ı gizle
            if (messageContainer.children.length === 0) {
                messageContainer.style.display = 'none';
            }
        });
    }

    // Mevcut mesajları initialize et
    document.querySelectorAll('.message-box').forEach(initializeMessage);

    // Yeni mesaj oluşturma fonksiyonu (JavaScript ile mesaj ekleme için)
    window.showMessage = function(message, type = 'info') {
        const messageBox = document.createElement('div');
        messageBox.className = `message-box ${type}`;
        
        let title = '';
        let icon = '';
        
        switch(type) {
            case 'success':
                title = 'Başarılı!';
                icon = 'fa-check-circle';
                break;
            case 'error':
                title = 'Hata!';
                icon = 'fa-times-circle';
                break;
            case 'warning':
                title = 'Uyarı!';
                icon = 'fa-exclamation-circle';
                break;
            case 'info':
                title = 'Bilgi';
                icon = 'fa-info-circle';
                break;
        }

        messageBox.innerHTML = `
            <div class="message-content">
                <i class="message-icon fas ${icon}"></i>
                <div class="message-text">
                    <h4>${title}</h4>
                    <p>${message}</p>
                </div>
            </div>
            <button type="button" class="message-close" aria-label="Kapat">
                <i class="fas fa-times"></i>
            </button>
        `;

        messageContainer.style.display = 'flex';
        messageContainer.appendChild(messageBox);
        initializeMessage(messageBox);
    };
});
