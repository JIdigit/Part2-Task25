
#vse rabotaet
spisok=input()
temp_spisok=spisok.split(' ')
temp_length=0
max_index=0
for temp in temp_spisok:
    if len(temp)>temp_length:
        temp_length=len(temp)
        max_index=temp_spisok.index(temp)
print('The longest word is '+str((temp_spisok[max_index]))+' letter count is :' + str(temp_length))
    
