from setuptools import setup, find_packages

setup(
    name="pyllm",
    version="1.0.0",
    description="Python Lightweight Language Model Template",
    author="Your Name",  # Replace with your actual name or username
    author_email="your-email@example.com",  # Optional: Replace with your email
    url="https://github.com/yourusername/pyllm",  # Optional: Replace with your project URL
    packages=find_packages(),
    install_requires=[
        # Add any external dependencies your project needs
        # For example:
        # "numpy",
        # "torch", 
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Change based on your license choice
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Specify minimum Python version required
    entry_points={
        "console_scripts": [
            "pyllm=pyllm.main:main",  # This points to your main function
        ],
    },
    include_package_data=True,  # If you have non-Python files to include (e.g., vocab.txt)
)
