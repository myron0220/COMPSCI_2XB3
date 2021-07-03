import math
import random
import timeit
import matplotlib.pyplot as plt
import xlsxwriter


def create_near_sorted_list(n, factor):
    L = create_random_list(n)
    L.sort()
    for _ in range(math.ceil(n*factor)):
        index1 = random.randint(0, n-1)
        index2 = random.randint(0, n-1)
        L[index1], L[index2] = L[index2], L[index1]
    return L

def create_random_list(n):
    L = []
    for _ in range(n):
        L.append(random.randint(1,n))
    return L

def timetest_1(f1, runs, n):
    total_f1 = 0
    for _ in range(runs):
        ##### change this line if need create_near_sorted_list(n, factor) #####
        ls1 = create_random_list(n)
        ##### change this line if need create_near_sorted_list(n, factor) #####
        start_f1 = timeit.default_timer()
        f1(ls1)
        end_f1 = timeit.default_timer()
        total_f1 += end_f1 - start_f1
    return total_f1 / runs
    
def get_data_1(f1, n_range, runs):
    t_range_f1 = []
    for n in n_range:
        t = timetest_1(f1, runs, n)
        t_range_f1.append(t)
    return t_range_f1
        
def print_1(f1, n_range, runs):
    t_range_f1 = get_data_1(f1, n_range, runs)
    # output
    print("List size(n) | Run time(second)")
    for i in n_range():
        print(n_range[i], t_range_f1[i])
        
def excel_1(f1, n_range, runs):
    t_range_f1 = get_data_1(f1, n_range, runs)
    # output
    func_name = str(f1).split()[1]
    data_path = "Data/" + func_name + ".xlsx"
    workbook = xlsxwriter.Workbook(data_path)
    data = workbook.add_worksheet(func_name)
    data.write(0, 0, "List size(n)")
    data.write_column(1, 0, n_range)
    data.write(0, 1, "Run time(second)")
    data.write_column(1, 1, t_range_f1)
    workbook.close()
    
def plot_1(f1, n_range, runs):
    t_range_f1 = get_data_1(f1, n_range, runs)
    # output
    func_name = str(f1).split()[1]
    plt.scatter(n_range, t_range_f1, marker='.',
                label=func_name)
    plt.xlabel("List size(n)")
    plt.ylabel("Run time(second)")
    plt.legend(loc='upper left')
    plt.show()
    plt.savefig("Figures/" + func_name)
    plt.close()

def timetest_2(f1, f2, runs, n):
    total_f1 = 0
    total_f2 = 0
    for _ in range(runs):
        ##### change this line if need create_near_sorted_list(n, factor) #####
        ls1 = create_random_list(n)
        ##### change this line if need create_near_sorted_list(n, factor) #####
        ls2 = ls1.copy()

        start_f1 = timeit.default_timer()
        f1(ls1)
        end_f1 = timeit.default_timer()

        start_f2 = timeit.default_timer()
        f2(ls2)
        end_f2 = timeit.default_timer()

        total_f1 += end_f1 - start_f1
        total_f2 += end_f2 - start_f2
    return (total_f1 / runs, total_f2 / runs)
    
def get_data_2(f1, f2, n_range, runs):
    t_range_f1 = []
    t_range_f2 = []
    for n in n_range:
        t = timetest_2(f1, f2, runs, n)
        t_range_f1.append(t[0])
        t_range_f2.append(t[1])
    return (t_range_f1, t_range_f2)
    
def print_2(f1, f2, n_range, runs):
    t_range_both = get_data_2(f1, f2, n_range, runs)
    # output
    print("List size(n) | f1 Run time(second) | f2 Run time(second)")
    for i in n_range():
        print(n_range[i], t_range_both[0][i], t_range_both[1][i])
    
def excel_2(f1, f2, n_range, runs):
    t_range_both = get_data_2(f1, f2, n_range, runs)
    # output
    func_names = [str(f1).split()[1], str(f2).split()[1]]
    data_path = "Data/" + func_names[0] + "_" + func_names[1] + ".xlsx"
    workbook = xlsxwriter.Workbook(data_path)
    data = workbook.add_worksheet(func_names[0] + "_" + func_names[1])
    data.write(0, 0, "List size(n)")
    data.write_column(1, 0, n_range)
    data.write(0, 1, "f1 Run time(second)")
    data.write_column(1, 1, t_range_both[0])
    data.write(0, 2, "f2 Run time(second)")
    data.write_column(1, 2, t_range_both[1])
    workbook.close()
    
def plot_2(f1, f2, n_range, runs):
    t_range_both = get_data_2(f1, f2, n_range, runs)
    # output
    labels = [str(f1).split()[1], str(f2).split()[1]]
    plt.scatter(n_range, t_range_both[0], marker='.',
                label=labels[0])
    plt.scatter(n_range, t_range_both[1], marker='.',
                label=labels[1])
    plt.xlabel("List size(n)")
    plt.ylabel("Run time(second)")
    plt.legend(loc='upper left')
    plt.show()
    plt.savefig("Figures/" + labels[0] + "_vs_" + labels[1])
    plt.close()
    
################# additional method for calculating how faster ###############
def compare(f1, f2, runs, n):
    total_f1 = 0
    total_f2 = 0
    for _ in range(runs):
        ls1 = create_random_list(n)
        ls2 = ls1.copy()

        start_f1 = timeit.default_timer()
        f1(ls1)
        end_f1 = timeit.default_timer()

        start_f2 = timeit.default_timer()
        f2(ls2)
        end_f2 = timeit.default_timer()

        total_f1 += end_f1 - start_f1
        total_f2 += end_f2 - start_f2
    return (total_f1 / runs, total_f2 / runs)
    
def plot(f1, f2, n_range, runs):
    t_range_f1 = []
    t_range_f2 = []
    t_range_comp = []
    for n in n_range:
        t = compare(f1, f2, runs, n)
        t_range_f1.append(t[0])
        t_range_f2.append(t[1])
        t_range_comp.append((t[0]-t[1])/t[1])
    labels = [str(f1).split()[1], str(f2).split()[1]]
    plt.scatter(n_range, t_range_f1, marker='.',
                label=labels[0])
    plt.scatter(n_range, t_range_f2, marker='.',
                label=labels[1])
    plt.xlabel("List size(n)")
    plt.ylabel("Run time(second)")
    plt.legend(loc='upper left')
    plt.savefig("Figures/" + labels[0] + "_vs_" + labels[1])
    plt.close()
    comp_result = sum(t_range_comp)/len(t_range_comp) * 100
    print(labels[1] + " is " + str(comp_result) + "% faster than " + labels[0])
