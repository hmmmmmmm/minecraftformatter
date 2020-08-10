from sys import argv, exit


def main():
    if len(argv) != 3:
        usage()

    # initialises items and materials lists
    items, materials = [], []

    # opens input file to read from
    with open(argv[1], "r") as in_text:
        # defines materials using first line
        materials = in_text.readline()
        # appends all following lines as list entries
        for line in in_text:
            items.append(line)

    # splits materials into list
    material = materials.split(",")

    # opens output file to write to
    with open(argv[2], "w+") as out_text:
        for item in items:
            # initialises string for this line
            line_string = ""

            # strips newlines and splits by commas
            item = item.rstrip("\n")
            item = item.split(",")

            # writes ""item1": {" to string
            line_string += f"\"{item[0]}\": {{"

            # iterates through materials and items except first item and last of both
            for j, k in zip(material[:-1], item[1:-1]):
                # strips whitespace
                j = j.lstrip(" ").rstrip("\n")
                k = k.strip(" ")

                # checks if item is invalid and if not, writes ""material_a": a1, " to string
                if k != "invalid":
                    line_string += f"\"{j}\":{k}, "

            # strips whitespace from final material/item
            material[-1] = material[-1].strip(" ").strip("\n")
            item[-1] = item[-1].strip(" ")

            # checks if final item is invalid and writes it if not
            if item[-1] != "invalid":
                line_string += f"\"{material[-1]}\":{item[-1]}"

            # writes final part of line: "}"
            line_string += f"}}\n"

            # checks if the final part of the string is empty and has comma, and replaces it if so
            line_string = line_string.replace(", }", "}")

            # writes line to file
            out_text.write(line_string)


def usage():
    print("Usage: python minecraftformatter.py inputfile.txt outputfile.txt")
    exit(1)


main()
