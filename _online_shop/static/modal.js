document.addEventListener('DOMContentLoaded', function() {
 var modal = document.getElementById('product-modal');
  var modalImage = document.getElementById('modal-image');
  var modalName = document.getElementById('modal-name');
  var modalPrise = document.getElementById('modal-prise');
  var modalStock = document.getElementById('modal-stock');

  var modalDesc = document.getElementById('modal-desc');
  var modalMeta = document.getElementById('modal-meta');
  var modalClose = document.querySelector('.modal-close');



  function openModal() {
    modal.classList.add('open');
    modal.setAttribute('aria-hidden', 'false');
  }
  
  function closeModal() {
    modal.classList.remove('open');
    modal.setAttribute('aria-hidden', 'true');
  }
function buildMetaHTML(attrs) {
    return `<p><strong>Category:</strong> ${attrs.category|| '-'}
      <div class="rating" data-rating="${attrs.rating || 0}">
        <span class="star">★</span>
        <span class="star">★</span>
        <span class="star">★</span>
        <span class="star">★</span>
        <span class="star">★</span>
      </div>

      • <strong>Sale:</strong> ${attrs.sale || 'False'}
      • <strong>Active:${attrs.active || 'False'}
</p>`;
  }
      



document.querySelectorAll('.btn-details').forEach(function(btn) {
    btn.addEventListener('click', function() {
      var attrs = {
        image: btn.getAttribute('data-image'),
        name: btn.getAttribute('data-name'),
        prise: btn.getAttribute('data-prise'),
        stock: btn.getAttribute('data-stock'),
        description: btn.getAttribute('data-description'),
        category: btn.getAttribute('data-category'),
        rating: btn.getAttribute('data-rating'),
        sale: btn.getAttribute('data-sale'),
        active: btn.getAttribute('data-active'),
        


      };


      modalImage.src = attrs.image;
      modalName.textContent = attrs.name;
      modalPrise.textContent = 'Prise: $' + attrs.prise;
      modalStock.textContent = 'Stock: ' + attrs.stock;
      modalDesc.textContent = attrs.description || 'No description';
      modalMeta.innerHTML = buildMetaHTML(attrs);

const ratingDiv = modal.querySelector('.rating');
      updateRatingStars(ratingDiv);

      openModal();
    });
  });

 modalClose.addEventListener('click', closeModal);
  modal.addEventListener('click', function(e) {
    if (e.target === modal) closeModal();
  });
  document.addEventListener('keydown', function(e) { if (e.key === 'Escape') closeModal(); });
});