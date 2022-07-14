# ctrl + alt + n to test within vscode

import grama as gr

DF = gr.Intention()

## Model "tuple trap"
md = (
    gr.Model()
    >> gr.cp_vec_function( 
        fun=lambda df: gr.df_make(y=df.x),
        var=["x"],
        out=["y"],
    ) # BAD COMMA
)
print(md) 
print(type(md) is tuple)
# if type(md) is tuple:
#     raise ValueError("Given model argument is type tuple. Please check to make sure your model is declared correctly. Have you declared your model with an extra comma after the closing `)`?")
gr.eval_df(md, "eoe")
# gr.eval_df()


## Helper functions
# # --------------------------------------------------
# def invariant_checks():
#     r"""Helper function to group common invariant checks for eval functions"""
#     if type(model) is tuple:
#         raise ValueError("Given model argument is type tuple")
#         ## UPDATE THIS ERROR MSG