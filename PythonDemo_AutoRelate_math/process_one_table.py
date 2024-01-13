import class_create
import pandas as pd
import table_formulas_discovery
import data_processing


# def run(max_violation_rate,data_path,degree_of_parallelism):
    
#     data = pd.DataFrame(pd.read_csv(data_path))
#     numerical_columns = data_processing.discover_numerical_columns(data)
#     rel_ce,abs_ce = 1e-09,1e-09
    
#     formulas_dict,running_type = table_formulas_discovery.formulas_discover_together_multiprocessing_easy_dirty('test_case',data,numerical_columns,
#                                                                                max_violation_rate,rel_ce,abs_ce,degree_of_parallelism)
    
    
#     # if len(formulas_dict.keys()) == 0:
#     #     print('No mathematical formula has been discovered.')
        
#     # else:
#     #     print('The mathematical formulas found are as follows: ')
#     #     for formula in formulas_dict.keys():
#     #         res = class_create.AutoRelate_Result(formula,formulas_dict[formula][0],formulas_dict[formula][1])
#     #         res.Print()
    
#     formulas = []
#     for formula in formulas_dict.keys():
#         res = class_create.AutoRelate_Result(formula,formulas_dict[formula][0],formulas_dict[formula][1])
#         formulas.append(res)
    
#     return formulas


def run(max_violation_rate,data_path,degree_of_parallelism,col_relationship=True,row_relationship=False):
    
    # data_path = 'transposed_data.csv'
    data = pd.DataFrame(pd.read_csv(data_path))
    formulas = []
    
    if col_relationship == True:
        numerical_columns = data_processing.discover_numerical_columns(data)
        rel_ce,abs_ce = 1e-09,1e-09
        
        formulas_dict,running_type = table_formulas_discovery.run('test_case',data,numerical_columns,max_violation_rate,
                                                                rel_ce,abs_ce,degree_of_parallelism)
    
        for formula in formulas_dict.keys():
            res = class_create.AutoRelate_Result(formula,formulas_dict[formula][0],formulas_dict[formula][1])
            formulas.append(res)
    
    
    if row_relationship == True:
        data_transposed = data.transpose()
        data_transposed.columns = ['row_{}'.format(i) for i in range(len(data_transposed.columns))]
        numerical_columns = data_processing.discover_numerical_columns(data_transposed)
        rel_ce,abs_ce = 1e-09,1e-09
        
        formulas_dict,running_type = table_formulas_discovery.run('test_case',data_transposed,numerical_columns,max_violation_rate,
                                                                  rel_ce,abs_ce,degree_of_parallelism)
    
        for formula in formulas_dict.keys():
            res = class_create.AutoRelate_Result(formula,formulas_dict[formula][0],formulas_dict[formula][1])
            formulas.append(res)
    
    
    return formulas
        

     
# max_violation_rate = 0
# rel_ce,abs_ce = 1e-09,1e-09
# data_path = r'F:\yifan\MSRA-Project\Datasets\Excel_AR\table_33981___xlsx_507925587250ec5298bddce77859e1c4f1c523db.xlsx___line_181\_table_with_col_formulas_without_violation.csv'
# run(max_violation_rate,rel_ce,abs_ce,data_path)