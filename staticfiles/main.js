
    document.addEventListener('DOMContentLoaded', function () {
        var collapseElementList = document.querySelectorAll('.collapse');

        collapseElementList.forEach(function (collapseEl) {
            collapseEl.addEventListener('show.bs.collapse', function () {
                // Cuando la sección se muestra, oculta el ícono de "+"
                collapseEl.previousElementSibling.querySelector('.bi-plus').classList.add('d-none');
                // Muestra el ícono de "-"
                collapseEl.previousElementSibling.querySelector('.bi-dash').classList.remove('d-none');
            });
            
            collapseEl.addEventListener('hide.bs.collapse', function () {
                // Cuando la sección se oculta, muestra el ícono de "+"
                collapseEl.previousElementSibling.querySelector('.bi-plus').classList.remove('d-none');
                // Oculta el ícono de "-"
                collapseEl.previousElementSibling.querySelector('.bi-dash').classList.add('d-none');
            });
        });
    });


    
    