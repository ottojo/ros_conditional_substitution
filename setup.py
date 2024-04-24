from setuptools import find_packages, setup

package_name = "conditional_substitution"

setup(
    name=package_name,
    version="1.0.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
    ],
    package_data={package_name: ["py.typed"]},
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Jonas Otto",
    maintainer_email="jonas@jonasotto.com",
    description="TODO: Package description",
    license="MIT",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [],
    },
)
