import sys
from temperature_converter import celsius_to_fahrenheit, fahrenheit_to_celsius
from temperature_converter.expections.str_to_int_conversion_error import StrToIntConversionError
from temperature_converter.messages import invalid_number_error_message, f2c_help, c2f_help, no_mode_message
from temperature_converter.constants import MODES


possible_modes = [getattr(MODES, mode) for mode in dir(MODES) if not mode.startswith('__')]


def calc_c2f(_numbers):
    return [celsius_to_fahrenheit(number) for number in _numbers]


def calc_f2c(_numbers):
    return [fahrenheit_to_celsius(number) for number in _numbers]


def convert_strs_to_ints(strs):
    try:
        return [int(number) for number in strs]
    except ValueError:
        raise StrToIntConversionError


if __name__ == '__main__':
    print(sys.argv)

    mode = sys.argv[1] if len(sys.argv) > 1 else None
    numbers = sys.argv[2:] if len(sys.argv) > 2 else []
    try:
        numbers = convert_strs_to_ints(sys.argv[2:])
    except StrToIntConversionError:
        print(invalid_number_error_message)
        exit(1)
    results = []

    if mode is None or mode not in possible_modes:
        print(no_mode_message)
        exit(1)

    if mode == MODES.C2F:
        if len(numbers) == 0:
            print(c2f_help)
            exit(1)

        results = calc_c2f(numbers)

    if mode == MODES.F2C:
        if len(numbers) == 0:
            print(f2c_help)
            exit(1)

        results = calc_f2c(numbers)

    print(', '.join([str(result) for result in results]))
