# Retrieve all the words starting with ‘b’ or ‘B’ from the following text.
""" text = "Betty bought a bit of butter, But the butter was so bitter,
So she bought some better butter, To make the bitter butter better." """

import re

text = """Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."""

List = re.findall(r'\b[bB]\w+', text)   # Using Regular Expression.
# print(List)
result = []
for l in List:
    if l not in result:
        result.append(l)

print(result)
