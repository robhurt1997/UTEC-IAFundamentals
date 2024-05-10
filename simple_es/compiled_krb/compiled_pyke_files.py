# compiled_pyke_files.py

from pyke import target_pkg

pyke_version = '1.1.1'
compiler_version = 1
target_pkg_version = 1

try:
    loader = __loader__
except NameError:
    loader = None

def get_target_pkg():
    return target_pkg.target_pkg(__name__, __file__, pyke_version, loader, {
         ('', 'simple_es\\', 'bc_simple_rules.krb'):
           [1715356155.5950062, 'bc_simple_rules_bc.py'],
         ('', 'simple_es\\', 'bc_simple_rules_questions.krb'):
           [1715356155.632549, 'bc_simple_rules_questions_bc.py'],
         ('', 'simple_es\\', 'facts.kfb'):
           [1715356155.6476207, 'facts.fbc'],
         ('', 'simple_es\\', 'questions.kqb'):
           [1715356155.661599, 'questions.qbc'],
        },
        compiler_version)

