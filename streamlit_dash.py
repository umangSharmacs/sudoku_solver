import streamlit as st
import pandas as pd
import numpy as np
import time

from validation import validate
from helper import helper

grid = [[[0] for i in range(9)] for j in range(9)]

grid = pd.DataFrame( {
    i:[0]*9 for i in range(9)
} )

user_grid = st.data_editor(grid)

if st.button('Submit and Validate'):
    user_grid = np.array(user_grid)
    validation = validate.validate(user_grid)
    
    helper.progress_bar("Validating...")
    validation.validate_rows()
    # helper.progress_bar("Validating Columns")
    validation.validate_cols()
    # helper.progress_bar("Validating Blocks")
    validation.validate_blocks()

    df = pd.DataFrame(user_grid)
    style = {'color': 'red'}
    # Errors
    errors = validation.get_errors()
    styler = df.style

    for error in errors:
        styler.set_properties(**style, subset=(df.index[error[0]], df.columns[error[1]]))

    if errors:
        st.write("Please try again.")
    else:
        st.write("All Good!")

    st.dataframe(styler)
        
user_grid = np.array(user_grid)




         
# Run Solver 
    
