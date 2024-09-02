mc-demo
=======

A fairly bare bones demo project that illustrates how to set up a basic
Django project that includes some of the MCFC registration application
code.

You should be able to clone this and get it running with something like:

    git clone https://github.com/drykath/mc-demo.git
    virtualenv myvirtualenv
    . myvirtualenv/bin/activate
    pip install -r mc-demo/requirements.txt
    vim mc-demo/democonvention/settings.py to set a SECURITY_KEY
    mc-demo/manage.py createsuperuser
    mc-demo/manage.py runserver

It certainly won't look pretty, but it should work, and hopefully will
be enough to get you going in the right direction.

If it's easier for editing the mc-* app code, you can also clone those
repositories to an adjacent folder and symlink the apps here:

    ln -s ../mc-convention/convention

To get a registration form working, you'll also need to:

1. Access the admin by hitting (site)/admin in your web browser.
2. Create a Convention object.
3. Create a Registration Level, Shirt Size, and a Payment Method (pending a rewrite of that)

The full steps for recreating this Django installation:

    django-admin startproject democonvention mc-demo
    vim requirements.txt
    vim democonvention/settings.py:
        add 'django.contrib.sites', 'bootstrap3', 'convention', and 'registration' to INSTALLED_APPS
        add 'SITE_ID = 1'
        in TEMPLATES, set DIRS=[BASE_DIR / 'templates'] -- (or wheverever you plan on stashing global templates)
        add the line "SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'"
    mkdir templates
    vim templates/base.html
    vim templates/index.html
