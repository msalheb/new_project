from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

crypto_configs = cisco_cfg.find_objects(r"^crypto map CRYPTO")


def main():

    pfs_g = cisco_cfg.find_objects_w_child(parentspec=r"crypto map CRYPTO",childspec=r"set pfs group2")

    for entry in pfs_g:
        print "  {0}".format(entry.text)
    print

if __name__ == "__main__":
    main()



