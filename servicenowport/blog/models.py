from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Objective(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self): return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self): return self.name

class Level(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self): return self.name

class Role(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self): return self.name

class Skill(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self): return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    category    = models.ForeignKey(Category, related_name='blogs', on_delete=models.PROTECT)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    objectives = models.ManyToManyField(Objective, blank=True)
    products = models.ManyToManyField(Product, blank=True)
    levels = models.ManyToManyField(Level, blank=True)
    roles = models.ManyToManyField(Role, blank=True)
    skills = models.ManyToManyField(Skill, blank=True)
    image = models.ImageField(
        upload_to='blogs/',
        blank=True, null=True,
        default='images/placeholder.png'
    )

    class Meta:
        ordering = ['-updated_at']

    def get_absolute_url(self):
        return reverse('blog:detail', args=[self.slug])    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog       = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    name       = models.CharField(max_length=100)
    email      = models.EmailField(null=True, blank=True)              
    comment    = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} on {self.blog.title}"