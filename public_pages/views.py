from django.views.generic import TemplateView

from public_pages.models import HomeFeaturedArticlePlaceholder


class ComingSoonView(TemplateView):
    template_name = 'coming-soon.html'

    def get_context_data(self, **kwargs):
        context = super(ComingSoonView, self).get_context_data()
        context['page_title'] = "Wise One Realty Home"

        return context


class HomeView(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data()
        context['page_title'] = "Wise One Realty Home"
        context['object'] = HomeFeaturedArticlePlaceholder.objects.get_or_create(pk=1)[0]

        return context
