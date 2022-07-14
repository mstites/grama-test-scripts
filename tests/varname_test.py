from varname import nameof
import grama as gr

df=gr.df_make(x=1)
df_det=gr.df_make(x=2)

def test(df1, df2):
    return nameof(df1)

print(test(df, df_det))
print(nameof(df))