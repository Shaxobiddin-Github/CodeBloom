from django.contrib import admin
from django.urls import path, include
from .views import (HomeView, AboutView, ContactView,
                    CoursesView, PlaylistView, profile_view,
                    teachers_profile_view, TeachersView, UpdateView,
                    WatchVideoView, user_login, register_user)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('courses/', CoursesView.as_view(), name='courses'),
    path('playlists/<int:course_id>/', PlaylistView.as_view(), name='playlists'),
    path('profile/', profile_view, name='profile'),
    path('teacher_profile/', teachers_profile_view, name='teacher_profile'),
    path('teachers/', TeachersView.as_view(), name='teachers'),
    path('update/', UpdateView.as_view(), name='update'),
    path('watch_videos/<int:video_id>', WatchVideoView.as_view(), name='watch_videos'),

    path('login/', user_login, name='login'),
    path('register/', register_user, name='register'),
    
]