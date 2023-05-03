from setuptools import setup,  find_packages
from typing import List


HYPEN_E_DOT='-e .'
def get_requirements(file_path:str) -> List[str]:
    '''
    this function will return the list of requirements
    '''
    requirement=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)




setup(
    name = 'e2e_mlproject',
    version='0.0.1',
    author='Deepak Thakur',
    author_email='deepak2009thakur@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)