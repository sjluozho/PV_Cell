from setuptools import setup, find_packages


setup(name='pvcell',
      version='0.1.0',
      description='A python package for predicting pce from smiles_str',
      url='https://github.com/sjluozho/PV_Cell',
      author='PVC Group, University of Washington (2019)',
      license='MIT',
      packages=find_packages(),
      install_requires=['keras==2.2.4',
                        'mordred==1.1.2',
                        'pandas==0.24.2',
                        'keras-applications==1.0.7',
                        'keras-preprocessing==1.0.9',
                        'matplotlib==3.0.3',
                        'notebook==5.7.6',
                        'numpy==1.16.2',
                        'scikit-learn==0.20.3',
                        'scipy==1.2.1',
                        'tensorflow==1.13.1',
                        'tensorflow-estimator==1.13.0'])
