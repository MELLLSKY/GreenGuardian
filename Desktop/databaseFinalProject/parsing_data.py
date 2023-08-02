import csv
def customer_status():
#    with open('telecomdata.csv','r') as file:
#        reader = csv.reader(file)
#        a = []
#        for row in reader:
#            if row[35] not in a:
#                a.append(row[35])
        #'Stayed', 'Churned', 'Joined'
    a=['Stayed', 'Churned', 'Joined']
    with open('telecomdata.csv','r') as file:
        reader = csv.reader(file)
        for row in reader:
            for i in a:
                if row[35] == i:
                    with open('customer.csv','a',newline='') as file:
                        writer = csv.writer(file, delimiter=',')
                        writer.writerow((row[0],row[1],"1",i))


def churn_cat():
   # with open('telecomdata.csv','r') as file:
   #     reader = csv.reader(file)
   #     a = []
   #     for row in reader:
   #         if row[36] not in a:
   #             a.append(row[36])
    a= ['Competitor', 'Dissatisfaction', 'Other', 'Price', 'Attitude']
    with open('telecomdata.csv','r') as file:
        reader = csv.reader(file)
        for row in reader:
            for i in a:
                if row[36] == i:
                    with open('churn_cat.csv','a',newline='') as file:
                        writer = csv.writer(file, delimiter=',')
                        writer.writerow((row[0],row[1],"2",i))

def churn_reason():
   # with open('telecomdata.csv','r') as file:
   #     reader = csv.reader(file)
   #     a = []
   #     for row in reader:
   #         if row[37] not in a:
   #             a.append(row[37])
   # print(a)
   #
   # ['Competitor had better devices', 'Product dissatisfaction', 'Network reliability',
   #  'Limited range of services', 'Competitor made better offer', "Don't know", 'Long distance charges',
   #  'Attitude of service provider', 'Attitude of support person', 'Competitor offered higher download speeds',
   #  'Competitor offered more data', 'Lack of affordable download/upload speed', 'Deceased', 'Moved',
   #  'Service dissatisfaction', 'Price too high', 'Lack of self-service on Website', 'Poor expertise of online support',
   #  'Extra data charges', 'Poor expertise of phone support']
    a=['Competitor had better devices', 'Product dissatisfaction', 'Network reliability',
    'Limited range of services', 'Competitor made better offer', "Don't know", 'Long distance charges',
    'Attitude of service provider', 'Attitude of support person', 'Competitor offered higher download speeds',
    'Competitor offered more data', 'Lack of affordable download/upload speed', 'Deceased', 'Moved',
    'Service dissatisfaction', 'Price too high', 'Lack of self-service on Website', 'Poor expertise of online support',
    'Extra data charges', 'Poor expertise of phone support']


    with open('telecomdata.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            for i in a:
                if row[37] == i:
                    with open('churn_reason.csv', 'a', newline='') as file:
                        writer = csv.writer(file, delimiter=',')
                        writer.writerow((row[0], row[1], "3", i))

def int_type():
    a=['Cable', 'Fiber Optic', 'DSL']
    with open('telecomdata.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            for i in a:
                if row[16] == i:
                    with open('int_type.csv', 'a', newline='') as file:
                        writer = csv.writer(file, delimiter=',')
                        writer.writerow((row[0], row[1], "4", i))

def offer():
    a=['None', 'Offer E', 'Offer D', 'Offer A', 'Offer B', 'Offer C']
    with open('telecomdata.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            for i in a:
                if row[11] == i:
                    with open('offer.csv', 'a', newline='') as file:
                        writer = csv.writer(file, delimiter=',')
                        writer.writerow((row[0], row[1], "5", i))

def contract():
    a=['One Year', 'Month-to-Month', 'Two Year']
    with open('telecomdata.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            for i in a:
                if row[26] == i:
                    with open('contract.csv', 'a', newline='') as file:
                        writer = csv.writer(file, delimiter=',')
                        writer.writerow((row[0], row[1], "6", i))

def payment_method():
    a=['Credit Card', 'Bank Withdrawal', 'Mailed Check']
    with open('telecomdata.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            for i in a:
                if row[28] == i:
                    with open('payment_method.csv', 'a', newline='') as file:
                        writer = csv.writer(file, delimiter=',')
                        writer.writerow((row[0], row[1], "7", i))

def total_extra():
    a=['0', '10', '20', '40', '120', '100', '130', '110', '60', '140', '50', '80', '150', '70', '30', '90']
    with open('telecomdata.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            for i in a:
                if row[32] == i:
                    with open('total_extra.csv', 'a', newline='') as file:
                        writer = csv.writer(file, delimiter=',')
                        writer.writerow((row[0], row[1], "5", i))

def tenur():
    a= ['9', '4', '13', '3', '71', '63', '7', '65', '54', '72', '5', '56', '34', '1', '45', '50', '23', '55', '26', '69', '37', '49', '66', '67', '20', '43', '59', '12', '27', '2', '25', '29', '14', '35', '64', '39', '40', '11', '6', '30', '70', '57', '58', '16', '32', '33', '10', '21', '61', '15', '44', '22', '24', '19', '47', '62', '46', '52', '8', '60', '48', '28', '41', '53', '68', '31', '36', '17', '18', '51', '38', '42']
    with open('telecomdata.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            for i in a:
                if row[10] == i:
                    with open('tenur.csv', 'a', newline='') as file:
                        writer = csv.writer(file, delimiter=',')
                        writer.writerow((row[0], row[1], "4", i))

def referrals():
    a=['2', '0', '1', '3', '8', '9', '10', '5', '4', '7', '6', '11']
    with open('telecomdata.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            for i in a:
                if row[9] == i:
                    with open('referrals.csv', 'a', newline='') as file:
                        writer = csv.writer(file, delimiter=',')
                        writer.writerow((row[0], row[1], "3", i))


def married():
    with open('telecomdata.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            with open('married.csv', 'a', newline='') as file:
                if row[3] == "Yes":
                    writer = csv.writer(file, delimiter=',')
                    writer.writerow((row[0], row[1], "1", "Y"))
                elif row[3] == "No":
                    writer = csv.writer(file, delimiter=',')
                    writer.writerow((row[0], row[1], "1", "N"))



def int_service():
    with open('telecomdata.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            with open('int_service.csv', 'a', newline='') as file:
                if row[15] == "Yes":
                    writer = csv.writer(file, delimiter=',')
                    writer.writerow((row[0], row[1], "3", "Y"))
                elif row[15] == "No":
                    writer = csv.writer(file, delimiter=',')
                    writer.writerow((row[0], row[1], "3", "N"))



def online_sec():
    with open('telecomdata.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            with open('online_sec.csv', 'a', newline='') as file:
                if row[18] == "Yes":
                    writer = csv.writer(file, delimiter=',')
                    writer.writerow((row[0], row[1], "4", "Y"))
                elif row[18] == "No":
                    writer = csv.writer(file, delimiter=',')
                    writer.writerow((row[0], row[1], "4", "N"))


def online_backup():
    with open('telecomdata.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            with open('online_backup.csv', 'a', newline='') as file:
                if row[19] == "Yes":
                    writer = csv.writer(file, delimiter=',')
                    writer.writerow((row[0], row[1], "5", "Y"))
                elif row[19] == "No":
                    writer = csv.writer(file, delimiter=',')
                    writer.writerow((row[0], row[1], "5", "N"))

def phone_service():
    with open('telecomdata.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            with open('phone_service.csv', 'a', newline='') as file:
                if row[12] == "Yes":
                    writer = csv.writer(file, delimiter=',')
                    writer.writerow((row[0], row[1], "6", "Y"))
                elif row[12] == "No":
                    writer = csv.writer(file, delimiter=',')
                    writer.writerow((row[0], row[1], "6", "N"))


def protection_plan():
    with open('telecomdata.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            with open('protection_plan.csv', 'a', newline='') as file:
                if row[20] == "Yes":
                    writer = csv.writer(file, delimiter=',')
                    writer.writerow((row[0], row[1], "7", "Y"))
                elif row[20] == "No":
                    writer = csv.writer(file, delimiter=',')
                    writer.writerow((row[0], row[1], "7", "N"))

def tech_support():
    with open('telecomdata.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            with open('tech_support.csv', 'a', newline='') as file:
                if row[21] == "Yes":
                    writer = csv.writer(file, delimiter=',')
                    writer.writerow((row[0], row[1], "8", "Y"))
                elif row[21] == "No":
                    writer = csv.writer(file, delimiter=',')
                    writer.writerow((row[0], row[1], "8", "N"))


def gender():
    with open('gender.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            with open('sex.csv', 'a', newline='') as file:
                if row[1] == "Female":
                    writer = csv.writer(file, delimiter=',')
                    writer.writerow((row[0], "2", "F"))
                elif row[1] == "Male":
                    writer = csv.writer(file, delimiter=',')
                    writer.writerow((row[0], "2", "M"))

def gb():
    with open('telecomdata.csv', 'r') as file:
        reader = csv.reader(file)
        a = []
        for row in reader:
            if row[17] not in a:
                a.append(row[17])

    if '' in a:
            a.remove('')
    with open('telecomdata.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            for i in a:
                if row[17] == i:
                    with open('gb.csv', 'a', newline='') as file:
                        writer = csv.writer(file, delimiter=',')
                        writer.writerow((row[0], row[1], "6", i))


