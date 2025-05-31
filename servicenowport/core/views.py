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
        'icon': ' 🚀',
        'title': 'Expert-Led Training',
        'desc': 'Learn from certified ServiceNow professionals with real-world experience. Our instructors bring deep platform knowledge and industry insight to every lesson.'
    },
    {
        'icon': '🎓',
        'title': 'Career-Focused Curriculum',
        'desc': 'We go beyond theory. Our curriculum is designed to prepare you for ServiceNow certifications and real job roles in ITSM, ITOM, HRSD, and more.'
    },
    {
        'icon': '🛠️',
        'title': 'Hands-On Labs & Projects',
        'desc': 'Practice what you learn in live environments. Our platform provides sandbox access, real use cases, and step-by-step labs to help you build confidence and skills.'
    },
    {
        'icon': '🌐',
        'title': 'Anywhere, Anytime Learning',
        'desc': 'Our flexible learning model supports your schedule. Access content online 24/7 from any device—learn at your pace, from anywhere in the world.'
    },
    {
        'icon': '💼',
        'title': 'Job-Ready Support',
        'desc': 'We offer resume building, interview prep, and job placement assistance to help you land your first or next ServiceNow role.'
    },
    {
        'icon': '🧭',
        'title': 'Guided Certification Path',
        'desc': 'From beginner to advanced, we provide a clear roadmap to help you pass CSA, CAD, CIS, and other ServiceNow certifications with confidence.'
    },
]


FEATURE_LIST = [
    {
        'title': 'ITSM',
        'description': (
            'ServiceNow ITSM (IT Service Management) describes the management of end-to-end IT service delivery to meet business goals, including the creation, delivery, and support of IT services. ITSM is the discipline of designing, delivering, managing, and improving the IT services an organization provides to its users. Key Modules of ITSM are Incident Management, Problem Management, Change Management, Knowledge Management, Request Management.'
        ),
        'image': 'images/feature_one.png',
        'link': '#',  # replace with your real URL
    },
    {
        'title': 'ITOM',
        'description': (
            'ServiceNow ITOM (IT Operations Management) is designed to help IT teams gain visibility, control, and automation across their infrastructure and services. ITOM focuses on the health and performance of the infrastructure that supports those services. IT Operations Management (ITOM) includes the tools and processes needed to monitor infrastructure and applications, ensure service availability and performance, automatically discover and map assets, Resolve issues proactively. Key Modules of ITOM are Discovery, Service Mapping, Event Management, Health Log Analytics, Cloud Management, Orchestration and Automation.'
        ),
        'image': 'images/feature_two.png',
        'link': '#',
    },
    {
        'title': 'ITAM',
        'description': (
            "ServiceNow ITAM (IT Asset Management) is a suite of tools that help organizations manage the lifecycle of their IT assets in an efficient way. It's tightly integrated with ITSM and ITOM to improve visibility, reduce costs, and ensure compliance. IT Asset Management (ITAM) is the process of tracking and managing the hardware, software, and other technological assets within an organization. Key Modules of ITAM are Hardware Asset Management (HAM), Software Asset Management (SAM), Cloud Insights (part of SAM Pro), Enterprise Asset Management (EAM)."
        ),
        'image': 'images/feature_third.png',
        'link': '#',
    },
    {
        'title': 'ITBM',
        'description': (
            "ServiceNow ITBM (IT Business Management) is referred to as Strategic Portfolio Management (SPM) helps organizations align their IT efforts with business goals by managing projects, portfolios, resources, and finances. IT Business Management (ITBM) helps organizations plan and prioritize work, manage demand and projects, track costs and resources, align IT investments with strategic objectives. Key Modules of ITBM are Project Portfolio Management (PPM), Demand Management, Resource Management, Financial Planning, Innovation Management, Agile Development."
        ),
        'image': 'images/feature_forth.png',
        'link': '#',
    },
    {
        'title': 'IRM/GRC',
        'description': (
            "ServiceNow IRM (Integrated Risk Management) also known as GRC (Governance, Risk, and Compliance) is a suite that helps organizations manage risks, meet compliance requirements, and make informed decisions to stay resilient. IRM/GRC is all about understanding, assessing, and responding to risks and compliance obligations across the organization. Key Modules of IRM/GRC are Policy and Compliance Management, Risk Management, Audit Management, Vendor Risk Management (VRM), Business Continuity Management (BCM), Operational Risk Management."
        ),
        'image': 'images/feature_fifth.png',
        'link': '#',
    },
    {
        'title': 'HRSD',
        'description': (
            "ServiceNow HRSD (Human Resources Service Delivery) is a module designed to modernize and streamline HR services through digital workflows making it easier for employees to access HR support and for HR teams to manage requests, tasks, and cases efficiently. HRSD helps HR teams, deliver consistent and personalized employee services, automate manual HR processes, Improve employee experience through self-service and case management. Key Modules of HRSD are Employee Center, Case and Knowledge Management, HR Services Catalog, Lifecycle Events, Employee Document Management, Mobile Access. "
        ),
        'image': 'images/feature_sixth.png',
        'link': '#',
    },
]

SERVICE_LIST = [
        {
            "title": "Service Portal",
            "description": "Gain hands-on expertise in developing and customizing responsive user interfaces with ServiceNow’s Service Portal. Learn to build dynamic widgets, manage portal themes, and deliver user-centric self-service experiences."
        },
        {
            "title": "Human Resources Service Delivery (HRSD)",
            "description": "Master the configuration and deployment of HRSD modules, enabling seamless case management, employee service centers, and lifecycle event automation within your enterprise."
        },
        {
            "title": "IT Service Management (ITSM)",
            "description": "Explore the foundational ITSM processes, including Incident, Problem, Change, and Request Management. Learn best practices aligned with ITIL and configure workflows to optimize IT service delivery."
        },
        {
            "title": "Service Catalog",
            "description": "Develop and manage scalable service catalogs to streamline service offerings. Learn how to build catalog items, define workflows, and configure access controls to support enterprise-wide requests."
        },
        {
            "title": "Integration (REST, SOAP, APIs)",
            "description": "Acquire practical knowledge of integrating ServiceNow with third-party systems using REST and SOAP web services. Learn scripted integrations, authentication methods, and testing techniques."
        },
        {
            "title": "Transform Maps & Data Import",
            "description": "Understand the use of Transform Maps for efficient data migration and transformation. Learn to map import sets to existing tables and automate data normalization processes."
        },
        {
            "title": "JavaScript in ServiceNow",
            "description": "Enhance your development skills with in-depth JavaScript training tailored to the ServiceNow platform. Learn client and server-side scripting, including Business Rules, Client Scripts, and Script Includes."
        },
        {
            "title": "Flow Designer",
            "description": "Master the Flow Designer to build automated workflows with minimal coding. Understand trigger-based logic, flow actions, subflows, and orchestration for streamlined process automation."
        },
        {
            "title": "Integration Hub",
            "description": "Explore IntegrationHub and its pre-built spokes to automate common business tasks. Learn to build reusable integrations and extend Flow Designer capabilities through custom actions."
        },
        {
            "title": "Scoped Application Development",
            "description": "Gain proficiency in building custom applications in ServiceNow Studio. Learn best practices for table design, data models, module configuration, and publishing applications within scoped environments."
        },
        {
            "title": "Automated Test Framework (ATF)",
            "description": "Develop, execute, and manage automated tests to validate functionality and minimize regression risks during updates. Learn test planning and best practices for continuous testing."
        },
        {
            "title": "Agile Development 2.0",
            "description": "Learn to manage software development lifecycles using Agile 2.0. Gain experience in configuring Agile boards, managing epics and user stories, and reporting on sprint progress."
        },
        {
            "title": "CMDB & Discovery",
            "description": "Understand the principles of Configuration Management and ServiceNow Discovery. Learn to populate the CMDB with accurate data and maintain CI relationships critical to IT operations."
        },
        {
            "title": "Reports & Dashboards",
            "description": "Build insightful reports and visual dashboards using Performance Analytics. Learn to track KPIs, design real-time analytics, and empower stakeholders with actionable data."
        },
        {
            "title": "IT Operations Management (ITOM)",
            "description": "Explore ITOM capabilities such as Event Management, Operational Intelligence, and Service Mapping. Learn how to proactively detect, analyze, and resolve IT infrastructure issues."
        }
    ]

def about_page(request):
    return render(request, 'core/about.html', {
        'features_list': ABOUT_FEATURES_LIST
    })

def services_page(request):
    return render(request, 'core/services.html', {
        'services': SERVICE_LIST
    })


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