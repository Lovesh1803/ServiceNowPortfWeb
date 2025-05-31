from django.shortcuts import redirect, render, get_object_or_404
from .models import Blog, Level, Role, ChallengeType, CertificationPractice, ContentType, Status
from .forms import CommentForm
from django.contrib import messages
from django.urls import reverse
from .forms import CommentForm
from django.core.paginator import Paginator
from django.utils.text import slugify
from bs4 import BeautifulSoup

def blog_list(request):
    blogs = Blog.objects.all()

    # Get raw lists from GET
    raw_levels       = request.GET.getlist('level')
    raw_roles        = request.GET.getlist('role')
    raw_challenges   = request.GET.getlist('challenge_type')
    raw_cert_prac    = request.GET.getlist('certification_practice')
    raw_content_types = request.GET.getlist('content_type')
    raw_statuses      = request.GET.getlist('status')


    # Clean them
    selected_levels       = [v for v in raw_levels if v.isdigit()]
    selected_roles        = [v for v in raw_roles if v.isdigit()]
    selected_challenges   = [v for v in raw_challenges if v.isdigit()]
    selected_cert_prac    = [v for v in raw_cert_prac if v.isdigit()]
    selected_content_types = [v for v in raw_content_types if v.isdigit()]
    selected_statuses      = [v for v in raw_statuses if v.isdigit()]

    # Apply filters
    if selected_levels:
        blogs = blogs.filter(levels__id__in=selected_levels)
    if selected_roles:
        blogs = blogs.filter(roles__id__in=selected_roles)
    if selected_challenges:
        blogs = blogs.filter(challenge_types__id__in=selected_challenges)
    if selected_cert_prac:
        blogs = blogs.filter(certification_practices__id__in=selected_cert_prac)
    if selected_content_types:
        blogs = blogs.filter(content_types__id__in=selected_content_types)
    if selected_statuses:
        blogs = blogs.filter(statuses__id__in=selected_statuses)

    blogs = blogs.distinct()

    # Pagination logic
    per_page = 6
    page_param = request.GET.get('page', '1')
    try:
        page = int(page_param)
        if page < 1:
            raise ValueError
    except ValueError:
        page = 1

    limit = per_page * page
    limit_blogs = blogs[:limit]
    total_blogs = blogs.count()
    has_next = total_blogs > limit
    next_page = page + 1

    return render(request, 'blog/blog_list.html', {
        'blogs': limit_blogs,
        'has_next': has_next,
        'next_page': next_page,
        'levels': Level.objects.all(),
        'roles': Role.objects.all(),
        'challenge_types': ChallengeType.objects.all(),
        'certification_practices': CertificationPractice.objects.all(),
        'content_types': ContentType.objects.all(),
        'statuses': Status.objects.all(),

        # selected filter ids for template rendering
        'selected_levels': selected_levels,
        'selected_roles': selected_roles,
        'selected_challenges': selected_challenges,
        'selected_cert_prac': selected_cert_prac,
        'selected_content_types': selected_content_types,
        'selected_statuses': selected_statuses,
    })

def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)

    # --- Build Table of Contents ---
    soup = BeautifulSoup(blog.content, 'html.parser')
    toc = []
    # look for h2 and h3 (you can extend to h4, etc.)
    for header in soup.find_all(['h2','h3']):
        text = header.get_text(strip=True)
        # generate or reuse an id
        hid = header.get('id') or slugify(text)
        header['id'] = hid
        toc.append({
            'id':    hid,
            'text':  text,
            'level': int(header.name[1]),  # 2 for h2, 3 for h3
        })
    # overwrite content with anchors in place
    blog.content = str(soup)

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
        'toc': toc,
        'comments': comments,
        'recent_posts': recent_posts,
        'recent_comments': recent_comments,
        'form': form,
    })


