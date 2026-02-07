// Florida Alignment & Suspension - Main JavaScript

document.addEventListener('DOMContentLoaded', function() {
    
    // Initialize fade-in animations
    initFadeAnimations();
    
    // Initialize smooth scrolling
    initSmoothScrolling();
    
    // Initialize form enhancements
    initFormEnhancements();
    
    // Initialize image lazy loading
    initLazyLoading();
    
    // Initialize performance optimizations
    initPerformanceOptimizations();
    
    // Initialize accessibility features
    initAccessibility();
    
});

/**
 * Initialize fade-in animations for elements
 */
function initFadeAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
            }
        });
    }, observerOptions);
    
    // Observe all fade-in elements
    document.querySelectorAll('.fade-in').forEach(el => {
        observer.observe(el);
    });
}

/**
 * Initialize smooth scrolling for anchor links
 */
function initSmoothScrolling() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

/**
 * Initialize form enhancements
 */
function initFormEnhancements() {
    // Add loading state to form submissions
    document.querySelectorAll('form').forEach(form => {
        form.addEventListener('submit', function(e) {
            const submitBtn = this.querySelector('input[type="submit"], button[type="submit"]');
            if (submitBtn) {
                submitBtn.classList.add('btn-loading');
                submitBtn.disabled = true;
            }
        });
    });
    
    // Auto-format phone numbers
    document.querySelectorAll('input[type="tel"]').forEach(input => {
        input.addEventListener('input', function(e) {
            let value = e.target.value.replace(/\D/g, '');
            if (value.length >= 6) {
                value = `(${value.slice(0,3)}) ${value.slice(3,6)}-${value.slice(6,10)}`;
            } else if (value.length >= 3) {
                value = `(${value.slice(0,3)}) ${value.slice(3)}`;
            }
            e.target.value = value;
        });
    });
    
    // Add validation feedback
    document.querySelectorAll('input, textarea, select').forEach(field => {
        field.addEventListener('blur', function() {
            validateField(this);
        });
    });
}

/**
 * Validate individual form field
 */
function validateField(field) {
    const value = field.value.trim();
    let isValid = true;
    let errorMessage = '';
    
    // Required field validation
    if (field.hasAttribute('required') && !value) {
        isValid = false;
        errorMessage = 'This field is required.';
    }
    
    // Email validation
    if (field.type === 'email' && value) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(value)) {
            isValid = false;
            errorMessage = 'Please enter a valid email address.';
        }
    }
    
    // Phone validation
    if (field.type === 'tel' && value) {
        const phoneRegex = /^\(\d{3}\) \d{3}-\d{4}$/;
        if (!phoneRegex.test(value)) {
            isValid = false;
            errorMessage = 'Please enter a valid phone number.';
        }
    }
    
    // Update field appearance
    field.classList.toggle('is-invalid', !isValid);
    field.classList.toggle('is-valid', isValid && value);
    
    // Show/hide error message
    let errorElement = field.parentNode.querySelector('.invalid-feedback');
    if (!isValid && errorMessage) {
        if (!errorElement) {
            errorElement = document.createElement('div');
            errorElement.className = 'invalid-feedback';
            field.parentNode.appendChild(errorElement);
        }
        errorElement.textContent = errorMessage;
    } else if (errorElement) {
        errorElement.remove();
    }
    
    return isValid;
}



/**
 * Initialize lazy loading for images
 */
function initLazyLoading() {
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    const src = img.getAttribute('data-src');
                    if (src) {
                        img.src = src;
                        img.removeAttribute('data-src');
                        img.classList.remove('lazy');
                        img.classList.add('loaded');
                    }
                    observer.unobserve(img);
                }
            });
        }, {
            rootMargin: '50px'
        });
        
        // Observe all lazy images
        document.querySelectorAll('img[data-src]').forEach(img => {
            img.classList.add('lazy');
            imageObserver.observe(img);
        });
    } else {
        // Fallback for older browsers
        document.querySelectorAll('img[data-src]').forEach(img => {
            img.src = img.getAttribute('data-src');
            img.removeAttribute('data-src');
        });
    }
}

/**
 * Initialize performance optimizations
 */
function initPerformanceOptimizations() {
    // Preload critical resources
    const preloadLinks = [
        { href: 'https://fonts.googleapis.com', rel: 'preconnect' },
        { href: 'https://cdnjs.cloudflare.com', rel: 'preconnect' },
        { href: 'https://cdn.jsdelivr.net', rel: 'preconnect' }
    ];
    
    preloadLinks.forEach(link => {
        if (!document.querySelector(`link[href="${link.href}"]`)) {
            const linkEl = document.createElement('link');
            linkEl.rel = link.rel;
            linkEl.href = link.href;
            if (link.rel === 'preconnect') linkEl.crossOrigin = 'anonymous';
            document.head.appendChild(linkEl);
        }
    });
    
    // Critical CSS loading optimization
    const nonCriticalCSS = document.querySelectorAll('link[rel="stylesheet"][media="print"]');
    nonCriticalCSS.forEach(link => {
        link.media = 'all';
    });
    
    // Defer non-critical JavaScript
    if (window.requestIdleCallback) {
        window.requestIdleCallback(() => {
            // Initialize non-critical features here
            initNonCriticalFeatures();
        });
    } else {
        setTimeout(initNonCriticalFeatures, 1000);
    }
}

/**
 * Initialize accessibility features
 */
function initAccessibility() {
    // Keyboard navigation for dropdowns and menus
    document.addEventListener('keydown', function(e) {
        // Escape key to close mobile menu
        if (e.key === 'Escape') {
            const mobileMenu = document.querySelector('.navbar-collapse.show');
            if (mobileMenu) {
                const toggleButton = document.querySelector('.navbar-toggler');
                if (toggleButton) {
                    toggleButton.click();
                    toggleButton.focus();
                }
            }
        }
        
        // Tab trapping for modal dialogs
        if (e.key === 'Tab') {
            trapTabInModal(e);
        }
    });
    
    // Add ARIA live regions for dynamic content
    createLiveRegions();
    
    // Enhance form accessibility
    enhanceFormAccessibility();
    
    // Add skip links functionality
    enhanceSkipLinks();
    
    // Announce page changes for screen readers
    announcePageContent();
    
    // Add keyboard support for interactive elements
    addKeyboardSupport();
}

/**
 * Create ARIA live regions for dynamic announcements
 */
function createLiveRegions() {
    if (!document.getElementById('aria-live-polite')) {
        const politeRegion = document.createElement('div');
        politeRegion.id = 'aria-live-polite';
        politeRegion.setAttribute('aria-live', 'polite');
        politeRegion.setAttribute('aria-atomic', 'true');
        politeRegion.className = 'sr-only';
        document.body.appendChild(politeRegion);
    }
    
    if (!document.getElementById('aria-live-assertive')) {
        const assertiveRegion = document.createElement('div');
        assertiveRegion.id = 'aria-live-assertive';
        assertiveRegion.setAttribute('aria-live', 'assertive');
        assertiveRegion.setAttribute('aria-atomic', 'true');
        assertiveRegion.className = 'sr-only';
        document.body.appendChild(assertiveRegion);
    }
}

/**
 * Announce messages to screen readers
 */
function announceToScreenReader(message, priority = 'polite') {
    const region = document.getElementById(`aria-live-${priority}`);
    if (region) {
        region.textContent = '';
        setTimeout(() => {
            region.textContent = message;
        }, 100);
    }
}

/**
 * Enhance form accessibility
 */
function enhanceFormAccessibility() {
    // Add proper labels and descriptions
    document.querySelectorAll('input, textarea, select').forEach(field => {
        // Add required indicator to screen readers
        if (field.hasAttribute('required')) {
            const label = document.querySelector(`label[for="${field.id}"]`);
            if (label && !label.textContent.includes('(required)')) {
                const requiredText = document.createElement('span');
                requiredText.className = 'sr-only';
                requiredText.textContent = ' (required)';
                label.appendChild(requiredText);
            }
        }
        
        // Add error association
        field.addEventListener('invalid', function() {
            this.setAttribute('aria-invalid', 'true');
            const errorId = `${this.id}-error`;
            this.setAttribute('aria-describedby', errorId);
        });
        
        field.addEventListener('input', function() {
            if (this.checkValidity()) {
                this.removeAttribute('aria-invalid');
            }
        });
    });
}

/**
 * Add keyboard support for interactive elements
 */
function addKeyboardSupport() {
    // Service cards keyboard navigation
    document.querySelectorAll('.service-card').forEach((card, index) => {
        card.setAttribute('tabindex', '0');
        card.setAttribute('role', 'button');
        card.setAttribute('aria-label', `View details for ${card.querySelector('.card-title').textContent}`);
        
        card.addEventListener('keydown', function(e) {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                const link = this.querySelector('a');
                if (link) link.click();
            }
        });
    });
    
    // Add keyboard navigation for custom interactive elements
    document.querySelectorAll('[role="button"]:not(button)').forEach(element => {
        element.addEventListener('keydown', function(e) {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                this.click();
            }
        });
    });
}

/**
 * Enhance skip links functionality
 */
function enhanceSkipLinks() {
    document.querySelectorAll('.skip-link').forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.focus();
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });
}

/**
 * Announce page content for screen readers
 */
function announcePageContent() {
    const pageTitle = document.title;
    const mainHeading = document.querySelector('h1');
    
    if (mainHeading) {
        setTimeout(() => {
            announceToScreenReader(`Page loaded: ${pageTitle}`, 'polite');
        }, 1000);
    }
}

/**
 * Tab trapping for modal dialogs
 */
function trapTabInModal(e) {
    const modal = document.querySelector('.modal.show');
    if (!modal) return;
    
    const focusableElements = modal.querySelectorAll(
        'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
    );
    
    if (focusableElements.length === 0) return;
    
    const firstElement = focusableElements[0];
    const lastElement = focusableElements[focusableElements.length - 1];
    
    if (e.shiftKey) {
        if (document.activeElement === firstElement) {
            e.preventDefault();
            lastElement.focus();
        }
    } else {
        if (document.activeElement === lastElement) {
            e.preventDefault();
            firstElement.focus();
        }
    }
}

/**
 * Initialize non-critical features
 */
function initNonCriticalFeatures() {
    // Add enhanced hover effects
    document.querySelectorAll('.service-card').forEach(card => {
        card.addEventListener('mouseenter', () => {
            card.style.transform = 'translateY(-8px)';
        });
        card.addEventListener('mouseleave', () => {
            card.style.transform = 'translateY(0)';
        });
    });
    
    // Add loading states to external links
    document.querySelectorAll('a[href^="http"]').forEach(link => {
        if (!link.href.includes(window.location.hostname)) {
            link.addEventListener('click', function(e) {
                if (!this.textContent.includes('Loading...')) {
                    const originalText = this.innerHTML;
                    this.innerHTML = '<i class="fas fa-spinner fa-spin me-1"></i>Loading...';
                    setTimeout(() => {
                        this.innerHTML = originalText;
                    }, 2000);
                }
            });
        }
    });
}

/**
 * Utility function to show notifications
 */
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `alert alert-${type} alert-dismissible fade show position-fixed`;
    notification.style.cssText = 'top: 20px; right: 20px; z-index: 1050; min-width: 300px;';
    notification.setAttribute('role', 'alert');
    notification.setAttribute('aria-live', type === 'danger' ? 'assertive' : 'polite');
    notification.innerHTML = `
        <div class="d-flex align-items-center">
            <i class="fas fa-${type === 'success' ? 'check-circle' : type === 'danger' ? 'exclamation-triangle' : 'info-circle'} me-2" aria-hidden="true"></i>
            <div class="flex-grow-1">${message}</div>
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close notification"></button>
        </div>
    `;
    
    document.body.appendChild(notification);
    
    // Announce to screen readers
    if (typeof announceToScreenReader === 'function') {
        announceToScreenReader(message, type === 'danger' ? 'assertive' : 'polite');
    }
    
    // Auto-remove after 5 seconds
    setTimeout(() => {
        if (notification.parentNode) {
            notification.remove();
        }
    }, 5000);
}

// Google Analytics Event Tracking
function trackEvent(eventName, eventCategory, eventLabel, value) {
    if (typeof gtag !== 'undefined') {
        gtag('event', eventName, {
            event_category: eventCategory,
            event_label: eventLabel,
            value: value
        });
    }
}

// Track phone clicks
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('a[href^="tel:"]').forEach(link => {
        link.addEventListener('click', function() {
            trackEvent('click', 'contact', 'phone_click', this.getAttribute('href'));
        });
    });
    
    // Track email clicks
    document.querySelectorAll('a[href^="mailto:"]').forEach(link => {
        link.addEventListener('click', function() {
            trackEvent('click', 'contact', 'email_click', this.getAttribute('href'));
        });
    });
    
    // Track service quote requests
    document.querySelectorAll('a[href*="contact"]').forEach(link => {
        if (link.textContent.toLowerCase().includes('quote')) {
            link.addEventListener('click', function() {
                trackEvent('click', 'lead_generation', 'quote_request', this.textContent);
            });
        }
    });
    
    // Track Calendly clicks
    document.querySelectorAll('a[href*="calendly"]').forEach(link => {
        link.addEventListener('click', function() {
            trackEvent('click', 'lead_generation', 'booking_click', 'calendly');
        });
    });
    
    // Track external link clicks
    document.querySelectorAll('a[href^="http"]').forEach(link => {
        if (!link.href.includes(window.location.hostname)) {
            link.addEventListener('click', function() {
                trackEvent('click', 'external', 'outbound_link', this.href);
            });
        }
    });
});

// Track contact form submissions
function trackContactFormSubmission(formData) {
    if (typeof gtag !== 'undefined') {
        gtag('event', 'generate_lead', {
            currency: 'USD',
            value: 150, // Average service value estimate
            event_category: 'lead_generation',
            event_label: 'contact_form_submit',
            custom_parameters: {
                service_type: formData.get('service_id') || 'general',
                urgency: formData.get('urgency') || 'normal'
            }
        });
    }
}

// Export functions for use in other scripts
window.FloridaAlignment = {
    showNotification,
    validateField,
    trackEvent,
    trackContactFormSubmission
};
