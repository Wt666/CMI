def transform_string(input_string):
    transformed_string = "^"
    for char in input_string:
        transformed_string += "[" + char.lower() + char.upper() + "]"
    transformed_string += "$"
    return transformed_string


list = ["Web", "Rex", "WANGG"]

for i in list:
    input_string = i
    output_string = transform_string(input_string)
    print(output_string)
