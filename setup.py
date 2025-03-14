from setuptools import find_packages,setup
from typing import List

hypen_e_dot = '-e.'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list o requirments
    '''
    requirements=[]
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace('\n','') for req in requirements ] 

        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)

    return requirements

setup(
    name = 'churn_prediction',
    version = '0.1',
    author = 'Adwait',
    author_email = 'adwaitjoshi99@gmail.com',
    package = find_packages(),
    install_requires = get_requirements('requirements.txt')
)