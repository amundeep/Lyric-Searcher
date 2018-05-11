from django.db import models

class Song(models.Model):
	song_name = models.CharField(max_length=200)

	image_url = models.URLField(max_length=200)