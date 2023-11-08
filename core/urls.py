from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),
    path('api/auth/', include('djoser.social.urls')),
    
    path('api/products/', include('apps.product.urls')),
    path('api/categorys/', include('apps.category.urls')),
    path('api/profile/', include('apps.user_profile.urls')),
    path('api/offers/', include('apps.offers.urls')),
    path('api/history/', include('apps.user_history.urls')),
    path('api/orders/', include('apps.orders.urls')),
    
    path('docs/', include_docs_urls(title='Docs API')),
    path('admin/', admin.site.urls),

    # path('api/comment/', include('apps.comments.urls')),
    # path('api/lists/', include('apps.lists.urls')),
    # path('api/recomendations/', include('apps.recommendation_system.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if not settings.DEBUG:
    urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]