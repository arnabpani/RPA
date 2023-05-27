def find_data_by_title(str,data):
    return [el for el in data if el["question"] == str]

def find_data_by_questions(arr_q,data):
    temp = []
    for el in data:
        responses_text = []
        for r_el in el["response"]:
            responses_text.append(r_el["text"])
        if sorted(arr_q) == sorted(responses_text):
            temp.append(el)
    return temp

def get_quizz_data(title,arr_q,data):
    by_tilte = find_data_by_title(title,data)
    by_questions = find_data_by_questions(arr_q,data)
    if(len(by_tilte) == 1):
        return by_tilte[0]
    else:
        return by_questions[0]
    

    
#print(get_quizz_data("To loop through all the available work items:",[],data_quizz))