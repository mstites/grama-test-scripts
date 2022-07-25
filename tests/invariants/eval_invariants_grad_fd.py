import grama as gr

## Define a ground-truth model
md_true = gr.make_pareto_random()
df_data = (
    md_true
    >> gr.ev_sample(n=2e3, seed=101, df_det="nom")
)
## Generate test/train data
df_train = (
    df_data
    >> gr.tf_sample(n=10)
)

df_test = (
    df_data
    >> gr.anti_join(
        df_train,
        by = ["x1","x2"]
    )
    >> gr.tf_sample(n=200)
)
## Fit a model to training data
md_fit = (
    df_train
    >> gr.ft_gp(
        var=["x1","x2"],
        out=["y1","y2"]
    )
)
## Rank training points by PND algorithm
df_pnd = (
    md_fit
    >> gr.ev_pnd(
        df_train,
        df_test,
        signs = {"y1":1, "y2":1},
        seed = 101
    )
    >> gr.tf_arrange(gr.desc(DF.pr_scores))
)