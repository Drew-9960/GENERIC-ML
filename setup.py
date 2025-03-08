from setuptools import setup, find_packages



setup(
    name='mlproject',
    version='0.1.0',
    author='Andrew Melendez',
    author_email='melendeza895@outlook.com',
    packages=find_packages(),   
    install_requires=['numpy', 'pandas', 'scikit-learn', 'matplotlib', 'seaborn'],
    
)