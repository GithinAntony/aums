from django.db import models
from django.utils.timezone import now

# Create your models here.
class Admin(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    username = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.username

class User(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=100,default='', null=False)
    email = models.CharField(max_length=255,default='', null=False)
    username = models.CharField(max_length=100,default='', null=False)
    password = models.CharField(max_length=500,default='', null=False)
    phone = models.CharField(max_length=15,default='', null=False)
    address = models.TextField(default='',null=False)
    usertype_choices = [
        ('admin', 'Admin'),
        ('user', 'User'),
        ('employee','Employee'),
    ]
    usertype = models.CharField(max_length=8, choices=usertype_choices, default="user")
    status_choices = [
        ('active', 'Active'),
        ('suspend', 'Suspend'),
    ]
    status = models.CharField(max_length=7, choices=status_choices, default="active")

    def __str__(self):
        return self.name


class Fback(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    username = models.CharField(max_length=100, null=True)
    feedback = models.CharField(max_length=255, null=True)
    response = models.CharField(max_length=25, null=True)

    def __str__(self):
        return self.name     


class Reg(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    Image = models.CharField(max_length=100, null=True)
    Name = models.CharField(max_length=255, null=True)
    Dob = models.CharField(max_length=25, null=True)
    Gender = models.CharField(max_length=255, null=True)
    Address = models.CharField(max_length=15, null=True)
    Mobileno = models.CharField(max_length=15, null=True)
    Nationality = models.CharField(max_length=255, null=True)
    Emailid = models.TextField(null=True)
    Username = models.CharField(max_length=255, null=True)
    Password = models.CharField(max_length=50, null=True)
    Status = models.TextField(null=True)

    def __str__(self):
        return self.name


class Emp(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    Image = models.CharField(max_length=100, null=True)
    Name = models.CharField(max_length=255, null=True)
    Dob = models.CharField(max_length=25, null=True)
    Gender = models.CharField(max_length=255, null=True)
    Address = models.CharField(max_length=15, null=True)
    Mobileno = models.TextField(null=True)
    Qualification = models.CharField(max_length=255, null=True)
    Emailid = models.IntegerField(null=True)
    Username = models.CharField(max_length=255, null=True)
    Password = models.CharField(max_length=15, null=True)
    Status = models.TextField(null=True)

    def __str__(self):
        return self.name     

class Salary(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=100, null=True)
    amount = models.CharField(max_length=255, null=True)
    sdate = models.CharField(max_length=25, null=True)
    username = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name        


class Amount(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=100, null=True)
    amount = models.CharField(max_length=255, null=True)
    tamo = models.CharField(max_length=25, null=True)
    result = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class Property(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    image = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=255, null=True)
    type = models.CharField(max_length=25, null=True)
    reserve_price = models.FloatField(null=True)
    intial_quote_amount = models.FloatField(null=True)
    mobile = models.CharField(max_length=15, null=True)
    date  = models.CharField(max_length=100, null=True)
    stime = models.CharField(max_length=100, null=True)
    etime = models.CharField(max_length=100, null=True)
    status_choices = [
        ('active', 'Active'),
        ('suspend', 'Suspend'),
    ]
    status = models.CharField(max_length=7, choices=status_choices, default="active")
    status_choices = [
        ('opened', 'Opened'),
        ('closed', 'Closed'),
    ]
    auction_status = models.CharField(max_length=7, choices=status_choices, default="closed")
    def __str__(self):
        return self.title
    choices = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    final_status = models.CharField(max_length=7, choices=choices, default="no")

class Property_gallery(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    property = models.ForeignKey("Property",on_delete=models.SET_NULL,null=True)
    user = models.ForeignKey("User",on_delete=models.SET_NULL,null=True)
    image = models.CharField(max_length=25, null=True)

    def __str__(self):
        return self.place

class Contact_message(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=255, null=True)
    message = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.name

class Gallery(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    photos = models.CharField(max_length=255, null=True)
    text = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.photos

class AuctionDetails(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    property = models.ForeignKey("Property",on_delete=models.SET_NULL,null=True)
    user = models.ForeignKey("User",on_delete=models.SET_NULL,null=True)
    amount = models.FloatField(null=True)
    choices = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    winner = models.CharField(max_length=7, choices=choices, default="no")
    choices = [
        ('opened', 'Opened'),
        ('closed', 'Closed'),
    ]
    status = models.CharField(max_length=7, choices=choices, default="opened")
    date_added = models.DateTimeField(default=now, editable=False)
    card_name = models.TextField(max_length=255, null=True)
    card_number = models.IntegerField(null=True)
    exp_date = models.TextField(max_length=255, null=True)
    cvc = models.IntegerField(null=True)
    choices = [
        ('debit_card', 'Debit Card'),
        ('credit_card', 'Credit Card'),
    ]
    card_type = models.CharField(max_length=11, choices=choices, default="debit_card"),
    advance_amount = models.FloatField(null=True)



