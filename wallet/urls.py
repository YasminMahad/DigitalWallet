from unicodedata import name
from django.urls import path
from .views import   customer_profile, edit_progile, list_account, list_card, list_customer, list_loan, list_notification, list_receipt, list_reward, list_thirdparty, list_transaction, list_wallet, register_account, register_card, register_customer, register_loan, register_notification, register_receipt, register_reward, register_thirdparty, register_transaction, register_wallet



urlpatterns =[
    path("customer/", register_customer,name="registration"),
    path("wallet/", register_wallet,name="wallet"),
    path("account/", register_account,name="account"),
    path("transaction/", register_transaction,name="transaction"),
    path("card/", register_card,name="card"),
    path("thirdparty/", register_thirdparty,name="thirdparty"),
    path("notification/", register_notification,name="notification"),
    path("receipt/", register_receipt,name="receipt"),
    path("loan/", register_loan,name="loan"),
    path("reward/", register_reward,name="reward"),

    path("customers/", list_customer,name="registration"),
    path("wallets/", list_wallet,name="wallet"),
    path("accounts/", list_account,name="account"),
    path("transactions/", list_transaction,name="transaction"),
    path("cards/", list_card,name="card"),
    path("thirdpartys/", list_thirdparty,name="thirdparty"),
    path("notifications/", list_notification,name="notification"),
    path("receipts/", list_receipt,name="receipt"),
    path("loans/", list_loan,name="loan"),
    path("rewards/", list_reward,name="reward"),

    path("customerss/<int:id>", customer_profile, name="customer_profile"),
    path("profile/edit/<int:id/", edit_profile, name="edit_profile"),
    path("wallets/<int:id>/", wallet_profile, name='wallet_profile'),
    path("wallets/edit/<int:id>/", edit_wallet_profile, name='edit_'),
    path("receipts/<int:id>/", receipt_profile, name='receipt_profile'),
    path("receipts/edit/<int:id>/", edit_receipt_profile, name='edit_receipt'),
    path("transactions/<int:id>/", transaction_profile, name='transaction_profile'),
    path("transactions/edit/<int:id>/", edit_transaction_profile, name='edit_transaction'),
    path("cards/<int:id>/", card_profile, name='card_profile'),
    path("cards/edit/<int:id>/", edit_card_profile, name='edit_card'),
    path("accounts/<int:id>/", account_profile, name='account_profile'),
    path("accounts/edit/<int:id>/", edit_account_profile, name='edit_account'),
]
    