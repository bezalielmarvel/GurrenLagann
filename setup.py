#!./venv/bin python3.5
# -*- coding: utf-8 -*-
 
from setuptools import setup, find_packages
from gurrenlagann_lib import *
 
setup(
 
    name='gl_lib',
 
    packages=find_packages(),
 
    author="Gurren Lagann Team",
 
    #author_email="lesametlemax@gmail.com",
 
    # Une description courte
    description="bibliothèque permettant la mise en mouvement d'un robot",


 
    # Vous pouvez rajouter une liste de dépendances pour votre lib
    # et même préciser une version. A l'installation, Python essayera de
    # les télécharger et les installer.
    #
    # Ex: ["gunicorn", "docutils >= 0.3", "lxml==0.5a7"]
    #
    # Dans notre cas on en a pas besoin, donc je le commente, mais je le
    # laisse pour que vous sachiez que ça existe car c'est très utile.
    # install_requires= ,
 
    # Une url qui pointe vers la page officielle
    url='https://github.com/bezalielmarvel/GurrenLagann',
 
    # La liste des marqueurs autorisées est longue:
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers.
    classifiers=[
        "Programming Language :: Python",
        "Natural Language :: French",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.5",
        "Topic :: Communications",
    ],
  
    # A fournir uniquement si votre licence n'est pas listée dans "classifiers"
    # ce qui est notre cas
    license="WTFPL",
 
)
