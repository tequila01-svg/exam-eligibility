fees=238000
classes=48
std_attendance=int(input("insert number of classes:"))
std_fee_paid=int(input("insert fee paid:"))
if std_fee_paid>=200000 and std_attendance>=40:
    print("you are eligible")
else:
    print("you are not eligibile for the exam due to unpaid fees and little attendance")