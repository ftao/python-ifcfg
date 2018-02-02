from __future__ import print_function

import json

import ifcfg


def main():
    print(json.dumps(ifcfg.interfaces(), indent=2))


if __name__ == "__main__":
    main()
