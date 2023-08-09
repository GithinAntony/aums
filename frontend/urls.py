from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('site-admin', views.admin_login, name='site-admin'),
    path('site-admin-dashboard', views.admin_dashboard, name='site-admin-dashboard'),
    path('site-admin-users', views.admin_users, name='site-admin-users'),
    path('site-admin-emp', views.admin_emp, name='site-admin-emp'),
    path('site-admin-record-status/<int:id>/<slug:slug1>/<slug:slug2>', views.admin_record_status,
         name='admin_record_status'),
    path('site-admin-record-delete/<int:id>/<slug:slug1>', views.admin_record_delete, name='admin_record_delete'),
    path('site-admin-property', views.admin_property, name='admin-property'),
    path('site-admin-property-view/<int:id>', views.admin_property_view, name='admin-property-view'),
    path('site-admin-cmessages', views.admin_contactus, name='admin-contactus'),
    path('site-admin-gallery', views.admin_gallery, name='admin-gallery'),
    path('site-admin-custom-delete/<int:id>/<slug:slug>', views.admin_delete, name='admin-delete'),

    path('', views.home, name='home'),
    path('home', views.home, name='home'),

    path('user-login', views.user_login, name='user-login'),
    path('user-register', views.user_register, name='user-register'),
    path('user-dashboard', views.user_dashboard, name='user-dashboard'),
    path('user-listings', views.user_listings, name='user-listings'),
    path('view-listing-details/<int:id>', views.view_listings_details, name='user-listings-details'),
    path('view-listing-advance-pay/<int:id>', views.view_listings_details_advance_pay, name='user-listings-details-advance-pay'),

    path('emp-login', views.emp_login, name='emp-login'),
    path('emp-register', views.emp_register, name='emp-register'),
    path('emp-dashboard', views.emp_dashboard, name='emp-dashboard'),
    path('emp-add-property', views.emp_add_property, name='emp-add-property'),
    path('emp-listings', views.emp_listings, name='emp-listings'),
    path('emp-listings-delete/<int:id>', views.emp_listings_delete, name='emp-listings-delete'),
    path('emp-listings-gallery/<int:property_id>', views.property_gallery, name='emp-listings-gallery'),
    path('emp-listings-gallery-delete/<int:property_id>/<int:id>', views.property_gallery_delete, name='emp-listings-gallery-delete'),
    path('emp-listings-auction/<int:property_id>', views.property_auction, name='emp-listings-auction'),
    path('emp-listings-auction-status/<int:property_id>/<slug:slug>', views.property_auction_status, name='emp-listings-auction-status'),
    path('emp-listings-auction-status-2/<int:id>/<int:property_id>/<slug:slug>', views.property_auction_status_2,
         name='emp-listings-auction-status-2'),

    path('logout', views.logout, name='logout'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('gallery', views.gallery, name='gallery'),

    path('userprofile', views.userprofile, name='userprofile'),
    path('logout', views.logout, name='logout')
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
