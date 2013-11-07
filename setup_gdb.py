""" Setup script -- debugging mode (no OpenMP, no optimizations, etc.). """

from distutils.core import setup
from Cython.Distutils import build_ext, Extension
from numpy import get_include

_incl = [get_include()]
_args = ['-Wall', '-O0']

setup(
    name="truthy_measure",
    description='Graph-theoretic measures of truthiness',
    version='0.0.1pre',
    author='Giovanni Luca Ciampaglia',
    author_email='gciampag@indiana.edu',
    packages=['truthy_measure'],
    cmdclass={'build_ext': build_ext},
    ext_modules=[
        Extension("truthy_measure.heap", ["truthy_measure/heap.pyx", ],
                  extra_compile_args=_args,
                  include_dirs=_incl,
                  pyrex_gdb=True),
        Extension("truthy_measure._maxmin", ["truthy_measure/_maxmin.pyx", ],
                  extra_compile_args=_args,
                  include_dirs=_incl,
                  pyrex_gdb=True),
        Extension("truthy_measure._closure", ["truthy_measure/_closure.pyx", ],
                  extra_compile_args=_args,
                  include_dirs=_incl,
                  pyrex_gdb=True),
        Extension("truthy_measure.cmaxmin_node",
                  ["truthy_measure/cmaxmin_node.pyx", ],
                  extra_compile_args=_args,
                  include_dirs=_incl,
                  pyrex_gdb=True)
    ],
    scripts=[
        'scripts/closure.py',
        'scripts/cycles.py',
        'scripts/ontoparse.py',
        'scripts/test_dag.py',
        'scripts/prep.py',
    ]
)
