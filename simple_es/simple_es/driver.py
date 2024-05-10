import contextlib
import sys

from pyke import knowledge_engine
from pyke import krb_traceback

engine = knowledge_engine.engine(__file__)


def bc_test_covid():
    engine.reset()  # Allows us to run tests multiple times.

    engine.activate('bc_simple_rules_questions')  # STUDENTS: you will need to edit the name of your rule file here

    print("Realizando prueba covid")

    try:
        with engine.prove_goal(
                'bc_simple_rules_questions.que_diagnostico_tiene($bring)') as gen:  # STUDENTS: you will need to edit this line
            for vars, plan in gen:
                print("Tu primer diagnostico %s" % (vars['bring']))  # STUDENTS: you will need to edit this line

    except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)

    print()
    print("done")
