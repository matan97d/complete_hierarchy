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


def trim_non_json(txt, filter_str):
    # print(txt)
    try:
        trimmed = txt.split("Attaching...\r\n")[1]
        trimmed = trimmed.split("[")[0]
        trimmed = trimmed.split("\r\n")
    except:
        trimmed = txt.split("Attaching...\n")[1]
        trimmed = trimmed.split("[")[0]
        trimmed = trimmed.split("\n")
    trimmed = ''.join(trimmed)
    json_trimmed = json.loads(trimmed)
    trimmed_dict = trim_dictionary(json_trimmed, filter_str)
    # print(trimmed_dict)
    filename = filter_str[0] + "1.txt"
    file = open(filename, "w", newline='')
    sys.stdout = file
    pprint.pprint(trimmed_dict)
    file.close()
    # file.write(pprint.pprint(trimmed_dict))


def main(argv):
    file = open("Robo.txt", "rb")
    contents = file.read()
    contents = contents.decode("utf-8")
    trim_non_json(contents, argv)
    # print(contents)
    # print(file.read


if __name__ == '__main__':
    main(sys.argv[1:])
