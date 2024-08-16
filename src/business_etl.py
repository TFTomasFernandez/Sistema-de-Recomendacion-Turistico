from google.cloud import storage
from google.cloud import bigquery
import pandas as pd
from datetime import datetime
import io

# Reemplazamos ciudades que esten mal escritas
city_mapping = {
      'Indianpolis': 'Indianapolis',
      'INDIANAPOLIS': 'Indianapolis',
      'Indianapolis ': 'Indianapolis',
      'indianapolis': 'Indianapolis',
      "indianopolis": 'Indianapolis',
      'NEW ORLEANS': 'New Orleans',
      'New Orleans': 'New Orleans',
      'new orleans': 'New Orleans',
      'new orleans': 'New Orleans',
      'New orleans': 'New Orleans',
      'Metairie': 'Metairie',
      'metairie': 'Metairie',
      'Metarie': 'Metairie',
      'Meterie': 'Metairie',
      'Metarie ': 'Metairie',
      'St. Rose': 'Saint Rose',
      'St.Rose': 'Saint Rose',
      'Saint Rose': 'Saint Rose',
      'St Rose': 'Saint Rose',
      'Mc Cordsville': 'McCordsville',
      'Mccordsville': 'McCordsville',
      'lawrence': 'Lawrence',
      'Lawrence Township': 'Lawrence',
      'Jefferson Parish': 'Jefferson',
      'Belle Chasse': 'Belle Chasse',
      'Belle Chase': 'Belle Chasse',
      'French Quarter': 'New Orleans',
      'French Quarter - CBD': 'New Orleans',
      'Downtown': 'Indianapolis',
      'Downtown Indianapolis': 'Indianapolis',
      'INpolis': 'Indianapolis',
      'New Orlaens': 'New Orleans',
      'elmwood': 'Elmwood',
      'Zionsville In': 'Zionsville',
      'Indianapolis,': 'Indianapolis',
      'NEW ORLEANS AP': 'New Orleans',
      'Indianapolis city (balance)': 'Indianapolis',
      'Plainfiled': 'Plainfield',
      'Chalemette': 'Chalmette',
      'AVON': 'Avon'
  }
# Definimos los codigos postales en los que nos basaremos para designar los estados
postal_codes = {
    'Alabama': [('31905', '31905'), ('35001', '36999'), ('38852', '38852')],
    'Alaska': [('98791', '98791'), ('99501', '99999')],
    'Arizona': [('84531', '84531'), ('84536', '84536'), ('85001', '86599'), ('86631', '86631'), ('87328', '87328'), ('89024', '89024')],
    'Arkansas': [('38041', '38041'), ('38063', '38063'), ('38769', '38769'), ('65729', '65729'), ('65733', '65733'), ('65761', '65761'), ('71601', '72999'), ('75502', '75502'), ('75556', '75556'), ('78081', '78081')],
    'California': [('89010', '89010'), ('89019', '89019'), ('89060', '89060'), ('89439', '89439'), ('90001', '96199'), ('96222', '96222'), ('97635', '97635')],
    'Colorado': [('80000', '81699'), ('82063', '82063')],
    'Connecticut': [('06001', '06999')],
    'Delaware': [('19700', '19999')],
    'District of Columbia': [('20001', '20599'), ('56901', '56999')],
    'Florida': [('32001', '34999')],
    'Georgia': [('30001', '31999'), ('32350', '32350'), ('39801', '39899'), ('39901', '39901')],
    'Hawaii': [('96371', '96371'), ('96373', '96373'), ('96385', '96385'), ('96477', '96477'), ('96701', '96899')],
    'Idaho': [('59847', '59847'), ('83111', '83111'), ('83120', '83120'), ('83201', '83899'), ('89832', '89832'), ('97910', '97913'), ('99128', '99128')],
    'Illinois': [('52761', '52761'), ('60001', '62999'), ('63673', '63673')],
    'Indiana': [('46001', '47999')],
    'Iowa': [('50001', '52899'), ('55954', '55954'), ('56027', '56027'), ('56129', '56129'), ('68119', '68120')],
    'Kansas': [('66001', '67999'), ('68325', '68325'), ('68978', '68978')],
    'Kentucky': [('38079', '38079'), ('40001', '42799')],
    'Louisiana': [('70000', '71499'), ('71545', '71545'), ('71749', '71749')],
    'Maine': [('03901', '04999')],
    'Maryland': [('20331', '20331'), ('20588', '20588'), ('20601', '21999')],
    'Massachusetts': [('01001', '02799'), ('5501', '5501'), ('5544', '5544')],
    'Michigan': [('48001', '49999'), ('54554', '54554')],
    'Minnesota': [('51360', '51360'), ('55001', '56799'), ('57026', '57026'), ('57030', '57030'), ('57068', '57068'), ('58225', '58225')],
    'Mississippi': [('38160', '38160'), ('38514', '38514'), ('38597', '38597'), ('38601', '39799'), ('71233', '71233')],
    'Missouri': [('51630', '51630'), ('51640', '51640'), ('52542', '52542'), ('52573', '52573'), ('52626', '52626'), ('63001', '65899'), ('72644', '72644')],
    'Montana': [('57724', '57724'), ('59000', '59999'), ('82801', '82801')],
    'Nebraska': [('51557', '51557'), ('57078', '57078'), ('66541', '66541'), ('68001', '69399'), ('80758', '80758'), ('82082', '82082')],
    'Nevada': [('84034', '84034'), ('88901', '89999')],
    'New Hampshire': [('00210', '00215'), ('03001', '03899')],
    'New Jersey': [('07001', '08999'), ('10004', '10004')],
    'New Mexico': [('79837', '79837'), ('79922', '79922'), ('81137', '81137'), ('86504', '86504'), ('86515', '86515'), ('87001', '88499'), ('88603', '88603')],
    'New York': [('501', '501'), ('544', '544'), ('6390', '6390'), ('10001', '14999')],
    'North Carolina': [('27001', '28999')],
    'North Dakota': [('56701', '56799'), ('57638', '57638'), ('57641', '57642'), ('57645', '57645'), ('57648', '57648'), ('57660', '57660'), ('57683', '57683'), ('58000', '58899'), ('58982', '58982'), ('59221', '59221'), ('59270', '59270'), ('59275', '59275')],
    'Ohio': [('43001', '45999')],
    'Oklahoma': [('67950', '67950'), ('73001', '73199'), ('73367', '73367'), ('73371', '73371'), ('73401', '74999'), ('76356', '76356'), ('79051', '79051')],
    'Oregon': [('89421', '89421'), ('97001', '97999'), ('99362', '99362')],
    'Pennsylvania': [('15001', '19699'), ('19815', '19815'), ('19853', '19853'), ('19925', '19925')],
    'Rhode Island': [('2029', '2029'), ('2789', '2789'), ('02801', '02999')],
    'South Carolina': [('29001', '29999')],
    'South Dakota': [('51001', '51001'), ('51023', '51023'), ('56144', '56144'), ('56164', '56164'), ('56219', '56219'), ('57001', '57799'), ('57840', '57841'), ('57949', '57949'), ('58234', '58234'), ('58439', '58439'), ('58623', '58623'), ('58649', '58649'), ('58653', '58653'), ('68719', '68719'), ('69201', '69201'), ('69212', '69212'), ('69216', '69216'), ('82701', '82701')],
    'Tennessee': [('31788', '31788'), ('37001', '38599'), ('42223', '42223'), ('72338', '72338')],
    'Texas': [('73301', '73301'), ('73344', '73344'), ('73949', '73949'), ('73960', '73960'), ('75001', '79999'), ('88501', '88599')],
    'Utah': [('81324', '81324'), ('82930', '82930'), ('83312', '83312'), ('83342', '83342'), ('84001', '84799'), ('86044', '86044'), ('86514', '86514')],
    'Vermont': [('05001', '05499'), ('05601', '05999')],
    'Virginia': [('20101', '20199'), ('20598', '20598'), ('22001', '24699')],
    'Washington': [('98001', '99499'), ('99536', '99536')],
    'West Virginia': [('24604', '24604'), ('24701', '26899'), ('26905', '26905')],
    'Wisconsin': [('52820', '52820'), ('53001', '54999')],
    'Wyoming': [('57717', '57717'), ('82001', '83199'), ('83414', '83414')]
}

def assign_state(df, postal_codes):
    """
    Asigna el estado en el DataFrame basándose en el código postal.
    
    df (pd.DataFrame): DataFrame con una columna 'postal_code'.
    postal_codes (dict): Diccionario que mapea estados a rangos de códigos postales.
    
    Returns:
    pd.DataFrame: DataFrame con una nueva columna 'state' que indica el estado correspondiente.
    """
    def find_state(postal_code):
        for state, ranges in postal_codes.items():
            for start, end in ranges:
                if int(start) <= int(postal_code) <= int(end):
                    return state
        return 'Unknown'
    
    df['state'] = df['postal_code'].apply(find_state)
    
    return df


def upload_business_to_big_query():
    month = datetime.now().strftime("%B").lower()
    platforms = ["yelp","google"]
    business_month : pd.DataFrame = ""
    for platform in platforms:
        
        try:
            if(platform == "yelp"):
                print("ATRIBUTOS")
                business_month = pd.read_pickle(f"/home/airflow/gcs/dags/{platform}/business_{month}.pkl")
                business_month= business_month.iloc[:,0:14]
                business_month['postal_code'] = pd.to_numeric(business_month['postal_code'], errors='coerce')
                business_month.drop(columns=["hours","attributes","postal_code","is_open"],inplace=True)
                business_month = business_month.dropna(subset=['postal_code'])
                business_month["city"] = business_month["city"].replace(city_mapping)
                business_month = assign_state(business_month, postal_codes)



            else: 
                business_month =  pd.read_json(f"/home/airflow/gcs/dags/{platform}/business_{month}.json")
                business_month.drop(columns=["description","hours","state","price","MISC","relative_results","url"],inplace=True)
                business_month = business_month[~business_month["gmap_id"].duplicated()]
        
        


            buffer = io.BytesIO()
            # Write the DataFrame to the buffer as Parquet
            business_month.to_parquet(buffer, engine='pyarrow')
            # Load data from Cloud Storage to BigQuery
            client = bigquery.Client()
            job_config = bigquery.job.LoadJobConfig()
            job_config.create_disposition = "CREATE_IF_NEEDED"
            job_config.write_disposition = bigquery.WriteDisposition.WRITE_APPEND 
            table = f"{platform}.business"
            job = client.load_table_from_dataframe(business_month,table,job_config=job_config)

        except:
            print("Data Not Available")

upload_business_to_big_query()


def upload_reviews_to_big_query():
    try:
        month = datetime.now().strftime("%B").lower()
        # Leer archivo reviews
        reviews = pd.read_json(f"/home/airflow/gcs/dags/yelp/{month}.json")
        reviews.drop(columns=["useful","funny","cool"],inplace=True)
        reviews["date"] = reviews["date"].astype("date64[pyarrow]")
        buffer = io.BytesIO()
        # Write the DataFrame to the buffer as Parquet
        reviews.to_parquet(buffer, engine='pyarrow')
        # Load data from Cloud Storage to BigQuery
        client = bigquery.Client()
        job_config = bigquery.job.LoadJobConfig()
        job_config.create_disposition = "CREATE_IF_NEEDED"
        job_config.write_disposition = bigquery.WriteDisposition.WRITE_APPEND 
        table = "yelp.reviews"
        job = client.load_table_from_dataframe(reviews,table,job_config=job_config)
    except:
        print("No data")

upload_reviews_to_big_query()