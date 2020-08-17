import pytest
import random
import string
import session5
import os
import inspect
import re
import math
import cmath
from decimal import Decimal

CHECK_FOR_FUNCT_IMPL = [
    'time_it',
    'squared_power_list',
    'polygon_area',
    'temp_converter',
    'speed_converter'


 ]


README_CONTENT_CHECK_FOR = [
     'time_it',
    'squared_power_list',
    'polygon_area',
    'temp_converter',
    'speed_converter'
]

# Tests related to readme
def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r", encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            print(c)
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10, "Readme is not formatted properly"

# --------------------------------------------------------------------------------------
# Tests related Contents in session 4 file

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session5)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session5, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_all_functions_implemented():
    code_lines = inspect.getsource(session5)
    FUNCS_IMPL = True
    for c in CHECK_FOR_FUNCT_IMPL:
        if c not in code_lines:
            print(c)
            FUNCS_IMPL = False
            pass
    assert FUNCS_IMPL == True, 'You forgot to implement all functions! Try again!'

def test_decimal_used_or_not():
    code_lines = inspect.getsource(session5)
    assert 'math' in code_lines, 'Math function is not used '
    assert 'import' in code_lines, 'You have not imported anything!'

# --------------------------------------------------------------------------------------

# def test_time_it_definition():
#     help(session5.time_it)

def test_function_squared_power_list():
    num = random.randint(1,10)
    start = random.randint(0,5)
    stop = random.randint(5,10)
    result = session5.squared_power_list(num,start,stop)
    test_result = []
    for i in range(start,stop):
        test_result.append(math.pow(num,i))
    assert test_result == result, "Squared list implementaion is wrong..."

def test_function_squared_power_list_for_float_start_stop():
    with pytest.raises(ValueError):
        session5.squared_power_list(20, 10,5.4)

def test_function_squared_power_list_for_start_stop():
    with pytest.raises(ValueError):
        session5.squared_power_list(20, 10,0)


def test_function_polygon_area_for_square():
    side_length = random.randint(1,100)
    result = session5.polygon_area( side_length, sides = 4)
    test_result = side_length * side_length
    assert test_result == result, "Area for Square is wrong"

def test_function_polygon_area_for_hexagon():
    side_length = random.randint(1,100)
    result = session5.polygon_area( 10, sides = 6)
    test_result = 3 * math.sqrt(3) *  (side_length * side_length) / 2
    assert math.isclose(result, test_result, rel_tol = 1e-5), " Area of a hexagon is wrong!!"

def test_function_polygon_area_invalid_length():
    with pytest.raises(ValueError):
        session5.polygon_area(-1,2)

def test_function_polygon_area_larger_sides():
    with pytest.raises(ValueError):
        session5.polygon_area(10,7)

def test_function_polygon_area_negative_sides():
    with pytest.raises(ValueError):
        session5.polygon_area(10,-3)

def test_function_speed_converter_raise_error_distance():
    with pytest.raises(ValueError):
        session5.speed_converter(100, dist = "s", time = "hr")


    
    














