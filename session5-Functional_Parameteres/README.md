
> Workflow is setup in EPAI folder. Go back to see the actions
# Functional Parameters
This session was all about Functional Paramenters. Type of parameters, way of passing them. 
About *args, **quargs.

## Functions 

## 1. time_it 
    Gives the average time taken by the given function. 

    ```
        syntax : 

        time_it(fn, *args, repetitons= 1, **kwargs)
        fn : function that should be be executed
        repetions : No of times function should execute.

    ```
## 2. squared_power_list
    It returns the list of the powers of the given number from start to end.

    ```
        syntax : 

        squared_power_list(num,start,end)
        num : Number for which we will be calculating power for.
        start : start index of the power
        end : End index of the power

    ```
## 3. polygon_area
    It gives the area of the given polygon. It can give the area upto hexagon.

    ```
        syntax : 
        polygon_area( side_length, sides = 3)
        side_length: length of the side. Should always be a positive 
        sides. No of sides
        

    ```
## 4. temp_converter 
    It converts the temperater to fahrenheit to Celsious based on the given type.

    ```
        syntax : 
        temp_converter(base_temp, temp_given_in)
        base_temp : Value of temperature
        temp_given_in : Unit in which the given temperature is present.
       

    ```


## 5. speed_converter
     It converts to speed to the specified unit.

    ```
        syntax : 
        speed_converter(source_value = 100, dist='km', time='hr')
        source_value : value of given speed
        dist : distance unit which it should be converted to
        time : time unit which it should be converted to


    ```

## Tests

1. test_readme_exists : To check whether readme file exists or not.
2. test_readme_contents: To check the read contains text or not.
3. test_readme_proper_description:  to check if readme has relavant descriptions or not.
4. test_readme_file_for_formatting: to test readme file proper formattiong
5. test_indentations: checks the indentation of source file 
6. test_function_name_had_cap_letter:checks if functions have capital letter or not
7. test_all_functions_implemented: checks if all the required function is implemented or not
8. test_math_used_or_not: test whether math function is used or not
9. test_function_time_it_repetitons_negative_error: check if the exception is raised for negative repetations
10. test_function_time_it_repetitons_type_error: check if the exception is raised for repetations other than int or not.
11. test_function_time_it: tests time it function by inputting the implemented function
12. test_function_squared_power_list: tests the correctness of squared power list
13. test_function_squared_power_list_for_float_start_stop: checks if the error is thrown for start ,stop other than float type
14. test_function_squared_power_list_for_start_stop: checks if the error is thrown for if start is greater than stop
15. test_function_polygon_area_for_square: tests for area of square in polygon area function
16. test_function_polygon_area_for_hexagon:tests for area of hexagon in polygon area function
17. test_function_polygon_area_invalid_length: checks for error for given invalid length
18. test_function_polygon_area_larger_sides: checks for error for number of sides greate than 6
19. test_function_polygon_area_negative_sides:checks for error for negative sides
20. test_function_speed_converter_raise_error_distance: checks for error for invalid distance value
21. test_function_speed_converter_raise_error_time: checks for error for invalid time value
22. test_function_speed_converter: checks the implementaion of speed converter
23. test_function_temp_converter_raise_error_temp_given_in: checks for error for invalid temp_given_in parameter
24. test_function_temp_converter_temp_given_in_f: checks the implementation of temp converter for fahreineite
25. test_function_temp_converter_temp_given_in_c: checks the implementation of temp converter for celsious
26. test_function_time_for_repition_one(): checks if the print function time exection for one time is close to 0 or not.
   

