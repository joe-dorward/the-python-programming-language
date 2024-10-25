The promise of DITA XML includes the creation of *reusable content* (that is) content that is created as stand-alone components (the *single source*) that are available to be reused by anyone for any purpose, and that (as in this example) includes the text in the user interface being 'read in' from a DITA XML file during a build.

```dita
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE topic PUBLIC "-//OASIS//DTD DITA Topic//EN" "topic.dtd">
<topic id="terms_and_definitions">
	<title>Terms, and Definitions</title>
	<body>
		<label id="purchase_order_number_term" outputclass="term">
			Purchase Order:
		</label>
		<label id="purchase_order_number_definition" outputclass="definition">
			A Purchase Order number, is a
			nine-digit number in the form:
			1234-56789, with '1234' being
			the unique supplier identifier
		</label>
	</body>
</topic>
```
