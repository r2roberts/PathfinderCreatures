from WrathOfDestroyer import c
import lxml_creature as lc

print(lc.to_html(c))

filename = "../" + \
    c._name.replace(' ', '_').replace('(', '').replace(')', '') + '.html'
print(filename)

with open(filename, "w") as fp:
    fp.write(lc.to_html(c))
print(f"{filename} written")
