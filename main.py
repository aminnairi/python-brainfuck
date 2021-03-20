#!/usr/bin/env python

import sys
import re

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
            content         = brainfuck.clean(file_content)
            content_length  = len(content)
            memory          = {0: 0}
            memory_index    = 0
            content_index   = 0
            inner_loops     = 0

            while content_index < content_length:
                character = content[content_index]

                if character == ".":
                    try:
                        memory_value            = memory[memory_index]
                        memory_value_character  = chr(memory_value)

                        print(memory_value_character, end = "")

                    except:
                        memory[memory_index]    = 0
                        memory_value            = memory[memory_index]
                        memory_value_character  = chr(memory_value)

                        print(memory_value_character, end = "")

                elif character == ",":
                    text                    = input("")
                    first_character         = text[0]
                    first_character_code    = ord(first_character)
                    memory[memory_index]    = first_character_code

                elif character == "+":
                    try:
                        new_memory_value        = memory[memory_index] + 1
                        memory[memory_index]    = new_memory_value

                    except:
                        memory[memory_index] = 1

                elif character == "-":
                    try:
                        new_memory_value = memory[memory_index] - 1

                        if new_memory_value < 0:
                            memory[memory_index] = 0

                        else:
                            memory[memory_index] = new_memory_value

                    except:
                        memory[memory_index] = 0

                elif character == ">":
                    memory_index = memory_index + 1

                elif character == "<":
                    new_memory_index = memory_index - 1

                    if new_memory_index < 0:
                        memory_index = 0
                    else:
                        memory_index = new_memory_index

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

    except error:
        print(f"Unknown error: {error}")
        sys.exit(5)

if __name__ == "__main__":
    main()
