# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 17:04:34 2020

@author: obazgir
"""

from argparse import ArgumentParser

parser=ArgumentParser()

parser.add_argument('--data_dir', type=str, required=True, help="Path to the input data file in Initial_MDS.py")
parser.add_argument('--output_file', type=str, default='Init_MDS_Euc.pickle', help="Path to the output pickle file  in Initial_MDS.py")

parser.add_argument('--init', type=str, default='Init.pickle')
parser.add_argument('--mapping', type=str, default='theMapping.pickle')
parser.add_argument('--evolution', type=str, default='Evolv.csv')
parser.add_argument('--num', type=int, default=5)

args= parser.parse_args()