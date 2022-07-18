import grama as gr
from numpy import array, pi
from eval_invariants import color
import traceback    
def make_pareto_random(twoDim = True):
    """ Create a model of random points for a pareto frontier evaluation
    Args:
        twoDim (bool): determines whether to create a 2D or 3D model
    """
    if twoDim == True:
        # Model to make dataset
        md_true = (
            gr.Model()
            >> gr.cp_vec_function(
                fun=lambda df: gr.df_make(
                    y1=df.x1 * gr.cos(df.x2),
                    y2=df.x1 * gr.sin(df.x2),
                ),
                var=["x1", "x2"],
                out=["y1", "y2"],
            )
            >> gr.cp_marginals(
                x1=dict(dist="uniform", loc=0, scale=1),
                x2=dict(dist="uniform", loc=0, scale=pi/2),
            )
            >> gr.cp_copula_independence()
        )

        return md_true
    else:
        # Model to make dataset
        md_true = (
            gr.Model()
            >> gr.cp_vec_function(
                fun=lambda df: gr.df_make(
                    y1=df.x1 * gr.cos(df.x2),
                    y2=df.x1 * gr.sin(df.x2),
                    y3=df.x1 * gr.tan(df.x2),
                ),
                var=["x1", "x2","x3"],
                out=["y1", "y2","y3"],
            )
            >> gr.cp_marginals(
                x1=dict(dist="uniform", loc=0, scale=1),
                x2=dict(dist="uniform", loc=0, scale=pi/2),
                x3=dict(dist="uniform", loc=0, scale=pi/4)
            )
            >> gr.cp_copula_independence()
        )

        return md_true

md_true = make_pareto_random()
# Create dataframe
df_data = (
    md_true
    >> gr.ev_sample(n=2e3, seed=101, df_det="nom")
)
## Select training set
df_train = (
    df_data
    >> gr.tf_sample(n=10)
)
## select test set
df_test = (
    df_data
        >> gr.tf_anti_join(
            df_train,
            by=["x1", "x2"],
        )
        >> gr.tf_sample(n=200)
)

# Create fitted model
md_fit = (
    df_train
    >> gr.ft_gp(
        var=["x1", "x2"],
        out=["y1", "y2"],
    )
)

# Call eval_pnd
md_no_func = (
    gr.Model()
)
wrong_type=[None, (1,2), 2, "a", [1, 8], md_no_func]
for wrong in wrong_type:
    df_test = wrong
    try:
        df_pnd = (
            gr.eval_pnd(
                md_fit,
                df_train,
                df_test,
                signs = {"y1":1, "y2":1},
                seed = 101
            )
    )
    except Exception as exc:
        print ("\n" + traceback.format_exc())
        print (color.RED + str(exc) + color.END + "\n") 
    #         print(color.UNDERLINE + "value: " + str(wrong) + color.END)
    # print(df_pnd)