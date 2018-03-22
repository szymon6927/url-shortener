$(document).ready(function () {  

  var form = $("#link-form");

  form.validate({
    rules: {
      phone: {
        required: true,
        minlength: 8
      },
      url_to_short: {
        required: true,
        url: true
      }
    },
    //For custom messages
    messages: {
      phone: {
        required: "Enter a phone number",
        minlength: "Enter at least 8 characters"
      },
      url_to_short: "Enter a website url",
    },
    errorElement: 'div',
    errorPlacement: function (error, element) {
      var placement = $(element).data('error');
      if (placement) {
        $(placement).append(error)
      } else {
        error.insertAfter(element);
      }
    }
  });

  $('#link-form').submit(function (event) {
    if(form.valid()) {
      event.preventDefault();
      let phone = $('#phone').val();
      let link = $('#url_to_short').val();
  
      $.ajax({
        type: "POST",
        url: "/addLink",
        data: {
          phone: phone,
          link: link
        },
        success: function (data) {
          data = JSON.parse(data)
          $('#card-alert').hide();
          $('.shorted-link').html('<span>' + data.info + '</span>');
        },
        error: function (data) {
          $('#card-alert').hide();
          $('#card-alert .card-content').html(data)
        }
      })
    }

  });
})