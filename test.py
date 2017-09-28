import base

tcgaClinical = base.tcga_clinical('/Users/zhangya/Documents/GBM/72f13144-870b-4e3e-8111-8644f880a6b8/nationwidechildrens.org_clinical.TCGA-12-0691.xml')

tcgaClinical.print_nodes()

elements = tcgaClinical.dict_clinical
for key in elements:
    print(key)
