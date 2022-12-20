
from django.db import models

from movies.models import Movie
from account.models import User

class CommentMovie(models.Model):
    movie = models.ForeignKey(Movie, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='movie_comments', on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.movie} -> {self.body}'

class RatingMovie(models.Model):
    movie = models.ForeignKey(Movie, related_name='ratings', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='ratings', on_delete=models.CASCADE)
    value = models.IntegerField(choices=[(1,1), (2,2), (3,3), (4,4), (5,5)])
    rated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} -> {self.movie}: {self.value}'

    class Meta:
        # а вот эта команда и не даст повторно голосовать
        unique_together = ('author', 'movie')
