import setuptools

if __name__ == "__main__":
    setuptools.setup(
        name='sandbox',
        version='0.0.1',
        packages=setuptools.find_packages(),
        entry_points={
            'console_scripts':[
                'sandbox = sandbox.main:main',
            ],
        },
    )
