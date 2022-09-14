import setuptools

setuptools.setup(name='phidias',
                 version='1.1.0',
                 description='phidias',
                 long_description=open('README.md').read().strip(),
                 author='Corrado Santoro',
                 py_modules=['phidias'],
                 install_requires=['requests', 'parse'],
                 license='MIT License',
                 zip_safe=False,
                 keywords='phidias',
                 classifiers=[
                    'Intended Audience :: Developers',
                    'Topic :: Scientific/Engineering :: Artificial Intelligence',
                    'License :: MIT License',
                    'Programming Language :: Python :: 3.9',
                ])