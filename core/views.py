from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import contacts, subscription
from django.shortcuts import render
from django.http import HttpResponse
import json, requests
from django.http import JsonResponse
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# Create your views here.
def homepage(request):
    context={

    }

    return render(request, 'index.html', context)

def boardresult(request):
    context={

    }

    return render(request, 'boardresult.html', context)

def uniresult(request):
    context={

    }

    return render(request, 'uniresult.html', context)

def about(request):
    context={

    }

    return render(request, 'about.html', context)

def contact(request):
    context={

    }
    if request.POST.get('action') == 'post':
        fname = (request.POST['fname'])
        lname = (request.POST['lname'])
        email = (request.POST['email'])
        content = (request.POST['content'])

        contacts.objects.create(fname=fname,lname=lname,email=email,content=content)
    else:
        pass

    return render(request, 'contact.html', context)

def subscribe(request):
    context={

    }
    if request.POST.get('action') == 'post':
        name = (request.POST['name'])
        email = (request.POST['email'])
        print(email)

        subscription.objects.create(name = name, email = email)
    else:
        pass

    return HttpResponse(status=200)


def pairing(request):
    context={
    }


    return render(request, 'pairing.html', context)

def datesheets(request):
    context={

    }

    return render(request, 'datesheets.html', context)

def merit(request):
    html=""
    context={
        'htmlcontent': html,
    }

    return render(request, 'merit.html', context)

def lahoreboard(request):
    context = {
    }


    if request.POST.get('action') == 'post':
        if request.POST['rollno'] == "":

            return render(request, 'lahoreboard.html', context) # If roll number empty Return default page

        #   Selecting SSC or HSSC on the basis of matric and Inter
        if (request.POST['deg']) == "matric":
            course = 'SSC'
        else:
            course ='HSSC'

        # Scarping HTML from Board website
        import requests
        url = 'http://result.biselahore.com/'
        data_to_post = {
            '__VIEWSTATE': '/wEPDwUJNjgxMTYyNzg0ZBgBBQl0eHRGb3JtTm8PDzwrAAcAZGSjiSBSTdMwm22HlxZIjK/3GosLd7qQGbLdJGzAL6r6Xw==',
            '__VIEWSTATEGENERATOR': 'CA0B0334',
            'rdlistCourse': course,
            'txtFormNo': (request.POST['rollno']),
            'ddlExamType': (request.POST['part']),
            'ddlExamYear': (request.POST['year']),
            'Button1': 'View Result'
        }
        html = requests.post(url, data=data_to_post)
        html = html.text


        #   Adding base url to images so they are visible.
        html=(html.replace("Images/", "http://result.biselahore.com/Images/"))
        half = (html[html.find("Checkbrowser('") + 14:])
        image_url=(half[:half.find("'")])
        print(image_url)
        # Profile pic
        html = (html.replace('<img id="imgDisplay"', '<img id="imgDisplay" src="http://result.biselahore.com/ImageLoader.aspx?Updateid='+image_url+'"'))


        context={
            'htmlcontent': html,
        }
    else:
        pass
    return render(request, 'lahoreboard.html', context)


def federalboard(request):
    context = {
    }


    if request.POST.get('action') == 'post':
        if request.POST['rollno'] == "":

            return render(request, 'federalboard.html', context) # If roll number empty Return default page

        #   Selecting SSC or HSSC on the basis of matric and Inter
        if (request.POST['deg']) == "matric":
            course = 'SSC'
        else:
            course = 'HSSC'

        part = (request.POST['part'])
        print(course,part)

        # Scarping HTML from Board website
        import requests
        if course == 'HSSC':
            if part == "2":
                url = "https://www.fbise.edu.pk/res-hssc-II.php/"
            elif part == "1":
                url = "https://www.fbise.edu.pk/res-hssc-I.php/"
            elif part == "0":
                url = "https://www.fbise.edu.pk/res-hsscsup.php/"
        elif course == 'SSC':
            if part == "2":
                url = "https://www.fbise.edu.pk/res-ssc-II.php/"
            elif part == "1":
                url = "https://www.fbise.edu.pk/res-ssc-I.php/"
            elif part == "0":
                url = "https://www.fbise.edu.pk/res-sscsup.php/"

        data_to_post = {
            'roll_no': (request.POST['rollno']),
        }

        html = requests.post(url, data=data_to_post)
        html = html.text



        html = (html[html.find("<table width='850'"):])
        if len(html) <100:
            html = "<h1 style='background-color: rgb(255,0,0);color: rgb(255,255,255)'>ROLL NUMBER NOT FOUND</h1>"


        context={
            'htmlcontent': html,
        }
    else:
        pass
    return render(request, 'federalboard.html', context)

def karachiboard(request):
    context={

    }

    return render(request, 'karachiboard.html', context)

def multanboard(request):
    context = {
    }


    if request.POST.get('action') == 'post':
        if request.POST['rollno'] == "":

            return render(request, 'multanboard.html', context) # If roll number empty Return default page

        #   Selecting SSC or HSSC on the basis of matric and Inter
        if (request.POST['deg']) == "matric":
            course = 'SSC'
        else:
            course = 'HSSC'

        part = (request.POST['part'])
        year = (request.POST['year'])

        url = "https://www.bisemultan.edu.pk/ajax/res2.php"

        # Scarping HTML from Board website
        import requests
        if course == 'HSSC':
            if part == "2":
                typee = 'c2YzMmZkI2ExMg~~'
                if year == "2019":
                    year = 'c2YzMmZkI2kxMjAxOXAy'
                elif year == "2018":
                    year = 'c2YzMmZkI2kxMjAxOHAy'
                elif year == "2017":
                    year = 'c2YzMmZkI2kxMjAxN3Ay'
                elif year == "2016":
                    year = 'c2YzMmZkI2kxMjAxNnAy'
                elif year == "2015":
                    year = 'c2YzMmZkI2kxMjAxNXAy'
                elif year == "2014":
                    year = "c2YzMmZkI2kxMjAxNHAy"
                elif year == "2013":
                    year = "c2YzMmZkI2kxMjAxM3Ay"
                elif year == "2012":
                    year = 'c2YzMmZkI2kxMjAxMnAy'

            elif part == "1":
                typee = 'c2YzMmZkI2ExMQ~~'
                if year == "2019":
                    year = 'c2YzMmZkI2kxMjAxOXAx'
                elif year == "2018":
                    year = 'c2YzMmZkI2kxMjAxOHAx'
                elif year == "2017":
                    year = 'c2YzMmZkI2kxMjAxN3Ax'
                elif year == "2016":
                    year = 'c2YzMmZkI2kxMjAxNnAx'
                elif year == "2015":
                    year = 'c2YzMmZkI2kxMjAxNXAx'
                elif year == "2014":
                    year = "c2YzMmZkI2kxMjAxNHAx"
                elif year == "2013":
                    year = "c2YzMmZkI2kxMjAxM3Ax"
                elif year == "2012":
                    year = 'c2YzMmZkI2kxMjAxMnAx'
            elif part == "0":
                typee = 'c2YzMmZkI2ExMg~~'
                if year == "2019":
                    year = 'c2YzMmZkI2kyMjAxOXAy'
                elif year == "2018":
                    year = 'c2YzMmZkI2kyMjAxOHAy'
                elif year == "2017":
                    year = 'c2YzMmZkI2kyMjAxN3Ay'
                elif year == "2016":
                    year = 'c2YzMmZkI2kyMjAxNnAy'
                elif year == "2015":
                    year = 'c2YzMmZkI2kyMjAxNXAy'
                elif year == "2014":
                    year = "c2YzMmZkI2kyMjAxNHAy"
                elif year == "2013":
                    year = "c2YzMmZkI2kyMjAxM3Ay"
                elif year == "2012":
                    year = 'c2YzMmZkI2kyMjAxMnAy'



        elif course == 'SSC':
            if part == "2":
                typee='c2YzMmZkI2ExMA~~'
                if year == "2019":
                    year = 'c2YzMmZkI2FubnVhbDIwMTk~'
                elif year == "2018":
                    year = 'c2YzMmZkI2FubnVhbDIwMTg~'
                elif year == "2017":
                    year = 'c2YzMmZkI2FubnVhbDIwMTc~'
                elif year == "2016":
                    year = 'c2YzMmZkI2FubnVhbDIwMTY~'
                elif year == "2015":
                    year = 'c2YzMmZkI2FubnVhbDIwMTU~'
                elif year == "2014":
                    year = "c2YzMmZkI2FubnVhbDIwMTQ~"
                elif year == "2013":
                    year = "c2YzMmZkI2FubnVhbDIwMTM~"
                elif year == "2012":
                    year = 'c2YzMmZkI2FubnVhbDIwMTI~'
            elif part == "1":
                typee='c2YzMmZkI2E5'
                if year == "2019":
                    year = 'c2YzMmZkI2FubnVhbDIwMTlwMQ~~'
                elif year == "2018":
                    year = 'c2YzMmZkI2FubnVhbDIwMThwMQ~~'
                elif year == "2017":
                    year = 'c2YzMmZkI2FubnVhbDIwMTdwMQ~~'
                elif year == "2016":
                    year = 'c2YzMmZkI2FubnVhbDIwMTZwMQ~~'
                elif year == "2015":
                    year = 'c2YzMmZkI2FubnVhbDIwMTVwMQ~~'
                elif year == "2014":
                    year = "c2YzMmZkI2FubnVhbDIwMTRwMQ~~"
                elif year == "2013":
                    year = "c2YzMmZkI2FubnVhbDIwMTNwMQ~~"
                elif year == "2012":
                    year = 'c2YzMmZkI2FubnVhbDIwMTJwMQ~~'
            elif part == "0":
                typee='c2YzMmZkI2ExMA~~'
                if year == "2019":
                    year = 'c2YzMmZkI3N1cHBseTIwMTk~'
                elif year == "2018":
                    year = 'c2YzMmZkI3N1cHBseTIwMTg~'
                elif year == "2017":
                    year = 'c2YzMmZkI3N1cHBseTIwMTc~'
                elif year == "2016":
                    year = 'c2YzMmZkI3N1cHBseTIwMTY~'
                elif year == "2015":
                    year = 'c2YzMmZkI3N1cHBseTIwMTU~'
                elif year == "2014":
                    year = "c2YzMmZkI3N1cHBseTIwMTQ~"
                elif year == "2013":
                    year = "c2YzMmZkI3N1cHBseTIwMTM~"
                elif year == "2012":
                    year = 'c2YzMmZkI3N1cHBseTIwMTI~'



        data_to_post = {
            'rno': (request.POST['rollno']),
            'session': year,
            'type': typee,
        }
        html = requests.post(url, data=data_to_post)
        html = html.text




        context={
            'htmlcontent': html,
        }
    else:
        pass
    return render(request, 'multanboard.html', context)

def peshawarboard(request):
    context = {
    }

    if request.POST.get('action') == 'post':
        if request.POST['rollno'] == "":
            return render(request, 'peshawarboard.html', context)  # If roll number empty Return default page


        # Scarping HTML from Board website
        import requests
        url = "https://www.bisep.com.pk/results/ShowResult.php?Search=RollNo&RollNo="+request.POST['rollno']



        html = requests.get(url)
        html = html.text

        # html = (html[html.find("<table width='850'"):])
        # if len(html) < 100:
        #     html = "<h1 style='background-color: rgb(255,0,0);color: rgb(255,255,255)'>ROLL NUMBER NOT FOUND</h1>"

        context = {
            'htmlcontent': html,
        }
    else:
        pass

    return render(request, 'peshawarboard.html', context)

def rawalpindiboard(request):
    context={

    }

    return render(request, 'rawalpindiboard.html', context)

def faisalabadboard(request):
    context={

    }

    return render(request, 'faisalabadboard.html', context)

def gujranwalaboard(request):
    context={

    }

    return render(request, 'gujranwalaboard.html', context)

def hyderabadboard(request):
    context={

    }

    return render(request, 'hyderabadboard.html', context)

def abbottabadboard(request):
    context={

    }

    return render(request, 'abbottabadboard.html', context)

def mardanboard(request):
    context={

    }

    return render(request, 'mardanboard.html', context)

def sukkurboard(request):
    context={

    }

    return render(request, 'sukkurboard.html', context)

def sargodhaboard(request):
    context={

    }

    return render(request, 'sargodhaboard.html', context)

def bannuboard(request):
    context={

    }

    return render(request, 'bannuboard.html', context)

def larkanaboard(request):
    context={

    }

    return render(request, 'larkanaboard.html', context)

def sahiwalboard(request):
    context={

    }

    return render(request, 'sahiwalboard.html', context)

def swatboard(request):
    context={

    }

    return render(request, 'swatboard.html', context)

def mipurkhasboard(request):
    context={

    }

    return render(request, 'mirpurkhasboard.html', context)

def bahawalpurboard(request):
    context={

    }

    return render(request, 'bahawalpurboard.html', context)

def dgkhanboard(request):
    context={

    }

    return render(request, 'dgkhanboard.html', context)

def dikhanboard(request):
    context={

    }

    return render(request, 'dikhanboard.html', context)

def aghakhanboard(request):
    context={

    }

    return render(request, 'aghakhanboard.html', context)

def malakandboard(request):
    context={

    }

    return render(request, 'malakandboard.html', context)

def kohatboard(request):
    context={

    }

    return render(request, 'kohatboard.html', context)

def pbteboard(request):
    context={

    }

    return render(request, 'pbteboard.html', context)

def kpbteboard(request):
    context={

    }

    return render(request, 'kpbteboard.html', context)

def sbteboard(request):
    context={

    }

    return render(request, 'sbteboard.html', context)

def ajkboard(request):
    context={

    }

    return render(request, 'ajkboard.html', context)

def baecboard(request):
    context={

    }

    return render(request, 'baecboard.html', context)

def quettaboard(request):
    context={

    }

    return render(request, 'quettaboard.html', context)

def fdeboard(request):
    context={

    }

    return render(request, 'fdeboard.html', context)

def doebboard(request):
    context={

    }

    return render(request, 'doebboard.html', context)

def pecboard(request):
    context={

    }

    return render(request, 'pecboard.html', context)
    
    
def pieas(request):
    context={
    }
    entry_test = 60
    matric = 15
    fsc = 25

    if request.POST.get('action') == 'post':
        if request.POST['omatric'] == "" or request.POST['tmatric'] == "" or request.POST['ofsc'] == ""\
                or request.POST['tfsc'] == "" or request.POST['oentry'] == "" or request.POST['tentry'] == "":
            html = "<h1 style='color: red;text-align:center'>PLEASE ENTER ALL INFORMATION</h1>"
            return render(request, 'pieascal.html', {'htmlcontent':html}) # If roll number empty Return default page


        omatric = int(request.POST['omatric'])
        tmatric = int(request.POST['tmatric'])
        ofsc = int(request.POST['ofsc'])
        tfsc = int(request.POST['tfsc'])
        oentry = int(request.POST['oentry'])
        tentry = int(request.POST['tentry'])
        m_number = int(request.POST['number'])


        agg = (((omatric/tmatric)*matric/100)+((ofsc/tfsc)*fsc/100)+((oentry/tentry)*entry_test/100))*100
        agg = str(agg)

        disip = ""
        if m_number <= 150:
            disip += "Mechanical Engineering<br>"
        if m_number <= 350:
            disip += "Electrical Engineering<br>"
        if m_number <= 550:
            disip += "Chemical Engineering<br>"
        if m_number <= 800:
            disip += "BS Computer Science<br>"
        if m_number <= 950:
            disip += "Material And Matallurgical Engineering<br>"
        if m_number <= 1050:
            disip += "BS Physics<br>"

        html = "<h1 style='color: white;text-align:center'> Your Aggregate</h1>" \
               "<h1 style='color: green;text-align:center'>" + agg[:agg.find(".") + 3] + "%</h1>" \
                                                                                         "<h1 style='color: white;text-align:center'> You're Selected in:</h1> " \
                                                                                         "<p style='color: white;text-align:center'>" + disip + "</p>"
        context={
            'htmlcontent': html,
        }
    else:
        pass
    return render(request, 'pieascal.html', context)
    
def mdcat(request):
    context={
    }
    entry_test = 50
    fsc = 50
    tentry = 100

    if request.POST.get('action') == 'post':
        if request.POST['ofsc'] == ""\
                or request.POST['tfsc'] == "" or request.POST['oentry'] == "":
            html = "<h1 style='color: red;text-align:center'>PLEASE ENTER ALL INFORMATION</h1>"
            return render(request, 'pieascal.html', {'htmlcontent':html}) # If roll number empty Return default page



        ofsc = int(request.POST['ofsc'])
        tfsc = int(request.POST['tfsc'])
        oentry = int(request.POST['oentry'])


        agg = (((ofsc/tfsc)*fsc/100)+((oentry/tentry)*entry_test/100))*100


        disip = ""
        if agg >= 69:
            disip += "KIDS<br>"
        if agg >= 70:
            disip += "NMC<br>"
            disip += "KCD<br>"
            disip += "ADS<br>"
        if agg >= 71:
            disip += "KIMS<br>"
            disip += "GMC<br>"
            disip += "BMC<br>"
            disip += "GKMC<br>"
        if agg >= 72:
            disip += "SMC<br>"
        if agg >= 73:
            disip += "BKMC<br>"
            disip += "AMC<br>"
        if agg >= 74:
            disip += "KGMC<br>"
        if agg >= 75:
            disip += "KMC<br>"
        agg= str(agg)
        html = "<h1 style='color: white;text-align:center'> Your Aggregate</h1>" \
               "<h1 style='color: green;text-align:center'>" + agg[:agg.find(".") + 3] + "%</h1>" \
                                                                                         "<h1 style='color: white;text-align:center'> You're Selected in:</h1> " \
                                                                                         "<p style='color: white;text-align:center'>" + disip + "</p>"
        context={
            'htmlcontent': html,
        }
    else:
        pass
    return render(request, 'mdcatcal.html', context)
 
def nust(request):
    context = {
    }
    entry_test = 75
    fsc = 15
    matric = 10
    tentry = 200

    if request.POST.get('action') == 'post':
        if request.POST['ofsc'] == "" \
                or request.POST['tfsc'] == "" or request.POST['oentry'] == "" or request.POST['omatric'] == "" or request.POST['tmatric'] == "":
            html = "<h1 style='color: red;text-align:center'>PLEASE ENTER ALL INFORMATION</h1>"
            return render(request, 'nustcal.html', {'htmlcontent': html})  # If roll number empty Return default page

        omatric = int(request.POST['omatric'])
        tmatric = int(request.POST['tmatric'])
        ofsc = int(request.POST['ofsc'])
        tfsc = int(request.POST['tfsc'])
        oentry = int(request.POST['oentry'])

        agg = (((omatric/tmatric)*matric/100)+((ofsc / tfsc) * fsc / 100) + ((oentry / tentry) * entry_test / 100)) * 100
        disip = ""

        if agg >= 79.5:
            disip += "BS Mechanical Engineering (Islamabad)<br>"
        if agg >= 77.8:
            disip += "BS Electrical Engineering (Islamabad)<br>"
        if agg >= 74.9:
            disip += "BS Civil Engineering (Islamabad)<br>"
        if agg >= 74:
            disip += "BS Chemical Engineering (Islamabad)<br>"
        if agg >= 73:
            disip += "BS Software Engineering (Islamabad)<br>"
        if agg >= 69.9:
            disip += "BS Environmental Engineering (Islamabad)<br>"
        if agg >= 69:
            disip += "BS Geo Informatics Engineering (Islamabad)<br>"
        if agg >= 70.4:
            disip += "BS Computer Science (Islamabad)<br>"

        if agg >= 79:
            disip += "BS Electrical Engineering (CEME Rawalpindi)<br>"
        if agg >= 78.8:
            disip += "BS Mechanical Engineering (CEME Rawalpindi)<br>"
        if agg >= 75.7:
            disip += "BS Mechatronics Engineering (CEME Rawalpindi)<br>"

        if agg >= 71.25:
            disip += "BS Computer Software Engineering (MCS Rawalpindi)<br>"
        if agg >= 70.1:
            disip += "BS Computer Engineering (MCS Rawalpindi)<br>"
        if agg >= 70.55:
            disip += "BS Telecom Engineering (MCS Rawalpindi)<br>"
            disip += "BS Material Engineering (Islamabad)<br>"

        if agg >= 78.2:
            disip += "BS Aerospace Engineering (Risalpur)<br>"
        if agg >= 76.1:
            disip += "BS Avionics Engineering (Risalpur)<br>"
        if agg >= 72.3:
            disip += "BS Civil Engineering (Risalpur))<br>"

        agg = str(agg)

        html = "<h1 style='color: white;text-align:center'> Your Aggregate</h1>" \
               "<h1 style='color: green;text-align:center'>" + agg[:agg.find(".") + 3] + "%</h1>" \
                                                                                         "<h1 style='color: white;text-align:center'> You're Selected in:</h1> " \
                                                                                         "<p style='color: white;text-align:center'>" + disip + "</p>"

        context = {
            'htmlcontent': html,
        }
    else:
        pass
    return render(request, 'nustcal.html', context)
 
def uetlahore(request):
    context = {
    }
    entry_test = 30
    fsc = 70
    tentry = 400

    if request.POST.get('action') == 'post':
        if request.POST['ofsc'] == "" \
                or request.POST['tfsc'] == "" or request.POST['oentry'] == "":
            html = "<h1 style='color: red;text-align:center'>PLEASE ENTER ALL INFORMATION</h1>"
            return render(request, 'uetlahorecal.html', {'htmlcontent': html})  # If roll number empty Return default page

        ofsc = int(request.POST['ofsc'])
        tfsc = int(request.POST['tfsc'])
        oentry = int(request.POST['oentry'])

        agg = (((ofsc / tfsc) * fsc / 100) + ((oentry / tentry) * entry_test / 100)) * 100
        disip = ""

        if agg >= 67:
            disip += "BS - Mining Engineering<br>"
            disip += "BS - Geological Engineering<br>"
            disip += "BS - Product And Industrial Design<br>"
        if agg >= 69:
            disip += "BS - Transport Engineering<br>"
            disip += "BS - Environment Engineering<br>"
        if agg >= 70:
            disip += "BS - Matallurgical And Mterial Engineering<br>"
            disip += "BS - City And Reigonal Planing<br>"
        if agg >= 71:
            disip += "BS - Architecture<br>"
        if agg >= 72:
            disip += "BS - Computer Science<br>"
            disip += "BS - Industrial And Manufacturing Engineering<br>"
        if agg >= 73:
            disip += "BS - Building And Architectural Engineering<br>"
            disip += "BS - Petroleum And Gas Engineering<br>"
        if agg >= 74:
            disip += "BS - Chemical Engineering<br>"
            disip += "BS - Mechatronics<br>"
        if agg >= 75:
            disip += "BS - Computer Engineering<br>"
            disip += "BS - Electrical Engineering<br>"
            if agg >= 76:
                disip += "BS - Civil Engineering<br>"
            if agg >= 78:
                disip += "BS - Mechanical Engineerinng<br>"

        agg = str(agg)

        html = "<h1 style='color: white;text-align:center'> Your Aggregate</h1>" \
               "<h1 style='color: green;text-align:center'>" + agg[:agg.find(".") + 3] + "%</h1>" \
                                                                                         "<h1 style='color: white;text-align:center'> You're Selected in:</h1> " \
                                                                                         "<p style='color: white;text-align:center'>" + disip + "</p>"

        context = {
            'htmlcontent': html,
        }
    else:
        pass
    return render(request, "uetlahorecal.html", context)


def comsats(request):
    context={
    }
    entry_test = 50
    matric = 10
    fsc = 40

    if request.POST.get('action') == 'post':
        if request.POST['omatric'] == "" or request.POST['tmatric'] == "" or request.POST['ofsc'] == ""\
                or request.POST['tfsc'] == "" or request.POST['oentry'] == "" or request.POST['tentry'] == "":
            html = "<h1 style='color: red;text-align:center'>PLEASE ENTER ALL INFORMATION</h1>"
            return render(request, 'comsatscal.html', {'htmlcontent':html}) # If roll number empty Return default page


        omatric = int(request.POST['omatric'])
        tmatric = int(request.POST['tmatric'])
        ofsc = int(request.POST['ofsc'])
        tfsc = int(request.POST['tfsc'])
        oentry = int(request.POST['oentry'])
        tentry = int(request.POST['tentry'])

        agg = (((omatric/tmatric)*matric/100)+((ofsc/tfsc)*fsc/100)+((oentry/tentry)*entry_test/100))*100

        disip = ""

        if agg >= 50:
            disip += "BS - Psychology<br>"
            disip += "BS - Math<br>"
            disip += "BS - Economics<br>"
            disip += "BS - Accounting & Finance<br>"
            disip += "BS - Bio Sciences<br>"
            disip += "BS - Bio Informatics<br>"
            disip += "BS - Physics<br>"
            disip += "BS - Electronics<br>"
        if agg >= 55:
            disip += "BS - Business Administration<br>"
        if agg >= 60:
            disip += "BS - Electrical Telecommunication Engineering<br>"
            disip += "BS - Electrical Computer Engineering<br>"
        if agg >= 65:
            disip += "BS - Electrical Power Engineering<br>"
        if agg >= 67:
            disip += "BS - Electrical Electronics Engineering<br>"
        if agg >= 69:
            disip += "BS - Computer Science<br>"

        agg = str(agg)


        html = "<h1 style='color: white;text-align:center'> Your Aggregate</h1>" \
               "<h1 style='color: green;text-align:center'>"+agg[:agg.find(".")+3]+"%</h1>" \
               "<h1 style='color: white;text-align:center'> You're Selected in:</h1> " \
                "<p style='color: white;text-align:center'>"+ disip +"</p>"

        context={
            'htmlcontent': html,
        }
    else:
        pass
    return render(request, 'comsatscal.html', context)
    
 
def giki(request):
    context = {
    }
    entry_test = 85
    matric = 5
    fsc = 10

    if request.POST.get('action') == 'post':
        if request.POST['omatric'] == "" or request.POST['tmatric'] == "" or request.POST['ofsc'] == "" \
                or request.POST['tfsc'] == "" or request.POST['oentry'] == "" or request.POST['tentry'] == "":
            html = "<h1 style='color: red;text-align:center'>PLEASE ENTER ALL INFORMATION</h1>"
            return render(request, 'gikical.html', {'htmlcontent': html})  # If roll number empty Return default page

        omatric = int(request.POST['omatric'])
        tmatric = int(request.POST['tmatric'])
        ofsc = int(request.POST['ofsc'])
        tfsc = int(request.POST['tfsc'])
        oentry = int(request.POST['oentry'])
        tentry = int(request.POST['tentry'])

        agg = (((omatric / tmatric) * matric / 100) + ((ofsc / tfsc) * fsc / 100) + (
                    (oentry / tentry) * entry_test / 100)) * 100
        disip = ""

        if agg >= 70:
            disip += "BS Computer Science.<br>"
            disip += "BS Engineering Sciences.<br>"
            disip += "BS Management Science.<br>"
        if agg >= 74:
            disip += "BS Computer Engineering.<br>"
        if agg >= 79:
            disip += "BS Chemical Engineering<br>"
            disip += "BS Electrical Engineering.<br>"
        if agg >= 85:
            disip += "BS Mechanical Engineering.<br>"

        agg = str(agg)

        html = "<h1 style='color: white;text-align:center'> Your Aggregate</h1>" \
               "<h1 style='color: green;text-align:center'>" + agg[:agg.find(".") + 3] + "%</h1>" \
                                                                                         "<h1 style='color: white;text-align:center'> You're Selected in:</h1> " \
                                                                                         "<p style='color: white;text-align:center'>" + disip + "</p>"

        context = {
            'htmlcontent': html,
        }
    else:
        pass
    return render(request, 'gikical.html', context)
    
 
def fast(request):
    context = {
    }
    entry_test = 40
    fsc = 60

    if request.POST.get('action') == 'post':
        if request.POST['ofsc'] == "" \
                or request.POST['tfsc'] == "" or request.POST['oentry'] == "" or request.POST['tentry'] == "":
            html = "<h1 style='color: red;text-align:center'>PLEASE ENTER ALL INFORMATION</h1>"
            return render(request, 'fastcal.html', {'htmlcontent': html})  # If roll number empty Return default page


        ofsc = int(request.POST['ofsc'])
        tfsc = int(request.POST['tfsc'])
        oentry = int(request.POST['oentry'])
        tentry = int(request.POST['tentry'])

        agg = (((ofsc / tfsc) * fsc / 100) + (
                (oentry / tentry) * entry_test / 100)) * 100
        disip = ""

        if agg >= 65:
            disip += "BBA<br>"
            disip += "Artificial Intelligence<br>"
        disip += "Cybr Security<br>"
        if agg >= 80:
            disip += "Electrical Engineering<br>"
        if agg >= 82:
            disip += "Civil Engineering<br>"
        if agg >= 84:
            disip += "	Computer Science<br>"

        agg = str(agg)

        html = "<h1 style='color: white;text-align:center'> Your Aggregate</h1>" \
               "<h1 style='color: green;text-align:center'>" + agg[:agg.find(".") + 3] + "%</h1>" \
                                                                                         "<h1 style='color: white;text-align:center'> You're Selected in:</h1> " \
                                                                                         "<p style='color: white;text-align:center'>" + disip + "</p>"

        context = {
            'htmlcontent': html,
        }
    else:
        pass
    return render(request, 'fastcal.html', context)
    
    
 
def gcu(request):
    context = {
    }
    entry_test = 50
    fsc = 50

    if request.POST.get('action') == 'post':
        if request.POST['ofsc'] == "" \
                or request.POST['tfsc'] == "" or request.POST['oentry'] == "" or request.POST['tentry'] == "":
            html = "<h1 style='color: red;text-align:center'>PLEASE ENTER ALL INFORMATION</h1>"
            return render(request, 'gcucal.html', {'htmlcontent': html})  # If roll number empty Return default page

        ofsc = int(request.POST['ofsc'])
        tfsc = int(request.POST['tfsc'])
        oentry = int(request.POST['oentry'])
        tentry = int(request.POST['tentry'])
        agg = (((ofsc / tfsc) * fsc / 100) + (
                (oentry / tentry) * entry_test / 100)) * 100


        disip = ""

        if ofsc >= 899:
            disip += "Arts<br>"
        if ofsc >= 864:
            disip += "General Science<br>"
        if ofsc >= 973:
            disip += "Commerce<br>"
        if ofsc >= 1025:
            disip += "Computer Science<br>"
        if ofsc >= 1046:
            disip += "Pre Engineering<br>"
        if ofsc >= 1055:
            disip += "Pre Medical<br>"
        agg = str(agg)

        html = "<h1 style='color: white;text-align:center'> Your Aggregate</h1>" \
               "<h1 style='color: green;text-align:center'>" + agg[:agg.find(".") + 3] + "%</h1>" \
                                                                                         "<h1 style='color: white;text-align:center'> You're Selected in:</h1> " \
                                                                                         "<p style='color: white;text-align:center'>" + disip + "</p>"


        context = {
            'htmlcontent': html,
        }
    else:
        pass
    return render(request, 'gcucal.html', context)


def pucit(request):
    context = {
    }
    entry_test = 30
    fsc = 35
    matric = 35

    if request.POST.get('action') == 'post':
        if request.POST['ofsc'] == "" \
                or request.POST['tfsc'] == "" or request.POST['oentry'] == "" or request.POST['tentry'] == "":
            html = "<h1 style='color: red;text-align:center'>PLEASE ENTER ALL INFORMATION</h1>"
            return render(request, 'pucitcal.html', {'htmlcontent': html})  # If roll number empty Return default page


        omatric = int(request.POST['omatric'])
        tmatric = int(request.POST['tmatric'])
        ofsc = int(request.POST['ofsc'])
        tfsc = int(request.POST['tfsc'])
        oentry = int(request.POST['oentry'])
        tentry = int(request.POST['tentry'])

        agg = (((omatric / tmatric) * matric / 100) + ((ofsc / tfsc) * fsc / 100) + (
                    (oentry / tentry) * entry_test / 100)) * 100
        disip = ""

        if agg >= 79:
            disip += "BS Informatics Technology<br>"
        if agg >= 81:
            disip += "BS Computer Science<br>"
        if agg >= 85:
            disip += "BS Software Engineering<br>"

        agg = str(agg)

        html = "<h1 style='color: white;text-align:center'> Your Aggregate</h1>" \
               "<h1 style='color: green;text-align:center'>" + agg[:agg.find(".") + 3] + "%</h1>" \
                                                                                         "<h1 style='color: white;text-align:center'> You're Selected in:</h1> " \
                                                                                         "<p style='color: white;text-align:center'>" + disip + "</p>"

        context = {
            'htmlcontent': html,
        }
    else:
        pass

    return render(request, 'pucitcal.html', context)
    
def ist(request):
    context = {
    }
    entry_test = 40
    fsc = 40
    matric = 20

    if request.POST.get('action') == 'post':
        if request.POST['ofsc'] == "" \
                or request.POST['tfsc'] == "" or request.POST['oentry'] == "" or request.POST['tentry'] == "":
            html = "<h1 style='color: red;text-align:center'>PLEASE ENTER ALL INFORMATION</h1>"
            return render(request, 'istcal.html', {'htmlcontent': html})  # If roll number empty Return default page

        omatric = int(request.POST['omatric'])
        tmatric = int(request.POST['tmatric'])
        ofsc = int(request.POST['ofsc'])
        tfsc = int(request.POST['tfsc'])
        oentry = int(request.POST['oentry'])
        tentry = int(request.POST['tentry'])

        agg = (((omatric / tmatric) * matric / 100) + ((ofsc / tfsc) * fsc / 100) + (
                (oentry / tentry) * entry_test / 100)) * 100
        disip = ""

        if agg >= 76:
            disip += "	Space Science<br>"
        if agg >= 78:
            disip += "Material Science And Engineering<br>"
        if agg >= 79:
            disip += "Electrical Engineering<br>"
        if agg >= 81:
            disip += "Mechanical Engineering<br>"
            disip += "Aerospace Engineering<br>"

        agg = str(agg)

        html = "<h1 style='color: white;text-align:center'> Your Aggregate</h1>" \
               "<h1 style='color: green;text-align:center'>" + agg[:agg.find(".") + 3] + "%</h1>" \
                                                                                         "<h1 style='color: white;text-align:center'> You're Selected in:</h1> " \
                                                                                         "<p style='color: white;text-align:center'>" + disip + "</p>"

        context = {
            'htmlcontent': html,
        }
    else:
        pass

    return render(request, 'istcal.html', context)

def iba(request):
    context = {
    }
    fsc = 50
    matric = 50

    if request.POST.get('action') == 'post':
        if request.POST['ofsc'] == "" \
                or request.POST['tfsc'] == "" :
            html = "<h1 style='color: red;text-align:center'>PLEASE ENTER ALL INFORMATION</h1>"
            return render(request, 'ibacal.html', {'htmlcontent': html})  # If roll number empty Return default page

        omatric = int(request.POST['omatric'])
        tmatric = int(request.POST['tmatric'])
        ofsc = int(request.POST['ofsc'])
        tfsc = int(request.POST['tfsc'])
        hifz = request.POST['hifz']


        agg = ((omatric / tmatric) * matric / 100) + ((ofsc / tfsc) * fsc / 100)
        agg = agg * 100
        if hifz == "Yes":
            agg += 5


        disip = ""

        if agg >= 76:
            disip += "	Space Science<br>"
        if agg >= 78:
            disip += "Material Science And Engineering<br>"
        if agg >= 79:
            disip += "Electrical Engineering<br>"
        if agg >= 81:
            disip += "Mechanical Engineering<br>"
            disip += "Aerospace Engineering<br>"

        agg = str(agg)

        html = "<h1 style='color: white;text-align:center'> Your Aggregate</h1>" \
               "<h1 style='color: green;text-align:center'>" + agg[:agg.find(".") + 3] + "%</h1>" \
                                                                                         "<h1 style='color: white;text-align:center'> You're Selected in:</h1> " \
                                                                                         "<p style='color: white;text-align:center'>" + disip + "</p>"

        context = {
            'htmlcontent': html,
        }
    else:
        pass

    return render(request, 'ibacal.html', context)
    
def lums(request):
    context = {
    }
    fsc = 30
    matric = 70

    if request.POST.get('action') == 'post':
        if request.POST['ofsc'] == "" \
                or request.POST['tfsc'] == "" :
            html = "<h1 style='color: red;text-align:center'>PLEASE ENTER ALL INFORMATION</h1>"
            return render(request, 'lumscal.html', {'htmlcontent': html})  # If roll number empty Return default page

        omatric = int(request.POST['omatric'])
        tmatric = int(request.POST['tmatric'])
        ofsc = int(request.POST['ofsc'])
        tfsc = int(request.POST['tfsc'])

        agg = (((omatric / tmatric) * matric / 100) + ((ofsc / tfsc) * fsc / 100)) * 100
        disip = ""

        if agg >= 72:
            disip += "School of Humanities<br>"
        if agg >= 78:
            disip += "School of Science<br>"
        if agg >= 83:
            disip += "School of Business<br>"


        agg = str(agg)

        html = "<h1 style='color: white;text-align:center'> Your Aggregate</h1>" \
               "<h1 style='color: green;text-align:center'>" + agg[:agg.find(".") + 3] + "%</h1>" \
                                                                                         "<h1 style='color: white;text-align:center'> You're Selected in:</h1> " \
                                                                                         "<p style='color: white;text-align:center'>" + disip + "</p>"

        context = {
            'htmlcontent': html,
        }
    else:
        pass

    return render(request, 'lumscal.html', context)
    
def ntu(request):
    context = {
    }
    entry_test = 10
    fsc = 45
    matric = 45

    if request.POST.get('action') == 'post':
        if request.POST['ofsc'] == "" \
                or request.POST['tfsc'] == "" or request.POST['oentry'] == "" or request.POST['tentry'] == "":
            html = "<h1 style='color: red;text-align:center'>PLEASE ENTER ALL INFORMATION</h1>"
            return render(request, 'ntucal.html', {'htmlcontent': html})  # If roll number empty Return default page

        omatric = int(request.POST['omatric'])
        tmatric = int(request.POST['tmatric'])
        ofsc = int(request.POST['ofsc'])
        tfsc = int(request.POST['tfsc'])
        oentry = int(request.POST['oentry'])
        tentry = int(request.POST['tentry'])

        agg = (((omatric / tmatric) * matric / 100) + ((ofsc / tfsc) * fsc / 100) + (
                (oentry / tentry) * entry_test / 100)) * 100
        disip = ""

        if agg >= 67:
            disip += "BS - Mining Engineering<br>"
            disip += "BS - Geological Engineering<br>"
            disip += "BS - Product And Industrial Design<br>"
        if agg >= 69:
            disip += "BS - Transport Engineering<br>"
            disip += "BS - Environment Engineering<br>"
        if agg >= 70:
            disip += "BS - Matallurgical And Mterial Engineering<br>"
            disip += "BS - City And Reigonal Planing<br>"
        if agg >= 71:
            disip += "BS - Architecture<br>"
        if agg >= 72:
            disip += "BS - Computer Science<br>"
            disip += "BS - Industrial And Manufacturing Engineering<br>"
        if agg >= 73:
            disip += "BS - Building And Architectural Engineering<br>"
            disip += "BS - Petroleum And Gas Engineering<br>"
        if agg >= 74:
            disip += "BS - Chemical Engineering<br>"
            disip += "BS - Mechatronics<br>"
        if agg >= 75:
            disip += "BS - Computer Engineering<br>"
            disip += "BS - Electrical Engineering<br>"
        if agg >= 76:
            disip += "BS - Civil Engineering<br>"
        if agg >= 78:
            disip += "BS - Mechanical Engineerinng<br>"

        agg = str(agg)

        html = "<h1 style='color: white;text-align:center'> Your Aggregate</h1>" \
               "<h1 style='color: green;text-align:center'>" + agg[:agg.find(".") + 3] + "%</h1>" \
                                                                                         "<h1 style='color: white;text-align:center'> You're Selected in:</h1> " \
                                                                                         "<p style='color: white;text-align:center'>" + disip + "</p>"

        context = {
            'htmlcontent': html,
        }
    else:
        pass

    return render(request, 'ntucal.html', context)
    
def bzu(request):
    context = {
    }

    fsc = 100


    if request.POST.get('action') == 'post':
        if request.POST['ofsc'] == "" \
                or request.POST['tfsc'] == "":
            html = "<h1 style='color: red;text-align:center'>PLEASE ENTER ALL INFORMATION</h1>"
            return render(request, 'bzucal.html', {'htmlcontent': html})  # If roll number empty Return default page



        ofsc = int(request.POST['ofsc'])
        tfsc = int(request.POST['tfsc'])



        agg =  ((ofsc / tfsc) * fsc / 100)* 100
        disip = ""

        if agg >= 54:
            disip += "BS - Bio Informatics<br>"
        if agg >= 55:
            disip += "BS - Bio Sciences<br>"
        if agg >= 56:
            disip += "BS - Economics<br>"
        if agg >= 58:
            disip += "BS - Electronics<br>"
        if agg >= 61:
            disip += "BS - Psycology<br>"
        if agg >= 62:
            disip += "BS - Accounting And Finance<br>"
        if agg >= 63:
            disip += "BS - Bussiness Administrarion<br>"
            disip += "BS - Math<br>"
        if agg >= 74:
            disip += "BS - Electrical Engineering<br>"
            disip += "BS - Electrical Electronics Engineering<br>"
        if agg >= 75:
            disip += "BS - Software Engineering<br>"
            disip += "BS - Computer Engineering<br>"
        if agg >= 79:
            disip += "BS - Computer Science<br>"

        agg = str(agg)

        html = "<h1 style='color: white;text-align:center'> Your Aggregate</h1>" \
               "<h1 style='color: green;text-align:center'>" + agg[:agg.find(".") + 3] + "%</h1>" \
                                                                                         "<h1 style='color: white;text-align:center'> You're Selected in:</h1> " \
                                                                                         "<p style='color: white;text-align:center'>" + disip + "</p>"

        context = {
            'htmlcontent': html,
        }
    else:
        pass

    return render(request, 'bzucal.html', context)
    
def air(request):
    context = {
    }
    entry_test = 50
    fsc = 35
    matric = 15

    if request.POST.get('action') == 'post':
        if request.POST['ofsc'] == "" \
                or request.POST['tfsc'] == "" or request.POST['oentry'] == "" or request.POST['tentry'] == "":
            html = "<h1 style='color: red;text-align:center'>PLEASE ENTER ALL INFORMATION</h1>"
            return render(request, 'aircal.html', {'htmlcontent': html})  # If roll number empty Return default page

        omatric = int(request.POST['omatric'])
        tmatric = int(request.POST['tmatric'])
        ofsc = int(request.POST['ofsc'])
        tfsc = int(request.POST['tfsc'])
        oentry = int(request.POST['oentry'])
        tentry = int(request.POST['tentry'])

        agg = (((omatric / tmatric) * matric / 100) + ((ofsc / tfsc) * fsc / 100) + (
                (oentry / tentry) * entry_test / 100)) * 100
        disip = ""

        if agg >= 55:
            disip += "Bachelor of Science in Information Technology (BSIT)<br>"
        if agg >= 65:
            disip += "Bachelor of Science in Cyber Security<br>"
            disip += "Bachelor of Science in Computer Sciences (BSCS)<br>"
        if agg >= 70:
            disip += "Mechanical Engineering<br>"
            disip += "Electrical Engineering<br>"
            disip += "Mechatronics Engineering<br>"
            disip += "Computer Engineering<br>"
        if agg >= 85:
            disip += "Bachelor of Science Aviation Management (BS AviMgt)<br>"

        agg = str(agg)

        html = "<h1 style='color: white;text-align:center'> Your Aggregate</h1>" \
               "<h1 style='color: green;text-align:center'>" + agg[:agg.find(".") + 3] + "%</h1>" \
                                                                                         "<h1 style='color: white;text-align:center'> You're Selected in:</h1> " \
                                                                                         "<p style='color: white;text-align:center'>" + disip + "</p>"

        context = {
            'htmlcontent': html,
        }
    else:
        pass

    return render(request, 'aircal.html', context)

def uetpeshawar(request):
    context = {
    }
    entry_test = 50
    fsc = 35
    matric = 15

    if request.POST.get('action') == 'post':
        if request.POST['ofsc'] == "" \
                or request.POST['tfsc'] == "" or request.POST['oentry'] == "" or request.POST['tentry'] == "":
            html = "<h1 style='color: red;text-align:center'>PLEASE ENTER ALL INFORMATION</h1>"
            return render(request, 'uetpeshawarcal.html', {'htmlcontent': html})  # If roll number empty Return default page

        ofsc = int(request.POST['ofsc'])
        tfsc = int(request.POST['tfsc'])
        oentry = int(request.POST['oentry'])
        tentry = int(request.POST['tentry'])

        agg =  + (((ofsc / tfsc) * fsc / 100) + (
                (oentry / tentry) * entry_test / 100)) * 100
        disip = ""

        if agg >= 67:
            disip += "BS - Mining Engineering<br>"
            disip += "BS - Geological Engineering<br>"
            disip += "BS - Product And Industrial Design<br>"
        if agg >= 69:
            disip += "BS - Transport Engineering<br>"
            disip += "BS - Environment Engineering<br>"
        if agg >= 70:
            disip += "BS - Matallurgical And Mterial Engineering<br>"
            disip += "BS - City And Reigonal Planing<br>"
        if agg >= 71:
            disip += "BS - Architecture<br>"
        if agg >= 72:
            disip += "BS - Computer Science<br>"
            disip += "BS - Industrial And Manufacturing Engineering<br>"
        if agg >= 73:
            disip += "BS - Building And Architectural Engineering<br>"
            disip += "BS - Petroleum And Gas Engineering<br>"
        if agg >= 74:
            disip += "BS - Chemical Engineering<br>"
            disip += "BS - Mechatronics<br>"
        if agg >= 75:
            disip += "BS - Computer Engineering<br>"
            disip += "BS - Electrical Engineering<br>"
        if agg >= 76:
            disip += "BS - Civil Engineering<br>"
        if agg >= 78:
            disip += "BS - Mechanical Engineerinng<br>"

        agg = str(agg)

        html = "<h1 style='color: white;text-align:center'> Your Aggregate</h1>" \
               "<h1 style='color: green;text-align:center'>" + agg[:agg.find(".") + 3] + "%</h1>" \
                                                                                         "<h1 style='color: white;text-align:center'> You're Selected in:</h1> " \
                                                                                         "<p style='color: white;text-align:center'>" + disip + "</p>"

        context = {
            'htmlcontent': html,
        }
    else:
        pass


    return render(request, 'uetpeshawarcal.html', context)

def qau(request):
    context = {
    }
    fsc = 70
    matric = 30

    if request.POST.get('action') == 'post':
        if request.POST['ofsc'] == "" \
                or request.POST['tfsc'] == "":
            html = "<h1 style='color: red;text-align:center'>PLEASE ENTER ALL INFORMATION</h1>"
            return render(request, 'qaucal.html', {'htmlcontent': html})  # If roll number empty Return default page

        omatric = float(request.POST['omatric'])
        tmatric = float(request.POST['tmatric'])
        ofsc = float(request.POST['ofsc'])
        tfsc = float(request.POST['tfsc'])


        agg = (((omatric / tmatric) * matric / 100) + ((ofsc / tfsc) * fsc / 100) * 100)
        disip = ""

        if agg >= 67:
            disip += "BS - Mining Engineering<br>"
            disip += "BS - Geological Engineering<br>"
            disip += "BS - Product And Industrial Design<br>"
        if agg >= 69:
            disip += "BS - Transport Engineering<br>"
            disip += "BS - Environment Engineering<br>"
        if agg >= 70:
            disip += "BS - Matallurgical And Mterial Engineering<br>"
            disip += "BS - City And Reigonal Planing<br>"
        if agg >= 71:
            disip += "BS - Architecture<br>"
        if agg >= 72:
            disip += "BS - Computer Science<br>"
            disip += "BS - Industrial And Manufacturing Engineering<br>"
        if agg >= 73:
            disip += "BS - Building And Architectural Engineering<br>"
            disip += "BS - Petroleum And Gas Engineering<br>"
        if agg >= 74:
            disip += "BS - Chemical Engineering<br>"
            disip += "BS - Mechatronics<br>"
        if agg >= 75:
            disip += "BS - Computer Engineering<br>"
            disip += "BS - Electrical Engineering<br>"
        if agg >= 76:
            disip += "BS - Civil Engineering<br>"
        if agg >= 78:
            disip += "BS - Mechanical Engineerinng<br>"

        agg = str(agg)

        html = "<h1 style='color: white;text-align:center'> Your Aggregate</h1>" \
               "<h1 style='color: green;text-align:center'>" + agg[:agg.find(".") + 3] + "%</h1>" \
                                                                                         "<h1 style='color: white;text-align:center'> You're Selected in:</h1> " \
                                                                                         "<p style='color: white;text-align:center'>" + disip + "</p>"

        context = {
            'htmlcontent': html,
        }
    else:
        pass

    return render(request, 'qaucal.html', context)

def preperation(request):
    context={
    }

    return render(request, 'preperation.html', context)

def matricinter(request):
    context={
    }

    return render(request, 'matricinter.html', context)

def entrytest(request):
    context={
    }

    return render(request, 'entrytest.html', context)

def bookpdf(request):
    context={
    }

    return render(request, 'bookpdf.html', context)

def puresult(request):
    context={
    }

    return render(request, 'puresult.html', context)

def kuresult(request):
    context={
    }

    return render(request, 'kuresult.html', context)

def uosresult(request):
    context={
    }

    return render(request, 'uosresult.html', context)

def uopresult(request):
    context={
    }

    return render(request, 'uopresult.html', context)

def aiouresult(request):
    context={
    }

    return render(request, 'aiouresult.html', context)

def ajkresult(request):
    context={
    }

    return render(request, 'ajkresult.html', context)

def islamiaresult(request):
    context={
    }

    return render(request, 'islamiaresult.html', context)

def bzuresult(request):
    context={
    }

    return render(request, 'bzuresult.html', context)

def fifthclassbook(request):
    context={
    }

    return render(request, '5class.html', context)

def eighthclassbook(request):
    context={
    }

    return render(request, '8class.html', context)

def ninthclassbook(request):
    context={
    }

    return render(request, '9class.html', context)

def tenthclassbook(request):
    context={
    }

    return render(request, '10class.html', context)

def eleventhclassbook(request):
    context={
    }

    return render(request, '11class.html', context)

def twelvethclassbook(request):
    context={
    }

    return render(request, '12class.html', context)

def prizebond(request):
    htmlDropdown="<option>Select Amount First</option>"
    final_result=''
    url = "http://savings.gov.pk/latest/results.php"

    if request.POST.get('action') == 'post':
        if request.POST.get('forum') == 'DropDown':
            prize = request.POST.get('prize')
            if prize == "1":
                htmlDropdown = '<option value="">Select Draw Date</option><option value="all">All</option><option value="283">15 May, 2020 </option><option value="274">17 February, 2020 </option><option value="264">15 November, 2019 </option><option value="259">16 September, 2019 </option><option value="255">16 August, 2019 </option><option value="246">15 May, 2019 </option><option value="236">15 February, 2019 </option><option value="227">15 November, 2018 </option><option value="218">15 August, 2018 </option><option value="209">15 May, 2018 </option><option value="200">15 February, 2018 </option><option value="191">15 November, 2017 </option><option value="179">15 August, 2017 </option><option value="163">15 May, 2017 </option><option value="59">15 February, 2017 </option><option value="1">15 November, 2016 </option><option value="2">15 August, 2016 </option><option value="8">16 May, 2016 </option><option value="9">15 February, 2016 </option><option value="10">16 November, 2015 </option><option value="11">17 August, 2015 </option><option value="12">15 May, 2015 </option><option value="13">16 February, 2015 </option><option value="14">17 November, 2014 </option><option value="15">15 August, 2014 </option><option value="16">15 May, 2014 </option><option value="17">17 February, 2014 </option><option value="18">18 November, 2013 </option><option value="19">15 August, 2013 </option><option value="20">15 May, 2013 </option><option value="21">15 February, 2013 </option>'
            if prize == "2":
                htmlDropdown = '><option value="">Select Draw Date</option><option value="all">All</option><option value="285">15 June, 2020 </option><option value="277">16 March, 2020 </option><option value="269">16 December, 2019 </option><option value="258">16 September, 2019 </option><option value="249">17 June, 2019 </option><option value="240">15 March, 2019 </option><option value="231">17 December, 2018 </option><option value="222">17 September, 2018 </option><option value="213">19 June, 2018 </option><option value="204">15 March, 2018 </option><option value="195">15 December, 2017 </option><option value="186">15 September, 2017 </option><option value="173">15 June, 2017 </option><option value="58">15 March, 2017 </option><option value="30">15 December, 2016 </option><option value="31">15 September, 2016 </option><option value="32">15 June, 2016 </option><option value="33">15 March, 2016 </option><option value="83">15 December, 2015 </option><option value="35">15 September, 2015 </option><option value="98">15 July, 2015 </option><option value="36">15 June, 2015 </option><option value="37">16 March, 2015 </option><option value="38">15 December, 2014 </option><option value="39">15 September, 2014 </option><option value="41">17 June, 2014 </option><option value="40">16 June, 2014 </option><option value="130">17 March, 2014 </option><option value="42">16 December, 2013 </option><option value="43">16 September, 2013 </option><option value="44">17 June, 2013 </option><option value="45">15 March, 2013 </option><option value="46">17 December, 2012 </option><option value="47">17 September, 2012 </option><option value="48">15 June, 2012 </option><option value="49">15 March, 2012 </option>'
            if prize == "3":
                htmlDropdown = '<option value="">Select Draw Date</option><option value="all">All</option><option value="287">15 July, 2020 </option><option value="279">15 April, 2020 </option><option value="271">15 January, 2020 </option><option value="261">15 October, 2019 </option><option value="251">15 July, 2019 </option><option value="242">15 April, 2019 </option><option value="233">15 January, 2019 </option><option value="224">15 October, 2018 </option><option value="215">16 July, 2018 </option><option value="206">16 April, 2018 </option><option value="197">15 January, 2018 </option><option value="188">16 October, 2017 </option><option value="175">17 July, 2017 </option><option value="128">17 April, 2017 </option><option value="51">16 January, 2017 </option><option value="53">17 October, 2016 </option><option value="52">18 July, 2016 </option><option value="77">15 April, 2016 </option><option value="92">15 January, 2016 </option><option value="88">15 October, 2015 </option><option value="96">15 July, 2015 </option><option value="103">15 April, 2015 </option><option value="109">15 January, 2015 </option><option value="115">15 October, 2014 </option><option value="121">15 July, 2014 </option><option value="127">15 April, 2014 </option><option value="135">15 January, 2014 </option><option value="141">21 October, 2013 </option><option value="147">15 July, 2013 </option><option value="153">15 April, 2013 </option><option value="159">15 January, 2013 </option><option value="169">15 October, 2012 </option>'

            if prize == "4":
                htmlDropdown = '<option value="">Select Draw Date</option><option value="all">All</option><option value="282">15 May, 2020 </option><option value="275">17 February, 2020 </option><option value="265">15 November, 2019 </option><option value="254">16 August, 2019 </option><option value="245">15 May, 2019 </option><option value="237">15 February, 2019 </option><option value="228">15 November, 2018 </option><option value="219">15 August, 2018 </option><option value="210">15 May, 2018 </option><option value="201">15 February, 2018 </option><option value="192">15 November, 2017 </option><option value="178">15 August, 2017 </option><option value="164">15 May, 2017 </option><option value="50">15 February, 2017 </option><option value="54">15 November, 2016 </option><option value="57">15 August, 2016 </option><option value="56">16 May, 2016 </option><option value="80">15 February, 2016 </option><option value="85">15 November, 2015 </option><option value="91">17 August, 2015 </option><option value="100">15 May, 2015 </option><option value="106">16 February, 2015 </option><option value="112">17 November, 2014 </option><option value="118">15 August, 2014 </option><option value="124">15 May, 2014 </option><option value="132">17 February, 2014 </option><option value="138">18 November, 2013 </option><option value="144">15 August, 2013 </option><option value="150">15 May, 2013 </option><option value="156">15 February, 2013 </option><option value="166">15 November, 2012 </option><option value="181">15 August, 2012 </option>'

            if prize == "5":
                htmlDropdown = '<option value="">Select Draw Date</option><option value="all">All</option><option value="288">03 August, 2020 </option><option value="281">04 May, 2020 </option><option value="273">03 February, 2020 </option><option value="262">01 November, 2019 </option><option value="253">01 August, 2019 </option><option value="243">02 May, 2019 </option><option value="234">01 February, 2019 </option><option value="225">01 November, 2018 </option><option value="216">01 August, 2018 </option><option value="207">02 May, 2018 </option><option value="199">01 February, 2018 </option><option value="189">01 November, 2017 </option><option value="176">01 August, 2017 </option><option value="162">02 May, 2017 </option><option value="64">01 February, 2017 </option><option value="67">01 November, 2016 </option><option value="70">01 August, 2016 </option><option value="75">02 May, 2016 </option><option value="82">01 February, 2016 </option><option value="87">02 November, 2015 </option><option value="95">03 August, 2015 </option><option value="102">04 May, 2015 </option><option value="108">02 February, 2015 </option><option value="113">05 November, 2014 </option><option value="119">04 August, 2014 </option><option value="126">02 May, 2014 </option><option value="134">03 February, 2014 </option><option value="140">01 November, 2013 </option><option value="145">01 August, 2013 </option><option value="151">02 May, 2013 </option><option value="158">01 February, 2013 </option><option value="168">01 November, 2012 </option><option value="183">01 August, 2012 </option>'

            if prize == "6":
                htmlDropdown = '<option value="">Select Draw Date</option><option value="all">All</option><option value="286">02 July, 2020 </option><option value="278">01 April, 2020 </option><option value="270">02 January, 2020 </option><option value="260">01 October, 2019 </option><option value="250">02 July, 2019 </option><option value="241">01 April, 2019 </option><option value="232">02 January, 2019 </option><option value="223">01 October, 2018 </option><option value="214">03 July, 2018 </option><option value="205">02 April, 2018 </option><option value="196">02 January, 2018 </option><option value="187">02 October, 2017 </option><option value="174">04 July, 2017 </option><option value="60">03 April, 2017 </option><option value="65">03 January, 2017 </option><option value="68">03 October, 2016 </option><option value="72">04 July, 2016 </option><option value="78">01 April, 2016 </option><option value="93">04 January, 2016 </option><option value="89">01 October, 2015 </option><option value="97">02 July, 2015 </option><option value="104">01 April, 2015 </option><option value="110">02 January, 2015 </option><option value="116">01 October, 2014 </option><option value="122">02 July, 2014 </option><option value="129">01 April, 2014 </option><option value="136">02 January, 2014 </option><option value="142">01 October, 2013 </option><option value="148">02 July, 2013 </option><option value="154">01 April, 2013 </option><option value="160">02 January, 2013 </option><option value="170">01 October, 2012 </option>'

            if prize == "7":
                htmlDropdown = '<option value="">Select Draw Date</option><option value="all">All</option><option value="289">03 August, 2020 </option><option value="280">04 May, 2020 </option><option value="272">03 February, 2020 </option><option value="263">01 November, 2019 </option><option value="252">01 August, 2019 </option><option value="244">02 May, 2019 </option><option value="235">01 February, 2019 </option><option value="226">01 November, 2018 </option><option value="217">01 August, 2018 </option><option value="208">02 May, 2018 </option><option value="198">01 February, 2018 </option><option value="190">01 November, 2017 </option><option value="177">01 August, 2017 </option><option value="161">02 May, 2017 </option><option value="63">01 February, 2017 </option><option value="61">01 November, 2016 </option><option value="71">01 August, 2016 </option><option value="76">02 May, 2016 </option><option value="81">01 February, 2016 </option><option value="86">02 November, 2015 </option><option value="94">03 August, 2015 </option><option value="101">04 May, 2015 </option><option value="107">02 February, 2015 </option><option value="114">05 November, 2014 </option><option value="120">04 August, 2014 </option><option value="125">02 May, 2014 </option><option value="133">03 February, 2014 </option><option value="139">01 November, 2013 </option><option value="146">01 August, 2013 </option><option value="152">02 May, 2013 </option><option value="157">01 February, 2013 </option><option value="167">01 November, 2012 </option><option value="182">01 August, 2012 </option>'

            if prize == "8":
                htmlDropdown = '<option value="">Select Draw Date</option><option value="all">All</option><option value="247">03 June, 2019 </option><option value="238">01 March, 2019 </option><option value="229">03 December, 2018 </option><option value="220">03 September, 2018 </option><option value="211">01 June, 2018 </option><option value="202">01 March, 2018 </option><option value="193">04 December, 2017 </option><option value="184">05 September, 2017 </option><option value="171">01 June, 2017 </option><option value="62">01 March, 2017 </option><option value="84">01 December, 2016 </option><option value="66">01 December, 2016 </option><option value="69">01 September, 2016 </option><option value="74">01 June, 2016 </option><option value="79">01 March, 2016 </option><option value="90">01 September, 2015 </option><option value="99">01 June, 2015 </option><option value="105">02 March, 2015 </option><option value="111">01 December, 2014 </option><option value="117">01 September, 2014 </option><option value="123">02 June, 2014 </option><option value="131">03 March, 2014 </option><option value="137">02 December, 2013 </option><option value="143">02 September, 2013 </option><option value="149">03 June, 2013 </option><option value="155">01 March, 2013 </option><option value="165">03 December, 2012 </option><option value="180">01 September, 2012 </option>'

            if prize == "9":
                htmlDropdown = '<option value="">Select Draw Date</option><option value="all">All</option><option value="284">10 June, 2020 </option><option value="276">10 March, 2020 </option><option value="266">10 December, 2019 </option><option value="257">11 September, 2019 </option><option value="248">10 June, 2019 </option><option value="239">11 March, 2019 </option><option value="230">10 December, 2018 </option><option value="221">10 September, 2018 </option><option value="212">11 June, 2018 </option><option value="203">12 March, 2018 </option><option value="194">11 December, 2017 </option><option value="185">11 September, 2017 </option><option value="172">12 June, 2017 </option>'

            data = {'htmlDropdown': htmlDropdown}
            return HttpResponse(json.dumps(data))

        if request.POST.get('forum') == 'Result':
            country = request.POST.get('country')
            state = request.POST.get('state')
            state = state[2:2+3]
            range_from = request.POST.get('range_from')
            range_to = request.POST.get('range_to')
            pb_number_list = request.POST.get('pb_number_list')

            to_post = {
                "country": country,
                "state": state,
                "range_from": range_from,
                "range_to": range_to,
                "pb_number_list": pb_number_list,
                "btnsearch": "Search",
            }


            final_result = (requests.post(url, data = to_post)).text

            final_result = final_result[final_result.find('<div id="focus">'):]
            final_result = final_result[:final_result.find("</div></div></div>")+18]

            print(final_result)

            if len(final_result) < 25:
                final_result = '<h1 style="color: red; text-align:center;">Sorry Try Again</h1>'
            else:
                final_result = '<h1 style="color: green; text-align:center;">You Won!</h1>' + final_result


            data = {'Finalresult': final_result}

            print(data)

            return JsonResponse(data)


    context={
        "htmlDropdown": htmlDropdown,
        "Finalresult": final_result,

    }

    return render(request,'prizebond.html',context)

def coronavirus(request):
    r = requests.get("http://coronavirus.result.pk/")
    content = r.text

    table_start_index = content.find('<table id="corona-table1">')
    table_end_index = content.find("</table>")
    pak_table = content[table_start_index:table_end_index+8]
    pak_table = pak_table.replace('<a','<ass')

    content = content[table_end_index+8:]

    table_start_index = content.find('<table id="corona-table">')
    table_end_index = content.find("</table>")

    global_table = content[table_start_index:table_end_index + 8]
    global_table_first = global_table[:global_table.find('<th colspan="10" style="text-align: left;">')]
    global_table_second = global_table[global_table.find('#FF0">News')+22:]
    global_table = global_table_first + global_table_second
    global_table = global_table.replace('<a', '<ass')

##############
    content = r.text
    global_stats = content[content.find('<h2 style="border: none; font-size: 30px; color: #444;">Total Coronavirus Cases in World</h2>'):]
    global_stats = global_stats[:global_stats.find('<div style="text-align: center; float: left; width: 100%')]

    content = r.text
    pak_stats = content[content.find('<h2 style="border: none; font-size: 25px; color: #444;">'):]
    pak_stats = pak_stats[:pak_stats.find('<div style="text-align: center; float: left; width: 100%; margin-bottom:10px;"')]



    context={
        "global_table": global_table,
        "pak_table": pak_table,
        "global_stats": global_stats,
        "pak_stats": pak_stats,
    }

    return render(request, 'coronavirus.html', context)

def prizebondschedule(request):
    context={
    }

    return render(request, 'schedule.html', context)

def comingsoon(request):
    context={
    }

    return render(request, 'comingsoon.html', context)