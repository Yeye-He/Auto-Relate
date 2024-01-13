

class Data_Case:
    def __init__(self, data, case_id):
        self.data = data
        self.case_id = case_id
        
class HT_Score:
    def __init__(self):
        self.exist = 1
        
        
class AutoRelate_Result:
    def __init__(self, formula, ht1_score, columns):
        self.formula = formula
        self.ht1_score = ht1_score
        self.input_cols = columns[:-1]
        self.output_col = columns[-1]
        
    def Print(self):
        print("Formula: ", self.formula)
        print("HT1 Score: ", self.ht1_score)
        print("Input Columns: ", self.input_cols)
        print("Output Column: ", self.output_col)
        print('\n')