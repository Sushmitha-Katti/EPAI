import pytest
import random
import string
import session5
import os
import inspect
import re
import math
import time

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

def test_math_used_or_not():
    code_lines = inspect.getsource(session5)
    assert 'math' in code_lines, 'Math function is not used '
    assert 'import' in code_lines, 'You have not imported anything!'

# --------------------------------------------------------------------------------------

def test_function_time_it_repetitons_negative_error():
    with pytest.raises(ValueError):
        session5.time_it(print, 1, 2, 3, sep='-', end= ' ***\n', repetitons=-2)

def test_function_time_it_repetitons_type_error():
    with pytest.raises(ValueError):
        session5.time_it(print, 1, 2, 3, sep='-', end= ' ***\n', repetitons=2.907)

def test_function_time_it():
    assert session5.time_it(print, 1, 2, 3, sep='-', end= ' ***\n', repetitons=5), "No cheating!!!"
    assert session5.time_it(session5.squared_power_list, 2, start=0, end=5, repetitons=5), "Beware, time_it is wrong"
    assert session5.time_it(session5.polygon_area, 15, sides = 3, repetitons=10), "Beware, time_it is wrong"
    assert session5.time_it(session5.temp_converter, 100, temp_given_in = 'f', repetitons=100), "Beware, time_it is wrong"
    assert session5.time_it(session5.speed_converter, 100, dist='km', time='m', repetitons=200), "Beware, time_it is wrong"




def test_function_squared_power_list():
    num = random.randint(1,10)
    start = random.randint(0,5)
    stop = random.randint(5,10)
    print(type(start),type(stop))
    result = session5.squared_power_list(num,start,stop)
    test_result = []
    for i in range(start,stop+1):
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
    assert math.isclose(result, test_result, rel_tol = 1e-5, abs_tol= 1e-5), "Area for Square is wrong"

def test_function_polygon_area_for_hexagon():
    side_length = random.randint(1,100)
    result = session5.polygon_area( side_length, sides = 6)
    test_result = 3 * math.sqrt(3) *  (side_length * side_length) / 2
    assert math.isclose(result, test_result, rel_tol = 1e-5, abs_tol= 1e-5), " Area of a hexagon is wrong!!"

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

def test_function_speed_converter_raise_error_time():
    with pytest.raises(ValueError):
        session5.speed_converter(100, dist = "m", time = "z")

def test_function_speed_converter():

    tests = {'m_s':27.777778, 'm_day': 2.4e+6, 'ft_s':91.1344 }
    for test in tests:
        result = session5.speed_converter(100, dist = test.split('_')[0], time = test.split('_')[1])
        assert math.isclose(result, tests[test], rel_tol = 1e-4, abs_tol= 1e-4), " Area of a hexagon is wrong!!"


        

def test_function_temp_converter_raise_error_temp_given_in():
    with pytest.raises(ValueError):
        session5.temp_converter(100, 'z')


def test_function_temp_converter_temp_given_in_f():
    base_temp = random.random()
    result = session5.temp_converter(base_temp, 'f')
    test_result = (base_temp - 32) * 5/9
    assert (result == test_result),"Temp Converter is wrong!!!"

def test_function_temp_converter_temp_given_in_c():
    base_temp = random.random()
    result = session5.temp_converter(base_temp, 'c')
    test_result = (base_temp * 9/5) + 32
    assert (result == test_result), "Temp Converter is wrong!!!"

def test_function_time_for_repition_one():
    result = session5.time_it(print, 1, 2, 3, sep='-', end= ' ***\n', repetitons=1)
    assert math.isclose(result, 0.000, rel_tol = 1e-3, abs_tol= 1e-3), "something is wrong in time it"



    







    
    














