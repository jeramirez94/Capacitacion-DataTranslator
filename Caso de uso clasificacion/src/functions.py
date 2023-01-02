#funcion para sustituir los nullos por la media
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import numpy as np
from datetime import date

class Cleaner:
    def __init__(self, cols_to_keep):
        self.cols_to_keep = cols_to_keep

    def fit(self, X_train):
        self.mode_phone = X_train.phone.mode()[0]
        self.mode_city=X_train.city.mode()[0]
        temp_df = X_train.copy()
        temp_df.phone = temp_df.phone.fillna(self.mode_phone)
        temp_df.city = temp_df.city.fillna(self.mode_city)
        self.enc_phone = OneHotEncoder(drop='first', sparse=False, handle_unknown='ignore')
        self.enc_phone.fit(temp_df[['phone']])
        self.enc_city=OneHotEncoder(drop='first', sparse=False, handle_unknown='ignore')
        self.enc_city.fit(temp_df[['city']])

        
    def transform(self, df_base):
        df = df_base[self.cols_to_keep].copy()
        df['last_trip_date']=pd.to_datetime(df['last_trip_date'])
        df['signup_date']=pd.to_datetime(df['signup_date'])
        df['avg_rating_of_driver'].fillna(df['avg_rating_of_driver'].mean(), inplace=True)
        df['avg_rating_by_driver'].fillna(df['avg_rating_by_driver'].mean(), inplace=True)
        df['luxury_car_user']=df["luxury_car_user"].astype(int)
        df['last_trip_date']= df['last_trip_date'].map(date.toordinal)
        df['signup_date']= df['signup_date'].map(date.toordinal)

        df.phone = df.phone.fillna(self.mode_phone)
        df.city= df.city.fillna(self.mode_city)
        temp_df = pd.DataFrame(self.enc_phone.transform(df[['phone']]), columns=self.enc_phone.get_feature_names_out())
        temp_df=pd.concat([temp_df,  pd.DataFrame(self.enc_city.transform(df[['city']]), columns=self.enc_city.get_feature_names_out())], axis=1)
        
        df = df.drop(['phone','city'], axis=1)
        return pd.concat([df, temp_df], axis=1)


    def get_target(self, df):
        boleanos = {False:0, True:1}
        df['target'] = df[['last_trip_date']]>= '2014-06-01'
        df['target']=df['target'].map(boleanos).values
        return df.target

        
    