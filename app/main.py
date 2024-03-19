def copy_file(command: str) -> None:

    if len(command.split()) != 3:
        print("Invalid command format")
        return

    key_word, read_file, write_file = command.split()

    if key_word == "cp" and read_file != write_file:
        with (
            open(read_file, "r") as file_in,
            open(write_file, "w") as file_out
        ):
            file_out.write(file_in.read())
