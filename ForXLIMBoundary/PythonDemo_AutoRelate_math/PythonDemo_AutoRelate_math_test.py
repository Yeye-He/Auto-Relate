
import process_one_table
import os
# print(os.getcwd())


def AutoRelate_math(file, ht1_threshold=0.5):
    max_violation_rate = 0
    # rel_ce,abs_ce = 1e-09,1e-09
    #data_path = 'test_data_row_relation.csv'
    degree_of_parallelism = 20
    col_relationship = True 
    row_relationship = True
    results_list = process_one_table.run(max_violation_rate, file, degree_of_parallelism,
                                         col_relationship,row_relationship)
    
    results_list = [r for r in results_list if r.ht1_score < ht1_threshold]
    
    return results_list

# run cases from xlim boundary
def run_xlim_case():
    test_files = ['data/case-11a.num_only.csv', 'data/case-11b.num_only.csv', 'data/case-2b.num_only.csv', 'data/case-2a.num_only.csv']
    
    for f in test_files:
        results_list = AutoRelate_math(f)
        for res in results_list:
            res.Print()
    

def simple_test_row():
    
    file = 'test_data_row_relation.csv' ## pass in a csv file with a number-only region from XLSX
    results_list = AutoRelate_math(file)
    for res in results_list:
        res.Print()
        
    # except:
    # Formula:  row_2=row_0+row_1
    # HT1 Score:  0.4814814814814815
    # Input Columns:  ['row_0', 'row_1']
    # Output Column:  row_2



    #################################




    # test_data except:
    # Formula:  J=L+D
    # HT1 Score:  0.010000000000001452
    # Input Columns:  ['L', 'D']
    # Output Column:  J


    # Formula:  G=D+K
    # HT1 Score:  0.010000000000001452
    # Input Columns:  ['D', 'K']
    # Output Column:  G


    # Formula:  N=(L/K)*M
    # HT1 Score:  0.19500000000000073
    # Input Columns:  ['L', 'K', 'M']
    # Output Column:  N


    # Formula:  K=(L-J)+G
    # HT1 Score:  0.005000000000000726
    # Input Columns:  ['L', 'J', 'G']
    # Output Column:  K




if __name__ == "__main__":
    #simple_test_row()

    run_xlim_case()