from django.shortcuts import render
from django.db import connections
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from .models import Post




@login_required
def home_view(request):
    user_groups = request.user.groups.values_list('name', flat=True)

    posts = Post.objects.filter(grade__in=user_groups)  # فیلتر بر اساس نام گروه‌ها

    if request.user.groups.filter(name='0').exists():
        all_posts = Post.objects.all()
        posts = posts.union(all_posts)

    context = {'posts': posts, 'username': request.user.username}
    return render(request, 'home.html', context)


# @login_required
# def home_view(request):
#     user_groups = request.user.groups.values_list('name', flat=True)

#     posts = Post.objects.filter(grade__in=user_groups)  # فیلتر بر اساس نام گروه‌ها

#     context = {'posts': posts, 'username': request.user.username}
#     return render(request, 'home.html', context)



# @login_required
# def home_view(request):
#     # اتصال به پایگاه داده
#     cursor = connections['lib'].cursor()

#     # اجرای کوئری
#     cursor.execute("SELECT * FROM posts")

#     # دریافت ردیف‌های نتیجه
#     rows = cursor.fetchall()

#     # تبدیل نتیجه به لیست دیکشنری‌ها
#     posts = []
#     for row in rows:
#         post = {
#             'title': row[1],
#             'content': row[2],
#             'url': row[3],
#             'grade': row[4]
#         }
#         # اضافه کردن پست به لیست فقط اگر شرایط را برآورده کند
#         if request.user.groups.filter(name='10').exists() and post['grade'] == 10:
#             posts.append(post)
#         elif request.user.groups.filter(name='11').exists() and post['grade'] == 11:
#             posts.append(post)
#         elif request.user.groups.filter(name='12').exists() and post['grade'] == 12:
#             posts.append(post)
#         elif request.user.groups.filter(name='0').exists():
#             posts.append(post)

#     # بستن اتصال
#     cursor.close()

#     # ارسال اطلاعات به تمپلیت
#     context = {'posts': posts, 'username': request.user.username}
#     return render(request, 'home.html', context)








# @login_required
# def home_view(request):
#     # اتصال به پایگاه داده
#     cursor = connections['lib'].cursor()

#     # اجرای کوئری
#     cursor.execute("SELECT * FROM posts")

#     # دریافت ردیف‌های نتیجه
#     rows = cursor.fetchall()

#     # تبدیل نتیجه به لیست دیکشنری‌ها
#     posts = []
#     for row in rows:
#         post = {
#             'title': row[1],
#             'content': row[2],
#             'url': row[3],
#             'grade': row[4]
#         }
#         posts.append(post)

#     # بستن اتصال
#     cursor.close()

#     # ارسال اطلاعات به تمپلیت
#     context = {'posts': posts, 'username': request.user.username}
#     return render(request, 'home.html', context)
