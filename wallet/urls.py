from django.urls import path
from .views import  list_account, list_card, list_customers, list_loan, list_notification, list_receipt, list_reward, list_thirdparty, list_transaction, list_wallets, register_account, register_card, register_customer, register_loan, register_notification, register_receipt, register_reward, register_thirdparty, register_transaction, register_wallet


urlpatterns =[
    path("register/", register_customer,name="registration"),
    path("wallet/", register_wallet,name="wallet"),
    path("account/", register_account,name="account"),
    path("transaction/", register_transaction,name="transaction"),
    path("card/", register_card,name="card"),
    path("thirdparty/", register_thirdparty,name="thirdparty"),
    path("notification/", register_notification,name="notification"),
    path("receipt/", register_receipt,name="receipt"),
    path("loan/", register_loan,name="loan"),
    path("reward/", register_reward,name="reward"),]