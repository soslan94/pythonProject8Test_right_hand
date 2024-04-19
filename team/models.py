from django.db import models


class Team_Member(models.Model):
    """
    Model representing a team member. Field 'image' is a profile picture of the team member
    """
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=300)
    image = models.ImageField(upload_to="team")

    def __str__(self):
        return self.name


class Volunteer(models.Model):
    """
    Model representing a volunteer. Field 'image' is a profile picture of the volunteer
    """
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=300)
    image = models.ImageField(upload_to="volunteer")

    def __str__(self):
        return self.name


class Occupation(models.Model):
    """
    Model representing an occupation of the class 'Future_Volunteer'
    """
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Future_Volunteer(models.Model):
    """
    Model representing a future volunteer. Field 'image' is a profile picture of the volunteer
    """
    name = models.CharField(max_length=100)
    occupation = models.ForeignKey(Occupation, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    image = models.ImageField(upload_to="future_volunteer")

    def __str__(self):
        return self.name