#!/usr/bin/env python

import sys
import re
import collections

def clean(source):
    pattern         = r"[^+-.,<>\[\]]"
    substitution    = ""
    content         = re.sub(pattern, substitution, source)

    return content

def main():
    try:
        argument_count = len(sys.argv)

        if argument_count < 2:
            print("nothing to interpret")
            sys.exit(1)

        if argument_count > 2:
            print("Too much argument provided")
            sys.exit(2)

        file_to_interpret = sys.argv[1]

        with open(file_to_interpret, "r") as file:
            file_content    = file.read()
            content         = clean(file_content)
            content_length  = len(content)
            memory          = collections.defaultdict(int)
            memory_index    = 0
            content_index   = 0
            inner_loops     = 0

            while content_index < content_length:
                character = content[content_index]

                if character == ".":
                    print(chr(memory[memory_index]), end = "")

                elif character == ",":
                    text                    = input("")
                    first_character         = text[0]
                    first_character_code    = ord(first_character)
                    memory[memory_index]    = first_character_code

                elif character == "+":
                    memory[memory_index] += 1

                elif character == "-":
                    if memory[memory_index] > 0:
                        memory[memory_index] -= 1

                elif character == ">":
                    memory_index += 1

                elif character == "<":
                    if memory_index > 0:
                        memory_index -= 1

                elif character == "]":
                    if memory[memory_index] > 0:
                        content_index       = content_index - 1
                        inner_loops         = 1
                        previous_character  = content[content_index]

                        while inner_loops != 0 and content_index > 0:
                            if previous_character == "[":
                                inner_loops = inner_loops - 1
                            elif previous_character == "]":
                                inner_loops = inner_loops + 1

                            content_index       = content_index - 1
                            previous_character  = content[content_index]

                content_index = content_index + 1

    except FileNotFoundError:
        print(f"File not found: {file_to_interpret}")
        sys.exit(3)

    except KeyboardInterrupt:
        print(f"Interpretation interrupted");
        sys.exit(4)

    except:
        print(f"Unknown error")
        sys.exit(5)

if __name__ == "__main__":
    main()
