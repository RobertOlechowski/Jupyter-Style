import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='jupyter_style',
    version='1.1.2',
    description="""This is style generator, you can simply generate inline css to insert into your Jupyter notebook to change look of tables in your preview. """,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/RobertOlechowski/Jupyter-Style',
    author='Robert Olechowski',
    author_email='RobertOlechowski@gmail.com',
    license='MIT',
    packages=['jupyterStyle'],
    zip_safe=False,
    scripts=[],
    install_requires=[],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    )
