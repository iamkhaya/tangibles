var room = 1;
function add_upload() {
  room++;
  var target = document.getElementById("upload");
  var divUpload = document.createElement("div");
  divUpload.setAttribute("class", "form-group removeclass" + room);
  var rdiv = "removeclass" + room;

  //Clone the row
  var upload_row = document.getElementById("upload_row");
  var newUpload = upload_row.cloneNode(true);

  //hack to open up closing tag
  var trimmed = newUpload.innerHTML.trim().slice(0, -5);
  divUpload.innerHTML =
    trimmed +
    'div class="col-sm-1 nopadding"><button type="button" class="btn btn-danger" onclick="remove_education_fields(' +
    room +
    ');">Remove</button></div></div>';

  //set target
  target.appendChild(divUpload);
}

function remove_education_fields(div_id) {
  $(".removeclass" + div_id).remove();
}

function calculate_quote(price_list) {
  pl = price_list;
  //Add to table
  var target = document.getElementById("quotation-modal");
  quote = document.querySelectorAll("div#actual");
  quotation = [];

  quote.forEach(function(currentValue, currentIndex, listObj) {
    var inputs = currentValue.getElementsByTagName("input");
    quantity = inputs.Quantity.valueAsNumber;
    upload = inputs.Upload.value;

    var size_selection = currentValue.getElementsByTagName("select");
    size_id = size_selection.Size.value;

    quote_line = {
      upload: upload,
      quantity: quantity,
      size: size_selection.Size.selectedOptions[0].text,
      unit_cost: parseFloat(pl[size_id])
    };
    quotation.push(quote_line);
  });


  quotation.forEach(function(item) {
    var quotation_row = document.createElement("tr");
    quotation_row.innerHTML =
      "<td>" +
      item.upload +
      "</td><td>" +
      item.size +
      "</td><td>" +
      item.quantity +
      "</td><td>" +
      item.quantity * item.unit_cost +
      "</td>";
    target.appendChild(quotation_row);
  });

  var shipping_total = document.createElement("tr");
  shipping_total.innerHTML =
    "<td></td><td></td><td><b>Shipping</b></td><td>R 50.00</td>";
  target.appendChild(shipping_total);



  var total = document.createElement("tr");
  total.innerHTML = "<td></td><td></td><td><b>Total</b></td><td><b>R 400.00</b></td>";
  target.appendChild(total);
    $("#quotationModal").modal();
}
