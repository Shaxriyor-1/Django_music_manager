from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class MusicModel(models.Model):
    title = models.CharField(max_length=255)
    genre = models.ForeignKey('Genres', on_delete=models.CASCADE, null=True)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    listened_times = models.IntegerField(default=0)
    def validate_file_extension(value):
        import os
        ext = os.path.splitext(value.name)[1]
        valid_extensions = ['.mp3','.aac','.wav']
        if not ext in valid_extensions:
            raise ValidationError(u'File not supported! Supported files: .mp3  .aac  .wav')
    music = models.FileField(upload_to="media/music_files", validators=[validate_file_extension])
    class Meta:
        verbose_name = "Music"
        verbose_name_plural = "Musics"

    def __str__(self):
        return self.title
    
class Genres(models.Model):
    genre = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.genre}"

    class Meta:
        verbose_name_plural = "Genres"