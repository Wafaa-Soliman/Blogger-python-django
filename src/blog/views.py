from django.shortcuts import get_object_or_404, render

# Create your views here.
posts=[
    {
        'title': 'التدوينة الأولي',
        'content': 'نص التدوينة الأولي كنص تجريبي',
        'post_date': '10-10-2020',
        'author': 'Wafaa Soliman'
    },
    {
        'title': 'التدوينة الثانية',
        'content': 'نص التدوينة الثانية كنص تجريبي',
        'post_date': '15-10-2020',
        'author': 'Wafaa Soliman'
    },
    {
        'title': 'التدوينة الثالثة',
        'content': 'نص التدوينة الثالثة كنص تجريبي',
        'post_date': '20-10-2020',
        'author': 'Wafaa Soliman'
    },
    {
        'title': 'التدوينة الرابعة',
        'content': 'نص التدوينة الرابعة كنص تجريبي',
        'post_date': '25-10-2020',
        'author': 'Wafaa Soliman'
    },
    {
        'title': 'التدوينة الخامسة',
        'content': 'نص التدوينة الخامسة كنص تجريبي',
        'post_date': '4-10-2020',
        'author': 'Wafaa Soliman'
    },
]

def home(request):
    context = {
        'title': 'الصفحة الرئيسية',
        'posts': posts
    }
    return render(request,'blog/index.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'من أنا'})