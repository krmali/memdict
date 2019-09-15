from django.db import models

class Languages(models.Model):
	name = models.CharField(max_length=255, null=False)
	def __str__(self):
		return name

class Words(models.Model):
	language = models.ForeignKey(Languages, on_delete=models.CASCADE)
	word = models.CharField(max_length=255, null=False)
	def __str__(self):
		return word

class Meanings(models.Model):
	language = models.ForeignKey(Languages, on_delete=models.CASCADE)
	meaning = models.CharField(max_length=255, null=False)
	def __str__(self):
		return meaning

class Mnomonics(models.Model):
	language = models.ForeignKey(Languages, on_delete=models.CASCADE)
	word = models.ForeignKey(Words, on_delete=models.CASCADE)
	mnomonic = models.CharField(max_length=255, null=False)
	def __str__(self):
		return mnomonic


