import requests
import pandas as pd
import streamlit as st

def get_data():
    url = "https://api.rated.network/v0/eth/operators?window=1d&idType=entity&size=1000"
    headers = {
      'Authorization': 'Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJzY29wZXMiOltdLCJpZCI6IjIxNmUwOGZiZjFhNjRkMWU5NzFjY2M0NzM1ZmUxMmJjIiwic3ViIjoiMDViYmFmYTJmZGRhNGE0MjgwNjVmMWFkNWNhZGVhZjEiLCJleHAiOjE3MTAwNTc0NDh9.gKqSVY5yM17G2i0Zgbj2KGODe2suVZqFQjXuvqzmplThNBA-EL7KVOfp8LvZbwWoOkDpKdHgYtclibQz1z9IMA'
    }
    response = requests.request("GET", url, headers=headers)
    data = response.json()
    return data

def main():
    data = get_data()
    if isinstance(data, list) and isinstance(data[0], dict):  # check if data is list of dicts
        df = pd.DataFrame(data)
        df = df[['id', 'validatorCount', 'avgValidatorEffectiveness']]
        df.columns = ['LST Name', 'Validator Count', 'Rating']
        st.table(df)
    else:
        st.write("Data is not in the expected format.")


if __name__ == '__main__':
    main()
