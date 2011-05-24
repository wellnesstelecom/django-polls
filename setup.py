from setuptools import setup, find_packages

setup(name='django-polls', 
      author = 'Javi Santana', 
      author_email = 'jsantana@wtelecom.es',
      description = 'user satisfaction polls',
      url='',
      version='0.1',
      packages=find_packages(exclude=['example', 'example.*']),
      include_package_data=True
)
