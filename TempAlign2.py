import pandas as pd
import numpy as np
import pyam

def test():
    print('Hi')

def WorldScenarios():
    conn = pyam.iiasa.Connection()
    dg = pyam.read_iiasa(
        'ngfs_2',
        model='GCAM*',
        variable=['Emissions|Kyoto Gases', 'Final Energy','Diagnostics|Temperature|Global Mean|MAGICC6|Expected value'],
        region='World',
        meta=['category']
    )
    return dg

def PlotScenarios(dg):
    ax = dg.filter(variable='Emissions|Kyoto Gases').plot(
        color='scenario',
        legend=dict(loc='center left', bbox_to_anchor=(1.0, 0.5))
    )
    return ax

def PlotScenarioTemperatures(dg):
    ax = dg.filter(variable='Diagnostics|Temperature|Global Mean|MAGICC6|Expected value').plot(
        color='scenario',
        legend=dict(loc='center left', bbox_to_anchor=(1.0, 0.5))
    )
    return ax

def ScenarioTemperatures(data,yr):
    dd = data.filter(variable='Diagnostics|Temperature|Global Mean|MAGICC6|Expected value')
    d2 = dd.timeseries()
    d2 = d2.reset_index()
    d2 = d2[['scenario', 2100]]
    return d2




def CarbonIntensities(yr,gl = False):
    JtoKwH = 277777777777.78
    TroGram = 1000000000000
    if(gl):
        rg = 'World'
    else:
        rg = '*'

    dat = pyam.read_iiasa(
        'ngfs_2',
        model='GCAM*',
        scenario='Below 2°C',
        variable=['Emissions|Kyoto Gases', 'Final Energy'],
        region= rg,
        meta=['category']
    )
    dgpd = dat.timeseries()
    A = ['region', 'variable', yr]
    dgpd = dgpd.reset_index()
    tmp = dgpd[A]
    tmp.columns = ['region', 'variable', 'Value']
    tmp2 = tmp.pivot_table('Value', 'region', 'variable')
    tmp2 = tmp2.reset_index()
    tmp2['ENinKWh'] = tmp2['Final Energy'] * JtoKwH
    tmp2['CO2inG'] = tmp2['Emissions|Kyoto Gases'] * TroGram
    tmp2['CIntensity'] = tmp2['CO2inG'] / tmp2['ENinKWh']
    return tmp2

def ScenarioTemperature(yr,gl = False):
    JtoKwH = 277777777777.78
    TroGram = 1000000000000
    if(gl):
        rg = 'World'
    else:
        rg = '*'

    dat = pyam.read_iiasa(
        'ngfs_2',
        model='GCAM*',
        scenario='Below 2°C',
        variable=['Emissions|Kyoto Gases', 'Final Energy'],
        region= rg,
        meta=['category']
    )
    dgpd = dat.timeseries()
    A = ['region', 'variable', yr]
    dgpd = dgpd.reset_index()
    tmp = dgpd[A]
    tmp.columns = ['region', 'variable', 'Value']
    tmp2 = tmp.pivot_table('Value', 'region', 'variable')
    tmp2 = tmp2.reset_index()
    tmp2['ENinKWh'] = tmp2['Final Energy'] * JtoKwH
    tmp2['CO2inG'] = tmp2['Emissions|Kyoto Gases'] * TroGram
    tmp2['CIntensity'] = tmp2['CO2inG'] / tmp2['ENinKWh']
    return tmp2

def GlobalCarbonIntensities(yr):
    JtoKwH = 277777777777.78
    TroGram = 1000000000000

    dat = pyam.read_iiasa(
        'ngfs_2',
        model='GCAM*',
        scenario='*',
        variable=['Emissions|Kyoto Gases', 'Final Energy'],
        region= 'World',
        meta=['category']
    )
    dgpd = dat.timeseries()
    A = ['scenario','region', 'variable', yr]
    dgpd = dgpd.reset_index()
    tmp = dgpd[A]
    tmp.columns = ['scenario','region', 'variable', 'Value']
    tmp2 = tmp.pivot_table('Value', 'scenario', 'variable')
    tmp2 = tmp2.reset_index()
    tmp2['ENinKWh'] = tmp2['Final Energy'] * JtoKwH
    tmp2['CO2inG'] = tmp2['Emissions|Kyoto Gases'] * TroGram
    tmp2['CIntensity'] = tmp2['CO2inG'] / tmp2['ENinKWh']
    return tmp2