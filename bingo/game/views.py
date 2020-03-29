from django.shortcuts import render, redirect
from django.views import View

# Create your views here.

class IndexView(View):

    template_name = 'game/index.html'

    def get(self, request):
        return render(request, self.template_name, {'title': request.user.username})
