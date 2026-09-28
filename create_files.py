section = 4
subsection = 2
root = f"exercise\\{section}"
for i in range(1, 6):
    with open(f"{root}\\ex_{section}_{subsection}_{i}.py", "w", encoding="utf-8") as fi:
        fi.write("")