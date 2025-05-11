from django.shortcuts import redirect, render, get_object_or_404
from .models import Blog, Objective, Product, Level, Role, Skill, Comment
from .forms import CommentForm
from django.contrib import messages
from django.urls import reverse
from .forms import CommentForm
from django.core.paginator import Paginator

def blog_list(request):
    blogs = Blog.objects.all()

    # Get raw lists from GET
    raw_objectives = request.GET.getlist('objective')
    raw_products   = request.GET.getlist('product')
    raw_levels     = request.GET.getlist('level')
    raw_roles      = request.GET.getlist('role')
    raw_skills     = request.GET.getlist('skill')

    # Clean them: only keep strings that are all digits
    selected_objectives = [v for v in raw_objectives if v.isdigit()]
    selected_products   = [v for v in raw_products   if v.isdigit()]
    selected_levels     = [v for v in raw_levels     if v.isdigit()]
    selected_roles      = [v for v in raw_roles      if v.isdigit()]
    selected_skills     = [v for v in raw_skills     if v.isdigit()]

    # apply filters only if user selected something
    if selected_objectives:
        blogs = blogs.filter(objectives__id__in=selected_objectives)
    if selected_products:
        blogs = blogs.filter(products__id__in=selected_products)
    if selected_levels:
        blogs = blogs.filter(levels__id__in=selected_levels)
    if selected_roles:
        blogs = blogs.filter(roles__id__in=selected_roles)
    if selected_skills:
        blogs = blogs.filter(skills__id__in=selected_skills)

    blogs = blogs.distinct()

    # paginate: 5 per page
    paginator = Paginator(blogs, 5)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/blog_list.html', {
        'blogs': page_obj,
        'objectives': Objective.objects.all(),
        'products':   Product.objects.all(),
        'levels':     Level.objects.all(),
        'roles':      Role.objects.all(),
        'skills':     Skill.objects.all(),
        # pass the raw selected lists for template checks
        'selected_objectives': selected_objectives,
        'selected_products':   selected_products,
        'selected_levels':     selected_levels,
        'selected_roles':      selected_roles,
        'selected_skills':     selected_skills,
    })

def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    comments = blog.comments.order_by('created_at')
    recent_posts = Blog.objects.order_by('-created_at')[:3]
    recent_comments = blog.comments.order_by('-created_at')[:3]

    # Handle comment posting
    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, "You must be logged in to post a comment.")
            return redirect(f"{reverse('sign_in')}?next={request.path}")
        form = CommentForm(request.POST)
        if form.is_valid():
            c = form.save(commit=False)
            c.blog = blog
            # optionally associate with user: c.user = request.user
            c.save()
            messages.success(request, "Your comment has been posted!")
            return redirect('blog:detail', slug=slug)
    else:
        form = CommentForm()

    return render(request, 'blog/blog_detail.html', {
        'blog': blog,
        'comments': comments,
        'recent_posts': recent_posts,
        'recent_comments': recent_comments,
        'form': form,
    })


