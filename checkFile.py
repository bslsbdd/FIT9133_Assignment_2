def check_file(file1,file2):
    f1=open(file1,"r",encoding= 'utf-8')
    f2=open(file2,"r",encoding ='utf-8')
    n = 0
    for line1 in f1:
        n+=1
        for line2 in f2:
            if line1==line2:
            #print("SAME\n")
                break
            else:
                print(line1 + line2, n)
            break
    f1.close()
    f2.close()
#print(filecmp.cmp('pg16328_clean.txt','test.txt'))

#check_file('11-0_clean.txt','11-0.txttest.txt')
#check_file('84-0_clean.txt','84-0.txttest.txt')
#check_file('1342-0_clean.txt','1342-0.txttest.txt')
#check_file('1661-0_clean.txt','1661-0.txttest.txt')
#check_file('1952-0_clean.txt','1952-0.txttest.txt')
check_file('pg16328_clean.txt','pg16328.txttest.txt')
