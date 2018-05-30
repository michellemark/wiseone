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


class AboutWiseOneView(TemplateView):
    template_name = 'about-us.html'

    def get_context_data(self, **kwargs):
        context = super(AboutWiseOneView, self).get_context_data()
        context['page_title'] = "About Wise One Realty"

        return context


class BuyersInfoView(TemplateView):
    template_name = 'buyers-info.html'

    def get_context_data(self, **kwargs):
        context = super(BuyersInfoView, self).get_context_data()
        context['page_title'] = "Buy a Home in CNY with Wise One Realty"

        return context


class SellersInfoView(TemplateView):
    template_name = 'sellers-info.html'

    def get_context_data(self, **kwargs):
        context = super(SellersInfoView, self).get_context_data()
        context['page_title'] = "Sell my CNY Home with Wise One Realty"

        return context


class HomeEvaluationView(TemplateView):
    template_name = 'home-evaluation.html'

    def get_context_data(self, **kwargs):
        context = super(HomeEvaluationView, self).get_context_data()
        context['page_title'] = "Free Home Evaluation from Wise One Realty"

        return context
