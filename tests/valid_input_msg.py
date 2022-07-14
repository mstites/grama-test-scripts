def valid_inputs_msg(df_arg, strings_accepted, valid_strings):
    r"""Generates string explaining valid inputs for use in DataFrame
    TypeErrors and ValueErrors

    Args:
        df_arg (str): Name of df argument
        strings_accepted (bool): Indicates whether strings are accepted or not
        valid_strings (None, list(str)): Valid string inputs
    
    Returns:
        String"""
    msg = df_arg + " must be DataFrame" # general msg for valid args
    if strings_accepted: 
        # add on string options to msg
        if len(valid_strings) == 1:
            string_args = " or " + valid_strings[0]
        else:
            print("hi")
            string_args = ", "  # comma after "must be DataFrame"
            for arg in valid_strings:
                print(arg)
                if arg == valid_strings[-1]:
                    # last value -> add or
                    print("last value")
                    string_args += "or '" + arg + "'"
                else:
                    # not last value -> add comma
                    string_args += "'" + arg + "', "  # add comma
                    
        msg += string_args + "."
    else: 
        # no valid string inputs, end message
        msg += "."
    return msg 


# msg = valid_inputs_msg("df_det", True, ["nom", "det"])
# msg = valid_inputs_msg("df_rnd", True, ["nom", "det", "rnd"])
msg = valid_inputs_msg("df_rnd", True, ["nom"])
# msg = valid_inputs_msg("df", False, None)
print(msg)