import streamlit as st
from nsetools import Nse
import pandas as pd
from bsedata.bse import BSE


st.title('Market related stuff...')

nse = Nse()
bse = BSE()

selected_window = st.sidebar.selectbox('', ['Gainers', 'Losers', 'BSE'])

if selected_window == 'Gainers':
    st.dataframe(bse.topGainers())
elif selected_window == 'Losers':
    st.dataframe(bse.topLosers())
elif selected_window == 'BSE':
    code = st.number_input('Code:', )
    time = st.selectbox('Time:', ['1M', '3M', '6M', '12M'])
    history = bse.getPeriodTrend(str(int(code)),time)
    chart_data = pd.DataFrame(history)
    chart_data.drop('date', axis=1, inplace=True)
    st.line_chart(chart_data)
