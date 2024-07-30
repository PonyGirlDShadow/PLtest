import sys
import json

def handleTest(test, result_dict):
    if (test.get("value") != None):
        test["value"] = result_dict[test["id"]]
    if (test.get("values") == None): return
    for inner_test in test["values"]:
        handleTest(inner_test, result_dict)


def main():
    values_filepath = ""
    tests_filepath  = ""
    result_filepath  = ""
    if len(sys.argv) == 4:
        values_filepath = sys.argv[1]
        tests_filepath = sys.argv[2]
        result_filepath = sys.argv[3]
    else:
        values_filepath = input()
        tests_filepath = input()
        result_filepath = input()
    result_dict  = {}
    with open(values_filepath) as values:
        results = json.loads(values.read())
        for result in results["values"]:
            result_dict[result["id"]] = result["value"]
    with open(tests_filepath) as tests:
        tests = json.loads(tests.read())
    filled = tests
    for test in filled["tests"]:
        handleTest(test, result_dict)
    with open(result_filepath, "w") as output:
        output.write(json.dumps(filled, indent=2))
if __name__ == "__main__":
    main()