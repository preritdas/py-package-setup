def create_setup_file(
    description: str,
    package_name: str,
    author: str,
    email: str,
    required_packages: list,
    keywords: list,
    version: str = "0.0.1",
    read_me_source: str = 'README.md',
    read_me_type:str = 'text/markdown'
):
    setup_file_contents = f"""from setuptools import setup, find_packages

VERSION = "{version}"
DESCRIPTION = (
    "{description}"
)
 
def get_read_me():
    with open("{read_me_source}", "r") as f:
        return f.read()

# Setting up
setup(
    name = "{package_name}",
    version = VERSION,
    author = "{author}",
    author_email = "<{email}>",
    description = DESCRIPTION,
    long_description = get_read_me(),
    long_description_content_type = "text/markdown",
    packages = find_packages(),
    install_requires = {required_packages},
    keywords = {keywords},
    classifiers = [
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows"
    ]
)
    """

    with open('setup.py', 'x') as f:
        f.write(setup_file_contents)

def create_blank_setup_file():
    create_setup_file(
        description = 'DESCRIPTION',
        package_name = 'PACKAGENAME',
        author = 'AUTHORNAME',
        email = 'EMAILADDRESS',
        required_packages = ['mypytoolkit'],
        keywords = ['python']
    )