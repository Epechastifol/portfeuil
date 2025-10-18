 
document.addEventListener('DOMContentLoaded', function() { 
    // Amélioration de l'UX 
    const sidebarCollapse = document.querySelector('.sidebar-collapse'); 
    if (sidebarCollapse) { 
        sidebarCollapse.addEventListener('click', function() { 
            document.querySelector('.admin-sidebar').classList.toggle('collapsed'); 
        }); 
    } 
     
    // Confirmation pour les actions dangereuses 
    const deleteButtons = document.querySelectorAll('.btn-delete, .deletelink'); 
    deleteButtons.forEach(button => { 
        button.addEventListener('click', function(e) { 
            if (!confirm('Êtes-vous sûr de vouloir supprimer cet élément ?')) { 
                e.preventDefault(); 
            } 
        }); 
    }); 
     
    // Animation des cartes 
    const cards = document.querySelectorAll('.card-custom'); 
    cards.forEach(card => { 
        card.style.opacity = '0'; 
        card.style.transform = 'translateY(20px)'; 
         
        setTimeout(() => { 
            card.style.transition = 'all 0.5s ease'; 
            card.style.opacity = '1'; 
            card.style.transform = 'translateY(0)'; 
        }, 100); 
    }); 
});