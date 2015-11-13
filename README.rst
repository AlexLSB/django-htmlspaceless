=====
Django-htmlspaceless
=====

Django-htmlspaceless is a simple Django app to compress your html page source 
code. It doesn't parse your page's DOM structure, so works faster.

Quick start
-----------

1. Installation:

.. code-block:: python

    pip install git+git://github.com/AlexLSB/django-htmlspaceless

2. Add "htmlspaceless" to your INSTALLED_APPS setting like this::

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'htmlspaceless',
    )

3. Include the htmlspaceless midlleware in your project middleware classes like this:

.. code-block:: python

    MIDDLEWARE_CLASSES = (
        ...
        'htmlspaceless.middleware.SpacelessMiddleware',
    )
   
4. Add to your settings:

.. code-block:: python

    HTMLSPACELESS_ENABLED = True

5. You're done! Running your project you should see compressed HTML-code of your pages source code.
