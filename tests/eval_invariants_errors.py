import grama as gr
import numpy as np

domain_2d = gr.Domain(bounds={"x": [-1.0, +1], "y": [0.0, 1.0]})
marginals = {}
marginals["x"] = gr.MarginalNamed(
    d_name="uniform", d_param={"loc": -1, "scale": 2}
)
marginals["y"] = gr.MarginalNamed(
    sign=-1, d_name="uniform", d_param={"loc": 0, "scale": 1}
)
model_2d = gr.Model(
    functions=[
        gr.Function(
            lambda x: [x[0], x[1]], ["x0", "x1"], ["y0", "y1"], "test", 0
        ),
    ],
    domain=domain_2d,
    density=gr.Density(marginals=marginals),
)
gr.eval_nominal(model_2d, skip=True),