# about/views.py
# Импортировать TemplateView

# Описать класс AboutAuthorView для страницы about/author

# Описать класс AboutTechView для страницы about/tech


# views.py
# Импорт класса TemplateView, чтобы унаследоваться от него
from django.views.generic.base import TemplateView


class AboutAuthorView(TemplateView):
    template_name = 'about/author.html'


class AboutTechView(TemplateView):
    template_name = 'about/tech.html'
