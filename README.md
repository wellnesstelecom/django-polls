
basic poll app
==============

This small app provides an easy way to include an "user satisfaction poll" in your site.

install
.......

    pip install django-polls

then add django-polls to your INSTALLED_APPS:
    
    INSTALLED_APPS = (...
        ...
        polls,
        ...)

add urls to your urlpatterns:

    # urls.py
    urlpatterns = patterns('',
        ...
        (r'^polls/', include('polls.urls')),
        ...)

and finally:
    
    python manage.py syncdb

usage
.....

first create a poll in django admin.
then add in yout template:

{% polls_form poll next_url %}

and

{% polls_results poll %}

being next_url the url where user will be redirected when send poll and poll and Poll object:

    render_to_response('mytmpl.html' {'poll': Poll.objects.get(pk=poll_id)});







