One of the cool features of the Tkinter package, is that every 'thing' we
see is either (a) the main user interface, (b) a child-widget of it, or (c)
a child-widget of a child-widget - and the cool fact about that is that
the configuration values of the main user interface, and all widgets /
child-widgets can be interrogated by iteration.

Continuing the exploration of using Tkinter with Python, this version adds
the interrogation by iteration of widget configuration values.

||||
|-|-|-|
|![24_get_widget_config_values.py](illustrations/24_get_widget_config_values.png)|![24_get_widget_config_values.py](illustrations/ui_v1.24_get_widget_config_values_report_menu.png)|![24_get_widget_config_values.py](illustrations/ui_v1.24_get_widget_config_values_command_prompt)|
|The application runs showing the *Purchase Order* 'Entry' widget|The *Purchase Order* 'Entry' widget gets focus|The *OK* 'Button' widget gets focus|

```Python
