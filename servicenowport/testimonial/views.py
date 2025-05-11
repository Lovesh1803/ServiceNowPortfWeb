from django.shortcuts import render
from .models import Testimonial
from django.core.paginator import Paginator

def testimonials_page(request):
    per_page = 6
    # Safely parse page parameter
    page_param = request.GET.get('page', '1')
    try:
        page = int(page_param)
        if page < 1:
            raise ValueError
    except ValueError:
        page = 1

    # Calculate how many items to show
    limit = per_page * page

    all_testimonials = Testimonial.objects.order_by('-created_at')
    testimonials     = all_testimonials[:limit]

    has_next = all_testimonials.count() > limit
    next_page = page + 1

    return render(request, 'testimonial/testimonials.html', {
        'testimonials': testimonials,
        'has_next': has_next,
        'next_page': next_page,
    })

