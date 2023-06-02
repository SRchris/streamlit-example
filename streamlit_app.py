import streamlit as st
import requests
import pandas as pd

def get_data():
    url = "https://api.rated.network/v0/eth/operators?window=1d&idType=entity&size=1000"
    headers = {
      'Authorization': 'Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJzY29wZXMiOltdLCJpZCI6IjIxNmUwOGZiZjFhNjRkMWU5NzFjY2M0NzM1ZmUxMmJjIiwic3ViIjoiMDViYmFmYTJmZGRhNGE0MjgwNjVmMWFkNWNhZGVhZjEiLCJleHAiOjE3MTAwNTc0NDh9.gKqSVY5yM17G2i0Zgbj2KGODe2suVZqFQjXuvqzmplThNBA-EL7KVOfp8LvZbwWoOkDpKdHgYtclibQz1z9IMA'
    }
    response = requests.request("GET", url, headers=headers)
    data = response.json()
    return data

def create_dataframe(data):
    lst_name = []
    validator_count = []
    rating = []
    for item in data['data']:
        lst_name.append(item['id'])
        validator_count.append(item['validatorCount'])
        rating.append(item['avgValidatorEffectiveness'])
    df = pd.DataFrame({
        'LST name': lst_name,
        'Validator Count': validator_count,
        'Rating': rating
    })
    return df

data = get_data()
df = create_dataframe(data)

st.title('LST Table')
st.dataframe(df)
