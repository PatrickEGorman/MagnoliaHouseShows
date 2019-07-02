from django.db import models


class InfoPage(models.Model):
    image = models.ImageField(blank=True, null=True)
    image_caption = models.TextField(blank=True, null=True)
    title = models.TextField(default='', blank=True)
    text = models.TextField(default='')

    def __str__(self):
        if self.title:
            return "Page titled "+self.title
        elif len(self.text) < 50:
            return "Page text: "+self.text
        else:
            return "Page text preview: "+self.text[0: 49]


class Directions(InfoPage):
    starting_point = models.TextField(default='', blank=True)

    def __str__(self):
        if self.starting_point:
            return "Directions from "+self.starting_point
        else:
            return super()
