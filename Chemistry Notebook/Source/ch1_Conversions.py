import math
import numpy
import scipy

class conversions:
        
#.................................... length .................................... #
    m                   = 1
    ym                  = m * pow(10, 24)
    zm                  = m * pow(10, 21)
    at                  = m * pow(10, 18)
    fm                  = m * pow(10, 15)
    pm                  = m * pow(10, 12)
    nm                  = m * pow(10, 9)
    um                  = m * pow(10, 6)
    mm                  = m * pow(10, 3)
    cm                  = m * pow(10, 2)
    dm                  = m * pow(10, 1)
    dam                 = m * pow(10, -1)
    hm                  = m * pow(10, -2)
    km                  = m * pow(10, -3)
    Mm                  = m * pow(10, -6)
    Gm                  = m * pow(10, -9)
    Tm                  = m * pow(10, -11)
    Pm                  = m * pow(10, -15)
    Em                  = m * pow(10, -18)
    Zm                  = m * pow(10, -21)
    Ym                  = m * pow(10, -24)
    inch                = m * 39.370078740157
    feet                = m * 3.2808398950131
    yard                = m * 1.093613298377
    mile                = m * 0.00062137119223733
    nautical_mile       = m * 0.00053995680345572

    #.................................. mass .................................. #
    g                   = 1 
    yg                  = g * pow(10, 24)
    zg                  = g * pow(10, 21)
    at                  = g * pow(10, 18)
    fg                  = g * pow(10, 15)
    pg                  = g * pow(10, 12)
    ng                  = g * pow(10, 9)
    ug                  = g * pow(10, 6)
    mg                  = g * pow(10, 3)
    cg                  = g * pow(10, 2)
    dg                  = g * pow(10, 1) 
    dag                 = g * pow(10, -1)
    hg                  = g * pow(10, -2)
    kg                  = g * pow(10, -3)
    Mg                  = g * pow(10, -6)
    Gg                  = g * pow(10, -9)
    Tg                  = g * pow(10, -12)
    Pg                  = g * pow(10, -15)
    Eg                  = g * pow(10, -18)
    Zg                  = g * pow(10, -21)
    Yg                  = g * pow(10, -24)
    pound               = g * 0.002204622621848
    ounce               = g * 0.03527396194958
    carat               = g * 5
    Short_ton_US        = g * 0.000001102311310
    Long_ton_UK         = g * pow(9.8420652761106, -7)
    tonne               = g * 0.000001
    Grain               = g * 15.432358352941
    #...................................... area ...................................... #
    m2                  = 1
    ym2                 = m2 * pow(10, 24)
    zm2                 = m2 * pow(10, 21)
    at2                 = m2 * pow(10, 18)
    fm2                 = m2 * pow(10, 15)
    pm2                 = m2 * pow(10, 12)
    nm2                 = m2 * pow(10, 9)
    um2                 = m2 * pow(10, 6)
    mm2                 = m2 * pow(10, 3)
    cm2                 = m2 * pow(10, 2)
    dm2                 = m2 * pow(10, 1)
    am2                 = m2 * pow(10, -1)
    hm2                 = m2 * pow(10, -2)
    km2                 = m2 * pow(10, -3)
    Gm2                 = m2 * pow(10, -6)
    Mm2                 = m2 * pow(10, -9)
    Tm2                 = m2 * pow(10, -12)
    Pm2                 = m2 * pow(10, -15)
    Em2                 = m2 * pow(10, -18)
    Zm2                 = m2 * pow(10, -21)
    Ym2                 = m2 * pow(10, -24)
    sq_inch             = m2 * 1550.0031000062
    sq_foot             = m2 * 10.76391041671
    sq_yard             = m2 * 1.1959900463011
    sq_mile             = m2 * 3.8610215854782e-7
    acre                = m2 * 0.00024710538146717

    # ..........................................Volume
    L = 1
    yL = L * pow(10, 24)
    zL = L * pow(10, 21)
    aL = L * pow(10, 18)
    fL = L * pow(10, 15)
    pL = L * pow(10, 12)
    nL = L * pow(10, 9)
    uL = L * pow(10, 6)
    mL = L * pow(10, 3)
    cL = L * pow(10, 2)
    dL = L * pow(10, 1)
    daL = L * pow(10, -1)
    hL = L * pow(10, -2)
    kL = L * pow(10, -3)
    ML = L * pow(10, -6)
    GL = L * pow(10, -9)
    TL = L * pow(10, -12)
    PL = L * pow(10, -15)
    EL = L * pow(10, -18)
    ZL = L * pow(10, -21)
    YL = L * pow(10, -24)

    unit_dict = {
        "Length": {
            "m": m,          
            "ym" :  ym,       
            "zm" :  zm,     
            "at" :  at,       
            "fm" :  fm,      
            "pm" :  pm,       
            "nm" :  nm,       
            "um" :  um,       
            "mm" :  mm,       
            "cm" :  cm,       
            "dm" :  dm,       
            "dam" : dam,      
            "hm" :  hm,       
            "km" :  km,       
            "Mm" :  Mm,       
            "Gm" :  Gm,     
            "Tm" :  Tm,       
            "Pm" :  Pm,       
            "Em" :  Em,       
            "Zm" :  Zm,       
            "Ym" :  Ym,       
            "pound" : pound,       
            "ounce" : ounce,       
            "carat" : carat,
            "inch" : inch,
            "feet" : feet,
            "yard" : yard,
            "mile": mile,
            "nautical_mile" : nautical_mile
            },
        "Weight":{
            "g" : g,
            "yg" : yg,
            "zg" : zg,
            "at" : at,
            "fg" : fg,
            "pg": pg,
            "ng" : ng,
            "um" : um,
            "mg" : mg,
            "cg" : cg,
            "dg" : dg,
            "dag" : dag,
            "hg" : hg,
            "kg" : kg,
            "Mg" : Mg,
            "Gg" : Gg,
            "Tg" : Tg,
            "Pg" : Pg,
            "Eg" : Eg,
            "Zg" : Zg,
            "Yg" : Yg,       
            "Short_ton_US" : Short_ton_US,
            "Long_ton_UK" : Long_ton_UK, 
            "tonne" : tonne,        
            "Grain": Grain
            }, 
        "Area":{
            "m2"  : m2,
            "ym2" : ym2,
            "zm2" : zm2,
            "at2" : at2,
            "fm2" : fm2,
            "pm2" : pm2,
            "nm2" : nm2,
            "um2" : um2,
            "mm2" : mm2,
            "cm2" : cm2,
            "dm2" : dm2,
            "am2" : am2,
            "hm2" : hm2,
            "km2" : km2,
            "Mm2" : Mm2,
            "Gm2" : Gm2,
            "Tm2" : Tm2,
            "Pm2" : Pm2,
            "Em2" : Em2,
            "Zm2" : Zm2,
            "Ym2" : Ym2,
            "sq_inch" : sq_inch,
            "sq_foot" : sq_foot,
            "sq_yard" : sq_yard,
            "sq_mile" : sq_mile,
            "acre" : acre      
            }, 
        "Volume":{
            "L": 1,
            "yL": yL,
            "zL": zL,
            "aL": aL,
            "fL": fL,
            "pL": pL,
            "nL": nL,
            "uL": uL,
            "mL": mL,
            "cL": cL,
            "dL": dL,
            "daL" : daL,
            "hL": hL,
            "kL": kL,
            "ML": ML,
            "GL": GL,
            "TL": TL,
            "PL": PL,
            "EL": EL,
            "ZL": ZL,
            "YL": YL
            }    
        } 

    def __init__(self):
       self
        

    def convert(self, num, fro, to):
        self.fro = fro # from unit
        self.to = to # to unit
        ans = 0
        if num > 0:
            self.num = num #conversion number
            for x in self.unit_dict:
                for y in self.unit_dict[x]:
                    if fro == y:
                        fro = self.unit_dict[x][y]
                    if to == y:
                        to = self.unit_dict[x][y]
            ans = num * to / fro
        else:
            print("Num must be a number greater than zero")
            self.num = -1
            ans = "Conversion failed due to improper entry"
            
        self.ans = ans
        return(ans)

# Slash units turned into conversion factor
# 1 m / 1000 m
# 1000 mm / 1 m
# 1 min / 60 sec
# 60 sec / 1
# 1 km / 2.20 lb
#

# https://metricunitconversion.globefeed.com/


# ........................Weight Units............................

# Common weight units

# gram (g)            1
# Kilogram (kg)       0.001
# pound (lb)          0.002204622621848
# ounce (oz)          0.03527396194958
# carat ()            5
# Short ton (US)      0.000001102311310
# Long ton (UK)       9.8420652761106e-7
# tonne (metric ton)  0.000001
# Grain (gr)          15.432358352941

# SI WEIGHT UNITS

# Yoctogram (yg)        1e+24
# Zeptogram (zg)        1e+21
# Attogram (at)         1000000000000000000
# Femtogram (fg)        1000000000000000
# Picogram (pg)         1000000000000
# Nanogram (ng)         1000000000
# Microgram (um)        1000000
# Milligram (mg)        1000
# Centigram (cg)        100
# Decigram (dg)         10
# Gram (g)              1
# Decagram (dag)        0.1
# Hectogram (hg)        0.01
# Kilogram (kg)         0.001
# Megagram (Mg, tonne)  0.0000001
# Gigagram (Gg)         1e-9
# Teragram (Tg)         1e-12
# Petagram (Pg)         1e-15
# Exagram (Eg)          1e-18
# Zettagram (Zg)        1e-21
# Yottagram (Yg)        1e-24

# ...........................Length Units...............................

#Common Length units

# millimeter(mm)      =  1000
# centimeter (cm)     =  100 
# meter (m)           =  1
# kilometer (km)      =  0.001
# inch (in)           =  39.370078740157
# feet / foot (ft)    =  3.2808398950131
# yard (yd)           =  1.093613298377
# mile                =  0.00062137119223733
# nautical mile       =  0.00053995680345572


# SI LENGTH UNITS
# Yoctometer (ym)        1e+24
# Zeptometer (zm)        1e+21
# Attometer (at)         1000000000000000000
# Femtometer (fm)        1000000000000000
# Picometer (pm)         1000000000000
# Nanometer (nm)         1000000000
# Micrometer (um)        1000000
# Millimeter (mm)        1000
# Centimeter (cm)        100
# Decimeter (dm)         10
# meter (m)              1
# Decameter (dam)        0.1
# Hectometer (hm)        0.01
# Kilometer (km)         0.001
# Megameter (Mm)         0.0000001
# Gigameter (Gm)         1e-9
# Terameter (Tm)         1e-12
# Petameter (Pm)         1e-15
# Exameter (Em)          1e-18
# Zettameter (Zm)        1e-21
# Yottameter (Ym)        1e-24

# ............................Area Units................................

#Common area units

# sq. centimeter       = 10000
# sq. meter            = 1
# hectare (ha)         = 0.0001
# sq. kilometer        = 0.000001
# sq.inch              = 1550.0031000062
# sq. foot/feet        = 10.76391041671
# sq. yard             = 1.1959900463011
# sq. mile             = 3.8610215854782e-7
# acre (ac)            = 0.00024710538146717

#SI Area units

# Square Yoctometer (ym2)       1e+24
# Square Zeptometer (zm2)       1e+21
# Square Attometer (at2)        1000000000000000000
# Square Femtometer (fm2)       1000000000000000
# Square Picometer (pm2)        1000000000000
# Square Nanometer (nm2)        1000000000
# Square Micrometer (um2)       1000000
# Square Millimeter (mm2)       1000
# Square Centimeter (cm2)       100
# Square Decimeter (dm2)        10
# Square meter (m2)             1
# Square Decameter (dam2)       0.1
# Square Hectometer (hm2)       0.01
# Square Kilometer (km2)        0.001
# Square Megameter (Gm2)        0.0000001
# Square Gigameter (Gm2)        1e-9
# Square Terameter (Tm2)        1e-12
# Square Petameter (Pm2)        1e-15
# Square Exameter (Em2)         1e-18
# Square Zettameter (Zm2)       1e-21
# Square Yottameter (Ym2)       1e-24

# ...........................Volume Units...............................
