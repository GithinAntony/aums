from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

# Create your views here.
def admin_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data_record = form.cleaned_data
            if Admin.objects.filter(username=data_record['username']) and Admin.objects.filter(
                    password=data_record['password']):
                user_details = Admin.objects.get(username=data_record['username'], password=data_record['password'])
                request.session['is_logged_in'] = True
                request.session['email'] = ''
                request.session['full_name'] = ''
                request.session['user_id'] = user_details.id
                request.session['username'] = user_details.username
                request.session['usertype'] = 'admin'
                return redirect('/site-admin-dashboard')
            else:
                messages.error(request, 'Invalid Credentials!')
                return redirect('/site-admin')
    context = {'form': form}
    return render(request, 'admin-login.html',context)

def admin_dashboard(request):
    return render(request, 'admin-dashboard.html')

def admin_users(request):
    record_details = User.objects.filter(usertype='user').all()
    context = {'record_details': record_details}
    return render(request, 'admin-users.html', context)

def admin_property(request):
    property = Property.objects.filter().all()
    context = {'property': property}
    return render(request, 'admin-property.html', context)

def admin_property_view(request, id):
    property = Property.objects.get(id=id)
    auction_details = AuctionDetails.objects.filter(property=Property.objects.get(id=id)).all()
    context = {'property': property, 'auction_details': auction_details}
    return render(request, 'admin-property-view.html', context)

def admin_emp(request):
    record_details = User.objects.filter(usertype='employee').all()
    context = {'record_details': record_details}
    return render(request, 'admin-emp.html', context)

def admin_record_status(request, id, slug1, slug2):
    if slug1 == 'users':
      record = User.objects.get(id=id)
      record.status = slug2
      record.save()
      messages.error(request, 'User status updated!')
      return redirect('/site-admin-users')
    elif slug1 == 'emp':
        record = User.objects.get(id=id)
        record.status = slug2
        record.save()
        messages.error(request, 'Employee status updated!')
        return redirect('/site-admin-emp')

def admin_record_delete(request, id, slug1):
    if slug1 == 'users':
       User.objects.filter(id=id).delete()
       messages.error(request, 'User deleted!')
       return redirect('/site-admin-users')
    elif slug1 == 'emp':
      User.objects.filter(id=id).delete()
      messages.error(request, 'Employee deleted!')
      return redirect('/site-admin-emp')
    elif slug1 == 'gallery':
      Gallery.objects.filter(id=id).delete()
      messages.error(request, 'Image deleted!')
      return redirect('/site-admin-gallery')
    elif slug1 == 'cmessages':
      Contact_message.objects.filter(id=id).delete()
      messages.error(request, 'Messages deleted!')
      return redirect('/site-admin-cmessages')


def admin_contactus(request):
    context = {'record_details': Contact_message.objects.filter()}
    return render(request, 'admin-cmessages.html', context)


def admin_gallery(request):
    form = GalleryForm()
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['photos']
            fs = FileSystemStorage()
            file_name = fs.save(uploaded_file.name, uploaded_file)
            data_record = form.cleaned_data
            gallery = Gallery(
                photos=fs.url(file_name),
                text=data_record['text'],
            )
            gallery.save()
            messages.success(request, 'Image added successfully!')
            return redirect('/site-admin-gallery')
    context = {'form': form, 'gallery': Gallery.objects.filter()}
    return render(request, 'admin-gallery.html', context)


def admin_delete(request, id, slug):
    if slug == 'gallery':
        Gallery.objects.filter(id=id).delete()
        messages.error(request, 'Image deleted!')
        return redirect('/admin-gallery')
    elif slug == 'contact':
        Contact_message.objects.filter(id=id).delete()
        messages.error(request, 'Messages deleted!')
        return redirect('/admin-cmessages')

def home(request):
    property = Property.objects.all()
    context = {'property': property}
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def gallery(request):
    context = {'gallery': Gallery.objects.filter()}
    return render(request, 'gallery.html', context)

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data_record = form.cleaned_data
            contact = Contact_message(
            name=data_record['name'],
            email=data_record['email'],
            message=data_record['message'],
            )
            contact.save()
            messages.success(request, 'Message registered successfully!')
            return redirect('/contact')
    context = {'form': form}
    return render(request, 'contact.html', context)

def user_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data_record = form.cleaned_data
            if User.objects.filter(username=data_record['username'],password=data_record['password'],usertype='user'):
               user_details = User.objects.get(username=data_record['username'],password=data_record['password'],usertype='user')
               if user_details.status == 'active':
                     request.session['is_logged_in'] = True
                     request.session['email'] = user_details.email
                     request.session['full_name'] = user_details.name
                     request.session['user_id'] = user_details.id
                     request.session['username'] = user_details.username
                     request.session['usertype'] = user_details.usertype
                     return redirect('/user-dashboard')
               else:
                   messages.error(request, 'User is suspended. Contact the admin!')
                   return redirect('/user-login')
            else:
               messages.error(request, 'Invalid Credentials!')
               return redirect('/user-login')
    context = {'form': form}
    return render(request, 'user-login.html', context)

def user_register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            data_record = form.cleaned_data
            user = User(
            name=data_record['name'],
            email=data_record['email'],
            username=data_record['username'],
            password=data_record['password'],
            phone=data_record['phone'],
            address=data_record['address'],
            status='suspend',
            usertype='user',
            )
            user.save()
            messages.success(request, 'User registered successfully!')
            return redirect('/user-login')
    context = {'form': form}
    return render(request, 'user-register.html', context)

def user_dashboard(request):
    return render(request, 'user-dashboard.html')

def user_listings(request):
    property = Property.objects.all()
    context = {'property': property}
    return render(request, 'user-listings.html', context)


def view_listings_details(request,id):
    form = ViewListingDetail()
    auction_details = AuctionDetails.objects.filter(user=User.objects.get(id=request.session['user_id']),property=Property.objects.get(id=id)).first()
    if request.method == 'POST':
        form = ViewListingDetail(request.POST)
        if form.is_valid():
           data_record = form.cleaned_data
           if auction_details:
             record = AuctionDetails.objects.get(id=auction_details.id)
             record.amount = data_record['amount']
             record.save()
             messages.success(request, 'Bid updated successfully!')
           else:
             auction_details1 = AuctionDetails(
             amount=data_record['amount'],
             user=User.objects.get(id=request.session['user_id']),
             property=Property.objects.get(id=id)
             )
             auction_details1.save()
             messages.success(request, 'Bid added successfully!')
           return redirect('/view-listing-details/'+str(id))
    property = Property.objects.get(id=id)
    property_gallery = Property_gallery.objects.filter(property=Property.objects.get(id=id)).all()
    auction_details_bids = AuctionDetails.objects.filter(property=Property.objects.get(id=id)).all().order_by('-amount')
    context = {'property': property,'property_gallery':property_gallery,'auction_details':auction_details,'auction_details_bids':auction_details_bids,'form':form}
    return render(request, 'user-listings-details.html', context)

def view_listings_details_advance_pay(request,id):
    form = UserAdvancePay()
    auction_details_bids = AuctionDetails.objects.filter(id=id).get()
    if request.method == 'POST':
        form = UserAdvancePay(request.POST)
        if form.is_valid():
            data_record = form.cleaned_data
            record = AuctionDetails.objects.get(id=id)
            record.card_name=data_record['name_on_card']
            record.card_number=data_record['credit_card_number']
            record.exp_date=data_record['expiration']
            record.cvc=data_record['cvc']
            record.card_type=data_record['payment_type']
            record.advance_amount=record.amount*0.1
            record.save()
            messages.success(request, 'Advance payment added successfully!')
        return redirect('/view-listing-details/' + str(auction_details_bids.property_id))
    context = {'auction_details_bids':auction_details_bids,'form': form}
    return render(request, 'user-listings-details-advance-pay.html', context)

def emp_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data_record = form.cleaned_data
            if User.objects.filter(username=data_record['username'],password=data_record['password'],usertype='employee'):
               user_details = User.objects.get(username=data_record['username'],password=data_record['password'],usertype='employee')
               if user_details.status == 'active':
                     request.session['is_logged_in'] = True
                     request.session['email'] = user_details.email
                     request.session['full_name'] = user_details.name
                     request.session['user_id'] = user_details.id
                     request.session['username'] = user_details.username
                     request.session['usertype'] = user_details.usertype
                     return redirect('/emp-dashboard')
               else:
                   messages.error(request, 'Employee is suspended. Contact the admin!')
                   return redirect('/emp-login')
            else:
               messages.error(request, 'Invalid Credentials!')
               return redirect('/emp-login')
    context = {'form': form}
    return render(request, 'emp-login.html', context)

def emp_register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            data_record = form.cleaned_data
            user = User(
            name=data_record['name'],
            email=data_record['email'],
            username=data_record['username'],
            password=data_record['password'],
            phone=data_record['phone'],
            address=data_record['address'],
            status='suspend',
            usertype='employee',
            )
            user.save()
            messages.success(request, 'Employee registered successfully!')
            return redirect('/emp-login')
    context = {'form': form}
    return render(request, 'emp-register.html', context)

def emp_dashboard(request):
    return render(request, 'emp-dashboard.html')

def emp_add_property(request):
    form = AddNewPropertyForm()
    if request.method == 'POST':
        form = AddNewPropertyForm(request.POST,request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['image']
            fs = FileSystemStorage()
            file_name = fs.save(uploaded_file.name, uploaded_file)
            property = Property(
                user=User.objects.get(id=request.session['user_id']),
                title=request.POST['title'],
                description=request.POST['description'],
                image = fs.url(file_name),
                location=request.POST['location'],
                type=request.POST['type'],
                reserve_price=request.POST['reserve_price'],
                intial_quote_amount=request.POST['initial_amount'],
                mobile=request.POST['mobile_no'],
                status = 'active'
            )
            property.save()
            messages.success(request, 'Item added!')
            return redirect('/emp-listings')
    context = {'form': form}
    return render(request, 'emp-add-property.html',context)

def emp_listings(request):
    property = Property.objects.filter(user=User.objects.get(id=request.session['user_id'])).all()
    context = {'property': property}
    return render(request, 'emp-listings.html', context)

def property_auction(request,property_id):
    property = Property.objects.get(id=property_id)
    auction_details = AuctionDetails.objects.filter(property=Property.objects.get(id=property_id)).all()
    context = {'property': property,'auction_details':auction_details}
    return render(request, 'emp-property-auction.html', context)

def property_auction_status(request,property_id, slug):
      record = Property.objects.get(id=property_id)
      record.auction_status = slug
      record.save()
      if slug == 'opened':
        messages.success(request, 'Auction is opened! Wait for the people to add thir quotes!')
      else:
          messages.error(request, 'Auction is closed! Find the best quote and accept it to proceed further!')
      return redirect('/emp-listings-auction/'+str(property_id))

def property_auction_status_2(request, id, property_id, slug):
    record = AuctionDetails.objects.get(id=id)
    record.status = 'yes'
    record.save()
    record1 = Property.objects.get(id=property_id)
    record1.auction_status = 'closed'
    record1.final_status = 'yes'
    record1.save()
    messages.success(request, 'Auction is accepted! And its closed!')
    return redirect('/emp-listings-auction/' + str(property_id))


def emp_listings_delete(request, id):
    Property.objects.filter(id=id).delete()
    messages.error(request, 'Property deleted!')
    return redirect('/emp-listings')
    return render(request, 'emp-listings.html', context)

def property_gallery(request, property_id):
    property_gallery = Property_gallery.objects.filter(property=Property.objects.get(id=property_id),user=User.objects.get(id=request.session['user_id']))
    form = PropertyGallery()
    if request.method == 'POST':
        form = PropertyGallery(request.POST,request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['main_photo']
            fs = FileSystemStorage()
            file_name = fs.save(uploaded_file.name, uploaded_file)
            property_gallery = Property_gallery(
                user=User.objects.get(id=request.session['user_id']),
                property=Property.objects.get(id=property_id),
                image=fs.url(file_name),
            )
            property_gallery.save()
            messages.success(request, 'Image added successfully')
            return redirect('/emp-listings-gallery/'+str(property_id))
    context = {'property_gallery': property_gallery, 'form':form }
    return render(request, 'emp-listings-gallery.html', context)

def property_gallery_delete(request,property_id,id):
    Property_gallery.objects.filter(id=id).delete()
    messages.error(request, 'Image deleted!')
    return redirect('/emp-listings-gallery/'+str(property_id))

def userprofile(request):
    context = { 'user' : User.objects.filter(username=request.session['username']) }
    return render(request, 'userprofile.html', context )

def logout(request):
    del request.session['is_logged_in']
    del request.session['username']
    return redirect('/home')