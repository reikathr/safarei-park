from django.urls import path
from main.views import show_main, create_animal, show_xml, show_json
from main.views import show_xml_by_id, show_json_by_id
from main.views import register, login_user, logout_user, update_animal_amount, get_animal_json, add_animal_ajax, delete_animal_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-animal', create_animal, name='create_animal'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('update-amount', update_animal_amount, name='update_amount'),
    path('get-animal/', get_animal_json, name='get_animal_json'),
    path('add-animal-ajax/', add_animal_ajax, name='add_animal_ajax'),
    path('delete-animal-ajax/', delete_animal_ajax, name='delete_animal_ajax'),
]