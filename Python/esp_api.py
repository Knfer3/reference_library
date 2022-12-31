import requests
from decouple import config
import pandas as pd
import datetime


class ESP:
    '''Class: data from the Eskom se push API'''
    # url to determine region: 
    # url = "https://developer.sepush.co.za/business/2.0/areas_nearby?lat=-24.347600&lon=30.973200"
   
    #  API key - subscribe from ESP website
    esp_token = config('ESP_LICENSE_KEY')

    def get_shed_hours(self, ls_stage):
        '''retrieve the total Loadshedding hours for a specified (param)
             loadshedding stage, for the predetermined region'''

        #  API url - with static area (ID)
        url = "https://developer.sepush.co.za/business/2.0/area?id=eskdo-10-hoedspruitemakhazenimpumalanga&test=current"
        payload={}
        headers = {'token': self.esp_token}
        response = requests.request("GET", url, headers=headers, data=payload)

        json_data = response.json()['schedule']['days'][0]['stages'][ls_stage + 1]
        json_data_date = response.json()['schedule']['days'][0]['date']

        shed_duration = datetime.timedelta(
                days = 0,
                hours = 0,
                minutes = 0,
                )

        for shed in json_data:

            sTime = datetime.timedelta(
                days = int(json_data_date[8:10]),
                hours = int(shed[:2]),
                minutes = int(shed[3:5]),
                )
            eTime = datetime.timedelta(
                days = int(json_data_date[8:10]),
                hours = int(shed[6:8]),
                minutes = int(shed[9:]),
                )

            shed_duration += eTime-sTime

        print(f'At loadshedding stage {ls_stage}, total time shed is {shed_duration} hours')



if __name__ == '__main__':
    e1 = ESP()
    e1.get_shed_hours(4)
