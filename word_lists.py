import csv

l2_u1_l1_list = []
l2_u1_l2_list = []
l2_u1_l3_list = []
l2_u1_l4_list = []

l2_u2_l1_list = []
l2_u2_l2_list = []
l2_u2_l3_list = []
l2_u2_l4_list = []

l2_u3_l1_list = []
l2_u3_l2_list = []
l2_u3_l3_list = []
l2_u3_l4_list = []

l2_u4_l1_list = []
l2_u4_l2_list = []
l2_u4_l3_list = []
l2_u4_l4_list = []

l2_u5_l1_list = []
l2_u5_l2_list = []
l2_u5_l3_list = []
l2_u5_l4_list = []

l2_u6_l1_list = []
l2_u6_l2_list = []
l2_u6_l3_list = []
l2_u6_l4_list = []

l2_u7_l1_list = []
l2_u7_l2_list = []
l2_u7_l3_list = []
l2_u7_l4_list = []

l2_u8_l1_list = []
l2_u8_l2_list = []
l2_u8_l3_list = []
l2_u8_l4_list = []

l2_u9_l1_list = []
l2_u9_l2_list = []
l2_u9_l3_list = []
l2_u9_l4_list = []

l2_u10_l1_list = []
l2_u10_l2_list = []
l2_u10_l3_list = []
l2_u10_l4_list = []

l2_u11_l1_list = []
l2_u11_l2_list = []
l2_u11_l3_list = []
l2_u11_l4_list = []

l2_u12_l1_list = []
l2_u12_l2_list = []
l2_u12_l3_list = []
l2_u12_l4_list = []

# csv_from_book = 'SYM_2_WordList.csv' # movie this & function call to main app file

def generate_word_lists(csv_from_book):
    with open(csv_from_book, encoding='utf-8') as level_2_word_list_csv:
        all_word_list = csv.reader(level_2_word_list_csv)
        next(all_word_list) #skips header row
        for row in all_word_list:
            if row[0] == '1':
                if row[1] == '1':
                    l2_u1_l1_list.append(row[2])
                elif row[1] == '2':
                    l2_u1_l2_list.append(row[2])
                elif row[1] == '3':
                    l2_u1_l3_list.append(row[2])
                elif row[1] == '4':
                    l2_u1_l4_list.append(row[2])
            elif row[0] == '2':
                if row[1] == '1':
                    l2_u2_l1_list.append(row[2])
                elif row[1] == '2':
                    l2_u2_l2_list.append(row[2])
                elif row[1] == '3':
                    l2_u2_l3_list.append(row[2])
                elif row[1] == '4':
                    l2_u2_l4_list.append(row[2])
            elif row[0] == '3':
                if row[1] == '1':
                    l2_u3_l1_list.append(row[2])
                elif row[1] == '2':
                    l2_u3_l2_list.append(row[2])
                elif row[1] == '3':
                    l2_u3_l3_list.append(row[2])
                elif row[1] == '4':
                    l2_u3_l4_list.append(row[2])
            elif row[0] == '4':
                if row[1] == '1':
                    l2_u4_l1_list.append(row[2])
                elif row[1] == '2':
                    l2_u4_l2_list.append(row[2])
                elif row[1] == '3':
                    l2_u4_l3_list.append(row[2])
                elif row[1] == '4':
                    l2_u4_l4_list.append(row[2])
            elif row[0] == '5':
                if row[1] == '1':
                    l2_u5_l1_list.append(row[2])
                elif row[1] == '2':
                    l2_u5_l2_list.append(row[2])
                elif row[1] == '3':
                    l2_u5_l3_list.append(row[2])
                elif row[1] == '4':
                    l2_u5_l4_list.append(row[2])
            elif row[0] == '6':
                if row[1] == '1':
                    l2_u6_l1_list.append(row[2])
                elif row[1] == '2':
                    l2_u6_l2_list.append(row[2])
                elif row[1] == '3':
                    l2_u6_l3_list.append(row[2])
                elif row[1] == '4':
                    l2_u6_l4_list.append(row[2])
            elif row[0] == '7':
                if row[1] == '1':
                    l2_u7_l1_list.append(row[2])
                elif row[1] == '2':
                    l2_u7_l2_list.append(row[2])
                elif row[1] == '3':
                    l2_u7_l3_list.append(row[2])
                elif row[1] == '4':
                    l2_u7_l4_list.append(row[2])
            elif row[0] == '8':
                if row[1] == '1':
                    l2_u8_l1_list.append(row[2])
                elif row[1] == '2':
                    l2_u8_l2_list.append(row[2])
                elif row[1] == '3':
                    l2_u8_l3_list.append(row[2])
                elif row[1] == '4':
                    l2_u8_l4_list.append(row[2])
            elif row[0] == '9':
                if row[1] == '1':
                    l2_u9_l1_list.append(row[2])
                elif row[1] == '2':
                    l2_u9_l2_list.append(row[2])
                elif row[1] == '3':
                    l2_u9_l3_list.append(row[2])
                elif row[1] == '4':
                    l2_u9_l4_list.append(row[2])
            elif row[0] == '10':
                if row[1] == '1':
                    l2_u10_l1_list.append(row[2])
                elif row[1] == '2':
                    l2_u10_l2_list.append(row[2])
                elif row[1] == '3':
                    l2_u10_l3_list.append(row[2])
                elif row[1] == '4':
                    l2_u10_l4_list.append(row[2])
            elif row[0] == '11':
                if row[1] == '1':
                    l2_u11_l1_list.append(row[2])
                elif row[1] == '2':
                    l2_u11_l2_list.append(row[2])
                elif row[1] == '3':
                    l2_u11_l3_list.append(row[2])
                elif row[1] == '4':
                    l2_u11_l4_list.append(row[2])
            elif row[0] == '12':
                if row[1] == '1':
                    l2_u12_l1_list.append(row[2])
                elif row[1] == '2':
                    l2_u12_l2_list.append(row[2])
                elif row[1] == '3':
                    l2_u12_l3_list.append(row[2])
                elif row[1] == '4':
                    l2_u12_l4_list.append(row[2])
   

