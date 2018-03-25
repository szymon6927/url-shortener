function clearForm(form) {
  form.find("#phone").val('');
  form.find("#url_to_short").val('');
}

$(document).ready(function () {

  new ClipboardJS('.btn');

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
    if (form.valid()) {
      event.preventDefault();
      var phone = $('#phone').val();
      var link = $('#url_to_short').val();

      $('.ajax-info').show();
      $('.ajax-info .ajax-text span').html('Link jest generowany !');

      $.ajax({
        type: "POST",
        url: "/addLink",
        data: {
          phone: phone,
          link: link
        },
        success: function (data) {
          data = JSON.parse(data);

          $('.ajax-info').hide();

          $('#card-alert').hide();
          $('#copy-input').val(data.info);

          clearForm(form);
        },
        error: function (data) {
          $('#card-alert').show();
          $('#card-alert .card-content').html(data)
        }
      })
    }

  });
});


$(window).bind("load", function () {

  var footerHeight = 0,
    footerTop = 0,
    $footer = $(".page-footer");

  positionFooter();

  function positionFooter() {
    footerHeight = $footer.height();
    // 20 is as padding height
    footerTop = ($(window).scrollTop() + $(window).height() - footerHeight - 20) + "px";

    if (($(document.body).height() + footerHeight) < $(window).height()) {
      $footer.css({
        position: "absolute",
        width: "100%"
      }).animate({
        top: footerTop
      })
    }
    else {
      $footer.css({
        position: "static"
      })
    }

  }

  $(window)
    .scroll(positionFooter)
    .resize(positionFooter)
});