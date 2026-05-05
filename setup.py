from setuptools import find_packages,setup
from typing import List
EDOT = "-e."

def get_requirements(file_path: str) -> List[str]:
    '''
        This function will return list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n"," ") for req in requirements]
        if EDOT in requirements:
            requirements.remove(EDOT)
    return requirements

setup(
name= 'mlproject',
version= '0.0.1',
author= 'Derin',
author_email = "blestoderin2005@gmail.com",
packages = find_packages(),
install_requires= get_requirements('requirements.txt')
)