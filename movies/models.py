from django.db import models

class Genre(models.Model):
    title = models.CharField(max_length=70)
    
    def __str__(self):
        return self.title

class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.ForeignKey(Genre, related_name='movies', on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
    poster = models.FileField(upload_to='movies')
    runtime = models.PositiveIntegerField()
    cast = models.TextField()
    rating = models.PositiveIntegerField()

    @property
    def average_rating(self):
        rates = self.rating.all()
        values = []
        for rate in rates:
            values.append(rate)
        if values:
            return sum(values) / len(values)
        return 0

    def __str__(self):
        return self.title       







  
    # @property
    # def average_rating(self):
    #     rates = self.rating.all()
    #     values = []
    #     for rate in rates:
    #         values.append(rate)
    #     if values:
    #         return sum(values) / len(values)
    #     return 0

    def str(self):
        return self.title
