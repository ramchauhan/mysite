from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from core.views import main, post, month, add_comment, delete_comment, HomePageView, AllQuestionView
from django.contrib import admin
from mysite import settings
admin.autodiscover()




urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/$', main, name="blog_page"),
    url(r"^(\d+)/$", post, name="blog_post"),
    url(r"^add_comment/(\d+)/$", add_comment, name="add_comment"),
    url(r"^delete_comment/(\d+)/$", delete_comment, name="delete_comment"),
    url(r"^delete_comment/(\d+)/(\d+)/$", delete_comment),
    url(r"^month/(\d+)/(\d+)/$", month),
    url(r"^home/$", HomePageView.as_view(), name="homepage"),
    url(r"home/(?P<slug>[\w\.\-_/]*)/$", AllQuestionView.as_view(), name='allquestion'),    
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
