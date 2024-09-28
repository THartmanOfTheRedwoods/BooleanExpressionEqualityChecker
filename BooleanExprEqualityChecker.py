#!/usr/bin/env python

import itertools
import re
from curses.ascii import isalpha


def split_on_multiple_delimiters(main_str, delimiters):
    pattern = '|'.join(map(re.escape, delimiters))
    return re.split(pattern, main_str)

def is_not_logic_operator(token):
    return token not in ['and', 'or', 'not', '^', ''] and isalpha(token)

def remove_logic_operators(expression):
    return set(filter(is_not_logic_operator, split_on_multiple_delimiters(expression, [' ', '(', ')'])))

def get_variables(expression):
    # Extract variable names (assume lowercase letters a-z are variables)
    return sorted( remove_logic_operators(expression) )


def evaluate_expression(expression, values):
    # Evaluate a boolean expression using eval() and given variable values
    return eval( expression, {}, values )


def generate_truth_table(variables):
    # Generate all combinations of True/False for the given variables
    return list( itertools.product( [True, False], repeat=len( variables ) ) )


def print_truth_table(expression1, expression2, variables, truth_table):
    # Print the markdown formatted truth table
    header = "| " + "     | ".join( variables ) + f"     | {expression1} | {expression2} | Equivalent |"
    separator = "| " + " | ".join( ["-----"] * len( variables ) ) + f" | {'':-^{len(expression1)}} | {'':-^{len(expression2)}} | {'':-^10} |"
    print( header )
    print( separator )

    for row in truth_table:
        values = dict( zip( variables, row ) )
        result1 = evaluate_expression( expression1, values )
        result2 = evaluate_expression( expression2, values )
        equivalent = result1 == result2
        row_values = " | ".join( str( val ) if not val else str(val)+' ' for val in row )
        print( f"| {row_values} | {str(result1):>{len(expression1)}} | {str(result2):>{len(expression2)}} | {str(equivalent):>10} |" )


def are_equivalent(expression1, expression2):
    # Extract variables
    variables = sorted( set( get_variables( expression1 ) + get_variables( expression2 ) ) )

    # Generate the truth table
    truth_table = generate_truth_table( variables )

    # Print the truth table
    print_truth_table( expression1, expression2, variables, truth_table )

    # Check equivalence for all rows
    all_equivalent = all(
        evaluate_expression( expression1, dict( zip( variables, row ) ) ) ==
        evaluate_expression( expression2, dict( zip( variables, row ) ) )
        for row in truth_table
    )

    # Return whether expressions are equivalent
    return all_equivalent


# Example usage
#expression1 = "(a and b) or (not c)"
#expression2 = "b or not a or c"
expression1 = "(a and b) or (not a)"
expression2 = "b or not a"

if are_equivalent( expression1, expression2 ):
    print( f"\nThe expressions `{expression1}` and `{expression2}` are equivalent." )
else:
    print( f"\nThe expressions `{expression1}` and `{expression2}` are not equivalent." )