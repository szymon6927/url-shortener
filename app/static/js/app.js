$(document).ready(function() {
  console.log("Wow!")

  $('#link-form').submit(function(event) {
    console.log("click");
    event.preventDefault();
    let phone = $('#phone').val();
    let link = $('#url_to_short').val();

    console.log("link ", link, "phone ", phone);

    $.ajax({
      type: "POST",
      url: "/addLink",
      data: {
        phone: phone,
        link: link
      },
      success: function(data) {
        data = JSON.parse(data)
        console.log(data);
        $('.shorted-link').html(data.html);
      },
      error: function(data) {
        console.log("error: ", data);
      }
    })
  });
})