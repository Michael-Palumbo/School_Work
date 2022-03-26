
COMMENT_SYMBOL = "#"

CONFIG_VARIABLES = {"port_mode":False, "pasv_mode":False}

def get_variables(all_text):
    for line in all_text:
        if line[0] != COMMENT_SYMBOL and len(line) > 2:
            get_variable(line)

def get_variable(line):
    words = line.split()
    if words[0] in CONFIG_VARIABLES.keys():
        CONFIG_VARIABLES[words[0]] = value_to_bool(words[2])

def value_to_bool(value):
    return value == 'true'

def main():
    with open("ftpserverd.conf", "r") as conf:
        get_variables(conf.readlines())
    
    print(f'port_mode = {CONFIG_VARIABLES["port_mode"]}')
    print(f'pasv_mode = {CONFIG_VARIABLES["pasv_mode"]}')

    print("Program Ended")

if __name__ == "__main__":
    main()