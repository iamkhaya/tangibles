var room = 1;
function education_fields() {
  room++;
  var objTo = document.getElementById("education_fields");
  var divtest = document.createElement("div");
  divtest.setAttribute("class", "form-group removeclass" + room);
  var rdiv = "removeclass" + room;
  divtest.innerHTML ='<div class="row"><div class="col-sm-3"><div class="form-group"> <input type="file" class="form-control" id="Picture" name="Picture[]" value=""></div></div><div class="col-sm-4 nopadding"><div class="form-group"> <input type="number" class="form-control" id="Major" name="Major[]" value="" placeholder="Quantity"></div></div><div class="col-sm-4 nopadding"> <select class="custom-select" id="inputGroupSelect01"><option selected>Photo Size (mm)</option><option value="1">102 x 152</option><option value="2">127 x 178</option><option value="3">152 x 203</option><option value="1">203 x 254</option><option value="2">406 x 508</option><option value="3">508 x 610</option> </select></div><div class="col-sm-1 nopadding"><div class="form-group"> <button type="button" class="btn btn-danger" onclick="remove_education_fields('+ room +');">Remove</button></div></div></div>';

  objTo.appendChild(divtest);
}

function remove_education_fields(div_id) {
  $(".removeclass"+div_id).remove();
}
