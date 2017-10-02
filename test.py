from clinical import clinical
from meta import meta

clinicalMeta = meta("/Users/zhangya/Documents/GBM/gdc_gbm_clinical.2017-09-25T08-50-24.108521.txt")
countAll = 0
countValid = 0
with open('result.txt', 'w') as txt_file:
    for id, file in clinicalMeta.files():
        tcgaClinical = clinical('/Users/zhangya/Documents/GBM/' + file)
        #tcgaClinical.print_nodes()

        #values = tcgaClinical.retrive_by_prefered_name_path(['patient/days_to_death'])
        #print(file + str(values))
        info = tcgaClinical.retrive_days_to_death()
        days_to_death = info['days_to_death']
        countAll = countAll + 1
        if(days_to_death != 0):
            countValid = countValid + 1
            print("%s:%s" % (id, info))

        txt_file.write("%s:%s\n" % (id, info))

print("valid: %d, all:%d" %(countValid, countAll))
