# minecraftformatter
A simple script for a friend that takes a certain input text file and outputs a text file with a java array for minecraft modding.

Input format:
```
    material_a, material_b, material_c, ...
item1, a1, b1, invalid, ...
item2, a2, b2, c2, ...
item3, a3, b3, c3, ...
```

Output format:
```
"item1": {"material_a":a1, "material_b":b1}
"item2": {"material_a":a2, "material_b":b2, "material_c":c2}
"item3": {"material_a":a3, "material_b":b3, "material_c":c3}
```

Usage: `python minecraftformatter.py inputfile.txt outputfile.txt`
