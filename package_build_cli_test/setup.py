from setuptools import setup, find_packages
  
with open('requirements.txt') as f:
    requirements = f.readlines()
  
long_description = 'Sample Package made for a demo \
      of its making for the funproject.'
  
setup(
        name ='funproject',
        version ='1.0.0',
        author ='Morteza',
        author_email ='mortezash404@gmail.com',
        url ='https://github.com/morteza404/package_build_cli_test',
        description ='Demo Package for funproject.',
        long_description = long_description,
        long_description_content_type ="text/markdown",
        license ='MIT',
        packages = find_packages(),
        entry_points ={
            'console_scripts': [
                'funproject = scripts.funproject:main'
            ]
        },
        classifiers =(
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ),
        keywords ='Morteza funproject python package funproject',
        install_requires = requirements,
        zip_safe = False
)