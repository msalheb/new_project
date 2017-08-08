from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

crypto_configs = cisco_cfg.find_objects(r"^crypto map CRYPTO")


def main():

    pfs_g = cisco_cfg.find_objects_wo_child(parentspec=r"crypto map CRYPTO",childspec=r"AES")

    for entry in pfs_g:
        print "\nCrypto map without AES is:"
        print "  {0}".format(entry.text)
        print "\nTransform Set used is:"
        for child in entry.children:
            print child.text
    print

if __name__ == "__main__":
    main()



