JSON (JavaScript Object Notation) is a lightweight data-interchange format. 
It is easy for humans to read and write. It is easy for machines to parse and generate.
A collection of name/value pairs.

def json_extract(obj, key):
    """Recursively fetch values from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    values = extract(obj, arr, key)
    return values

The above code for extracting json parsing is one of the example of recursively iterating through the json so as to extract the required information.
It works like searching recursively to get values for the key. So in the extraction part it checks for the presence of dictionary if it is then iterate through key-value pairs. If there is value then if there is dictionary and list is present if it is then extract. Otherwise append it to value.
If there is only a list then for each item extract the item, array and key. Finally return the values. 



