from clinical import clinical
from meta import meta

clinicalMeta = meta("/Users/zhangya/Documents/GBM/gdc_gbm_clinical.2017-09-25T08-50-24.108521.txt")
countAll = 0
countValid = 0
with open('result.txt', 'w') as txt_file:
    txt_file.write("id,days_to_death\n")
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


        days_to_death = info['days_to_death']
        if not days_to_death:
            days_to_death = None
        else:
            days_to_death = max(days_to_death)

        
        days_to_last_followup = info['days_to_last_followup']
        if not days_to_last_followup:
            days_to_last_followup = None
        else:
            days_to_last_followup = max(days_to_last_followup)
            
        vital_status = info['vital_status']

        if not vital_status:
            vital_status = None
        elif 'Dead' in vital_status:
            vital_status = 'Dead'
        else:
            vital_status = 'Alive'

        
        if vital_status == 'Dead':
            if days_to_death is not None:
                days_to_death = days_to_death
            else:
                print ("warn: %s days to death is not avaiable, \
                        using days_to_last_followup" % id)
                days_to_death = days_to_last_followup
        elif vital_status == 'Alive':
            days_to_death = None
        else:
            print("error: data corrupted")
        
        txt_file.write("%s,%s\n" % (id, str(days_to_death)))
                                    

print("valid: %d, all:%d" %(countValid, countAll))
