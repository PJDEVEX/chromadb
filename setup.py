from setuptools import find_packages, setup

setup(
    name='chromadb',
    version='0.0.1',
    author='piyankara Jayadewa (PJ)',
    author_email='piyankara.jayadewa@gmail.com',
    install_requires=["openai","langchain","python-dotenv","tiktoken", "chromadb"],
    packages=find_packages(),
)