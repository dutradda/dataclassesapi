import os
import sys

from setuptools import setup, find_packages


ext_modules = None
if (
    not any(arg in sys.argv for arg in ['clean', 'check'])
    and 'SKIP_CYTHON' not in os.environ
):
    try:
        from Cython.Build import cythonize
    except ImportError:
        pass
    else:
        compiler_directives = {}
        if 'CYTHON_TRACE' in sys.argv:
            compiler_directives['linetrace'] = True
        os.environ['CFLAGS'] = '-O3'
        ext_modules = cythonize(
            [
                'apidaora/*.py',
                'apidaora/asgi/*.py',
                'apidaora/controllers/*.py',
                'apidaora/core/*.py',
                'apidaora/route/*.py',
            ],
            nthreads=int(os.getenv('CYTHON_NTHREADS', 0)),
            language_level=3,
            compiler_directives=compiler_directives,
        )

setup(
    name='apidaora',
    version='0.26.1',
    description='Fast, asynchronous and efficient Python web framework',
    author='Diogo Dutra',
    author_email='diogodutradamata@gmail.com',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries',
    ],
    ext_modules=ext_modules,
    extra_require={
        'doc': [
            'mkdocs',
            'mkdocs-material',
            'markdown-include'
        ],
        'redis': ['aioredis'],
        'test': [
            'asgi-testclient',
            'bumpversion',
            'black',
            'flake8',
            'isort',
            'ipython',
            'mypy',
            'pytest-asyncio',
            'pytest-cov',
            'pytest-mock',
            'pytest>=5.1.1',
            'uvicorn',
            'aioredis'
        ]
    },
    install_requires=['jsondaora', 'dictdaora'],
    license='MIT',
    packages=find_packages(),
    python_requires='>=3.8',
    setup_requires=['Cython<4'],
    url='https://dutradda.github.io/apidaora/',
    zip_safe=False,
)
