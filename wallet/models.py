from django.db import models
from datetime import datetime



# Create your models here.
class Customer(models.Model):
    firstname = models.CharField(max_length=15,null=True)
    lastname = models.CharField(max_length=15,null=True)
    gender_type= (
        ('F','Female'),
        ('M','Male')
    )
    address = models.TextField()
    email = models.EmailField()
    gender = models.CharField(max_length=10,null=True,choices=gender_type)
    nationality = models.CharField(max_length=15,null=True)
    age = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=15,null=True)
    employment_status = models.BooleanField(null=True)
    proile_picture = models.ImageField(default='default.jpg', upload_to='profile_pics')
    martialStatus=models.CharField(max_length=8,null=True)
    signature=models.ImageField(default='default.jpg',upload_to='profile_pics')



class Wallet(models.Model):
    dateCreated=models.DateTimeField(default="")
    balance = models.IntegerField(default=0)
    customer = models.ForeignKey('Customer', on_delete= models.CASCADE,related_name='Wallet_customer',null= True)
    pin = models.CharField(max_length=15,default="")
    isActive=models.BooleanField(null=True)
    currency= models.CharField(max_length=23,null=True) 
    


class Account(models.Model):
    account_number = models.IntegerField(default=0)
    accountChoice = (
        ('f','fixed account'),
        ('c','current account')
    )
    account_type = models.CharField(max_length=30,null=True,choices=accountChoice)
    balance = models.IntegerField(default=0)
    wallet = models.ForeignKey(Wallet, on_delete= models.CASCADE,null=True)

class Transaction(models.Model):
    transaction_code = models.IntegerField(null=True)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE,null=True)
    transaction_amount = models.IntegerField(null=True)
    trans_type = (
        ('D','Deposite'),
        ('W','Withdrawal')
    )
    transaction_type = models.CharField(max_length=30,null=True,choices=trans_type)
    transaction_charge = models.IntegerField(null=True)
    transaction_date = models.DateTimeField(default=datetime.now)
    transactionreciept = models.CharField(max_length=8,null=True)
    origin_account = models.ForeignKey(Account, on_delete=models.CASCADE,null=True)
    

class Card(models.Model):
    card_number = models.IntegerField()
    issue_date = models.CharField(max_length=30,null=True)
    card_name = models.CharField(max_length=30,null=True)
    type = (
        ('C','Credit Card'),
        ('D','Debit Card')
    )
    card_type = models.CharField(max_length=30,null=True,choices=type)
    expiry_date = models.DateTimeField(default=datetime.now)
    card_status = models.CharField(max_length=30,null=True)
    security_code = models.IntegerField(null=True)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE,null=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE,null=True)
    issuer_type = (
        ('M','Master Card'),
        ('V','Visa Card')
    )
    issuer = models.CharField(max_length=30,null=True,choices=issuer_type)

class Thirdparty(models.Model):
    transaction_account = models.IntegerField(null=True)
    name = models.CharField(max_length=15,null=True)
    account = models.ForeignKey(Account,on_delete=models.CASCADE,null=True)
    currency = models.CharField(max_length=3,null=True)
    phone_number = models.IntegerField(null=True)
    location = models.CharField(max_length=15,null=True)
   

class Notification(models.Model):
    name=models.CharField(max_length=20, null=True)
    recipient=models.ForeignKey('Customer', on_delete=models.CASCADE,related_name='Notification_recipient',null=True)
    status=models.BooleanField(null=True)
    date_and_time=models.DateTimeField(default=datetime.now)

class Receipt(models.Model):
    receipt_type = models.CharField(max_length=20,null=True)
    receipt_date = models.DateTimeField()
    total_amount = models.IntegerField(null=True)
    bill_number = models.IntegerField(null=True)
    receipt_file = models.FileField(null=True)

class Loan(models.Model):
    loan_id = models.IntegerField(null=True)
    amount = models.IntegerField(default=0)
    loan_type = models.CharField(max_length=5,null=True)
    wallet = models.ForeignKey(Wallet,on_delete=models.CASCADE,null=True)
    interest_rate = models.IntegerField(null=True)
    loan_Term=models.IntegerField(null=True)
    payment_due_date = models.DateTimeField()
    loan_balance = models.IntegerField(default=0)
    guarantor = models.ForeignKey(Thirdparty,on_delete=models.CASCADE,null=True) 


class Reward(models.Model):
    name = models.CharField(max_length=15,null=True)
    recipient = models.OneToOneField(Account,on_delete=models.CASCADE,null=True)
    bonus =models.IntegerField(null=True)
    gender = models.CharField(max_length=6,null=True)
    reward_points = models.IntegerField(null=True)
    date_of_reward = models.DateTimeField()
    
