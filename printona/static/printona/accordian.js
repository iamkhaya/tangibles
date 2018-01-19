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
  divUpload.innerHTML = trimmed + 'div class="col-sm-1 nopadding"><button type="button" class="btn btn-danger" onclick="remove_education_fields('+ room +');">Remove</button></div></div>';

  //set target
  target.appendChild(divUpload);

}

function remove_education_fields(div_id) {
  $(".removeclass"+div_id).remove();
}

function calculate_quote() {
  alert("test");
}
