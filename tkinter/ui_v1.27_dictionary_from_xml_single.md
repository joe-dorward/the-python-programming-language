Continuing the exploration of using Tkinter with Python, this version
is a digression into reading this XML data from a file.

```xml
<?xml version='1.0'?>
<racks>
  <rack>
    <identifier>Rack 1</identifier>
  </rack>
  <rack>
    <identifier>Rack 2</identifier>
  </rack>
  <rack>
    <identifier>Rack 3</identifier>
  </rack>
</racks>
```
This version reads the list of rack-identifiers, and adds them to the one-dimensional
Python dictionary `rack_dictionary`.

|||
|-|-|
|![ui_v1.27_dictionary_from_xml_single.py](illustrations/ui_v1.27_dictionary_from_xml_single.png)|
