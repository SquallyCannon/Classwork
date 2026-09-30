This project uses a lot of questionary select functions for the majority of it's navigation.

line2 = [line.strip() for line in inventory] and targetline = inventory.readlines() are used very interchangeably because they do act ever so slightly differently in the way they interpret splits.
Both are used for indexing when referencing inventory.txt.

