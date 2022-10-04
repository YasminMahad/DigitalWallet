from django.shortcuts import render,redirect

from wallet.models import Account, Card, Customer, Loan, Notification, Receipt, Reward, Thirdparty, Transaction, Wallet

from .forms import CustomerRegistrationForm
from .forms import WalletRegistrationForm
from .forms import AccountRegistrationForm
from .forms import TransactionRegistrationForm
from .forms import CardRegistrationForm
from .forms import ThirdpartyRegistrationForm
from .forms import NotificationRegistrationForm
from .forms import ReceiptRegistrationForm
from .forms import LoanRegistrationForm
from .forms import RewardRegistrationForm


# Create your views here.
def register_customer(request):
    if request.method == "POST":
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=CustomerRegistrationForm()
    return render(request,"wallet/register_customer.html" ,{"form":form})

def list_customer(request):
    customers = Customer.objects.all()
    return render  (request,"wallet/customerList.html",{"customers":customers})

def customer_profile(request,id):
    customer = Customer.objects.get(id=id)
    return render(request, "wallet/customer_profile.html", {"customer":customer})

def register_wallet(request):
    if request.method == "POST":
        form = WalletRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=WalletRegistrationForm()
    return render(request,"wallet/register_wallet.html" ,{"form":form})

def list_wallet(request):
    wallets = Wallet.objects.all()
    return render  (request,"wallet/walletList.html",{"wallets":wallets})

def register_account(request):
    if request.method == "POST":
        form = AccountRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=AccountRegistrationForm()
    return render(request,"wallet/register_account.html" ,{"form":form})

def list_account(request):
    accounts = Account.objects.all()
    return render  (request,"wallet/accountList.html",{"accounts":accounts})

def register_transaction(request):
    if request.method == "POST":
        form = TransactionRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=TransactionRegistrationForm()
    return render(request,"wallet/register_transaction.html" ,{"form":form})

def list_transaction(request):
    transactions = Transaction.objects.all()
    return render  (request,"wallet/transactionList.html",{"transactions":transactions})

def register_card(request):
    if request.method == "POST":
        form = CardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=CardRegistrationForm()
    return render(request,"wallet/register_card.html" ,{"form":form})

def list_card(request):
    cards = Card.objects.all()
    return render  (request,"wallet/cardList.html",{"cards":cards})


def register_thirdparty(request):
    if request.method == "POST":
        form = ThirdpartyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=ThirdpartyRegistrationForm()
    return render(request,"wallet/register_thirdparty.html" ,{"form":form})

def list_thirdparty(request):
    thirdpartys = Thirdparty.objects.all()
    return render  (request,"wallet/thirdpartyList.html",{"thirdparties":thirdpartys})    

def register_notification(request):
    if request.method == "POST":
        form = NotificationRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=NotificationRegistrationForm()
    return render(request,"wallet/register_notification.html" ,{"form":form})

def list_notification(request):
    notifications = Notification.objects.all()
    return render  (request,"wallet/notificationList.html",{"notifications":notifications})     

def register_receipt(request):
    if request.method == "POST":
        form = ReceiptRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=ReceiptRegistrationForm()
    return render(request,"wallet/register_receipt.html" ,{"form":form})

def list_receipt(request):
    receipts = Receipt.objects.all()
    return render  (request,"wallet/receiptList.html",{"receipts":receipts})     

def register_loan(request):
    if request.method == "POST":
        form = LoanRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=LoanRegistrationForm()
    return render(request,"wallet/register_loan.html" ,{"form":form})

def list_loan(request):
    loans = Loan.objects.all()
    return render  (request,"wallet/loanList.html",{"loans":loans})    

def register_reward(request):
    if request.method == "POST":
        form = RewardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=RewardRegistrationForm()
    return render(request,"wallet/register_reward.html" ,{"form":form})

def list_reward(request):
    rewards = Reward.objects.all()
    return render  (request,"wallet/rewardList.html",{"rewards":rewards})

def edit_profile(request, id):
    customer = Customer.objects.get(id = id)
    if request.method =="POST":
        form = CustomerRegistrationForm(request.POST, instance=Customer)
        if form.isvalid():
            form.save()
            return redirect("customer_profile", id= customer.id)
        else: 
            form = CustomerRegistrationForm(instance=customer)
            return render(request,"wallet/edit_profile.html", {"form":form})


def wallet_profile(request,id):
   wallet= Wallet.objects.get(id=id)
   return render(request,"wallet/wallet_profile.html", {'wallets':wallet })
   
def edit_wallet_profile(request, id):
    wallet =Wallet.objects.get(id=id)
    if request.method == "POST":
        form = WalletRegistrationForm(request.POST, instance=wallet)
        if form.is_valid():
            form.save()
            return redirect("wallet_profile", id =wallet.id)
    else:
            form = WalletRegistrationForm(instance=wallet)
    return render(request, "wallet/edit_wallet.html",{'form':form})

def account_profile(request,id):
   account= Account.objects.get(id=id)
    #we inject the variable in the request
   return render(request,"wallet/account_profile.html", {'accounts':account })
   
def edit_account_profile(request, id):
    account =Account.objects.get(id=id)
    if request.method == "POST":
        form = AccountRegistrationForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            return redirect("account_profile", id = account.id)
    else:
            form = AccountRegistrationForm(instance = account)
    return render(request, "wallet/edit_account.html",{'form':form})

def card_profile(request,id):
   card= Card.objects.get(id=id)
    #we inject the variable in the request
   return render(request,"wallet/card_profile.html", {'cards':card })
   
def edit_card_profile(request, id):
    card = Card.objects.get(id=id)
    if request.method == "POST":
        form = CardRegistrationForm(request.POST, instance = card)
        if form.is_valid():
            form.save()
            return redirect("card_profile", id = card.id)
    else:
            form = CardRegistrationForm(instance=card)
    return render(request, "wallet/edit_card.html",{'form':form})


def receipt_profile(request,id):
   receipt= Receipt.objects.get(id=id)
    #we inject the variable in the request
   return render(request,"wallet/receipt_profile.html", {'receipts':receipt })
   
def edit_receipt(request, id):
    receipt = Receipt.objects.get(id=id)
    if request.method == "POST":
        form = ReceiptRegistrationForm(request.POST, instance = receipt)
        if form.is_valid():
            form.save()
            return redirect("receipt_profile", id = receipt.id)
    else:
            form = ReceiptsRegistrationForm(instance = receipt)
    return render(request, "wallet/edit_receipt.html",{'form':form})