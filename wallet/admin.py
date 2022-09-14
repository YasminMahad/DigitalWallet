from django.contrib import admin
from .models import Wallet,Customer,Account,Transaction,Card,Thirdparty,Notification,Receipt,Loan,Reward

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("firstname","lastname","address","email","phone_number","age","gender","nationality","martialStatus","employment_status","signature")
    search_fields = ("firstname","lastname","address","email","phone_number","age","gender","nationality","martialStatus","employment_status","signature")
admin.site.register(Customer,CustomerAdmin)


class WalletAdmin(admin.ModelAdmin):
    list_display = ("dateCreated","balance","customer","pin","isActive","currency")
    search_fields = ("dateCreated","balance","customer","pin","isActive","curency")
admin.site.register(Wallet,WalletAdmin)


class AccountAdmin(admin.ModelAdmin):
    list_display = ("account_number","accountChoice","balance","wallet")
    search_fields = ("account_number","accountChoice","balance","wallet")
admin.site.register(Account,AccountAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ("transaction_code","wallet","transaction_amount","transaction_type","transaction_date","transactionreciept","origin_account")
    search_fields = ("transaction_code","wallet","transaction_amount","transaction_type","transaction_date","transactionreciept","origin_account")
admin.site.register(Transaction,TransactionAdmin)

class CardAdmin(admin.ModelAdmin):
    list_display = ("card_number","card_name","type","card_type","expiry_date","card_status","security_code","wallet","account","issuer_type","issuer")
    search_fields = ("card_number","card_name","type","card_type","expiry_date","card_status","security_code","wallet","account","issuer_type","issuer")
admin.site.register(Card,CardAdmin)


class ThirdPartyAdmin(admin.ModelAdmin):
    list_display = ("transaction_account","name","account","currency","phone_number","location" )
    search_fields = ("transaction_account","name","account","currency","phone_number","location")
admin.site.register(Thirdparty,ThirdPartyAdmin)

class NotificationAdmin(admin.ModelAdmin):
    list_display = ("name","recipient","status","date_and_time")
    search_fields = ("name","recipient","status","date_and_time")
admin.site.register(Notification,NotificationAdmin)

class ReceiptAdmin(admin.ModelAdmin):
    list_display = ("receipt_type","receipt_date", "total_amount","bill_number", "receipt_file")
    search_fields = ("receipt_type","receipt_date","total_amount","bill_number","receipt_file")
admin.site.register(Receipt,ReceiptAdmin)


class LoanAdmin(admin.ModelAdmin):
    list_display = ("loan_id","amount","loan_type","wallet","interest_rate","loan_Term","payment_due_date","loan_balance","guarantor" )
    search_fields = ("loan_id","amount","loan_type","wallet","interest_rate","loan_Term","payment_due_date","loan_balance","guarantor")
admin.site.register(Loan,LoanAdmin)


class RewardAdmin(admin.ModelAdmin):
    list_display = ("name","recipient","bonus","gender","reward_points","date_of_reward" )
    search_fields = ("name","recipient","bonus","gender","reward_points","date_of_reward")
admin.site.register(Reward,RewardAdmin)
