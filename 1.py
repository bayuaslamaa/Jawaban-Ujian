name = "Bayu Aslama Zulfikar Ahmad"
age = str(23)
address = "Villa Mas Garden F 158-159 Perwira Bekasi Utara 17122"
my_hobbies = ['coding', 'reading', 'writing']
status = input('Choose \"bayu\" or \"other\" for showing the status in the bio: ') 
school = ['TKIT Bani Shaleh Bekasi', 'SDIT Al-Manar', 'SMPIT Darul Hikmah', 'MAN 1 Bekasi', 'ITS Surabaya']
def Bio():
    print("My Bio", "\nName: " , name ,"\nAge: " , age ,"\nAddress: " , address, "\nHobby: ", my_hobbies[0], "\nSMP: ", school[2], "2008-2009" , "\nSMA: ", school[3] , "\nUniversitas: ", school[4])
    
    if status == 'bayu':
        print('status: is married')
        return True
    elif gener == '2':
        print('status is single')
        return False
print()

Bio()
