def transform_string(input_string):
    transformed_string = "^"
    for char in input_string:
        # print(char)
        transformed_string += "[" + char.lower() + char.upper() + "]"
    transformed_string += "$"
    return transformed_string


list = ["AbbottOTP", "SHEIN", "ROMWE","BAIWU","BWHK","SupportChat"]

for i in list:
    input_string = i
    output_string = transform_string(input_string)
    print(output_string)
