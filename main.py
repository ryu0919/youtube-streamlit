import streamlit as st
import numpy as np
import pandas as pd

st.title('streamlit入門')

st.write('DataFrame')

df = pd.DataFrame({
    '１列目': [1, 2, 3, 4],
    '２列目': [10, 20, 30, 40],
})

st.table(df.style.highlight_max(axis=0))

"""
# 章
## 節
### コード

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""