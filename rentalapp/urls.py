from django.urls import path

from . import views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index),
    path("index/", views.index, name="index"),
    # path('checkout/', views.checkout),
    path("forgotPswd/", views.forgotPswd, name="forgotPswd"),
    path('resetPswd/<str:token>/', views.reset_password, name='resetPswd'),
    path("checkout/<int:id>", views.checkout),
    path("checkoutform", views.checkoutform),
    path("services/", views.services),
    path("vehicles", views.vehicles),
    path("contact", views.contact),
    path("showdata", views.showdata),
    path("checklogin", views.checklogin),
    path("contactdata", views.contactdata),
    path("feedback", views.feedbackpage),
    path("feedbackshow", views.feedbackshow),
    path("logout", views.logout),
    path("booking", views.bookingshow),
    path("bookingpage", views.bookingpage),
    path("termsandconpage", views.termsandconpage),
    path("myprofile", views.myprofile),
    path("inbox", views.inbox),
    path("helps", views.helps),
    path("settings", views.settings),
    path('invoice/<str:t_no>/',views.invoice.as_view(),name='invoice'),
    path('imageUpload',views.imageUpload,name="imageUpload"),
    path('cancel/<str:t_no>/',views.cancel.as_view(),name="cancel")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
