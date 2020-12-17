import sys
from regipy.registry import RegistryHive

if __name__ == "__main__":
    try:
        # todo: use argparse for better usability
        if len(sys.argv) == 4:
            try:
                reg_file = RegistryHive(sys.argv[1])
                # e.g. "SOFTWARE\\Microsoft\\NET Framework Setup\\NDP\\v4\\full\\Release"
                key = sys.argv[2]
                val = sys.argv[3]
                print(reg_file.get_key(key).get_value(val, as_json=True, raise_on_missing=True))
            except:
                print("Registry key not found or you have provided an incorrect key")
        else:
            print("incomplete argument list")
            print("Usage: regireader.exe <registry_file> <key> <value>")
    except Exception as ex:
        print("Regi-reader gets the registry key from an offline registry hive")
        print("Usage: regireader.exe <registry_file> <key> <value>")
    