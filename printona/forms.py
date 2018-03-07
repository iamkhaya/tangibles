from django import forms
from django.forms import ModelForm
from .models import Order, OrderItem
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Fieldset, Row
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class CreateOrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'surname', 'street_address', 'surburb', 'city', 'postal_code']

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        super(CreateOrderForm, self).__init__(*args, **kwargs)


class UploadPhotosForm(ModelForm):
    class Meta:
        model = OrderItem
        fields = ['product_id', 'quantity', 'file_name']

    def __init__(self, *args, **kwargs):
        super(UploadPhotosForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'upload-form-id'

        self.helper.form_method = 'post'
        self.helper.form_tag = True
        self.helper.form_action = 'quote'


        self.helper.layout = Layout(
            HTML("<div id='upload_row'>"),
            HTML("""
                <div class="row" id="actual">
            <div class="col-sm-3">
              <div class="form-group">
                <input type="file" class="form-control" id="Upload" name="picture_files" value="">
              </div>
            </div>
            <div class="col-sm-4 nopadding">
              <div class="form-group">
                <input type="number" class="form-control" id="Quantity" name="quantities" value="1" placeholder="Quantity">
              </div>
            </div>
            <div class="col-sm-4 nopadding">
              <select class="custom-select" id="Size" name="sizes">
                 <option selected>Photo Size (mm)</option>
                 {% for item in price_list.all %}
                    <option value="{{ item.id }}">{{ item.length }} x {{ item.width }}</option>
                 {% endfor %}
               </select>
            </div>
          </div>
        </div>
        <div id='upload'> </div>
        <div class="row">
          <div class="col-sm-2">
            <button type="button" class="btn btn-success" onclick="add_upload();"> Add another picture</button>
          </div>
          <div class="col-sm-1 nopadding">
            <div class="form-group">
              <input type="submit" class="btn btn-primary" value="Get Quotation" />
            </div>
          </div>
        </div>"""),

        )

        self.fields['product_id'].label = ""
        self.fields['quantity'].label = ""
        self.fields['file_name'].label = ""
