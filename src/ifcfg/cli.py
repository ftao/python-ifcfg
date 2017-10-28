import ifcfg
import json


def main():
    print json.dumps(ifcfg.interfaces(), indent=2)


if __name__ == "__main__":
    main()
