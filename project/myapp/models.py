from django.db import models

# Create your models here.
# 1. user_login - id, uname ,passwd ,u_type 
# 2. user_details - id, user_id ,fname ,lname ,gender ,dob ,addr ,pin ,contact ,email
# 3. pic_pool - id, pic_path ,category_master_id ,location_master_id 
# 4. location_master - id, loc_name ,addr1 ,addr2 ,addr3 ,pin ,lat ,lng ,radius ,remarks 
# 5. category_master - id, category_name 
# 6. user_search_history - id, user_id ,pic_path ,result ,dt ,tm ,status 
# 7. general_news - id, user_id ,subject ,news ,dt ,tm ,status

class user_login(models.Model):
    uname = models.CharField(max_length=100)
    passwd = models.CharField(max_length=25)
    u_type = models.CharField(max_length=10)

    def __str__(self):
        return self.uname

class user_details(models.Model):
    user_id = models.IntegerField()
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=200)
    gender = models.CharField(max_length=25)
    age = models.IntegerField()
    addr = models.CharField(max_length=500)
    pin = models.IntegerField()
    contact = models.IntegerField()
    email = models.CharField(max_length=25)

    def __str__(self):
        return self.fname

class pic_pool(models.Model):
    pic_path = models.CharField(max_length=150)
    category_master_id = models.IntegerField()
    location_master_id = models.IntegerField()

    def __str__(self):
        return self.pic_path

class location_master(models.Model):
    loc_name = models.CharField(max_length=150)
    addr1 = models.CharField(max_length=150)
    addr2 = models.CharField(max_length=150)
    addr3 = models.CharField(max_length=150)
    pin = models.CharField(max_length=50)
    lat = models.CharField(max_length=50)
    lng = models.CharField(max_length=50)
    radius = models.CharField(max_length=50)
    remarks = models.CharField(max_length=1500)

    def __str__(self):
        return self.loc_name

class category_master(models.Model):
    category_name = models.CharField(max_length=150)

    def __str__(self):
        return self.category_name

class user_search_history(models.Model):
    user_id = models.IntegerField()
    pic_path = models.CharField(max_length=150)
    result = models.CharField(max_length=150)
    dt = models.CharField(max_length=50)
    tm = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.pic_path


class general_news(models.Model):
    user_id = models.IntegerField()
    subject = models.CharField(max_length=150)
    news = models.CharField(max_length=1500)
    dt = models.CharField(max_length=50)
    tm = models.CharField(max_length=50)
    status = models.CharField(max_length=50)


# 6. feedback - id, user_id, msg, dt, tm, status
class feedback(models.Model):
    # id
    user_id = models.IntegerField()
    msg = models.CharField(max_length=250)
    dt = models.CharField(max_length=15)
    tm = models.CharField(max_length=15)
    status = models.CharField(max_length=10)