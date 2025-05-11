from django.db import models

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    image = models.ImageField(
        upload_to='testimonials/',
        blank=True, null=True,
        default='images/testimonial_placeholder.png'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
