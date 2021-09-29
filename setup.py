import setuptools

setuptools.setup(
    name="reg-degeneration",
    python_requires=">=3.6",
    entry_points = {
        'console_scripts': ['reg-degeneration=reg_degeneration:main'],
    },
    install_requires=[
        "ipyxact==0.2.4",
        "pyuvm@git+https://github.com/pyuvm/pyuvm#219fcf05262660f09209aba4464d831d42af628a",
    ]
)
