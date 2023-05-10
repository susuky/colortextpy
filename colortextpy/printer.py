# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/03_printer.ipynb.

# %% auto 0
__all__ = ['available']

# %% ../nbs/03_printer.ipynb 4
import sys

from .ansicolor import Fore, Back, Style


def _create_printer(color):
    name = f'{color}_print'
    args = r"*value, bold=False, sep=' ', end='\n', file=sys.stdout, flush=False"
    document = f'''
        Prints the values to a stream, or to sys.stdout by default with `Fore.{color}` color.

        Parameters
        ----------
        bold: bool
            whether to use bold font

        file: 
            a file-like object (stream); defaults to the current sys.stdout.

        sep: str  
            string inserted between values, default a space.

        end: str  
            string appended after the last value, default a newline.

        flush: bool 
            whether to forcibly flush the stream.

    '''        
    func_body = (
    "    prefix = Style['bold'] if bold else ''\n"
    f"    color = Fore['{color}']\n"
    "    text = sep.join(f'{f}' for f in value)\n"
    "    reset = Fore.reset_all\n"
    "    print(f'{prefix}{color}{text}{reset}', sep=sep, end=end, file=file, flush=flush)"
    )
    exec('def {0}({1}):\n    """{2}"""\n{3}'.format(name, args, document, func_body), globals())

    
available = []

for color in Fore.available:
    available.append(f'{color}_print')
    _create_printer(color)
    
available = tuple(available)