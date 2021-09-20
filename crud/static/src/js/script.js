// Enter your code JavaScript

// Open image in modal
$(".person-listing__photo-open").on("click", function() {
  $('.person-listing__photo-full').attr('src', $(this).find('img').attr('src'));
  $('#ModalPhotoView').modal('show');
});

// Add path delete registry
$(".person-listing__btn-delete").on("click", function() {
  $('.person-model-delete__form').attr('action', $(this).find('i').attr('data-target'));
  $('#confirmDeleteModal').modal('show');
});

// Change input search mask SSA
$(".person-listing__search-select").change(function() {
  const select = $('.person-listing__search-select option:selected').val();
  const busca = $('.person-listing__search-input');
  if (select == "cpf") {
    busca.mask('000.000.000-00');
  } else if (select == "id") {
    busca.mask('0000000');
  } else {
    busca.unmask();
  }
});
