from django.shortcuts import render, get_object_or_404
from .models import Course, Video, Teacher, Comment, Student, SavedVideo, Enrollment,  Like,  Comment, Playlist

from django.views import View

# Bosh sahifa ko‘rinishi
class HomeView(View):
    def get(self, request):
        # Kurslar va ular haqidagi ma'lumotlarni olish
        all_courses = Course.objects.all()
        start_course = all_courses.order_by('-created_at')

        context = {
            'all_courses': all_courses,
            'start_course': start_course,
        }
        return render(request, 'home.html', context)


# Biz haqimizda sahifasi
class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')


# Aloqa sahifasi
class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')


# Kurslar sahifasi
class CoursesView(View):
    def get(self, request):
        # Barcha kurslarni olish
        all_courses = Course.objects.all()
        start_course = all_courses.order_by('-created_at')

        context = {
            'all_courses': all_courses,
            'start_course': start_course,
        }
        return render(request, 'courses.html', context)


# Kursning barcha videolarini ko‘rish uchun oynasi
class PlaylistView(View):
    def get(self, request, course_id):
        # Tanlangan kursni olish
        course = get_object_or_404(Course, id=course_id)
        videos = course.videos.all()  # Kursga tegishli videolarni olish
        video_count = videos.count()  # Videolar sonini hisoblash

        context = {
            'course': course,
            'videos': videos,
            'video_count': video_count,
        }
        return render(request, 'playlist.html', context)


# Profil sahifasi
class ProfileView(View):
    def get(self, request):
        return render(request, 'profile.html')


# O‘qituvchilar uchun profil sahifasi
class TeacherProfileView(View):
    def get(self, request, teacher_id):
        # Teacher modelidan user id orqali teacher ni olish
        teacher = get_object_or_404(Teacher, user__id=teacher_id)  # Userning id orqali Teacher'ni olish

        context = {
            'teacher': teacher,
        }
        return render(request, 'teacher_profile.html', context)


# O‘qituvchilar ro‘yxati sahifasi
class TeachersView(View):
    def get(self, request):
        # O‘qituvchilar haqidagi ma'lumotlarni olish
        all_teachers = Teacher.objects.all()

        context = {
            'all_teachers': all_teachers,
        }
        return render(request, 'teachers.html', context)


# Yangilash sahifasi
class UpdateView(View):
    def get(self, request):
        return render(request, 'update.html')


# Videoni tomosha qilish sahifasi
class WatchVideoView(View):
    def get(self, request, video_id):
        # Tanlangan videoni olish
        video = get_object_or_404(Video, id=video_id)
        course = video.course  # Ushbu video tegishli kursni olish

        context = {
            'course': course,
            'video': video,
        }
        return render(request, 'watch_video.html', context)
