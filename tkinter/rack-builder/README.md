Several years ago, I took on the task to to research and develop a drag-and-drop
data-centre rack configuration web-application with HTML, CSS, and JavaScript (DHTML).

The web-application would read a Sales Order (an XML component list) and draw
a data-centre rack layout based on positional information in the Sales Order. 
The user interface would allow drag-and-drop repositioning – and ‘on save’ – 
it would update the Sales Order.

The updated Sales Order would then be 'read' by VISIO - VBA to create a
VISIO illustration of the rack layout for use by installation engineers in
customer data centres.

**VERSIONS**
* `rack_builder_v1.01_add_wrappers.py` - adds three 'wrapper' Frame widgets
* `rack_builder_v1.02_read_xml.py` - reads the Sales Order and puts the data-values
into Python dictionaries

**DEFINITIONS**
In the context of this project, think of a:
* **Rack** as a 'frame' that has 42 spaces (called Units)
 
