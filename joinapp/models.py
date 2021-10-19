from django.db import models



class Author(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='course')

    def __str__(self):
        return self.name


class Investor(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Deal(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class InvestmentManager(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Investment(models.Model):    
    renewal_recommended_date = models.DateField(blank=True,null=True)
    investor_response = models.BooleanField(blank=True,null=True)
    investor_docs_sent = models.DateField(blank=True,null=True)
    accepted = models.BooleanField() # options 1,0
    approved = models.BooleanField(null=True) # options 1,0,null
    renewed_declined_response = models.BooleanField(null=True)
    after_maturity_mail_date = models.DateField(blank=True,null=True)
    investor_id = models.ForeignKey(Investor, on_delete=models.CASCADE, related_name='course',blank=True,null=True)
    investment_manager_id = models.ForeignKey(InvestmentManager, on_delete=models.CASCADE, blank=True,null=True)
    deal_id = models.ForeignKey(Deal, on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.name

