from re import A
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
    """Set correct values to test for testing provided."""
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

def test_suite(func, 
    wrong_type=[None, (1,2), 2, "a", [1, 8], gr.Model()], 
    df2_exists=False,
    md_corr=None, df_corr=None, df2_corr=None,
    mode="default",
    **kwargs):
    r"""Performs test on a given function for the wrong_types
    for both the model and df arguments.
    
    func: grama function to test
    wrong_type: list of wrong values to test
    df2_exists: bool to indicate whether func takes two dataframe arguments

    md, df, df2: override default values. 'None' will use default.
    mode: Specific function test? e.g. "default" for anything with model
        and df arguments in order and implicit."""
   
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
            test_func(func, md, df, df2, mode, kwargs = kwargs)

def test_func(func, md, df, df2, mode, **kwargs):
    r"""Performs one test of a function

    func: grama function to test
    md: Model variable
    df: Df variable
    df2: df variable if function takes df arguments
    """
    try:
        if mode == "default":
            if df2 is None:
                # not a test with df2
                print(func(md, df, kwargs))
            else:
                print(func(md, df, df2))
        elif mode == "keyword df_det":
            print(func(md, df_det=df))
        elif mode == "eval_grad_fd":
            print(func(md, df_base=df))
        elif mode == "eval_sample":
            print(func(md, df_det=df, n=5))
        elif mode == "eval_contour":
            print(func(md, df=df))
        # eval_opt
        elif mode == "eval_nls":
            print(func(md, df_data=df, df_init=df2))
        elif mode == "eval_min":
            print(func(md, df_start=df))
        elif mode == "eval_pnd":
            print(func(md, df, df2, signs = {"y1":1, "y2":1}, seed = 101))
        elif mode == "eval_sinews":
            print(func(md, df_det=df))
        elif mode == "eval_tail":
            print(func(md, df_corr=df, df_det=df2))
    except Exception as exc:
        print ("\n" + traceback.format_exc())
        print (color.RED + str(exc) + color.END + "\n") 
    return

if __name__ == "__main__":
    ## eval_defaults.py:
    # test_suite(gr.eval_df)
    # test_suite(gr.eval_nominal)
    # test_suite(gr.eval_grad_fd, mode="eval_grad_fd")
    # test_suite(gr.eval_conservative, mode="keyword df_det")
    # test_suite(gr.eval_sample, mode="eval_sample")
    ## eval_contour.py
    # test_suite(gr.eval_contour, mode="eval_contour")
    ## eval_opt.py
    # test_suite(gr.eval_nls, mode="eval_nls", df2_exists=True)
    # test_suite(gr.eval_min, mode="eval_min")
    ## eval_pnd.py
    # test_suite(gr.eval_pnd, df2_exists=True, mode="eval_pnd")
    ## eval_random.py
    # test_suite(gr.eval_sinews, mode="eval_sinews")
    # test_suite(gr.eval_hybrid, mode="keyword df_det")
    ## eval_tail.py
    # test_suite(gr.eval_form_pma, mode="eval_form_pma", df2_exists=True)
    test_suite(gr.eval_form_ria, mode="eval_tail", df2_exists=True)A