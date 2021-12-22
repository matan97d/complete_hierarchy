import json
import pprint
import sys


def key_contains_string(key, str):
    for st in str:
        if st in key:
            return True
    return False


def trim_dictionary(dict, str):
    new_dict = {}
    for k, v in dict.items():
        if len(v) == 0:
            if key_contains_string(k, str):
                new_dict[k] = v
            # else:
            #     return None
        else:
            trimmed_dict = trim_dictionary(v, str)
            if key_contains_string(k, str) or len(trimmed_dict) > 0:
                new_dict[k] = trimmed_dict
    return new_dict


# for bat script
def trim_non_json(txt):
    # print(txt)
    try:
        trimmed = txt.split("Attaching...\r\n")[1]  # need to change to "{" delimiter and join [1:] results
        trimmed = trimmed.split("[")[0]
        trimmed = trimmed.split("\r\n")
    except:
        trimmed = txt.split("Attaching...\n")[1]
        trimmed = trimmed.split("[")[0]
        trimmed = trimmed.split("\n")
    trimmed = ''.join(trimmed)
    return trimmed
    # file.write(pprint.pprint(trimmed_dict))


def create_trimmed_dictionary(txt, filter_str):
    json_trimmed = json.loads(txt)
    trimmed_dict = trim_dictionary(json_trimmed, filter_str)
    filename = filter_str[0] + "_trimmed.txt"
    file = open(filename, "w", newline='')
    sys.stdout = file
    print(json.dumps(trimmed_dict, indent=4))
    file.close()


def filter_tree(argv):
    file = open(argv[0] + ".txt", "rb")
    contents = file.read()
    contents = contents.decode("utf-8")
    create_trimmed_dictionary(contents, argv[1:])
    # print(contents)
    # print(file.read)


def testing_version(argv):
    file = open(argv[0] + ".txt", "rb")
    contents = file.read()
    contents = contents.decode("utf-8")
    trimmed = trim_non_json(contents)
    create_trimmed_dictionary(trimmed, argv[1:])


if __name__ == '__main__':
    testing_version(sys.argv[1:])
