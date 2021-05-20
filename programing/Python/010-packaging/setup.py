from setuptools import setup, find_packages

setup(
    name="yym",
    version="0.0.1",
    author="yym",
    packages=find_packages(),
    entry_points = {
        'console_scripts': [
            'echo=yym.utils:main',  # 没搞懂，一直从 __main__ 进去 
        ]
    }
)
