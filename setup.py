from setuptools import find_packages, setup

setup(
    name="dagster_and_dbt",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "boto3",
        "pandas",
        "matplotlib",
        "textblob",
        "tweepy",
        "wordcloud",
    ],
    extras_require={
        "dev": [
            "dagster-webserver",
            "dagster-dg-cli",
            "pytest",
        ]
    },
)