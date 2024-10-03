from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_Requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    Requirements=[]
    with open(file_path) as file_obj:
        Requirements=file_obj.readlines()
        Requirements=[req.replace("\n","") for req in Requirements]

        if HYPEN_E_DOT in Requirements:
            Requirements.remove(HYPEN_E_DOT)
    
    return Requirements

setup(
name='AirOptima',
version='0.0.1',
author='Aniska',
author_email='nayakaniska918@gmail.com',
packages=find_packages(),
install_requires=get_Requirements('Requirements.txt')

)