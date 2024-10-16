from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer, Category, Course, Lesson, Enrollment, Test, Question, Answer
from django.contrib.auth import login, authenticate
from .forms import CustomerCreationForm, CustomerLoginForm, CourseCreationForm, CourseEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required

def home_page(request):
    categories = Category.objects.all()
    courses = Course.objects.all()[:3]
    return render(request, 'startApp/home_page.html', {'categories': categories, 'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    lessons = Lesson.objects.filter(course=course)
    tests = Test.objects.filter(course=course)
    return render(request, 'startApp/course_detail.html', {
        'course': course,
        'lessons': lessons,
        'tests': tests
    })
    
def category_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    courses = Course.objects.filter(category=category)
    return render(request, 'startApp/category_detail.html', {
        'category': category,
        'courses': courses
    })

def register(request):
    if request.method == 'POST':
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home_page')
    else:
        form = CustomerCreationForm()
    return render(request, 'startApp/register.html', {'form': form})

def custom_login(request):
    if request.method == 'POST':
        form = CustomerLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                return render(request, 'startApp/login.html', {'form': form, 'error_message': 'Invalid login credentials.'})
        else:
            return render(request, 'startApp/login.html', {'form': form})
    else:
        form = CustomerLoginForm()
    return render(request, 'startApp/login.html', {'form': form})

@login_required
def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    course = lesson.course
    lessons = list(course.lesson_set.all().order_by('order'))

    try:
        index = lessons.index(lesson)
        previous_lesson = lessons[index - 1] if index > 0 else None
        next_lesson = lessons[index + 1] if index < len(lessons) - 1 else None
    except ValueError:
        previous_lesson = None
        next_lesson = None

    return render(request, 'startApp/lesson_detail.html', {
        'lesson': lesson,
        'course': course,
        'previous_lesson': previous_lesson,
        'next_lesson': next_lesson
    })
    
@login_required
def test_detail(request, test_id):
    test = get_object_or_404(Test, pk=test_id)
    questions = test.question_set.all()

    if request.method == 'POST':
        if request.user.is_authenticated:
            customer = get_object_or_404(Customer, user=request.user)
            for question in questions:
                answer_text = request.POST.get(f'answer_{question.id}')
                answer = Answer(
                    customer=customer,
                    question=question,
                    answer_text=answer_text
                )
                answer.save()
            return redirect('profile')
        else:
            return redirect('login')

    context = {
        'test': test,
        'questions': questions,
    }
    return render(request, 'startApp/test_detail.html', context)\
        
@login_required
def profile(request):
    user = request.user
    customer = get_object_or_404(Customer, user=user)

    student_courses = Enrollment.objects.filter(customer=customer)

    if customer.is_instructor:
        instructor_courses = Course.objects.filter(instructor=customer)
    else:
        instructor_courses = None

    context = {
        'customer': customer,
        'student_courses': student_courses,
        'instructor_courses': instructor_courses,
    }

    return render(request, 'startApp/profile.html', context)

@login_required
def create_course(request):
    customer = Customer.objects.get(user=request.user)
    if not customer.is_instructor:
        return redirect('profile')

    if request.method == 'POST':
        form = CourseCreationForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.instructor = customer
            course.save()
            return redirect('profile')
    else:
        form = CourseCreationForm()

    return render(request, 'startApp/create_course.html', {'form': form})

@login_required
def edit_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.user.customer != course.instructor:
        return redirect('profile')

    if request.method == 'POST':
        form = CourseEditForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    else:
        form = CourseEditForm(instance=course)
    return render(request, 'startApp/edit_course.html', {'form': form})

def about_project(request):
    return render(request, 'startApp/about_project.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileEditForm(instance=request.user)
    return render(request, 'startApp/edit_profile.html', {'form': form})
