from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=200)
	body = models.CharField(max_length=200)

	class Meta:
		ordering = 'name'
		verbose_name = 'Good'
		verbose_name_plural = 'Goods'

	def __str__(self):
		return self.name

class Subcategory(models.Model):
	name = models.CharField(max_length=200)
	body = models.CharField(max_length=200)
	category = models.ForeignKey(category, on_delete=models.CASCADE)

	class Meta:
		verbose_name = 'selected'
		verbose_name_plural = 'selections'

	def __str__(self):
    	return self.name

class Product(models.Model):
	name = models.CharField(max_length=200)
	user = models.ForeignKey(user, on_delete=models.CASCADE)
	description = models.CharField(max_length=300)
	subcategory = models.ForeignKey(subcategory, on_delete=models.CASCADE)
	price = models.FloatField(max_digits=10)

	    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

class Letter(models.Model):
	reciever = models.ForeignKey(User, on_delete=models.CASCADE)
	sender = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=300)
    def __str__(self):
        return str(self.sender)

    class Meta:
    	verbose_name = 'Letter'
    	verbose_name_plural = 'Letters'

class Profile(models.Model):
	user = models.OneToOne(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	phonenumber = models.CharField(max_length=15, blank=True)

	def __str__(self):
		return self.user.username


@receiver(post_save, sender=User, dispatch_uid="create_profile")
def update_profile(sender, instance, **kwargs):
    if kwargs["created"]:
        user_profile = Profile.objects.create(user=instance)

    
    		
