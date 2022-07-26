// Close alert sucsess automatic
$("#success-alert").hide();
$("#success-alert").fadeTo(2000, 500).slideUp(500, function(){
  $("#success-alert").slideUp(500);
});

// Add Popovers (Bootstrap)
const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
const popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
  return new bootstrap.Popover(popoverTriggerEl);
})

// Open image in modal
$(".modal__open-photo").on("click", function() {
  $('.clients-listing__photo-full').attr('src', $(this).attr('src'));
  $('#ModalPhotoView').modal('show');
});

// Temporarily change the image when it is uploaded.
$("#client__upload-photo").on("change", function(){
  if (this.files && this.files[0]) {
    var reader = new FileReader();
    reader.onload = function (e) {
        $(".modal__open-photo").attr('src', e.target.result);
        $(".modal__open-photo").hide();
        $(".modal__open-photo").fadeIn(650);
    }
    reader.readAsDataURL(this.files[0]);
  }
});

// Add path delete registry
$(".clients-btn-delete").on("click", function() {
  $('.clients-model-delete__form').attr('action', $(this).find('span').attr('data-target'));
  $('#confirmDeleteModal').modal('show');
});

// Change input search mask
$(".clients-listing__search-select").on("change", function() {
  const select = $('.clients-listing__search-select option:selected').val();
  const busca = $('.clients-listing__search-input');
  if (select === "cpf") {
    busca.mask('000.000.000-00');
  } else if (select === "cnpj") {
    busca.mask('00.000.000/0000-00');
  } else if (select === "id") {
    busca.mask('0000000');
  } else {
    busca.unmask();
  }
});

// Change input CPF/CNPJ mask
if ($('.clients-form__client_type option:selected').val() === "cpf") {
	$('.clients-form__input-cpf-cnpj').mask('000.000.000-00');
} else if ($('.clients-form__client_type option:selected').val() === "cnpj") {
	$('.clients-form__input-cpf-cnpj').mask('00.000.000/0000-00');
}
$(".clients-form__client_type").on("change", function() {
	const select = $('.clients-form__client_type option:selected').val();
	const input = $('.clients-form__input-cpf-cnpj');
  if (select === "cpf") {
    input.val('');
    input.mask('000.000.000-00');
  } else if (select === "cnpj") {
    input.val('');
    input.mask('00.000.000/0000-00');
  } else {
    input.unmask();
  }
});

// Table line clickable
$(".clickable-row").on("click", function() {
  window.location = $(this).data("href");
});

// Get CEP (API https://viacep.com.br)
$("#search_cep").on("click", function() {
  let getCEPNumbers = $('#id_cep').val().replace(/\D/g, '');
  if (getCEPNumbers !== "") {
    let validCep = /^[0-9]{8}$/;
    if(validCep.test(getCEPNumbers)) {
      $("#id_address").val("...");
      $("#id_district").val("...");
      $("#id_city").val("...");
      $("#id_state").val("...");
      $.getJSON(`https://viacep.com.br/ws/${getCEPNumbers}/json/?callback=?`, data => {
        if (!("erro" in data)) {
          $("#id_address").val(data.logradouro);
          $("#id_district").val(data.bairro);
          $("#id_city").val(data.localidade);
          $("#id_state").val(data.uf);
        }
        else {
            $("#id_address").val("");
            $("#id_district").val("");
            $("#id_city").val("");
            $("#id_state").val("");
            $('#ModalCEPNotFound').modal('show');
            $('#id_cep').val("");
        }
      });
    }
  }
});
