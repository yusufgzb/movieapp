from django.core import validators
from django.db import models
from django.db.models.fields import CharField
from ckeditor.fields import RichTextField

#Genre Modeli(filmin türünü belirten model)
class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Contact Modeli
class Contact(models.Model):
    address = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.address

#Person Modeli
#Contact ile 1-1 bağlı
class Person(models.Model):

    genders = (
        ('M','Erkek'),
        ('F','Kadın'),
    )

    duty_types = (
        ('1','Görevli'),
        ('2','Oyuncu'),
        ('3','Yönetmen'),
        ('4','Senarist'),
    )

    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    biography = CharField(max_length=3000)
    image_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField("Cinsiyet",max_length=1, choices=genders)
    duty_type = models.CharField("Görev",max_length=1, choices=duty_types)
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE, null=True, blank=True)


    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    full_name.fget.short_description = "ad soyad"

    class Meta:
        verbose_name     = "Kişi"
        verbose_name_plural = "Kişiler"

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.duty_types[int(self.duty_type)-1][1]})"

 
#Film Modeli
#people ile Person modeline çoka-çok bağlantılı
#genres ile Genre modeline çoka-çok bağlantılı
class Movie(models.Model):
    title = models.CharField("Başlık",max_length=100)
    description = RichTextField()
    image_name = models.ImageField(upload_to="movies")
    image_cover = models.ImageField(upload_to="movies")
    date = models.DateField()
    slug = models.SlugField(unique=True,db_index=True)
    budget = models.DecimalField(max_digits=19,decimal_places=2)
    language = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)
    people = models.ManyToManyField(Person)
    genres = models.ManyToManyField(Genre)

    class Meta():
        verbose_name = "Film"
        verbose_name_plural = "Filmler"


    def __str__(self):
        return self.title

class Slider(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="movies")
    movie = models.ForeignKey(Movie,on_delete=models.SET_NULL,null=True,blank=True)
    is_active = models.BooleanField(default=False)

#Yorum Modeli
#movie ile Movie modelini ve Comment modelini db de iki tabloyu bir birine bağlantılı
class Comment(models.Model):
    full_name = models.CharField(max_length=100)
    email =models.EmailField(default="")
    text = models.TextField(max_length=500)
    rating = models.IntegerField(null=True)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE,related_name="comments")
    date_added = models.DateTimeField(null= True,auto_now=True)


#Video Modeli
#movie ile Movie modelini ve Video modelini db de iki tabloyu bir birine bağlantılı
class Video(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.title