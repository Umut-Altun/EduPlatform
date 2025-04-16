document.addEventListener('DOMContentLoaded', function() {
    // Alert dismissal
    const alerts = document.querySelectorAll('.alert-dismissible');
    alerts.forEach(alert => {
        const closeButton = alert.querySelector('.btn-close');
        if (closeButton) {
            closeButton.addEventListener('click', () => {
                alert.remove();
            });
        }

        // Auto dismiss success messages after 5 seconds
        if (alert.classList.contains('alert-success')) {
            setTimeout(() => {
                alert.remove();
            }, 5000);
        }
    });

    // Form validation
    const forms = document.querySelectorAll('.settings-form');
    forms.forEach(form => {
        form.addEventListener('submit', function(event) {
            let isValid = true;
            const requiredInputs = form.querySelectorAll('input[required]');
            
            requiredInputs.forEach(input => {
                if (!input.value.trim()) {
                    isValid = false;
                    input.classList.add('is-invalid');
                    
                    // Create or update feedback message
                    let feedback = input.nextElementSibling;
                    if (!feedback || !feedback.classList.contains('invalid-feedback')) {
                        feedback = document.createElement('div');
                        feedback.classList.add('invalid-feedback');
                        input.parentNode.insertBefore(feedback, input.nextSibling);
                    }
                    feedback.textContent = 'Bu alan zorunludur.';
                } else {
                    input.classList.remove('is-invalid');
                    const feedback = input.nextElementSibling;
                    if (feedback && feedback.classList.contains('invalid-feedback')) {
                        feedback.remove();
                    }
                }
            });

            if (!isValid) {
                event.preventDefault();
            }
        });
    });

    // Input validation on change
    const formInputs = document.querySelectorAll('.form-control');
    formInputs.forEach(input => {
        input.addEventListener('input', function() {
            if (this.required && !this.value.trim()) {
                this.classList.add('is-invalid');
            } else {
                this.classList.remove('is-invalid');
                const feedback = this.nextElementSibling;
                if (feedback && feedback.classList.contains('invalid-feedback')) {
                    feedback.remove();
                }
            }
        });
    });

    // Password strength indicator for password change form
    const newPasswordInput = document.querySelector('input[name="new_password1"]');
    if (newPasswordInput) {
        newPasswordInput.addEventListener('input', function() {
            const password = this.value;
            let strength = 0;
            
            // Length check
            if (password.length >= 8) strength++;
            
            // Contains number
            if (/\d/.test(password)) strength++;
            
            // Contains letter
            if (/[a-zA-Z]/.test(password)) strength++;
            
            // Contains special character
            if (/[^A-Za-z0-9]/.test(password)) strength++;

            // Update strength indicator
            let strengthText = '';
            let strengthClass = '';
            
            switch(strength) {
                case 0:
                case 1:
                    strengthText = 'Zayıf';
                    strengthClass = 'text-danger';
                    break;
                case 2:
                case 3:
                    strengthText = 'Orta';
                    strengthClass = 'text-warning';
                    break;
                case 4:
                    strengthText = 'Güçlü';
                    strengthClass = 'text-success';
                    break;
            }

            // Create or update strength indicator
            let indicator = this.parentNode.querySelector('.password-strength');
            if (!indicator) {
                indicator = document.createElement('div');
                indicator.classList.add('password-strength', 'mt-1', 'small');
                this.parentNode.appendChild(indicator);
            }
            
            indicator.textContent = `Şifre Gücü: ${strengthText}`;
            indicator.className = `password-strength mt-1 small ${strengthClass}`;
        });
    }
}); 