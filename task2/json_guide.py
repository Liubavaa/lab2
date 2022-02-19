"""
Guide in JSON object
"""
import json


USING = """
Main information:
    Working with object:
        -print 'key' and then print necessary key of given ones to see its value.
        Example:
            Method: key
            Key: 'your key'
        
        -if there are many keys in given list, print 'search', then print necessary word 
        and you will get list of keys that contain inputted word in their name
        Example:
            Method: search
            Word: 'your word'
    
    You always can:
        -print 'back' to go back to previous keys
---------------------------------------
"""


def check_value(value) -> str:
    """
    Check if value is object, array or something else and give user some opportunity
    """
    if isinstance(value, list):
        print('Value is an array. '
              'Print "full" to see full array or print the number of the array item to see it')
        decision = input('Method: ')
        if decision == 'back':
            return 'back'
        if decision == 'full':
            print(value)
            check_value(value)
        else:
            try:
                decision = int(decision)
                check_value(value[decision])
            except ValueError:
                print('Bad input')
                check_value(value)
            except IndexError:
                print('Bad input')
                check_value(value)
    elif isinstance(value, dict):
        print('Value is an object. Print "full" to see full object or "keys" to see its keys')
        decision = input('Method: ')
        if decision == 'back':
            return 'back'
        if decision == 'full':
            print(value)
            check_value(value)
        elif decision == 'keys':
            object_guide(value)
        else:
            print('Incorrect input')
            check_value(value)
    else:
        print('-----  Value is:', value, ' -----')
        print('Previous keys:')
        return 'back'
    return 'back'


def object_guide(data: dict) -> str:
    """
    Responsible for user interaction with object
    """
    print('Given keys:')
    print(list(key for key in data.keys()))
    use_method = input('Method: ')
    if use_method == 'key':
        your_key = input('Key: ')
        if your_key in data.keys():
            check_value(data[your_key])
        else:
            print('Bed key')
        object_guide(data)
    elif use_method == 'back':
        return 'back'
    elif use_method == 'search':
        part_word = input('Word: ')
        fit_keys = [key for key in data.keys() if part_word in key]
        print('Result:')
        if len(fit_keys) > 0:
            print(fit_keys)
        else:
            print('No such keys')
        object_guide(data)
    else:
        print('Incorrect method')
        object_guide(data)
    return 'back'


def parse_information():
    """
    Print rules and start process
    """
    with open(input('Path to JSON file: '), 'r', encoding='UTF-8') as json_f:
        data = json.load(json_f)
    print(USING)
    object_guide(data)

if __name__ == '__main__':
    parse_information()
