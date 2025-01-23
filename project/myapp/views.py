from django.shortcuts import render

# Create your views here.
from django.db.models import Max
from .models import user_login

def index(request):
    return render(request, './myapp/index.html')


def about(request):
    return render(request, './myapp/about.html')


def contact(request):
    return render(request, './myapp/contact.html')

#####################################################################
##################################### ADMIN ###############################
def admin_login(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pwd = request.POST.get('pwd')
        #print(un,pwd)
        #query to select a record based on a condition
        ul = user_login.objects.filter(uname=un, passwd=pwd, u_type='admin')

        if len(ul) == 1:
            request.session['user_name'] = ul[0].uname
            request.session['user_id'] = ul[0].id
            return render(request,'./myapp/admin_home.html')
        else:
            msg = '<h1> Invalid Uname or Password !!!</h1>'
            context ={ 'msg1':msg }
            return render(request, './myapp/admin_login.html',context)
    else:
        msg = ''
        context ={ 'msg1':msg }
        return render(request, './myapp/admin_login.html',context)


def admin_home(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return admin_login(request)
    else:
        return render(request,'./myapp/admin_home.html')


def admin_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return admin_login(request)
    else:
        return admin_login(request)

def admin_changepassword(request):
    if request.method == 'POST':
        opasswd = request.POST.get('opasswd')
        npasswd = request.POST.get('npasswd')
        cpasswd = request.POST.get('cpasswd')
        uname = request.session['user_name']
        try:
            ul = user_login.objects.get(uname=uname,passwd=opasswd,u_type='admin')
            if ul is not None:
                ul.passwd=npasswd
                ul.save()
                context = {'msg': 'Password Changed'}
                return render(request, './myapp/admin_changepassword.html', context)
            else:
                context = {'msg': 'Password Not Changed'}
                return render(request, './myapp/admin_changepassword.html', context)
        except user_login.DoesNotExist:
            context = {'msg': 'Password Err Not Changed'}
            return render(request, './myapp/admin_changepassword.html', context)
    else:
        context = {'msg': ''}
        return render(request, './myapp/admin_changepassword.html', context)

from .models import category_master

def admin_category_master_add(request):
    if request.method == 'POST':
        category_name = request.POST.get('category_name')

        cm = category_master(category_name=category_name)
        cm.save()
        context={'msg':'Category Added'}
        return render(request, 'myapp/admin_category_master_add.html',context)

    else:
        return render(request, 'myapp/admin_category_master_add.html')

def admin_category_master_delete(request):
    id = request.GET.get('id')
    print("id="+id)

    cm = category_master.objects.get(id=int(id))
    cm.delete()

    cm_l = category_master.objects.all()
    context ={'category_list':cm_l,'msg':'Record Deleted'}
    return render(request,'myapp/admin_category_master_view.html',context)

def admin_category_master_view(request):
    cm_l = category_master.objects.all()
    context = {'category_list': cm_l}
    return render(request, 'myapp/admin_category_master_view.html', context)

def admin_location_master_add(request):
    if request.method == 'POST':
        loc_name =request.POST.get('loc_name')
        addr1 = request.POST.get('addr1')
        addr2 = request.POST.get('addr2')
        addr3 = request.POST.get('addr3')
        pin = request.POST.get('pin')
        lat = request.POST.get('lat')
        lng = request.POST.get('lng')
        radius = request.POST.get('radius')
        remarks = request.POST.get('remarks')
        lm = location_master(loc_name=loc_name,addr1=addr1,addr2=addr2,addr3=addr3,pin=pin,lat=lat,lng=lng,radius=radius,remarks=remarks)
        lm.save()
        context={'msg':'Record added'}
        return render(request, 'myapp/admin_location_master_add.html',context)

    else:
        return render(request, 'myapp/admin_location_master_add.html')

def admin_location_master_delete(request):
    id = request.GET.get('id')
    print("id="+id)

    lm = location_master.objects.get(id=int(id))
    lm.delete()

    lm_l = location_master.objects.all()
    context ={'location_list':lm_l}
    return render(request,'myapp/admin_location_master_view.html',context)

def admin_location_master_view(request):
    lm_l = location_master.objects.all()
    context = {'location_list': lm_l}
    return render(request, 'myapp/admin_location_master_view.html', context)

from .models import location_master, pic_pool
from django.core.files.storage import FileSystemStorage
def admin_pic_pool_add(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        pic_path = fs.save(uploaded_file.name, uploaded_file)

        category_master_id = int(request.POST.get('category_master_id'))
        location_master_id = int(request.POST.get('location_master_id'))
        pic_obj = pic_pool(pic_path=pic_path,category_master_id=category_master_id,location_master_id=location_master_id)
        pic_obj.save()
        category_list = category_master.objects.all()
        location_list = location_master.objects.all()

        context = {'category_list': category_list, 'location_list': location_list,'msg':'Uploaded'}

        return render(request, 'myapp/admin_pic_pool_add.html',context)
    else:
        category_list = category_master.objects.all()
        location_list = location_master.objects.all()

        context = {'category_list': category_list,'location_list':location_list}

        return render(request, 'myapp/admin_pic_pool_add.html',context)


def admin_pic_pool_delete(request):
    id = request.GET.get('id')
    print("id="+id)

    lm = pic_pool.objects.get(id=int(id))
    lm.delete()

    pp_l = pic_pool.objects.all()

    lm_l = location_master.objects.all()
    lmd = {}
    for nm in lm_l:
        lmd[nm.id] = nm.loc_name

    cm_l = category_master.objects.all()
    cmd = {}
    for nm in cm_l:
        cmd[nm.id] = nm.category_name

    context = {'pic_list':pp_l,'location_list': lmd,'category_list':cm_l}
    return render(request,'myapp/admin_pic_pool_view.html',context)

def admin_pic_pool_view(request):
    pp_l = pic_pool.objects.all()

    lm_l = location_master.objects.all()
    lmd = {}
    for nm in lm_l:
        lmd[nm.id] = nm.loc_name

    cm_l = category_master.objects.all()
    cmd = {}
    for nm in cm_l:
        cmd[nm.id] = nm.category_name

    context = {'pic_list': pp_l, 'location_list': lmd, 'category_list': cmd}
    return render(request, 'myapp/admin_pic_pool_view.html', context)

def admin_staff_user_add(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        password = request.POST.get('password')
        u_type = 'staff'

        ul = user_login(uname=uname,passwd=password,u_type=u_type)
        ul.save()
        context ={'msg':'Staff Created'}
        return render(request, 'myapp/admin_staff_user_add.html',context)

    else:
        return render(request, 'myapp/admin_staff_user_add.html')

def admin_staff_user_delete(request):
    id = request.GET.get('id')
    print("id="+id)

    nm = user_login.objects.get(id=int(id))
    nm.delete()

    nm_l = user_login.objects.filter(u_type='staff')
    context ={'staff_list':nm_l}
    return render(request,'myapp/admin_staff_user_view.html',context)

def admin_staff_user_view(request):
    nm_l = user_login.objects.filter(u_type='staff')
    context = {'staff_list': nm_l}
    return render(request, 'myapp/admin_staff_user_view.html', context)

############################################################################
################################## STAFF ########################
######STAFF###########
def staff_login(request):

    if request.method == 'POST':
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')

        ul = user_login.objects.filter(uname=uname, passwd=passwd,u_type='staff')

        if len(ul) == 1:
            request.session['user_id'] = ul[0].id
            request.session['user_name'] = ul[0].uname
            context = {'uname': request.session['user_name']}
            return render(request, 'myapp/staff_home.html',
                          context)
        else:
            return render(request, 'myapp/staff_login.html')
    else:
        return render(request, 'myapp/staff_login.html')

def staff_home(request):

    try:
        uname = request.session['user_id']
        print(uname)
    except:
        return staff_login(request)

    context = {'uname':request.session['user_name']}
    return render(request,'./myapp/staff_home.html',context)

def staff_changepassword(request):
    if request.method == 'POST':
        uname = request.session['user_name']
        new_password = request.POST.get('new_password')
        current_password = request.POST.get('current_password')
        print("username:::" + uname)
        print("current_password" + str(current_password))

        try:

            ul = user_login.objects.get(uname=uname, passwd=current_password)

            if ul is not None:
                ul.passwd = new_password  # change field
                ul.save()
                return render(request, './myapp/staff_settings.html')
            else:
                return render(request, './myapp/staff_settings.html')
        except user_login.DoesNotExist:
            return render(request, './myapp/staff_changepassword.html')
    else:
        return render(request, './myapp/staff_changepassword.html')


def staff_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return staff_login(request)
    else:
        return staff_login(request)

from .models import user_search_history
from datetime import datetime
def staff_search_history_add(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()

        pic_path = fs.save(randomString(10)+uploaded_file.name, uploaded_file)
        print(pic_path)

        pic_list = pic_pool.objects.all()
    
        cm = category_master.objects.get(id=int(1))

        user_id = int(request.session['user_id'])
        result = cm.category_name
        dt = datetime.today().strftime('%Y-%m-%d')
        tm = datetime.today().strftime('%H:%M:%S')

        status = ''

        ud = user_search_history(user_id=user_id, pic_path=pic_path, result=result, dt=dt, tm=tm, status=status)
        ud.save()

        context = {'category_name': cm.category_name}
        return render(request, 'myapp/staff_search_result.html',context)
    else:
        context = {}

        return render(request, 'myapp/staff_search_history_add.html',context)

def staff_search_history_delete(request):
    id = request.GET.get('id')
    print("id="+id)

    lm = user_search_history.objects.get(id=int(id))
    lm.delete()
    return staff_search_history_view(request)

def staff_search_history_view(request):
    user_id = int(request.session['user_id'])
    ush_l = user_search_history.objects.filter(user_id=int(user_id))

    context = {'search_list': ush_l}
    return render(request, 'myapp/staff_search_history_view.html', context)

###########################################################################
###################################################USER #########################
from .models import user_details

def user_login_check(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')

        ul = user_login.objects.filter(uname=uname, passwd=passwd, u_type='user')
        print(len(ul))
        if len(ul) == 1:
            request.session['user_id'] = ul[0].id
            request.session['user_name'] = ul[0].uname
            context = {'uname': request.session['user_name']}
            #send_mail('Login','welcome'+uname,uname)
            return render(request, 'myapp/user_home.html',context)
        else:
            context = {'msg': 'Invalid Credentials'}
            return render(request, 'myapp/user_login.html',context)
    else:
        return render(request, 'myapp/user_login.html')

def user_home(request):

    context = {'uname':request.session['user_name']}
    return render(request,'./myapp/user_home.html',context)
    #send_mail("heoo", "hai", 'snehadavisk@gmail.com')

def user_details_add(request):
    if request.method == 'POST':

        fname = request.POST.get('fname')
        lname = request.POST.get('lname')

        gender = request.POST.get('gender')
        age = request.POST.get('age')
        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('pwd')
        uname=email
        #status = "new"

        ul = user_login(uname=uname, passwd=password, u_type='user')
        ul.save()
        user_id = user_login.objects.all().aggregate(Max('id'))['id__max']

        ud = user_details(user_id=user_id,fname=fname, lname=lname, gender=gender, age=age,addr=addr, pin=pin, contact=contact, email=email )
        ud.save()

        print(user_id)
        context = {'msg': 'User Registered'}
        return render(request, 'myapp/user_login.html',context)

    else:
        return render(request, 'myapp/user_details_add.html')

def user_changepassword(request):
    if request.method == 'POST':
        uname = request.session['user_name']
        new_password = request.POST.get('new_password')
        current_password = request.POST.get('current_password')
        print("username:::" + uname)
        print("current_password" + str(current_password))

        try:

            ul = user_login.objects.get(uname=uname, passwd=current_password)

            if ul is not None:
                ul.passwd = new_password  # change field
                ul.save()
                context = {'msg':'Password Changed Successfully'}
                return render(request, './myapp/user_changepassword.html',context)
            else:
                context = {'msg': 'Password Not Changed'}
                return render(request, './myapp/user_changepassword.html', context)
        except user_login.DoesNotExist:
            context = {'msg': 'Password Not Changed'}
            return render(request, './myapp/user_changepassword.html', context)
    else:
        return render(request, './myapp/user_changepassword.html')



def user_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return user_login_check(request)
    else:
        return user_login_check(request)

#######################################################################

import random
import string

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

