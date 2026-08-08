# write a program to fill in a letter template given below with name and date.
letter_template = """Dear <|name|>, You are selected. <|date|>"""
print(letter_template.replace("<|name|>", "Kabir").replace("<|date|>", "14-January"))

#write a program to detect the double spaces in a string and replace them with single space.
string = "This  is  a  string  with  double  spaces."
print(string.replace("  ", " "))

