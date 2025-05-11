from django.shortcuts import render
from .models import Testimonial
from django.core.paginator import Paginator

def testimonials_page(request):
    testimonials = Testimonial.objects.all()

    # paginate: 5 per page
    paginator = Paginator(testimonials, 6)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    return render(request, 'testimonial/testimonials.html', {'testimonials': page_obj})
