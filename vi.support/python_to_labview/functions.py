#Copyright (c) 2009, 2010, 2011 Tom Schoonjans
#All rights reserved.

#Redistribution and use in source and binary forms, with or without
#modification, are permitted provided that the following conditions are met:
#    * Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
#    * The names of the contributors may not be used to endorse or promote products derived from this software without specific prior written permission.

#THIS SOFTWARE IS PROVIDED BY Tom Schoonjans ''AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL Tom Schoonjans BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


#"""Example of using various xraylib functionality in python."""

import xraylib
import math
import numpy as np

xraylib.XRayInit()

def ZtoName(Z):
    return xraylib.AtomicNumberToSymbol(Z)

def density(Z):
    return xraylib.ElementDensity(Z) # g/cm3"
    
def weight(Z):
    return xraylib.AtomicWeight(Z) # g/mol

def CsB_FL_K(Z,Lin,En):
    return xraylib.CSb_FluorLine_Kissel(Z,Lin,En)

def Cs_Total(Z,En):
    return xraylib.CS_Total(Z,En)

def NametoZ(At):
    return xraylib.SymbolToAtomicNumber(At)

def CsB_FL_K_loop(Z,Shell,Lin,En_array,Int_array):
    param=0
    En_abs=float(xraylib.EdgeEnergy(Z,Shell))
    print(En_abs)
    kk=1
    if Shell==0:
        if Lin==0:
            if Z>4:
                for i in range(len(En_array)):
                    if En_abs>0.15:
                        if En_array[i]>En_abs:
                            param+=(xraylib.CSb_FluorLine_Kissel(Z,Lin,En_array[i]))*Int_array[i]
                            kk=kk+1
        elif Lin==1:
            if Z>12:
                for i in range(len(En_array)):
                    if En_abs>0.15:
                        if En_array[i]>En_abs:
                            param+=(xraylib.CSb_FluorLine_Kissel(Z,Lin,En_array[i]))*Int_array[i]
                            kk=kk+1
    elif Shell==1:
        if Lin==2:
            if Z>20:
                for i in range(len(En_array)):
                    if En_abs>0.15:
                        if En_array[i]>En_abs:
                            param+=(xraylib.CSb_FluorLine_Kissel(Z,Lin,En_array[i]))*Int_array[i]
                            kk=kk+1    
    CsB_exit=np.array([kk, param])
    return CsB_exit

def Cs_Total_loop(Z,En_array,Int_array,rho):
    param1=0
    for i in range(len(En_array)):
        if En_array[i]>0.01:
            param1+=(xraylib.CS_Total(Z,En_array[i]))*Int_array[i]*rho
    return param1
    
#x = np.genfromtxt("En_array.dat")
#y = np.genfromtxt("Int_array.dat") 
#ZZ=int(input("Inserisci il valore di Z:\n"))
#LL=1
#SH=0
#for ZZ in range(13,90,1):
#    print("Fluorescence Line per Z= {}".format(ZZ), ": {}".format(xraylib.LineEnergy(ZZ, LL)))
#    print("Cs Total per Z= {}".format(ZZ), ": {}".format(Cs_Total_loop(ZZ, x, y, xraylib.ElementDensity(ZZ)))) 
#    print("CsB per Z= {}".format(ZZ), ": {}".format(CsB_FL_K_loop(ZZ, 0, 0, x, y))) 
#    print("CsB per Z= {}".format(ZZ), ": {}".format(CsB_FL_K_loop(ZZ, SH, LL, x, y))) 
#    print("CsB per Z= {}".format(ZZ), ": {}".format(CsB_FL_K_loop(ZZ, 1, 2, x, y))) 