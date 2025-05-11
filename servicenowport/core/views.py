from testimonial.models import Testimonial
from blog.models import Blog
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, SignInForm, SetPasswordForm

User = get_user_model()

ABOUT_FEATURES_LIST = [
    {
        'icon': 'bi-lightbulb-fill',
        'title': 'Cutting-Edge Innovation',
        'desc': 'Experience groundbreaking technological advancements that push the boundaries of what’s possible, revolutionizing industries and transforming the way we live and work.'
    },
    {
        'icon': 'bi-wifi',
        'title': 'Seamless Connectivity',
        'desc': 'Stay connected anytime, anywhere with our robust and reliable network infrastructure, ensuring uninterrupted communication and effortless access to the digital world.'
    },
    {
        'icon': 'bi-ui-checks-grid',
        'title': 'Intuitive User Interface',
        'desc': 'Enjoy a seamless and intuitive user experience with our sleek and user-friendly interface, designed to simplify complex tasks and enhance productivity.'
    },
    {
        'icon': 'bi-people-fill',
        'title': 'Seamless Collaboration Tools',
        'desc': 'Gain valuable insights and make data-driven decisions with advanced analytics tools, fostering teamwork and boosting efficiency across your organization.'
    },
    {
        'icon': 'bi-cloud-fill',
        'title': 'Scalable Cloud Infrastructure',
        'desc': 'Streamline communication and foster teamwork with efficient collaboration tools, built on a secure and scalable cloud platform.'
    },
    {
        'icon': 'bi-bar-chart-fill',
        'title': 'Intelligent Data Analytics',
        'desc': 'Scale effortlessly with reliable and flexible data solutions that turn raw information into actionable business intelligence.'
    },
]


FEATURE_LIST = [
    {
        'title': 'ITSM & ITSM Licensing',
        'description': (
            'IT Service Management (ITSM) is all about delivering value-driven IT services '
            'that put the customer first. Rather than centering on hardware or systems, ITSM '
            'focuses on the complete service lifecycle and continuous improvement. Think of it '
            'as running IT “as a service”—covering every process, tool, and workflow your team '
            'relies on to plan, deliver, support, and refine technology across the organization.'
        ),
        'image': 'images/feature_one.png',
        'link': '#',  # replace with your real URL
    },
    {
        'title': 'ITBM & Its Key Modules',
        'description': (
            'IT Business Management (ITBM) equips leaders to forecast demand, assign resources smartly, '
            'and measure portfolio ROI. With ITBM you can rank incoming initiatives by business impact, '
            'keep budgets on track, and accelerate product delivery through streamlined workflows such as '
            'Project Portfolio Management, Demand Management, Agile Development, and more.'
        ),
        'image': 'images/feature_two.png',
        'link': '#',
    },
    {
        'title': 'ITOM Explained',
        'description': (
            'IT Operations Management (ITOM) is the strategic practice of designing, deploying, and running '
            'the tech foundations that power digital services. ServiceNow’s ITOM capabilities automate asset '
            'discovery, map service dependencies, enforce compliance, and consolidate event data—giving ops '
            'teams the real-time insight they need to keep everything humming.'
        ),
        'image': 'images/feature_third.png',
        'link': '#',
    },
]


def about_page(request):
    return render(request, 'core/about.html', {
        'features_list': ABOUT_FEATURES_LIST
    })

def services_page(request):
    return render(request, 'core/services.html')


def home_page(request):
    return render(request, 'core/home.html', {
    'features': FEATURE_LIST,            # list of dicts with title, desc, image, link
    'latest_blogs': Blog.objects.all()[:3],
    'testimonials': Testimonial.objects.all(),
})


def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = SignUpForm()
    return render(request, "sign_up.html", {"form": form})

def sign_in(request):
    if request.method == "POST":
        form = SignInForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = SignInForm()
    return render(request, "sign_in.html", {"form": form})

def sign_out(request):
    logout(request)
    return redirect("sign_in")

@login_required
def forgot_password(request):
    # For a production flow this should be behind a token link.
    if request.method == "POST":
        form = SetPasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your password has been updated.")
            return redirect("sign_in")
    else:
        form = SetPasswordForm(user=request.user)
    return render(request, "forgot_password.html", {"form": form})