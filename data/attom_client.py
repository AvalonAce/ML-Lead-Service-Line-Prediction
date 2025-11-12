import requests
import pandas as pd
import os
from dotenv import load_dotenv
import time

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))
ATTOM_API_KEY = os.getenv('ATTOM_API_KEY')

df = pd.read_csv(os.path.join(os.path.join(os.path.dirname(__file__), 'processed'), 'NY_SLI_YEARS_ADJUSTED_NO_UNKNOWNS.csv'))

CALL_LIMIT = 1000

def get_attom_property_basicprofile(address1, address2):
    url = f"https://api.gateway.attomdata.com/propertyapi/v1.0.0/property/basicprofile?address1={address1}&address2={address2}"
    headers = {
        "apikey": ATTOM_API_KEY
    }
    response = None
    try:
        response = requests.get(url, headers=headers, timeout=5)
    except requests.exceptions.RequestException as e:
        print(f"request failed {e}")
        return False, None
    
    if response.status_code == 200:
        data = response.json()
        status = data.get('status', {})
        if status.get('msg') == 'SuccessWithResult':
            return True, data
        else:
            return False, data
    else:
        return False, response.json()
def getAttomID(json):
    # attomID is first entry in property list since we are calling this for individual houses
    try:
        property_list = json.get('property', [])
        if isinstance(property_list, list) and property_list:
            identifier = property_list[0].get('identifier', {})
            attom_id = identifier.get('attomId')
            if attom_id is not None:
                return int(attom_id)
    except Exception:
        pass
    return None
def getLotSize2(json):
    try:
        property_list = json.get('property', [])
        if isinstance(property_list, list) and property_list:
            lot = property_list[0].get('lot', {})
            lot_size2 = lot.get('lotSize2')
            if lot_size2 is not None:
                return float(lot_size2)
    except Exception:
        pass
    return None
def getPropClass(json):
    try:
        property_list = json.get('property', [])
        if isinstance(property_list, list) and property_list:
            summary = property_list[0].get('summary', {})
            prop_class = summary.get('propClass')
            if prop_class is not None:
                return prop_class
    except Exception:
        pass
    return None
def getYearBuilt(json):
    try:
        property_list = json.get('property', [])
        if isinstance(property_list, list) and property_list:
            summary = property_list[0].get('summary', {})
            year_built = summary.get('yearBuilt')
            if year_built is not None:
                return int(year_built)
    except Exception:
        pass
    return None
def getLivingSize(json):
    try:
        property_list = json.get('property', [])
        if isinstance(property_list, list) and property_list:
            building = property_list[0].get('building', {})
            size = building.get('size', {})
            living_size = size.get('livingSize')
            if living_size is not None:
                return float(living_size)
    except Exception:
        pass
    return None
def getSizeInd(json):
    try:
        property_list = json.get('property', [])
        if isinstance(property_list, list) and property_list:
            building = property_list[0].get('building', {})
            size = building.get('size', {})
            size_ind = size.get('sizeInd')
            if size_ind is not None:
                return size_ind
    except Exception:
        pass
    return None
def getBeds(json):
    try:
        property_list = json.get('property', [])
        if isinstance(property_list, list) and property_list:
            building = property_list[0].get('building', {})
            rooms = building.get('rooms', {})
            beds = rooms.get('beds')
            if beds is not None:
                return int(beds)
    except Exception:
        pass
    return None
def getConstructionQuality(json):
    try:
        property_list = json.get('property', [])
        if isinstance(property_list, list) and property_list:
            building = property_list[0].get('building', {})
            construction = building.get('construction', {})
            quality = construction.get('condition')
            if beds is not None:
                return quality
    except Exception:
        pass
    return None
def getBathsTotal(json):
    try:
        property_list = json.get('property', [])
        if isinstance(property_list, list) and property_list:
            building = property_list[0].get('building', {})
            rooms = building.get('rooms', {})
            baths_total = rooms.get('bathsTotal')
            if baths_total is not None:
                return float(baths_total)
    except Exception:
        pass
    return None
def getLevels(json):
    try:
        property_list = json.get('property', [])
        if isinstance(property_list, list) and property_list:
            building = property_list[0].get('building', {})
            summary = building.get('summary', {})
            levels = summary.get('levels')
            if levels is not None:
                return int(levels)
    except Exception:
        pass
    return None
def getMarketTotalValue(json):
    try:
        property_list = json.get('property', [])
        if isinstance(property_list, list) and property_list:
            assessment = property_list[0].get('assessment', {})
            market = assessment.get('market', {})
            mkt_ttl_value = market.get('mktTtlValue')
            if mkt_ttl_value is not None:
                return float(mkt_ttl_value)
    except Exception:
        pass
    return None
def get_sample_split(df, n_samples=20):
    df = df[df['Service Line Locality'] != 'Pelham Manor'] #only lead here lol

    lead_df = df[df['SL Category Cleaned'] == 'Lead']
    nonlead_df = df[df['SL Category Cleaned'] != 'Lead']

    lead_locality_counts = lead_df['Service Line Locality'].value_counts()
    nonlead_locality_counts = nonlead_df['Service Line Locality'].value_counts()

    lead_df = lead_df.set_index('Service Line Locality').loc[lead_locality_counts.index].reset_index()
    nonlead_df = nonlead_df.set_index('Service Line Locality').loc[nonlead_locality_counts.index].reset_index()

    print(lead_locality_counts)
    print(nonlead_locality_counts)

    lead_sample = (
        lead_df.groupby('Service Line Locality')
        .apply(lambda x:  x.sample(n = n_samples) if (x.shape[0]>n_samples - 1) else x)
        .reset_index(drop=True)
        .set_index('Service Line Locality')
        .loc[lead_locality_counts.index]
        .reset_index()
    )
    nonlead_sample = (
        nonlead_df.groupby('Service Line Locality')
        .apply(lambda x:  x.sample(n = n_samples) if (x.shape[0]>n_samples - 1) else x)
        .reset_index(drop=True)
        .set_index('Service Line Locality')
        .loc[lead_locality_counts.index]
        .reset_index()
    )
    return lead_sample, nonlead_sample
def interleave(a, b):
    concat_df = pd.concat([a,b]).sort_index().reset_index(drop=True)
    return concat_df



i = 0


df.loc[df['Service Line Locality'] == "BX", 'Service Line Locality'] = "Bronx"
df.loc[df['Service Line Locality'] == "SI", 'Service Line Locality'] = "Staten Island"
df.loc[df['Service Line Locality'] == "BK", 'Service Line Locality'] = "Brooklyn"
df.loc[df['Service Line Locality'] == "QN", 'Service Line Locality'] = "Queens"
df.loc[df['Service Line Locality'] == "MN", 'Service Line Locality'] = "Manhattan"

manhattan_count = df[df['Service Line Locality'] == "Manhattan"].shape[0]
print(f"Number of rows in Manhattan: {manhattan_count}")

# df = df.sample(frac=1, random_state=42).reset_index(drop=True)

start_time = time.time()

# save the raw jsons just in case we want more later
home_jsons = []

lead_sample, nonlead_sample = get_sample_split(df, n_samples=20)

interleaved_samples = interleave(lead_sample, nonlead_sample)


for index, row in interleaved_samples.iterrows():
    if index > CALL_LIMIT:
        break
    try:
        print(row['Street Address'] + ' ' + row['Service Line Locality'] + ', ' + row['State'])
        success, json = get_attom_property_basicprofile(
            address1=row['Street Address'],
            address2=row['Service Line Locality'] + ', ' + row['State']
        )
        if not success:
            continue
        # attom id is how they index their own DB I think. This is more valuable than st. add
        attomID = getAttomID(json)
        if attomID is None:
            print("-------- could not find any thing!!! ---------")
            continue
        
        lot_size2 = getLotSize2(json)
        prop_class = getPropClass(json)
        year_built = getYearBuilt(json)
        living_size = getLivingSize(json)
        size_ind = getSizeInd(json)
        beds = getBeds(json)
        baths_total = getBathsTotal(json)
        levels = getLevels(json)
        market_total_value = getMarketTotalValue(json)
        construction_quality = getConstructionQuality(json)
        print(f"attomID: {attomID}")
        print(f"lot_size2: {lot_size2}")
        print(f"prop_class: {prop_class}")
        print(f"year_built: {year_built}")
        print(f"living_size: {living_size}")
        print(f"size_ind: {size_ind}")
        print(f"beds: {beds}")
        print(f"baths_total: {baths_total}")
        print(f"levels: {levels}")
        print(f"market_total_value: {market_total_value}")

        if beds == "None" or beds is None:
            beds = 0.0
        if baths_total == "None" or baths_total is None:
            baths_total = 0.0

        interleaved_samples.at[index, 'attomID'] = attomID
        interleaved_samples.at[index, 'lot_size2'] = lot_size2
        interleaved_samples.at[index, 'prop_class'] = prop_class
        interleaved_samples.at[index, 'year_built'] = year_built
        interleaved_samples.at[index, 'living_size'] = living_size
        interleaved_samples.at[index, 'size_ind'] = size_ind
        interleaved_samples.at[index, 'beds'] = beds
        interleaved_samples.at[index, 'baths_total'] = baths_total
        interleaved_samples.at[index, 'levels'] = levels
        interleaved_samples.at[index, 'market_total_value'] = market_total_value
        interleaved_samples.at[index, 'construction_condition'] = construction_quality

        home_jsons.append(json)
    except KeyboardInterrupt:
        print("Keyboard interrupt detected. Breaking out of loop.")
        break



end_time = time.time()
print(f"Loop took {end_time - start_time:.2f} seconds")

print(f"Row count: {len(interleaved_samples)}")
interleaved_samples = interleaved_samples.dropna(subset=['attomID'])

import json as pyjson
with open(os.path.join(os.path.dirname(__file__), 'raw/home_jsons.json'), 'w') as f:
    pyjson.dump(home_jsons, f, indent=2)

json_df = pd.DataFrame(home_jsons)
json_df.to_csv(os.path.join(os.path.dirname(__file__), 'raw/attom_scraped.csv'), index=False)

interleaved_samples.to_csv(os.path.join(os.path.dirname(__file__), 'processed/NY_SLI_ATTOM_NEW.csv'), index=False)

