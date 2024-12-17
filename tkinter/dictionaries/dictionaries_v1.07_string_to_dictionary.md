Continuing the exploration of using Tkinter with Python, this version
continues the exploration of using Python *Dictionaries* for storing and
processing data.

This version demonstrates how the dictionary-like string `dictionary_string`
(below) can be used to populate a dictionary.

```Python
dictionary_string = "{ 'SW-0001': {'stencil': 'Visio-Switches.vss', 'model': 'SW-1-1-1-A'} }"
```

||
|-|
|![dictionaries_v1.07_string_to_dictionary.py](illustrations/dictionaries_v1.07_string_to_dictionary.png)|

When the `Show Me` > `String to Dictionary` option is selected, content of
`dictionary_string` is comverted and used to populate `dictionary` with the
steps of the process being printed to the console.

```Console
dictionary_string={ 'SW-0001': {'stencil': 'Visio-Switches.vss', 'model': 'SW-1-1-1-A'} }
the 'type' of 'dictionary_string'='str'

the dictionary={'SW-0001': {'stencil': 'Visio-Switches.vss', 'model': 'SW-1-1-1-A'}}
the 'type' of 'dictionary'='dict'
```
