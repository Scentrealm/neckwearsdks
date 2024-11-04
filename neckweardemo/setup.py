from setuptools import setup, find_packages
# 生成whl文件 python setup.py sdist bdist_wheel
setup(
    name='NeckWearTest',
    version='1.0.1',
    description='ScentRealm sdk for NeckWear Test',  # 描述信息
    author='Ski',  # 作者
    packages=find_packages(),
    license='MIT',
    python_requires='>=3.7',
    # packages=['myPackage','myPackage.inner'],  # 包名
    # packages=find_packages(), # 会递归查找当前目录下的所有包名
)

