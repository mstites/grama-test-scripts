import grama as gr
import traceback

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

# model tests

def one_test(func, md, df, df2=None):
    r"""Performs one test of a function

    func: grama function to test
    md: Model variable
    df: Df variable
    df2: df variable if function takes df arguments
    """
    try:
        if df2 is None:
            print(func(md, df))
        else:
            print(func(md, df, df2))
    except Exception as exc:
        print ("\n" + traceback.format_exc())
        print (color.RED + str(exc) + color.END + "\n") 
    return

md_no_func = (
    gr.Model()
        # >> gr.cp_vec_function( 
        #     fun=None,
        #     var=["x"],
        #     out=["y"],
        # )
    )

def perform_tests(func, 
    wrong_type=[None, (1,2), 2, "a", [1, 8], md_no_func], 
    df2_exists=False,
    md_corr=None, df_corr=None, df2_corr=None):
    r"""Performs test on a given function for the wrong_types
    for both the model and df arguments.
    
    func: grama function to test
    wrong_type: list of wrong values to test
    df2_exists: bool to indicate whether func takes two dataframe arguments

    md, df, df2: override default values. 'None' will use default."""

    ## Default Values
    if md_corr is None:
        md_corr = (
        gr.Model()
            >> gr.cp_vec_function( 
                fun=lambda df: gr.df_make(y=df.x),
                var=["x"],
                out=["y"],
            )
        )
    if df_corr is None:
        df_corr=gr.df_make(x=1)

    ## List of tests to perform
    tests=["md", "df", "corr"]
    if df2_exists:
        tests.insert(-1, "df2") # df2 test second to last
        if df2_corr is None:
            # assign value to df2_corr
            df2_corr=df_corr
        else:
            df2_corr=None
            # declare something for use in the below

    ## Tests
    for test in tests: # for each test
        for wrong in wrong_type: # test each wrong type
            ## Set Values
            if test == "md":
                md = wrong
                df = df_corr
                df2 = df2_corr
                print(color.UNDERLINE + "md value: " + str(wrong) + color.END)
            elif test == "df":
                md = md_corr
                df = wrong
                df2 = df2_corr
                print(color.UNDERLINE + "df value: " + str(wrong) + color.END)
            elif test == "df2":
                md = md_corr
                df = df_corr
                df2 = wrong
                print(color.UNDERLINE + "df value: " + str(wrong) + color.END)
            elif test =="corr":
                md = md_corr
                df = df_corr
                df2 = df2_corr
                print(color.UNDERLINE + "Correct Test" + color.END)
            ## Test
            one_test(func, md, df, df2)

print(perform_tests(gr.eval_df))
# print(gr.eval_df(md, df)) # TESTED
# print(gr.eval_nominal(md, df))
# print(gr.eval_pnd(md, ))
# print(gr.eval_grad_fd(md, df_base=df))
# print(gr.eval_conservative(md, df_det=df))
# print(gr.eval_sample(md, n=30, df_det=df))

# def df_inv_test():



# def eval_inv_test(tests=["model", "dataframe", "corr"])
# for test in ["model", "dataframe", "corr"]:

#     # Announce type of test:
#     if test == "model":
#         print(color.BOLD + "\nTesting for Wrong Model Type\n" + color.END)
#     elif test == "dataframe":
#         print(color.BOLD + "\nTesting for Wrong DataFrame Type\n" + color.END)
    
#     # Perform tests:
#     for i in range(len(wrong_type)): # for each wrong type
#         wrong = wrong_type[i]
#         if test == "model":
#             md = wrong
#             print(color.UNDERLINE + "md value: " + str(wrong) + color.END)
#             df = df_corr
#         elif test == "dataframe":
#             md = md_corr
#             df = wrong
#             print(color.UNDERLINE + "df value: " + str(wrong) + color.END)
#         elif test =="corr":
#             md = md_corr
#             df = df_corr
#             print(color.UNDERLINE + "Correct Test" + color.END)
#         try:
#             # print(gr.eval_df(md, df)) # TESTED
#             # print(gr.eval_nominal(md, df))
#             print(gr.eval_pnd(md, ))
#             # print(gr.eval_grad_fd(md, df_base=df))
#             # print(gr.eval_conservative(md, df_det=df))
#             # print(gr.eval_sample(md, n=30, df_det=df))
#         except Exception as exc:
#             print ("\n" + traceback.format_exc())
#             print (color.RED + str(exc) + color.END + "\n")

# ):

# def eval_inv_test_pnd(

# ):
# # general case:



# # eval_pnd:
# df_train = (
#     df_data
#     >> gr.tf_sample(n=10)
# )
# ## select test set
# df_test = (
#     df_data
#         >> gr.tf_anti_join(
#             df_train,
#             by=["x1", "x2"],
#         )
#         >> gr.tf_sample(n=200)
# )