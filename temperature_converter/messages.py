from temperature_converter.constants import MODES

no_mode_message = 'Please select one of the conversion types:\n' \
                  f'{MODES.C2F} - celsius to fahrenheit\n' \
                  f'{MODES.F2C} - fahrenheit to celsius'

invalid_number_error_message = 'Please enter valid numbers as conversion arguments'

common_part_help = 'Pass one or several numbers to proceed'
c2f_help = f'Celsius to Fahrenheit calculation\n{common_part_help}'
f2c_help = f'Fahrenheit to Celsius calculation\n{common_part_help}'
