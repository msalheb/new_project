from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

crypto_configs = cisco_cfg.find_objects(r"^crypto map CRYPTO")


def main():
    for c_map in crypto_configs:
        print
        print c_map.text
        for child in c_map.children:
            print child.text
    print

if __name__ == "__main__":
    main()



