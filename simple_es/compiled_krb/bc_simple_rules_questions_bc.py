# bc_simple_rules_questions_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def no_covid_sinfiebre(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_fiebre', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.no_covid_sinfiebre: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_bring_raincoat(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_fiebre', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.what_to_bring_raincoat: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_cansado', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.what_to_bring_raincoat: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def no_covid_sincansancio(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_fiebre', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.no_covid_sincansancio: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_cansado', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.no_covid_sincansancio: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_tos', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions.no_covid_sincansancio: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def no_covid_sindolorcabeza(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_fiebre', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.no_covid_sindolorcabeza: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_tos', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.no_covid_sindolorcabeza: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_cansado', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions.no_covid_sindolorcabeza: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_dolorcabeza', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules_questions.no_covid_sindolorcabeza: got unexpected plan from when clause 4"
                        rule.rule_base.num_bc_rule_successes += 1
                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def no_covid_dolorgarganta(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_fiebre', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.no_covid_dolorgarganta: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_tos', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.no_covid_dolorgarganta: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_cansado', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions.no_covid_dolorgarganta: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_dolorcabeza', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules_questions.no_covid_dolorgarganta: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_dolorgarganta', context,
                                          (rule.pattern(1),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules_questions.no_covid_dolorgarganta: got unexpected plan from when clause 5"
                            rule.rule_base.num_bc_rule_successes += 1
                            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def no_covid_dificresp(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_fiebre', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.no_covid_dificresp: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_tos', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.no_covid_dificresp: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_cansado', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions.no_covid_dificresp: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_dolorcabeza', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules_questions.no_covid_dificresp: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_dolorgarganta', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules_questions.no_covid_dificresp: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_dificultadrespiratoria', context,
                                              (rule.pattern(1),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules_questions.no_covid_dificresp: got unexpected plan from when clause 6"
                                rule.rule_base.num_bc_rule_successes += 1
                                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def no_covid_difresp(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_fiebre', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.no_covid_difresp: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_tos', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.no_covid_difresp: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_cansado', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions.no_covid_difresp: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_dolorcabeza', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules_questions.no_covid_difresp: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_dolorgarganta', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules_questions.no_covid_difresp: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_dificultadrespiratoria', context,
                                              (rule.pattern(0),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules_questions.no_covid_difresp: got unexpected plan from when clause 6"
                                with engine.prove('questions', 'is_perdidasentidos', context,
                                                  (rule.pattern(1),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "bc_simple_rules_questions.no_covid_difresp: got unexpected plan from when clause 7"
                                    rule.rule_base.num_bc_rule_successes += 1
                                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def si_covid(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_fiebre', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions.si_covid: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_tos', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions.si_covid: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_cansado', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions.si_covid: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'is_dolorcabeza', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules_questions.si_covid: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'is_dolorgarganta', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules_questions.si_covid: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'is_dificultadrespiratoria', context,
                                              (rule.pattern(0),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules_questions.si_covid: got unexpected plan from when clause 6"
                                with engine.prove('questions', 'is_perdidasentidos', context,
                                                  (rule.pattern(0),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "bc_simple_rules_questions.si_covid: got unexpected plan from when clause 7"
                                    rule.rule_base.num_bc_rule_successes += 1
                                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('bc_simple_rules_questions')
  
  bc_rule.bc_rule('no_covid_sinfiebre', This_rule_base, 'que_diagnostico_tiene',
                  no_covid_sinfiebre, None,
                  (pattern.pattern_literal('solo_somatiza'),),
                  (),
                  (pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_bring_raincoat', This_rule_base, 'que_diagnostico_tiene',
                  what_to_bring_raincoat, None,
                  (pattern.pattern_literal('nocovid_resfriadocomun'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('no_covid_sincansancio', This_rule_base, 'que_diagnostico_tiene',
                  no_covid_sincansancio, None,
                  (pattern.pattern_literal('nocovid_resfriadocomun'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('no_covid_sindolorcabeza', This_rule_base, 'que_diagnostico_tiene',
                  no_covid_sindolorcabeza, None,
                  (pattern.pattern_literal('nocovid_resfriadocomun'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('no_covid_dolorgarganta', This_rule_base, 'que_diagnostico_tiene',
                  no_covid_dolorgarganta, None,
                  (pattern.pattern_literal('nocovid_resfriadocomun'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('no_covid_dificresp', This_rule_base, 'que_diagnostico_tiene',
                  no_covid_dificresp, None,
                  (pattern.pattern_literal('nocovid_resfriadocomun'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('no_covid_difresp', This_rule_base, 'que_diagnostico_tiene',
                  no_covid_difresp, None,
                  (pattern.pattern_literal('nocovid_resfriadocomun'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('si_covid', This_rule_base, 'que_diagnostico_tiene',
                  si_covid, None,
                  (pattern.pattern_literal('covid'),),
                  (),
                  (pattern.pattern_literal(True),))


Krb_filename = '..\\simple_es\\bc_simple_rules_questions.krb'
Krb_lineno_map = (
    ((14, 18), (5, 5)),
    ((20, 25), (7, 7)),
    ((38, 42), (10, 10)),
    ((44, 49), (12, 12)),
    ((50, 55), (13, 13)),
    ((68, 72), (16, 16)),
    ((74, 79), (18, 18)),
    ((80, 85), (19, 19)),
    ((86, 91), (20, 20)),
    ((104, 108), (23, 23)),
    ((110, 115), (25, 25)),
    ((116, 121), (26, 26)),
    ((122, 127), (27, 27)),
    ((128, 133), (28, 28)),
    ((146, 150), (31, 31)),
    ((152, 157), (33, 33)),
    ((158, 163), (34, 34)),
    ((164, 169), (35, 35)),
    ((170, 175), (36, 36)),
    ((176, 181), (37, 37)),
    ((194, 198), (40, 40)),
    ((200, 205), (42, 42)),
    ((206, 211), (43, 43)),
    ((212, 217), (44, 44)),
    ((218, 223), (45, 45)),
    ((224, 229), (46, 46)),
    ((230, 235), (47, 47)),
    ((248, 252), (50, 50)),
    ((254, 259), (52, 52)),
    ((260, 265), (53, 53)),
    ((266, 271), (54, 54)),
    ((272, 277), (55, 55)),
    ((278, 283), (56, 56)),
    ((284, 289), (57, 57)),
    ((290, 295), (58, 58)),
    ((308, 312), (61, 61)),
    ((314, 319), (63, 63)),
    ((320, 325), (64, 64)),
    ((326, 331), (65, 65)),
    ((332, 337), (66, 66)),
    ((338, 343), (67, 67)),
    ((344, 349), (68, 68)),
    ((350, 355), (69, 69)),
)
