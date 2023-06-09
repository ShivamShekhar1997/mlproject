from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:

    '''
    This function will get the list of requirements
    '''

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)  # To read just the library names excluding -e .

    return requirements        

setup(

    name='mlproject',
    version='0.0.1',
    author='Shivam',
    author_email='iamshivamshekhar@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('Requirements.txt')

)