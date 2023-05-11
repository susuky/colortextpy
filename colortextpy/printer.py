# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/03_printer.ipynb.

# %% auto 0
__all__ = ['Printer', 'colorprint']

# %% ../nbs/03_printer.ipynb 4
import sys

from . import colorizer, Fore


def colorprint(*value, color='black', bold=False, sep=' ', end='\n', file=sys.stdout, flush=False):
    '''
    Prints the values to a stream, or to sys.stdout by default with `Fore.color` color.

    Parameters
    ----------
    color : str, Fore,
        For example: 'red', Fore.red
    
    bold : bool
        Whether to use bold font

    file : 
        A file-like object (stream); defaults to the current sys.stdout.

    sep : str  
        String inserted between values, default a space.

    end : str  
        String appended after the last value, default a newline.

    flush : bool 
        Whether to forcibly flush the stream.
    '''
    
    text = sep.join(f'{f}' for f in value)
    print(colorizer(text, fore=color, styles='bold' if bold else ''), sep=sep, end=end, file=file, flush=flush)
    
    

class _Printer:
    def __init__(self):
        available = []
        for color in Fore.available:
            available.append(f'{color}_print')
            self._create_printer(color)

        self.available = tuple(available)

            
    def _create_printer(self, color):
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
        "    text = sep.join(f'{f}' for f in value)\n"
        f"    print(colorizer(text, fore='{color}', styles='bold' if bold else ''), sep=sep, end=end, file=file, flush=flush)"
        )
        exec('def {0}({1}):\n    """{2}"""\n{3}'.format(name, args, document, func_body))
        setattr(self, name, locals()[name])
        
    def __repr__(self):
        return 'Printer'
    
Printer = _Printer()
