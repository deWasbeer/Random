#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 14:53:37 2022

@author: windhoos
"""

import matplotlib.pyplot as plt

def berekening(panelenkWP):
    gas_kosten=2.15 #euro/m3
    stroom_kosten=0.6 #euro/kwh
    time=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec' ]
    WP=str(panelenkWP)+' kWp'
    
    gas_jaar_gem=1080*.8 #m3
    stroom_jaar_gem=3260*.8 #kwh
    
    gas_maand_frac=[0.24, 0.18, 0.10, 0.05, 0.03, 0.01, 0.0, 0.01, 0.03, 0.07, 0.11, 0.15]
    stroom_maand_frac=[]
    for i in range(12):
        stroom_maand_frac.append(1/12)
        
    gas_verbruik_traditioneel=[]
    for i in range(12):
        gas_verbruik_traditioneel.append(gas_maand_frac[i]*gas_jaar_gem)
        
    stroom_verbruik_traditioneel=[]
    for i in range(12):
        stroom_verbruik_traditioneel.append(stroom_maand_frac[i]*stroom_jaar_gem)
        
    gas_verbruik_persoonlijk=[0,0,0,0,0,0,0,0,0,0,0,0]
    
    gem=(326+111+322+137+297+154+265+167+244+131+330+80+318+37+350+9.5)/8
    
    jan=gem*1.25
    feb=gem*1.2
    mrt=gem*1.1
    dec=gem*1.2
    
    stroom_verbruik_persoonlijk=[jan,feb,mrt,326+111,322+137,297+154,265+167,244+131,330+80,318+37,350+9.5,dec]
    stroom_verbruik_persoonlijk_pv_base=[0,30,70,111,137,154,167,131,80,37,9.5,0]
    stroom_verbruik_persoonlijk_pv=[]
    for i in range(12):
        stroom_verbruik_persoonlijk_pv.append(stroom_verbruik_persoonlijk_pv_base[i]*panelenkWP/1.5)
    
    
    stroom_verbruik_verschil=[]
    for i in range(12):
        stroom_verbruik_verschil.append(stroom_verbruik_persoonlijk[i]-stroom_verbruik_persoonlijk_pv[i])
    
    #stroom en gas
    fig, ax = plt.subplots()
    title=fig.suptitle(f'Gas en stroomverbruik strandaard vs. warmtepop voor {WP} panelen', fontsize=16)
    ax.plot(time, gas_verbruik_traditioneel, label="gas std [m3]",color=(1, 0, 0),linestyle='dashed')
    ax.plot(time, stroom_verbruik_traditioneel, label="stroom std [kWh]",color=(1, 0, 0),linestyle='solid')
    ax.plot(time, gas_verbruik_persoonlijk, label="gas wp [m3]",color=(0, 1, 0),linestyle='dashed')
    ax.plot(time, stroom_verbruik_verschil, label="stroom tot wp [kWh]",color=(0, 1, 0),linestyle='solid')
    ax.plot(time, stroom_verbruik_persoonlijk_pv, label="stroom pv wp [kWh]",color=(0, 1, 0),linestyle='dotted')
    ax.grid()
    lgd=ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    #ax.legend()
    
    plt.savefig(f'Gas_stroom_vs_{WP}.png',dpi=300, bbox_extra_artists=(lgd,title), bbox_inches='tight')
    plt.show()
    plt.clf()
    
    gas_kosten_std=[]
    stroom_kosten_std=[]
    energie_kosten_std_tot=[]
    stroom_kosten_pers=[]
    
    for i in range(12):
        gas_kosten_std.append(gas_verbruik_traditioneel[i]*gas_kosten)
        stroom_kosten_std.append(stroom_verbruik_traditioneel[i]*stroom_kosten)
        stroom_kosten_pers.append(stroom_verbruik_verschil[i]*stroom_kosten)
        
    for i in range(12):
        energie_kosten_std_tot.append(gas_kosten_std[i]+stroom_kosten_std[i])
        
    #kosten
    fig, ax = plt.subplots()
    title=fig.suptitle(f'Kosten gas en stroomverbruik strandaard vs. warmtepomp voor {WP} panelen', fontsize=16)
    ax.plot(time, energie_kosten_std_tot, label="Totaal kosten std",color=(1, 0, 0),linestyle='solid')
    ax.plot(time, gas_kosten_std, label="Gas kosten std",color=(1, 0, 0),linestyle='dashed')
    ax.plot(time, stroom_kosten_std, label="Stroom kosten std",color=(1, 0, 0),linestyle='dashdot')
    ax.plot(time, stroom_kosten_pers, label="Totaal kosten wp",color=(0, 1, 0),linestyle='solid')
    ax.grid()
    plt.ylabel('Euro/maand')
    lgd=ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    #ax.legend()
    
    plt.savefig(f'Kosten_gas_stroom_vs_{WP}.png',dpi=300, bbox_extra_artists=(lgd,title), bbox_inches='tight')
    plt.show()
    plt.clf()
    
def main():
    berekening(1.5)
    berekening(3)
    berekening(4.5)
main()
