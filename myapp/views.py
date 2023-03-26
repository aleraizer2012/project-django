from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.db.models import Q
from .models import DocNumber
from .forms import DocNumberForm
from datetime import datetime

# Create your views here.
class HomeView(TemplateView):
    template_name = "home.html"

class RequestDocNumber(TemplateView):
    template_name = "requestdocnumber.html"

    def get(self, request, *args, **kwargs):

        doctype = kwargs['doctype']

        doctypelist = ['ci',
                       'edital',
                       'portaria']

        if doctype in doctypelist:
            
            form = DocNumberForm(request.POST or None)

            context = {'form' : form, 'doctype' : doctype}
            return render(request, self.template_name, context)
        else:
            self.template_name = "requestdocnumbererror.html"
            return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        
        docnumbers = DocNumber.objects.all()

        doctype = kwargs['doctype']


        form = DocNumberForm(request.POST or None)

        # check if form data is valid
        if form.is_valid():
            
            d = DocNumber()

            now = datetime.now()

            # save the form data to model
            if (len(docnumbers) == 0) or (len((docnumbers.filter(doctype__exact = doctype) & docnumbers.filter(year__exact = now.year))) == 0):
                
                number = 1
                
                d.doctype = doctype
                d.year = now.year
                d.number = number
                d.subject = request.POST.get('subject')
                d.recipient = request.POST.get('recipient')
                d.departmentrecipient = request.POST.get('departmentrecipient')
                d.save()
            else:
                lastyear = DocNumber.objects.filter(doctype__exact = doctype).order_by('-year').first().year
                presentyear = now.year
                if presentyear == lastyear:
                    lastnumber = DocNumber.objects.filter(Q(doctype = doctype) & Q(year = presentyear)).order_by('-number').first().number
                    number = lastnumber + 1

                    d.doctype = doctype
                    d.year = now.year
                    d.number = number
                    d.subject = request.POST.get('subject')
                    d.recipient = request.POST.get('recipient')
                    d.departmentrecipient = request.POST.get('departmentrecipient')
                    d.save()
                else:
                    if presentyear > lastyear:
                        number = 1
                        d.doctype = doctype
                        d.year = now.year
                        d.number = number
                        d.subject = request.POST.get('subject')
                        d.recipient = request.POST.get('recipient')
                        d.departmentrecipient = request.POST.get('departmentrecipient')
                        d.save()
                    else:
                        raise Http404




                
                

                
            
        form = DocNumberForm()    
        text = 'O número de {} é: {}'.format(doctype, number)    
        subject = '{}'.format(request.POST.get('subject'))
        context = {'form' : form, 'doctype' : doctype, 'text' : text, 'subject' : subject}
        return render(request, self.template_name, context)
        