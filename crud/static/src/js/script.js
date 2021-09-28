// Enter your code JavaScript

// Change input File label [DEPRECATED]
// $(".custom-file-input").on("change", function() {
//   filename = this.files[0].name
//   $(".clients-form__choose-file-label").text(filename);
// });

// Open image in modal
$(".clients-listing__photo-open").on("click", function() {
  $('.clients-listing__photo-full').attr('src', $(this).find('img').attr('src'));
  $('#ModalPhotoView').modal('show');
});

// Add path delete registry
$(".clients-btn-delete").on("click", function() {
  $('.clients-model-delete__form').attr('action', $(this).find('span').attr('data-target'));
  $('#confirmDeleteModal').modal('show');
});

// Change input search mask
$(".clients-listing__search-select").change(function() {
  const select = $('.clients-listing__search-select option:selected').val();
  const busca = $('.clients-listing__search-input');
  if (select == "cpf") {
    busca.mask('000.000.000-00');
  } else if (select == "cnpj") {
    busca.mask('00.000.000/0000-00');
  } else if (select == "id") {
    busca.mask('0000000');
  } else {
    busca.unmask();
  }
});

// Change input CPF/CNPJ mask
$(".clients-form__cpf_or_cnpj").change(function() {
  const select = $('.clients-form__cpf_or_cnpj option:selected').val();
  const input = $('.clients-form__input-cpf-cnpj');
  if (select == "cpf") {
    input.val('');
    input.mask('000.000.000-00');
  } else if (select == "cnpj") {
    input.val('');
    input.mask('00.000.000/0000-00');
  } else {
    input.unmask();
  }
});

// Change input cpf/cnpj mask
// $("#flexRadioCPF").on("click", function() {
//   const input = $('.clients-form__input-cpf-cnpj');
//   input.val('');
//   input.mask('000.000.000-00');
// });
// $("#flexRadioCNPJ").on("click", function() {
//   const input = $('.clients-form__input-cpf-cnpj');
//   input.val('');
//   input.mask('00.000.000/0000-00');
// });
