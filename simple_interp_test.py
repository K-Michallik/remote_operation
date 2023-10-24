import sendInterpreterFromFile as sendFile
from interpreter.interpreter import InterpreterHelper

host = '10.0.0.25'
commands = 'var_test.txt'

interp = InterpreterHelper(host)
interp.connect()

try:
    sendFile.send_cmd_interpreter_mode_file(interp, commands)
except Exception as e:
    # Look for "invalid state" in the interpreter error message. Raise exception otherwise.
    if 'invalid state' in e.args[1]:
        print('Robot program state invalid. Exiting...')
    else:
        raise
