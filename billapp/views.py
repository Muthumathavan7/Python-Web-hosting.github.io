from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


# from django.shortcuts import render, redirect
from django.core.mail import send_mail
# from .models import Purchase, PurchaseItem, Product
# from .forms import PurchaseForm, PurchaseItemForm

# def calculate_denominations(amount):
#     denominations = [500, 50, 20, 10, 5, 2, 1]
#     result = {}
#     for denom in denominations:
#         count = amount // denom
#         if count:
#             result[denom] = count
#             amount -= count * denom
#     return result

# def create_purchase(request):
#     if request.method == 'POST':
#         form = PurchaseForm(request.POST)
#         product_forms = [PurchaseItemForm(request.POST, prefix=str(i)) for i in range(3)]
        
#         if form.is_valid() and all(pf.is_valid() for pf in product_forms):
#             purchase = form.save(commit=False)
#             purchase.save()
            
#             total_price = 0
#             for pf in product_forms:
#                 item = pf.save(commit=False)
#                 item.purchase = purchase
#                 item.subtotal = item.product.price * item.quantity
#                 item.save()
#                 total_price += item.subtotal
            
#             purchase.total_amount = total_price
#             purchase.balance_amount = purchase.paid_amount - total_price
#             purchase.save()

#             # Calculate denominations
#             balance_denominations = calculate_denominations(purchase.balance_amount)

#             return render(request, 'invoice.html', {'purchase': purchase, 'balance_denominations': balance_denominations})

#     else:
#         form = PurchaseForm()
#         product_forms = [PurchaseItemForm(prefix=str(i)) for i in range(3)]
    
#     return render(request, 'home.html', {'form': form, 'product_forms': product_forms})


from django.shortcuts import render, redirect
from .models import Product, Customer, Purchase, PurchaseItem, Denomination

def create_purchase(request):
    products = Product.objects.all()
    denominations = Denomination.objects.all()

    if request.method == "POST":
        customer_email = request.POST.get("customer_email")
        paid_amount = float(request.POST.get("paid_amount", 0))

        # Create or get customer
        customer, created = Customer.objects.get_or_create(email=customer_email)

        # Create purchase
        purchase = Purchase.objects.create(customer=customer, total_amount=0)

        # Process products
        total_price = 0
        product_ids = request.POST.getlist("product[]")
        quantities = request.POST.getlist("quantity[]")

        for product_id, quantity in zip(product_ids, quantities):
            product = Product.objects.get(id=product_id)
            quantity = int(quantity)
            price = product.price * quantity
            tax = price * (product.tax_percentage / 100)
            total_price += price + tax

            # Create purchase items
            PurchaseItem.objects.create(
                purchase=purchase, product=product, quantity=quantity, price=price, tax=tax
            )

        # Update purchase total
        purchase.total_amount = total_price
        purchase.save()

        # Redirect to success page
        return redirect("billing_success")

    return render(request, "home.html", {"products": products, "denominations": denominations})


def send_invoice(purchase):
    send_mail(
        'Your Invoice',
        f'Total: {purchase.total_amount}, Paid: {purchase.paid_amount}, Balance: {purchase.balance_amount}', 
        'your_email@example.com',
        [purchase.customer_email],
        fail_silently=False,
    )
