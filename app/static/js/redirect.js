function check_ga() {
  if (typeof ga === 'function') {
    console.log('Loaded :' + ga);
    runAjax();
  }
  else {
    console.log('Not loaded');
    setTimeout(check_ga, 500);
  }
}

function runAjax() {
  var hash = $("#hash").val();
  var client_id = ga.getAll()[0].get('clientId');
  console.log("Starting ajax");

  $.ajax({
    type: "POST",
    url: "/redirect",
    data: {
      hash: hash,
      ga_client_id: client_id
    },
    success: function (data) {
      data = JSON.parse(data);
      console.log(data.info);
    },
    error: function (data) {
      console.log(data);
    }
  });
}

$(document).ready(function () {
  check_ga();
});