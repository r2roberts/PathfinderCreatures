import lxml_creature as lc


def generate(c):
    print(lc.to_html(c))

    filename = "../creatures/" + \
        c._name.replace(' ', '_').replace('(', '').replace(')', '') + '.html'
    print(filename)

    with open(filename, "w") as fp:
        fp.write(lc.to_html(c))
    print(f"{filename} written")


if __name__ == "__main__":
    from Kelleni import c
    generate(c)
