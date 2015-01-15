from .models import StandardPage, ContactPage

def global_vars(request):
    return {
        'about_us_page': StandardPage.objects.filter('slug'=='contactenos').get(),
        'contacts_page': ContactPage.objects.filter('slug'=='nosotros').get(),
    }