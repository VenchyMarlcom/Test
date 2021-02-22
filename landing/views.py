from django.shortcuts import render

##Starting landing view
def landing_view(requests):
    context = {}
    template_name = 'landing_page.html'

    return render(requests,template_name,context)
