Several years ago, I took on the task to to research and develop a drag-and-drop
data-centre rack configuration web-application with HTML, CSS, and JavaScript (DHTML).

The web-application would read a Sales Order (an XML component list) and draw
a data-centre rack layout based on positional information in the Sales Order. 
The user interface would allow drag-and-drop repositioning – and ‘on save’ – 
it would update the Sales Order.

The updated Sales Order would then be 'read' by VISIO - VBA to create a
VISIO illustration of the rack layout for use by installation engineers in
customer data centres.

**DEFINITIONS**

In the context of this project:
* A **Rack** is a 'frame' withs 42 spaces, each of which is called a Unit

**SCENARIO 01**

One of your customers is a small business with a few racks.
They've just ordered a Switch, a Controller, and two Disk Shelves (see `sales_order_01.xml`). 
Their 3rd, 4th, and 5th rack are empty - you are free to put the components anywhere.

**DATA**
* [`sales_order_00.xml`](sales_order_00.xml) - is the XML data-file used


 
