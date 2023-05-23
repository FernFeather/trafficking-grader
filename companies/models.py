from django.db import models

# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
        
class Companies(models.Model):
    GRADE_CHOICES = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('F', 'F'),
    )


    title = models.CharField(max_length=100)
    about = models.TextField()  # company about summary
    pretest = models.BooleanField() # is a pretest given?
    posttest = models.BooleanField()    # is a posttest given?
    languages = models.ManyToManyField(Language, blank=True)
    is_id_required = models.BooleanField(default=False)

    grade = models.CharField(max_length=1, choices=GRADE_CHOICES, blank=True, null=True) # company grade based off of factors

    def calculate_grade(self):
        satisfactory_points = 0
        grade = 'F'  # Default grade is 'F'

        if self.pretest:
            satisfactory_points += 1

        if self.posttest:
            satisfactory_points += 1

        language_count = self.languages.count()
        if language_count >= 5:
            satisfactory_points += 1
        elif language_count >= 3:
            satisfactory_points += 0.5

        if self.is_id_required: 
            satisfactory_points += 1

        if satisfactory_points >= 4:
            grade = 'A'
        elif satisfactory_points >= 3:
            grade = 'B'
        elif satisfactory_points >= 2:
            grade = 'C'
        elif satisfactory_points >= 1:
            grade = 'D'
        else:
            grade = 'F'

        self.grade = grade
        self.save()
