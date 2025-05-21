from tabulate import tabulate

data = [
    [1, "dog", "John Doe", 2020],
    [2, "cat", "Jane Smith", 2022]
]

headers = ["ID", "Title", "Author", "Year"]

print("Plain format:\n", tabulate(data, headers=headers, tablefmt="plain"), "\n")
print("Simple format:\n", tabulate(data, headers=headers, tablefmt="simple"), "\n")
print("Grid format:\n", tabulate(data, headers=headers, tablefmt="grid"), "\n")
print("Pipe format:\n", tabulate(data, headers=headers, tablefmt="pipe"), "\n")
print("HTML format:\n", tabulate(data, headers=headers, tablefmt="html"), "\n")
print("LaTeX format:\n", tabulate(data, headers=headers, tablefmt="latex"), "\n")
print("Fancy grid format:\n", tabulate(data, headers=headers, tablefmt="fancy_grid"), "\n")