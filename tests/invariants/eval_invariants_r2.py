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

def set_corr_vars(md_corr, df_corr, df2_exists, df2_corr):
    """Set correct values to test, if none provided."""
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

    if df2_exists and df2_corr is None:
        df2_corr=df_corr

    return md_corr, df_corr, df2_corr

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

def perform_tests(func, 
    wrong_type=[None, (1,2), 2, "a", [1, 8], gr.Model()], 
    df2_exists=False,
    md_corr=None, df_corr=None, df2_corr=None):
    r"""Performs test on a given function for the wrong_types
    for both the model and df arguments.
    
    func: grama function to test
    wrong_type: list of wrong values to test
    df2_exists: bool to indicate whether func takes two dataframe arguments

    md, df, df2: override default values. 'None' will use default."""
   
    md_corr, df_corr, df2_corr = set_corr_vars(md_corr, df_corr, df2_exists, df2_corr)

    tests=["md", "df", "corr"]
    if df2_exists:
        # add df2 test
        tests.insert(-1, "df2")

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


if __name__ == "__main__":
    perform_tests(gr.eval_df)
    # perform_tests(gr.eval_pnd, df2_ex ists=True, df_corr=df_train, df2_corr=df_test)
    # print(gr.eval_df(md, df)) # TESTED
    # print(gr.eval_nominal(md, df))
    # print(gr.eval_pnd(md, ))
    # print(gr.eval_grad_fd)
    # print(gr.eval_conservative(md, df_det=df))
    # print(gr.eval_sample(md, n=30, df_det=df))

