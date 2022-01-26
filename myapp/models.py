from django.db import models

# Create your models here.
# create model to store the resume data [db]

STATE_CHOICE = (
    ('Punjab', 'Punjab'),
    ('Sindh', 'Sindh'),
    ('Baluchistan', 'Baluchistan'),
    ('Sindh', 'Sindh'),
    ('Khyber Pakhton khawa', 'Khyber Pakhton khawa'),
    ('Gilgit Baltistan', 'Gilgit Baltistan'),
)


class Resume(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin = models.PositiveIntegerField()
    state = models.CharField(choices=STATE_CHOICE, max_length=50)
    mobile = models.PositiveIntegerField()
    email = models.EmailField()
    job_city = models.CharField(max_length=50)
    profile_image = models.ImageField(
        upload_to='media/profileimg/', blank=True)
    my_file = models.FileField(upload_to='media/doc/', blank=True)
