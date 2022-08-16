from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .forms import LetterForm
from .models import Letter


# Create your views here.
class HomeView(generic.FormView):

    form_class = LetterForm
    template_name = 'homepage.html'
    success_url = reverse_lazy('letter:my_letters')

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        if form.is_bound:
            user = self.request.user
            title = form.cleaned_data['title']
            msg = form.cleaned_data['message']
            date = form.cleaned_data['date']
            email = form.cleaned_data['email_address']
            aud = form.cleaned_data['audience']
            Letter.objects.create(
                user=user,
                title=title,
                message=msg,
                date=date,
                email_address=email,
                audience=aud
            )
        return super().form_valid(form)


class IndexView(generic.ListView):

    template_name = 'public_letters.html'
    queryset = Letter.objects.filter(audience='public, but as anon', delivered=True)


class LettersListView(LoginRequiredMixin, generic.ListView):

    template_name = 'my_letters.html'

    def get_queryset(self):
        queryset = Letter.objects.filter(user=self.request.user, delivered=False)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['delivered_letters'] = Letter.objects.filter(delivered=True)
        return context


class LetterDetailView(generic.DetailView, generic.DeleteView):

    model = Letter
    template_name = 'letter_detail.html'
    success_url = reverse_lazy('letter:my_letters')

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class LetterCreateView(LoginRequiredMixin, generic.CreateView):

    form_class = LetterForm
    template_name = 'create_letter.html'
    success_url = reverse_lazy('letter:my_letters')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
