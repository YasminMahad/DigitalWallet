from django.shortcuts import render

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
    customer = Customer.objects.all()
    return render  (request,"wallet/customerList.html",{"customers":customer})

def register_wallet(request):
    if request.method == "POST":
        form = WalletRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=WalletRegistrationForm()
    return render(request,"wallet/register_wallet.html" ,{"form":form})

def list_wallet(request):
    wallet = Wallet.objects.all()
    return render  (request,"wallet/walletList.html",{"wallets":wallet})

def register_account(request):
    if request.method == "POST":
        form = AccountRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=AccountRegistrationForm()
    return render(request,"wallet/register_account.html" ,{"form":form})

def list_account(request):
    account = Account.objects.all()
    return render  (request,"wallet/accountList.html",{"accounts":account})

def register_transaction(request):
    if request.method == "POST":
        form = TransactionRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=TransactionRegistrationForm()
    return render(request,"wallet/register_transaction.html" ,{"form":form})

def list_transaction(request):
    transaction = Transaction.objects.all()
    return render  (request,"wallet/transactionList.html",{"transactions":transaction})

def register_card(request):
    if request.method == "POST":
        form = CardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=CardRegistrationForm()
    return render(request,"wallet/register_card.html" ,{"form":form})

def list_card(request):
    card = Card.objects.all()
    return render  (request,"wallet/cardList.html",{"cards":card})


def register_thirdparty(request):
    if request.method == "POST":
        form = ThirdpartyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=ThirdpartyRegistrationForm()
    return render(request,"wallet/register_thirdparty.html" ,{"form":form})

def list_thirdparty(request):
    thirdparty = Thirdparty.objects.all()
    return render  (request,"wallet/thirdpartyList.html",{"thirdparties":thirdparty})    

def register_notification(request):
    if request.method == "POST":
        form = NotificationRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=NotificationRegistrationForm()
    return render(request,"wallet/register_notification.html" ,{"form":form})

def list_notification(request):
    notification = notification.objects.all()
    return render  (request,"wallet/notificationList.html",{"notifications":notification})     

def register_receipt(request):
    if request.method == "POST":
        form = ReceiptRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=ReceiptRegistrationForm()
    return render(request,"wallet/register_receipt.html" ,{"form":form})

def list_receipt(request):
    receipt = receipt.objects.all()
    return render  (request,"wallet/receiptList.html",{"receipts":receipt})     

def register_loan(request):
    if request.method == "POST":
        form = LoanRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=LoanRegistrationForm()
    return render(request,"wallet/register_loan.html" ,{"form":form})

def list_loan(request):
    loan = loan.objects.all()
    return render  (request,"wallet/loanList.html",{"loans":loan})    

def register_reward(request):
    if request.method == "POST":
        form = RewardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=RewardRegistrationForm()
    return render(request,"wallet/register_reward.html" ,{"form":form})

def list_reward(request):
    reward = reward.objects.all()
    return render  (request,"wallet/rewardList.html",{"rewards":reward})