results = {
    1: "❌",  2: "✅",  3: "❌",  4: "❌",  5: "❌",
    6: "❌",  7: "✅",  8: "❌",  9: "❌", 10: "✅",
   11: "❌", 12: "❌", 13: "❌", 14: "❌", 15: "✅",
}

lines = []

for i in range(1, 6):  # 1 dan 5 gacha
    line = (
        f"{i}.A {results[i]}    "
        f"{i+5}.A {results[i+5]}    "
        f"{i+10}.A {results[i+10]}"
    )
    lines.append(line)

text = "\n".join(lines)
print(text)
