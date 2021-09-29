import setuptools

setuptools.setup(
    name="reg-degeneration",
    python_requires=">=3.6",
    entry_points = {
        'console_scripts': ['reg-degeneration=reg_degeneration:main'],
    }
)
