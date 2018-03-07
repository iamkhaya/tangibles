from django.shortcuts import render
from django.template import loader

# Create your views here.
from django.http import HttpResponse
from .models import Product, OrderItem
import simplejson as json
from .forms import CreateOrderForm, UploadPhotosForm
from django.template.loader import render_to_string
from .forms import UploadPhotosForm
import uuid

def index(request):
    price_list = Product.objects.all()
    list_p = list(price_list.values())

    catalogue={}
    for price in list_p:
        catalogue[ price['id']] = str(price['cost'])


    template = loader.get_template('printona/index.html')
    context = {
        'price_list': price_list,
        'catalogue': catalogue,

        'upload_photos_form': UploadPhotosForm(request.POST or None)
    }

    return HttpResponse(template.render(context, request))



def quote(request):
    """view for quotation"""
    template = loader.get_template('printona/order.html')
    from IPython import embed
    # embed()
    if request.method == 'POST':
        quantities = request.POST.getlist('quantities')
        photo_sizes = request.POST.getlist('sizes')
        files = request.FILES.getlist('picture_files')
        order_id = uuid.uuid4()

        order_items = list(zip(files, photo_sizes, quantities))
        for order_item in order_items:
            photos = OrderItem()
            photos.order_id = str(order_id)
            photos.file_name = order_item[0]
            photos.product_id = order_item[1]
            photos.quantity = order_item[2]
            photos.save(order_items)


        order_items = OrderItem.objects.filter(order_id=order_id)

        quotation_row = []
        for item in order_items:
            product = Product.objects.get(id=item.product_id)
            unit_cost = product.cost
            size = '{0} x {1} {2}'.format(product.length, product.width, product.unit)
            total_cost = unit_cost * item.quantity
            row = {}

            row['total_cost']= total_cost
            row['size']= size
            row['quantity'] =item.quantity
            row['file_name']= item.file_name
            print("url is : {0}".format(item.file_name.url))

            quotation_row.append(row)
            # embed()


        context = {
            'create_order_form': CreateOrderForm(request.POST or None),
            'order_items': quotation_row,
            'order_id': order_id,
            'shipping_cost': 65.00,
            'total_cost': 590.00,
        }

        return HttpResponse(template.render(context, request))


def order(request):
    if request.method == 'POST':
        form = CreateOrderForm(request.POST)
        if form.is_valid():
            form.save()
            from IPython import embed
            embed()
            return HttpResponseRedirect('/success/url/')
        else:
            form = UploadFileForm()
            return render(request, 'upload.html', {'form': form})


def product(request):
    return HttpResponse("You're building an product.")

def user(request):
    return HttpResponse("You're building a user.")
