salary=int(input())
bonus=int(input())
endorsements=int(input())
total_amount=salary+bonus+endorsements
sal_per=(salary/total_amount)*100
bonus_per=(bonus/total_amount)*100
endorse_per=(endorsements/total_amount)*100
print("%.2f"%sal_per,"%.2f"%bonus_per,"%.2f"%endorse_per)
