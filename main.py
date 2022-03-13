# 1. Simple Usage

from json_excel_converter import Converter
from json_excel_converter.xlsx import Writer

data = [
    {'a': [1], 'b': 'hello'},
    {'a': [1, 2, 3], 'b': 'world'}
]

conv = Converter()
conv.convert(data, Writer(file='/tmp/test.xlsx'))


"""
# 2. Streaming Usage with Restart

from json_excel_converter import Converter, LinearizationError
from json_excel_converter.csv import Writer

conv = Converter()
writer = Writer(file='/tmp/test.csv')
while True:
    try:
        data = get_streaming_data()     # custom function to get iterator of data
        conv.convert_streaming(data, writer)
        break
    except LinearizationError:
        pass
"""

"""

"""
