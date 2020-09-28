from django.urls import path, include
from . import views
from django.views.decorators.cache import cache_page
app_name = "core"


urlpatterns = [

    path('', cache_page(60 * 15)(views.HomeView.as_view()), name="home"),
    path('shop/', cache_page(60 * 15)(views.ShopView.as_view()), name="shop"),
    path('about-us/', cache_page(60 * 15)
         (views.AboutView.as_view()), name="about"),
    path('product/<slug>', cache_page(60 * 15)
         (views.DetailView.as_view()), name="details"),
    path('cart/', cache_page(60 * 15)(views.CartView.as_view()), name="cart"),
    path('checkout/', views.CheckoutView.as_view(), name="checkout"),
    path('faq/', cache_page(60 * 15)(views.FaqView.as_view()), name="faq"),
    path('contact/', cache_page(60 * 15)
         (views.ContactView.as_view()), name="contact"),
    path('contact/success/', views.ContactSuccessView.as_view(),
         name="contact-success"),

    path('login/', cache_page(60 * 15)(views.LoginView.as_view()), name="login"),
    path('signup/', views.SignupView.as_view(), name="signup"),
    path('forgot-password/', views.ForgotView.as_view(), name="forgot"),
    path('payment/success/', cache_page(60 * 15)
         (views.ConfirmView.as_view()), name="pay"),
    path('payment/receipt/', cache_page(60 * 15)
         (views.PaystackView.as_view()), name="payment"),
    path('dashboard/', cache_page(60 * 15)
         (views.DashboardView.as_view()), name="dashboard"),
    path('dashboard/orders/', cache_page(60 * 15)
         (views.OrderView.as_view()), name="order"),

    path('dashboard/address/', cache_page(60 * 15)
         (views.AddressView.as_view()), name="address"),
    path('wishlist/<slug>/', views.wishlist, name="wishlist"),
    path('wishlist/home/<slug>/', views.wishlist_home, name="wishlist-home"),
    path('add_to_cart/<slug>', views.add_to_cart, name='add-to-cart'),
    #    path('pricing/', views.PricingView.as_view(), name="pricing" ),
    path('remove-from-cart/<slug>/',
         views.remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/',  views.remove_single_item_from_cart,
         name='remove-single-item-from-cart'),

    # path('newsletter/', views.newsletter, name="newsletter"),
    path('dashboard/order/<pk>', cache_page(60 * 15)
         (views.OrderDetailView.as_view()), name='ordered-detail'),
    path('wishlist/product/<slug>/',
         views.wishlist_product, name='wishlist-product'),
    path('category/<slug>/', cache_page(60 * 15)
         (views.CategoryView), name='categoryview'),

























]
