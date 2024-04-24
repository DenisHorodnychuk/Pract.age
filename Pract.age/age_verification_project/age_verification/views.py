from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html')

def home_18plus(request):
    age_cookie = request.COOKIES.get('user_age')
    if age_cookie:
        age = int(age_cookie)
    else:
        age = None
    if age and age >= 18:
        return render(request, 'home_18plus.html', {'age': age})
    else: 
        return redirect('home')

def set_age_cookie(request):
    if request.method == 'POST':
        age = request.POST.get('age')
        response = redirect('home')
        response.set_cookie('user_age', age)
        return response

