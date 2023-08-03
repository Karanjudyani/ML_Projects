from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e .'
def get_requirement(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    :param file_path:
    :return:
    '''
    requirement=[]
    with open(file_path) as file_obj:
        requirement=file_obj.readlines()
        requirement=[req.replace("\n","") for req in requirement]

        if HYPHEN_E_DOT in requirement:
            requirement.remove(HYPHEN_E_DOT)
    return requirement
setup(
    name='mlproject',
    version='0.0.1',
    author='KaranJ',
    author_email='karanjudyani@gmail.com',
    packages=find_packages(),
    install_requires=get_requirement('requirement.txt')

)