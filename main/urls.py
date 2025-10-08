from django.urls import path
from main.views import show_main, show_xml, show_json, show_xml_by_id, show_json_by_id, add_product, show_product, like_product, register, login_user, logout_user, edit_product, delete_product, add_product_entry_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<uuid:id>/', show_xml_by_id, name='show_xml_by_id'), 
    path('json/<uuid:id>/', show_json_by_id, name='show_json_by_id'),  # <--- UUID sekarang
    path('add_product/', add_product, name='add_product'),
    path('product/<uuid:id>/', show_product, name='show_product'),
    path('like/<uuid:id>/', like_product, name='like_product'),
    path('register/', register, name='register'), 
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('product/<uuid:id>/edit', edit_product, name='edit_product'),
    path('product/<uuid:id>/delete', delete_product, name='delete_product'),
    path('add-product-ajax', add_product_entry_ajax, name='add_product_entry_ajax'),
]