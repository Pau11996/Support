from django.urls import path
from rest_framework import routers
from .views import TicketView, \
    UpdateMessageView, \
    CreateListMessageView,\
    DestroyMessageView


router = routers.SimpleRouter()
router.register('tickets', TicketView)


urlpatterns = [
    path('tickets/<int:pk>/messages/', CreateListMessageView.as_view({'get': 'list',
                                                                      'post': 'create', })),
    path('tickets/<int:pk>/messages/<int:update_message_pk>', UpdateMessageView.as_view()),
    path('tickets/<int:pk>/messages/<int:delete_message_pk>', DestroyMessageView.as_view()),

]

urlpatterns += router.urls
