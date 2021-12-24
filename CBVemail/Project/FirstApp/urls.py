from django.urls import path
from .import views

urlpatterns=[
    path('add/',views.AddView.as_view(),name='add_lap'),
    path('show/',views.ShowView.as_view(),name='show_lap'),
    path('del/<int:i>/',views.DeleteView.as_view(),name='delete_lap'),
    path('upd/<int:i>/',views.Update.as_view(),name='update_lap')
]
