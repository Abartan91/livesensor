from setuptools import find_packages,setup


###def get_requirements()->list[str]:
   ### requirements_list=list[str] = []
    ###return get_requirements


def get_requirements() -> list[str]:
    with open("requirements.txt") as f:
        requirements = f.readlines()
        requirements = [r.strip() for r in requirements if r.strip() and not r.startswith("#")]
    return requirements

    

setup(
    name='sensor',
    version='0.0.1',
    author='price',
    packages=find_packages(),
    install_requires= get_requirements()
    
)