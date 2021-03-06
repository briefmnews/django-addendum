import sys

try:
    import django
    from django.conf import settings

    settings.configure(
        DEBUG=True,
        USE_TZ=True,
        USE_I18N=True,
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
            }
        },
        ROOT_URLCONF="tests.urls",
        INSTALLED_APPS=[
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sites",
            "addendum",
        ],
        MIDDLEWARE_CLASSES=(),
        SITE_ID=1,
        NOSE_ARGS=['-s'],
        FIXTURE_DIRS=['tests/fixtures'],
        LANGUAGE_CODE='es',
    )
    if hasattr(django, 'setup'):
        django.setup()

    from django_nose import NoseTestSuiteRunner
except ImportError:
    raise ImportError("To fix this error, run: pip install -r requirements-test.txt")


def run_tests(*test_args):
    if not test_args:
        test_args = ['tests']

    # Run tests
    test_runner = NoseTestSuiteRunner(verbosity=1)

    failures = test_runner.run_tests(test_args)

    if failures:
        sys.exit(failures)


if __name__ == '__main__':
    run_tests(*sys.argv[1:])
