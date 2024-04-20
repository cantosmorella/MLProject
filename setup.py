from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'#Tener en cuenta que no esta activo en requirements.txt
def get_requirements(file_path:str)->List[str]:
    #Esta funcion retorna la lista de requerimientos
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:#Tener en cuenta que no esta activo en requirements.txt
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup (
    name = 'mlproject',
    version = '0.0.1',
    author = 'Morella',
    author_email = 'cantosmorella@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)