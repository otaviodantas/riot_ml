from setuptools import setup

setup(
    name='web_app',
    version='1.0',
    python_requires='~=3.8',
    install_requires=[
        'pika ==1.2.0',
        'python-dotenv ==0.15.0',
        'Flask ==1.1.2',
    ]
)