from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    body = models.TextField()
# returns the title otherwise returns the objectname of the db
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # Reverse is a very handy utility function Django provides 
        # us to reference an object by its URL template name, in this
        # case post.detail
        # where post.detail is our url name in the url

#path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
# That means in order for this route to work we must also pass in an argument with the
# pk or primary key of the object. Confusingly, pk and id are interchangeable in Django
# though the Django docs recommend using self.id with get_absolute_url.

        return reverse('post_detail', args=[str(self.id)])