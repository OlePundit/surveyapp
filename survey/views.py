from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Survey

# Create your views here.


def index(request):
    surveys = Survey.objects.all()
    return render(request, 'index.html', {'surveys':surveys})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['username']
        password = request.POST['username']
        password2 = request.POST['username']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('register')

            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Used')
                return redirect('register')

            else:
                user = User.objects.create_user(username = username, email = email, password = password)
                user.save();
                return redirect('index')


        else:
            messages.info(request, 'Password Not The Same')
            return redirect('register')

    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username,password = password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')

        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')

    else:
        return render(request, 'login.html')

def businesses(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        description = request.POST.get('description')
        location = request.POST.get('location')
        image = request.FILES.get('image')
        question1 = request.POST.get('question1')
        questiontype1=request.POST.get('questiontype1')
        choice1a=request.POST.get('choice1a')
        choice2a=request.POST.get('choice2a')
        choice3a=request.POST.get('choice3a')
        choice4a=request.POST.get('choice4a')
        question2 = request.POST.get('question2')
        questiontype2=request.POST.get('questiontype2')
        choice1b=request.POST.get('choice1b')
        choice2b=request.POST.get('choice2b')
        choice3b=request.POST.get('choice3b')
        choice4b=request.POST.get('choice4b')
        question3 = request.POST.get('question3')
        questiontype3=request.POST.get('questiontype3')
        choice1c=request.POST.get('choice1c')
        choice2c=request.POST.get('choice2c')
        choice3c=request.POST.get('choice3c')
        choice4c=request.POST.get('choice4c')
        question4 = request.POST.get('question4')
        questiontype4=request.POST.get('questiontype4')
        choice1d=request.POST.get('choice1d')
        choice2d=request.POST.get('choice2d')
        choice3d=request.POST.get('choice3d')
        choice4d=request.POST.get('choice4d')
        question5 = request.POST.get('question5')
        questiontype5=request.POST.get('questiontype5')
        choice1e=request.POST.get('choice1e')
        choice2e=request.POST.get('choice2e')
        choice3e=request.POST.get('choice3e')
        choice4e=request.POST.get('choice4e')
        question6 = request.POST.get('question6')
        questiontype6=request.POST.get('questiontype6')
        choice1f=request.POST.get('choice1f')
        choice2f=request.POST.get('choice2f')
        choice3f=request.POST.get('choice3f')
        choice4f=request.POST.get('choice4f')
        question7 = request.POST.get('question7')
        questiontype7=request.POST.get('questiontype7')
        choice1g=request.POST.get('choice1g')
        choice2g=request.POST.get('choice2g')
        choice3g=request.POST.get('choice3g')
        choice4g=request.POST.get('choice4g')
        question8 = request.POST.get('question8')
        questiontype8=request.POST.get('questiontype8')
        choice1h=request.POST.get('choice1h')
        choice2h=request.POST.get('choice2h')
        choice3h=request.POST.get('choice3h')
        choice4h=request.POST.get('choice4h')
        question9 = request.POST.get('question9')
        questiontype9=request.POST.get('questiontype9')
        choice1i=request.POST.get('choice1i')
        choice2i=request.POST.get('choice2i')
        choice3i=request.POST.get('choice3i')
        choice4i=request.POST.get('choice4i')
        question10 = request.POST.get('question10')
        questiontype10=request.POST.get('questiontype10')
        choice1j=request.POST.get('choice1j')
        choice2j=request.POST.get('choice2j')
        choice3j=request.POST.get('choice3j')
        choice4j=request.POST.get('choice4j')
        bol1a = request.POST.get('bol1a')
        bol2a = request.POST.get('bol2a')
        bol3a = request.POST.get('bol3a')
        bol4a = request.POST.get('bol4a')
        bol1b = request.POST.get('bol1b')
        bol2b = request.POST.get('bol2b')
        bol3b = request.POST.get('bol3b')
        bol4b = request.POST.get('bol4b')
        bol1c = request.POST.get('bol1c')
        bol2c = request.POST.get('bol2c')
        bol3c = request.POST.get('bol3c')
        bol4c = request.POST.get('bol4c')
        bol1d = request.POST.get('bol1d')
        bol2d = request.POST.get('bol2d')
        bol3d = request.POST.get('bol3d')
        bol4d = request.POST.get('bol4d')
        bol1e = request.POST.get('bol1e')
        bol2e = request.POST.get('bol2e')
        bol3e = request.POST.get('bol3e')
        bol4e = request.POST.get('bol4e')
        bol1f = request.POST.get('bol1f')
        bol2f = request.POST.get('bol2f')
        bol3f = request.POST.get('bol3f')
        bol4f = request.POST.get('bol4f')
        bol1g = request.POST.get('bol1g')
        bol2g = request.POST.get('bol2g')
        bol3g = request.POST.get('bol3g')
        bol4g = request.POST.get('bol4g')
        bol1h = request.POST.get('bol1h')
        bol2h = request.POST.get('bol2h')
        bol3h = request.POST.get('bol3h')
        bol4h = request.POST.get('bol4h')
        bol1i = request.POST.get('bol1i')
        bol2i = request.POST.get('bol2i')
        bol3i = request.POST.get('bol3i')
        bol4i = request.POST.get('bol4i')
        bol1j = request.POST.get('bol1j')
        bol2j = request.POST.get('bol2j')
        bol3j = request.POST.get('bol3j')
        bol4j = request.POST.get('bol4j')
        en = Survey(category = category, description = description, location = location, image = image, question1 = question1, questiontype1 = questiontype1, choice1a = choice1a, choice2a = choice2a, choice3a = choice3a, choice4a = choice4a, question2 = question2, questiontype2 = questiontype2, choice1b = choice1b, choice2b = choice2b, choice3b = choice3b, choice4b = choice4b, question3 = question3, questiontype3 = questiontype3, choice1c = choice1c, choice2c = choice2c, choice3c = choice3c, choice4c = choice4c, question4 = question4, questiontype4 = questiontype4, choice1d = choice1d, choice2d = choice2d, choice3d = choice3d, choice4d = choice4d, question5 = question5, questiontype5 = questiontype5, choice1e = choice1e, choice2e = choice2e, choice3e = choice3e, choice4e = choice4e, question6 = question6, questiontype6 = questiontype6, choice1f = choice1f, choice2f = choice2f, choice3f = choice3f, choice4f = choice4f, question7 = question7, questiontype7 = questiontype7, choice1g = choice1g, choice2g = choice2g, choice3g= choice3g, choice4g = choice4g, question8 = question8, questiontype8 = questiontype8, choice1h = choice1h, choice2h = choice2h, choice3h = choice3h, choice4h = choice4h, question9 = question9, questiontype9 = questiontype9, choice1i = choice1i, choice2i = choice2i, choice3i = choice3i, choice4i = choice4i, question10 = question10, questiontype10 = questiontype10, choice1j = choice1j, choice2j = choice2j, choice3j = choice3j, choice4j = choice4j,bol1a = bol1a, bol2a = bol2a, bol3a = bol3a, bol4a = bol4a, bol1b = bol1b, bol2b = bol2b, bol3b = bol3b, bol4b = bol4b, bol1c = bol1c, bol2c = bol2c, bol3c = bol3c, bol4c = bol4c, bol1d = bol1d, bol2d = bol2d, bol3d = bol3d, bol4d = bol4d, bol1e = bol1e, bol2e = bol2e, bol3e = bol3e, bol4e = bol4e, bol1f = bol1f, bol2f = bol2f, bol3f = bol3f, bol4f = bol4f,  bol1g = bol1g, bol2g = bol2g, bol3g = bol3g, bol4g = bol4g, bol1h = bol1h, bol2h = bol2h, bol3h = bol3h, bol4h = bol4h, bol1i = bol1i, bol2i = bol2i, bol3i = bol3i, bol4i = bol4i, bol1j = bol1j, bol2j = bol2j, bol3j = bol3j, bol4j = bol4j)
        en.save()
        
        return redirect('/')
        
    return render(request, 'businesses.html')

def survey(request, pk):
    survey = Survey.objects.get(id=pk)
    return render(request, 'survey.html', {'survey':survey, 'survey':survey})