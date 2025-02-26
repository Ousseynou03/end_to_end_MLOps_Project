from setuptools import find_packages,setup
from typing import List

def get_requirements() -> List[str]:
    """
    Cette fonction retourne la liste des requirements
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            # Lecture des lignes depuis le fichier requirements
            lines=file.readlines()
            # Parcours chaque ligne
            for line in lines:
                requirement=line.strip()
                ## ignore les lignes vide et -e .
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not find")
    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Ousseynou Dione",
    author_email="dioneousseynou03@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()

)