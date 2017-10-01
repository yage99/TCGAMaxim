from clinical import clinical
from meta import meta

clinicalMeta = meta("/Users/zhangya/Documents/GBM/gdc_gbm_clinical.2017-09-25T08-50-24.108521.txt")
for id, file in clinicalMeta.files():
    tcgaClinical = clinical('/Users/zhangya/Documents/GBM/' + file)
    tcgaClinical.print_nodes()

    elements = tcgaClinical.dict_clinical
    for key in elements:
        print(key)
