import sys
from contextlib import contextmanager, closing, suppress, redirect_stdout, ExitStack
from urllib.request import urlopen
from unittest import mock

@contextmanager
def file_open(path):
    try:
        f_obj = open(path, 'w')
        yield f_obj
    except OSError:
        print('OSError!')
    finally:
        f_obj.close()

with file_open('contextlib_text.txt') as fobj:
    fobj.write('')

# closing
@contextmanager
def closing_impl(db):
    try:
        yield db.conn()
    finally:
        db.close()

# with closing function
# descriptor will close the web page
# after quiting from the with operator
with closing(urlopen('http://www.google.com')) as webpage:
    for line in webpage:
        pass

# suppress
# will ignore 'FileNotFoundError'
with suppress(FileNotFoundError):
    with open('fauxfile.txt') as fobj:
        for line in fobj:
            print(line)

# redirect_stdout
stdout_fileno = sys.stdout

sample_input = ['Hi', 'Hello from AskPython', 'exit']

for ip in sample_input:
    # Prints to stdout
    stdout_fileno.write(ip + '\n')


# path = 'contextlib_text.txt'
#
# with open(path, 'w') as fobj:
#     sys.stdout = fobj
#
# with open(path, 'w') as fobj:
#     with redirect_stdout(fobj):
#         print('sdads') # Prints messages from the terminal into the file

# ExitStack
def mock_available_location_types():
    mock_types = [
        'runtimeenv',
        'ecosystem',
        'superregion',
        'region',
        'habitat',
    ]
    patchers = [
        mock.patch(
            '_logging.logger',
            return_value=mock_types,
        ),
        mock.patch(
            'asyncio_module.main',
            return_value=mock_types,
        ),
    ]

    with ExitStack() as stack:
        yield tuple(stack.enter_context(patch) for patch in patchers)

# (<MagicMock name='logger' id='140487398502112'>, <AsyncMock name='main' id='140487398230816'>)
print(next(mock_available_location_types()))
