from distutils.core import setup

def readme():
    with open('README.md') as file:
        README = file.read()
    return README

setup(
  name = 'TOPSIS-Utkarsh-101803613',        
  packages = ['TOPSIS-Utkarsh-101803613'],   
  version = '0.1',      
  license='MIT',        
  description = 'Topsis Assignment',   
  author = 'Utkarsh Sinha',                  
  author_email = 'usinha_be18@thapar.edu',      
  url = 'https://github.com/utkarsh-1106',   
  download_url = 'https://github.com/utkarsh-1106',  #will update soon.  
  keywords = ['TOPSIS', 'PYTHON', 'ASSIGNMENT'],  
  install_requires=[            
          'numpy',
          'scrapeasy',
          'pandas',
          
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)