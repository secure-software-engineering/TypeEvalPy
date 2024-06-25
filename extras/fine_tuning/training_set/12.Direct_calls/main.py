def final_func():
    pass


def first_func():
    return_val = final_func
    return return_val


func_val = first_func
func_val()()
