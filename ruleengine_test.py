# test_ast_engine.py
from ast_engine import create_rule, combine_rules, evaluate_rule

def test_create_rule():
    rule = "age > 30 AND department = 'Sales'"
    ast = create_rule(rule)
    assert ast is not None

def test_evaluate_rule():
    ast = create_rule("age > 30")
    data = {"age": 35}
    assert evaluate_rule(ast, data) == True

# Additional tests for combining rules and error handling
