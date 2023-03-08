from django.db import models



class StoryModel(models.Model):
    title = models.CharField(max_length=150)
    # views = models.IntegerField()
    link = models.CharField(max_length=500)
    content = models.TextField()
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True, blank=True, null=True)
    tag = models.ManyToManyField("storys.TagModel")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class TagModel(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True, blank=True, null=True)

    class Meta:
        verbose_name = ("TagModel")
        verbose_name_plural = ("TagModels")

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("TagModel_detail", kwargs={"pk": self.pk})


# for tag in TagModel.objects.all():
#     print(tag.story.all.count())

