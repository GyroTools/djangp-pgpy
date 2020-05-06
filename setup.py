from setuptools import setup, find_packages

setup(name='django-pgpy',
      version='0.1.5',
      description='OpenPGP encryption for django.',
      author='Felix Eichenberger',
      author_email='felix.eichenberger@gyrotools.com',
      maintainer='Felix Eichenberger',
      maintainer_email='felix.eichenberger@gyrotools.com',
      license="BSD",
      zip_safe=True,
      url="https://github.com/gyrotools/django-pgpy",
      packages=find_packages(),
      install_requires=['setuptools',
                        'pycryptodome==3.9.4',
                        'django_enum_choices==2.1.1'],
      include_package_data=True,
      platforms=['any'],
      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Environment :: Web Environment',
    ],
)
