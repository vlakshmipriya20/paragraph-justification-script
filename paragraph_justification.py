import sys

def justify_paragraph(paragraph, page_width):
    words = paragraph.split()
    current_line = []
    justified_lines = []

    for word in words:
        if sum(len(ch) for ch in current_line) + len(current_line) + len(word) <= page_width:
            current_line.append(word)
        else:
            justified_lines.append(justify_each_line(current_line, page_width))
            current_line = [word]

    justified_lines.append(justify_each_line(current_line, page_width))

    return justified_lines


def justify_each_line(words, page_width):
    if len(words) == 1:
        return words[0].ljust(page_width)
    else:
        total_spaces = page_width - sum(len(w) for w in words)
        spaces_between_words = total_spaces // (len(words) - 1)
        extra_spaces_to_be_added = total_spaces % (len(words) - 1)

        justified_line = words[0]
        for i in range(1, len(words)):
            spaces = spaces_between_words + (1 if i <= extra_spaces_to_be_added else 0)
            justified_line += ' ' * spaces + words[i]

        return justified_line


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python paragraph_justification.py <paragraph> <page_width>")
        sys.exit(1)

    paragraph = sys.argv[1]

    try:
        page_width = int(sys.argv[2])
    except ValueError:
        print("Error: page_width must be an integer.")
        sys.exit(1)

    justified_paragraph_array = justify_paragraph(paragraph, page_width)

    index = 1
    for line in justified_paragraph_array:
        print(f"Array [{index}] = \"{line}\"")
        index += 1
