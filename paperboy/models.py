from django.db import models

class PaperBoy(models.Model):
    name = models.CharField(max_length=300)
    experience = models.PositiveIntegerField(default=0)
    earnings = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Paperboy {self.name} has {self.experience} experience and has earned ${self.earnings}.'

    # def quota(self): #An instance method that calculates the PaperBoy's quota.
    #     return 50 + (self.experience / 2) #Minimum quota is 50 plus half of experience (number of papers already delivered).

    # def deliver(self, start_address, end_address): #An instance method that calculates current_earnings based on quota, start_address, and end_address.
    #     quota = self.quota() #Gets quota for this route.
    #     current_route = abs(end_address - start_address) #Number of houses delivered on this route.
    #     self.experience += (current_route) #Adds current_route's houses to experience.

    #     if (current_route > quota): #If current_route is greater than the quota, PaperBoy is rewarded for going over.
    #         current_earnings = ((current_route - quota) * .5) + (quota * .25) #The current_earnings is $.50 for each house over quota, plus $.25 for each house in quota.
    #     else: #Else the current_route is less than the quota, PaperBoy is punished for going under. 
    #         current_earnings = (current_route * .25) - 2 #The current_earnings is $.25 for each house in quota, minus the $2 penalty.
    
    #     self.earnings += current_earnings #The self.earnings is added to the current_earnings.
    #     return current_earnings #The current_earnings is returned. (Not the self.earnings.)

    # def report(self): #Returns an plain-English string that describes the instance.
    #     return f"I'm {self.name}, I've delivered {self.experience} papers and I've earned ${self.earnings} so far!"