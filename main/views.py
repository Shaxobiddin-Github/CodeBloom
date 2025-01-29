from django.core.files.storage import default_storage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Video, Teacher, Profile, Comment, Student, SavedVideo, Enrollment,  Like,  Comment, Playlist

from django.views import View

# Bosh sahifa ko‘rinishi
class HomeView(View):
    def get(self, request):
        # Kurslar va ular haqidagi ma'lumotlarni olish
        all_courses = Course.objects.all()
        start_course = all_courses.order_by('-created_at')
        is_teacher = request.user.groups.filter(name='Teachers').exists()
        profile = get_object_or_404(Profile, user=request.user)  # User asosida profile topamiz

        

        context = {
            'all_courses': all_courses,
            'start_course': start_course,
            'is_teacher': is_teacher,  # Teacherni aniq qilish
        }
        return render(request, 'home.html', context)


# Biz haqimizda sahifasi
class AboutView(View):
    def get(self, request):
        profile = get_object_or_404(Profile, user=request.user)  # User asosida profile topamiz
        is_teacher = request.user.groups.filter(name='Teachers').exists()
        context = {
            'is_teacher': is_teacher,  # Teacherni aniq qilish
            'profile': profile,  # User asosida profile topamiz
        }
        return render(request, 'about.html', context)


# Aloqa sahifasi
class ContactView(View):
    def get(self, request):
        profile = get_object_or_404(Profile, user=request.user)  # User asosida profile topamiz
        is_teacher = request.user.groups.filter(name='Teachers').exists()
        context = {
            'is_teacher': is_teacher,  # Teacherni aniq qilish
            'profile': profile,  # User asosida profile topamiz
        }
        return render(request, 'about.html', context)


# Kurslar sahifasi
class CoursesView(View):
    def get(self, request):
        # Barcha kurslarni olish
        all_courses = Course.objects.all()
        start_course = all_courses.order_by('-created_at')
        profile = get_object_or_404(Profile, user=request.user)  # User asosida profile topamiz
        is_teacher = request.user.groups.filter(name='Teachers').exists()

        context = {
            'all_courses': all_courses,
            'start_course': start_course,
            'is_teacher': is_teacher,  # Teacherni aniq qilish
            'profile': profile,  # User asosida profile topamiz
        }
        return render(request, 'courses.html', context)


# Kursning barcha videolarini ko‘rish uchun oynasi
class PlaylistView(View):
    def get(self, request, course_id):
        # Tanlangan kursni olish
        course = get_object_or_404(Course, id=course_id)
        videos = course.videos.all()  # Kursga tegishli videolarni olish
        video_count = videos.count()  # Videolar sonini hisoblash
        profile = get_object_or_404(Profile, user=request.user)  # User asosida profile topamiz
        is_teacher = request.user.groups.filter(name='Teachers').exists()

        context = {
            'course': course,
            'videos': videos,
            'video_count': video_count,
            'is_teacher': is_teacher,  # Teacherni aniq qilish
            'profile': profile,  # User asosida profile topamiz
        }
        return render(request, 'playlist.html', context)


# Profil sahifasi
@login_required(login_url='login')
def profile_view(request):
    profile = get_object_or_404(Profile, user=request.user)  # User asosida profile topamiz
    is_teacher = request.user.groups.filter(name='Teachers').exists()
    return render(request, 'profile.html', {'profile': profile, 'is_teacher': is_teacher})







# O‘qituvchilar uchun profil sahifasi
@login_required(login_url='login')
def teachers_profile_view(request):
    teacher = get_object_or_404(Teacher, user=request.user)
    profile = get_object_or_404(Profile, user=request.user)  # User asosida profile topamiz
    is_teacher = request.user.groups.filter(name='Teachers').exists()
    context = {
        'teacher': teacher,
        'profile': profile,
        'is_teacher': is_teacher,  # Teacherni aniq qilish
    }
    return render(request, 'teacher_profile.html', context)


# O‘qituvchilar ro‘yxati sahifasi
class TeachersView(View):
    def get(self, request):

        all_teachers = Teacher.objects.all()
        profile = get_object_or_404(Profile, user=request.user)  # User asosida profile topamiz
        is_teacher = request.user.groups.filter(name='Teachers').exists()


        context = {
            'all_teachers': all_teachers,
            'is_teacher': is_teacher,  # Teacherni aniq qilish
            'profile': profile,  # User asosida profile topamiz
        }
        return render(request, 'teachers.html', context)


# Yangilash sahifasi
class UpdateView(View):
    def get(self, request):
        profile = get_object_or_404(Profile, user=request.user)  # User asosida profile topamiz
        is_teacher = request.user.groups.filter(name='Teachers').exists()

        context = {
            'is_teacher': is_teacher,  # Teacherni aniq qilish
            'profile': profile,  # User asosida profile topamiz
        }

        return render(request, 'update.html', context)


# Videoni tomosha qilish sahifasi
class WatchVideoView(View):
    def get(self, request, video_id):
        # Tanlangan videoni olish
        video = get_object_or_404(Video, id=video_id)
        course = video.course  # Ushbu video tegishli kursni olish
        profile = get_object_or_404(Profile, user=request.user)  # User asosida profile topamiz
        is_teacher = request.user.groups.filter(name='Teachers').exists()

        context = {
            'course': course,
            'video': video,
            'is_teacher': is_teacher,  # Teacherni aniq qilish
            'profile': profile,  # User asosida profile topamiz
        }
        return render(request, 'watch_video.html', context)








def user_login(request):
    profile = get_object_or_404(Profile, user=request.user)  # User asosida profile topamiz
    is_teacher = request.user.groups.filter(name='Teachers').exists()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home after login
        else:
            messages.error(request, 'Invalid username or password!')

    context = {
            'is_teacher': is_teacher,  # Teacherni aniq qilish
            'profile': profile,  # User asosida profile topamiz,
        }
    return render(request, 'login.html', context)






def register_user(request):
    profile = get_object_or_404(Profile, user=request.user)  # User asosida profile topamiz
    is_teacher = request.user.groups.filter(name='Teachers').exists()
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        profile_picture = request.FILES.get('profile_picture')


        # 🔴 Parollar bir-biriga mosligini tekshiramiz
        if password1 != password2:
            return render(request, 'register.html', {'error': "Passwords do not match!"})

        # 🔴 Foydalanuvchi mavjudligini tekshiramiz
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': "Username already taken!"})
        if User.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error': "Email already in use!"})

        # 🟢 Yangi user yaratamiz
        user = User.objects.create_user(username=username, email=email, password=password1)

        # 🟢 Profil rasmi saqlash
        profile = Profile(user=user, profile_picture=profile_picture)
        profile.save()

        # 🔵 Userni tizimga kiritamiz (login)
        login(request, user)
        return redirect('home')  # Bosh sahifaga yo‘naltiramiz
    context = {
        'is_teacher': is_teacher,  # Teacherni aniq qilish
        'profile': profile,  # User asosida profile topamiz,
    }  

    return render(request, 'register.html', context)

