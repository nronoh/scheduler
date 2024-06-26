#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 12:21:04 2024

@author: NRonoh
"""

import pandas as pd
import random
import numpy as np



MAT_COURSES =[{'CODE':'MAT 213',
               'YEAR':'2',
               'TITLE':'Linear Algebra II',
               'LECTURER':'Lec 1 MAT',
               'GROUPS':['SC', 'BAE', 'BSE'],
               'ROOM':['SL1', 'SR22']
              },
              {'CODE':'MAT 311',
               'YEAR':'3',
               'TITLE':'Real Analysis II',
               'LECTURER':'Lec 1 MAT',
               'GROUPS':['SC', 'BAE', 'BSE','EDS', 'ED', 'EDB', 'EDG', 'EDN'],
               'ROOM':['SL1']
              },
              {'CODE':'MAT 312',
               'YEAR':'3',
               'TITLE':'Complex Analysis I',
               'LECTURER':'Lec 2 MAT',
               'GROUPS':['SC', 'BAE', 'BSE'],
               'ROOM':['SL1', 'SR22']
              },
              {'CODE':'MAT 400',
               'YEAR':'4',
               'TITLE':'Analytic Applied Mathematics',
               'LECTURER':'Lec 2 MAT',
               'GROUPS':['ED','EDS','EDB','EDG','EDN'],
               'ROOM':['LH2']
              },
              {'CODE':'MAT 422',
               'YEAR':'4',
               'TITLE':'Operation Research II',
               'LECTURER':'Lec 2 MAT',
               'GROUPS':['SC', 'BAE', 'BSE'],
               'ROOM':['AH1','SR18','LR3']
              },
              {'CODE':'MAT 215/MAT 315', 
               'YEAR':'2 & 3',
               'TITLE':'Classical Mechanics', 
               'LECTURER':'Lec 3 MAT',
               'GROUPS':['SC', 'BAE', 'BSE','EDS', 'ED', 'EDB', 'EDG', 'EDN'],
               'ROOM':['SL1', 'SR22']
              },
              {'CODE':'MAT 316',
               'YEAR':'3',
               'TITLE':'Methods I',
               'LECTURER':'Lec 3 MAT',
               'GROUPS':['SC', 'BAE', 'BSE'],
               'ROOM':['LR3','SR18']
              },
              {'CODE':'MAT 424',
               'YEAR':'4',
               'TITLE':'Fluid Mechanics III',
               'LECTURER':'Lec 3 MAT',
               'GROUPS':['SC', 'BAE', 'BSE'],
               'ROOM':['AH1','SR3','SR18']
              },
              {'CODE':'MAT 419',
               'YEAR':'4',
               'TITLE':'Partial Differential Equations II',
               'LECTURER':'Lec 4 MAT',
               'GROUPS':['SC', 'BAE', 'BSE','EDS', 'ED','EDB','EDG', 'EDN'],
               'ROOM':['SL1', 'SR22']
              },
              {'CODE':'MAT 425',
               'YEAR':'4',
               'TITLE':'Fourier Analysis',
               'LECTURER':'Lec 4 MAT',
               'GROUPS':['SC', 'BAE', 'BSE'],
               'ROOM':['AH1','SR3','SR18']
              },
              {'CODE':'MAT 214',
               'YEAR':'2',
               'TITLE':'Vector Analysis',
               'LECTURER':'Lec 4 MAT',
               'GROUPS':['SC', 'BAE', 'BSE','EDS', 'ED', 'EDB','EDG', 'EDN'],
               'ROOM':['SL1', 'SR22']
              },
              {'CODE':'MAT 205',
               'YEAR':'2',
               'TITLE':'Ordinary Differential Equations I',
               'LECTURER':'Lec 5 MAT',
               'GROUPS':['EDS', 'ED', 'EDB','EDG', 'EDN'],
               'ROOM':['LH2']
              }, 
              {'CODE':'MAT 317',
               'YEAR':'3',
               'TITLE':'Numerical Analysis I',
               'LECTURER':'Lec 5 MAT',
               'GROUPS':['SC', 'BAE', 'BSE','EDS', 'ED', 'EDB','EDG', 'EDN'],
               'ROOM':['SL1', 'SR22']
              },
              {'CODE':'MAT 426',
               'YEAR':'4',
               'TITLE':'Methods II',
               'LECTURER':'Lec 5 MAT',
               'GROUPS':['SC', 'BAE', 'BSE'],
               'ROOM':['AH1','SR3','SR18']
              },
              {'CODE':'SMA 121',
               'YEAR':'1',
               'TITLE':'Geometry and Elementary Applied Mathematics',
               'LECTURER':'Lec 6 MAT',
               'GROUPS':['ACS', 'AST', 'SC', 
                         'BIO', 'COM', 'BSE',
                         'BAE', 'EDS', 'ED',
                         'EDB', 'EDG', 'EDG',
                         'EDN', 'AGN'
                        ],
               'ROOM':['SL1', 'SR22']
              },
              {'CODE':'MAT 313',
               'YEAR':'3',
               'TITLE':'Abstract Algebra',
               'LECTURER':'Lec 7 MAT',
               'GROUPS':['SC', 'BAE', 'BSE'],
               'ROOM':['AH1','SR3','SR18']
              },
              {'CODE':'MAT 411',
               'YEAR':'4',
               'TITLE':'Field Theory',
               'LECTURER':'Lec 7 MAT',
               'GROUPS':['SC', 'BAE', 'BSE'],
               'ROOM':['AH1','SR3','SR18']
              },
              {'CODE':'MAT 416',
               'YEAR':'4',
               'TITLE':'Functional Analysis',
               'LECTURER':'Lec 7 MAT',
               'GROUPS':['SC', 'BAE', 'BSE',
                         'EDS', 'ED', 'EDB',
                         'EDG', 'EDN'],
               'ROOM':['AH1','SR3','SR18']
              }, 
              {'CODE':'MAT 414',
               'YEAR':'4',
               'TITLE':'Topology II',
               'LECTURER':'Lec 8 MAT',
               'GROUPS':['SC', 'BAE', 'BSE'],
               'ROOM':['DC','LR3','SR18']
              },
              {'CODE':'MAT 415',
               'YEAR':'4',
               'TITLE':'Differential Geometry',
               'LECTURER':'Lec 9 MAT',
               'GROUPS':['SC', 'BAE', 'BSE',
                         'EDS', 'ED', 'EDB',
                         'EDG', 'EDN'],
               'ROOM':['DC','SR18','CR-SC']
              },
              {'CODE':'MAT 319',
               'YEAR':'3',
               'TITLE':'Advanced Calculus',
               'LECTURER':'Lec 8 MAT',
               'GROUPS':['SC', 'BAE', 'BSE'],
               'ROOM':['AH1','SR3','SR18']
              }, 
              {'CODE':'MAT 211',
               'YEAR':'2',
               'TITLE':'Calculus and Analytic Geometry',
               'LECTURER':'Lec 10 MAT',
               'GROUPS':['SC', 'BAE', 'BSE','COM', 'AST','ACS'],
               'ROOM':['SL1']
              },
              {'CODE':'MAT 314',
               'YEAR':'3',
               'TITLE':'Ordinary Differential Equations II',
               'LECTURER':'Lec 10 MAT',
               'GROUPS':['EDS', 'ED', 'EDG', 'EDB', 'EDN'],
               'ROOM':['SR22','CR-SC']
              },
              {'CODE':'MAT 427',
               'YEAR':'4',
               'TITLE':'Ordinary Differential Equations II',
               'LECTURER':'Lec 10 MAT',
               'GROUPS':['SC', 'BAE', 'BSE'],
               'ROOM':['AH1','SR3','SR18']
              },
              {'CODE':'MAT 200',
               'YEAR':'2',
               'TITLE':'Mathematics and Statistics',
               'LECTURER':'Lec 11 MAT',
               'GROUPS':['SC', 'BAE', 'BSE'],
               'ROOM':['DC','LR3']
              },
              {'CODE':'MAT 103',
               'YEAR':'1',
               'TITLE':'Basic Engineering Mathematics II',
               'LECTURER':'Lec 12 MAT',
               'GROUPS':['ENG'],
               'ROOM':['DO','FL1']
              },
              {'CODE':'MAT 208',
               'YEAR':'2',
               'TITLE':'Engineering Mathematics II',
               'LECTURER':'Lec 12 MAT',
               'GROUPS':['ENG'],
               'ROOM':['DO','FL1']
              }
             ]

PHY_COURSES =[{'CODE':'PHY 430E/COM 422',
               'YEAR':'4',
               'TITLE':'Electronic Circuits and Microprocessors',
               'LECTURER':'Lec 1 PHY',
               'GROUPS':['SC', 'BAE', 'BSE','COM'],
               'ROOM':['DC','LR3']
              },
              {'CODE':'ECE 121',
               'YEAR':'1',
               'TITLE':'Circuit Theory I',
               'LECTURER':'Lec 1 PHY',
               'GROUPS':['ENG'],
               'ROOM':['DO','FL1']
              },
              {'CODE':'PHY 315',
               'YEAR':'3',
               'TITLE':'Electromagnetism',
               'LECTURER':'Lec 2 PHY',
               'GROUPS':['SC', 'BAE', 'BSE','COM'],
               'ROOM':['DC','LR3']
              },
              {'CODE':'PHY 429E',
               'YEAR':'4',
               'TITLE':'Introduction to Lasers',
               'LECTURER':'Lec 2 PHY',
               'GROUPS':['SC', 'BAE', 'BSE','COM'],
               'ROOM':['AH1','LR3']
              },
              {'CODE':'PHY 222',
               'YEAR':'2',
               'TITLE':'Properties of Matter',
               'LECTURER':'Lec 3 PHY',
               'GROUPS':['SC', 'BAE', 'BSE','COM'],
               'ROOM':['DC','CR-SC']
              },
              {'CODE':'PHY 427E',
               'YEAR':'4',
               'TITLE':'Solar Energy Physics',
               'LECTURER':'Lec 3 PHY',
               'GROUPS':['SC', 'BAE', 'BSE','COM'],
               'ROOM':['AH1','LR3']
              },
              {'CODE':'SPH 121',
               'YEAR':'1',
               'TITLE':'Basic Physics II',
               'LECTURER':'Lec 4 PHY',
               'GROUPS':['SC','BIO', 'COM',
                         'BSE','BAE', 'EDS',
                         'ED','EDB', 'EDG', 
                         'EDG','EDN', 'AGN'
                        ],
               'ROOM':['SL1', 'SR22']
              },
              {'CODE':'PHY 316',
               'YEAR':'3',
               'TITLE':'Introduction to Material Science',
               'LECTURER':'Lec 4 PHY',
               'GROUPS':['SC', 'BAE', 'BSE'],
               'ROOM':['AH1','DC','SR3','SR18']
              },
              {'CODE':'PHY 210',
               'YEAR':'2',
               'TITLE':'Electricity and Magnetism',
               'LECTURER':'Lec 5 PHY',
               'GROUPS':['SC', 'BAE', 'BSE'],
               'ROOM':['AH1','DC','SR3','SR18']
              },
              {'CODE':'PHY 317',
               'YEAR':'3',
               'TITLE':'Classical Mechanics',
               'LECTURER':'Lec 5 PHY',
               'GROUPS':['SC', 'BAE', 'BSE'],
               'ROOM':['AH1','DC','SR3','SR18']
              },
              {'CODE':'PHY 212',
               'YEAR':'2',
               'TITLE':'Modern Physics',
               'LECTURER':'Lec 6 PHY',
               'GROUPS':['SC', 'BAE', 'BSE'],
               'ROOM':['AH1','DC','SR3','SR18']
              },
              {'CODE':'PHY 221',
               'YEAR':'2',
               'TITLE':'Electricity and Magnetism II',
               'LECTURER':'Lec 6 PHY',
               'GROUPS':['SC', 'BAE', 'BSE'],
               'ROOM':['AH1','DC','SR3','SR18']
              },
              {'CODE':'PHY 314',
               'YEAR':'3',
               'TITLE':'Quantum Mechanics',
               'LECTURER':'Lec 6 PHY',
               'GROUPS':['SC', 'BAE', 'BSE'],
               'ROOM':['AH1','DC','SR3','SR18']
              },
              {'CODE':'PHY 213',
               'YEAR':'2',
               'TITLE':'Electronics I',
               'LECTURER':'Lec 7 PHY',
               'GROUPS':['SC', 'BAE', 'BSE'],
               'ROOM':['AH1','DC','SR3','SR18']
              },
              {'CODE':'PHY 416',
               'YEAR':'4',
               'TITLE':'Atomic and Nuclear Physics',
               'LECTURER':'Lec 7 PHY',
               'GROUPS':['SC', 'BAE', 'BSE'],
               'ROOM':['AH1','DC','SR3','SR18']
              },
              {'CODE':'PHY 415',
               'YEAR':'4',
               'TITLE':'Statistical Mechanics',
               'LECTURER':'Lec 7 PHY',
               'GROUPS':['SC', 'BAE', 'BSE'],
               'ROOM':['AH1','DC','SR3','SR18']
              },
              {'CODE':'PHY 105',
               'YEAR':'1',
               'TITLE':'Physics for Engineers',
               'LECTURER':'Lec 8 PHY',
               'GROUPS':['ENG'],
               'ROOM':['DO','FL1']
              }
             ]

STA_COURSES =[{'CODE':'STA 219',
               'YEAR':'2',
               'TITLE':'Categorical Data Analysis',
               'LECTURER':'Lec 1 STA',
               'GROUPS':['SC', 'ACS','AST'],
               'ROOM':['LR3','DC','SR18','CR-SC']
              },
              {'CODE':'STA 328',
               'YEAR':'3',
               'TITLE':'Applied Regression Analysis II',
               'LECTURER':'Lec 1 STA',
               'GROUPS':['SC', 'ACS','AST'],
               'ROOM':['LR3','DC','SR18','CR-SC']
              },
              {'CODE':'STA 414/STA 430',
               'YEAR':'4',
               'TITLE':'Non-Parametric and Robust Methods',
               'LECTURER':'Lec 2 STA',
               'GROUPS':['SC', 'ACS','AST'],
               'ROOM':['LR3','DC','SR18','CR-SC']
              },
              {'CODE':'STA 312',
               'YEAR':'3',
               'TITLE':'Regression Analysis and Analysis of Variance',
               'LECTURER':'Lec 2 STA',
               'GROUPS':['SC', 'ACS','AST'],
               'ROOM':['LR3','DC','SR18','CR-SC']
              },
              {'CODE':'STA 321',
               'YEAR':'3',
               'TITLE':'Test of Hypothesis',
               'LECTURER':'Lec 3 STA',
               'GROUPS':['SC', 'ACS','AST'],
               'ROOM':['LR3','DC','SR18','CR-SC']
              },
              {'CODE':'STA 314/STA 326',
               'YEAR':'3',
               'TITLE':'Statistical Quality Control Methods',
               'LECTURER':'Lec 3 STA',
               'GROUPS':['SC', 'ACS','AST'],
               'ROOM':['LR3','DC','SR18','CR-SC']
              },
              {'CODE':'STA 423',
               'YEAR':'4',
               'TITLE':'Biometric Methods',
               'LECTURER':'Lec 4 STA',
               'GROUPS':['SC', 'ACS','AST'],
               'ROOM':['LR3','DC','SR18','CR-SC']
              },
              {'CODE':'STA 217',
               'YEAR':'2',
               'TITLE':'Principles of Statistical Inference',
               'LECTURER':'Lec 5 STA',
               'GROUPS':['BSE', 'ACS','AST'],
               'ROOM':['LR3','DC','SR18','CR-SC']
              },
              {'CODE':'STA 427',
               'YEAR':'4',
               'TITLE':'Survival Analysis',
               'LECTURER':'Lec 5 STA',
               'GROUPS':['AST'],
               'ROOM':['LR3','DC']
              },
              {'CODE':'STA 415',
               'YEAR':'4',
               'TITLE':'Design and Analysis of Experiments II',
               'LECTURER':'Lec 5 STA',
               'GROUPS':['SC'],
               'ROOM':['AH1']
              },
              {'CODE':'STA 218',
               'YEAR':'2',
               'TITLE':'Introduction to Time Series Analysis',
               'LECTURER':'Lec 6 STA',
               'GROUPS':['SC', 'ACS','AST'],
               'ROOM':['LR3','DC','SR18','CR-SC']
              },
              {'CODE':'STA 320',
               'YEAR':'3',
               'TITLE':'Design and Analysis of Experiments I',
               'LECTURER':'Lec 6 STA',
               'GROUPS':['SC', 'ACS','AST'],
               'ROOM':['LR3','DC','SR18','CR-SC']
              },
              {'CODE':'STA 313',
               'YEAR':'3',
               'TITLE':'Theory of Estimations',
               'LECTURER':'Lec 6 STA',
               'GROUPS':['SC', 'ACS','AST'],
               'ROOM':['LR3','DC','SR18','CR-SC']
              },
              {'CODE':'STA 122',
               'YEAR':'1',
               'TITLE':'Computer Applications for Data Analysis',
               'LECTURER':'Lec 7 STA',
               'GROUPS':['SC', 'ACS','AST'],
               'ROOM':['LR3','DC','SR18','CR-SC']
              },
              {'CODE':'STA 124',
               'YEAR':'1',
               'TITLE':'Fundamentals of Data Science',
               'LECTURER':'Lec 7 STA',
               'GROUPS':['SC', 'ACS','AST'],
               'ROOM':['LR3','DC','SR18','CR-SC']
              },
              {'CODE':'STA 425',
               'YEAR':'4',
               'TITLE':'Sampling Theory and Methods II',
               'LECTURER':'Lec 7 STA',
               'GROUPS':['SC', 'ACS','AST'],
               'ROOM':['LR3','DC','SR18','CR-SC']
              },
              {'CODE':'STA 216',
               'YEAR':'2',
               'TITLE':'Mathematical Statistics II',
               'LECTURER':'Lec 8 STA',
               'GROUPS':['SC', 'ACS','AST'],
               'ROOM':['LR3','DC','SR18','CR-SC']
              },
              {'CODE':'STA 121',
               'YEAR':'1',
               'TITLE':'Principles of Sample Survey',
               'LECTURER':'Lec 9 STA',
               'GROUPS':['SC', 'ACS','AST'],
               'ROOM':['LR3','DC','SR18','CR-SC']
              },
              {'CODE':'STA 211',
               'YEAR':'2',
               'TITLE':'Introduction to Statistics and Probability II',
               'LECTURER':'Lec 9 STA',
               'GROUPS':['SC', 'ACS','AST'],
               'ROOM':['LR3','DC','SR18','CR-SC']
              },
              {'CODE':'STA 416',
               'YEAR':'4',
               'TITLE':'Sequential Analysis and Decision Theory',
               'LECTURER':'Lec 9 STA',
               'GROUPS':['SC', 'ACS','AST'],
               'ROOM':['LR3','DC','SR18','CR-SC']
              },
              {'CODE':'STA 123',
               'YEAR':'1',
               'TITLE':'Introduction to Mathematics for Finance',
               'LECTURER':'Lec 10 STA',
               'GROUPS':['ACS','AST'],
               'ROOM':['LR3','DC','SR18','CR-SC']
              },
              {'CODE':'STA 319',
               'YEAR':'3',
               'TITLE':'Sampling Theory and Methods I',
               'LECTURER':'Lec 11 STA',
               'GROUPS':['SC', 'ACS','AST'],
               'ROOM':['LR3','DC','SR18','CR-SC']
              },
              {'CODE':'STA 205',
               'YEAR':'2',
               'TITLE':'Statistics and Probability',
               'LECTURER':'Lec 11 STA',
               'GROUPS':['SC', 'ACS','AST'],
               'ROOM':['LR3','DC','SR18','CR-SC']
              },
              {'CODE':'STA 305',
               'YEAR':'3',
               'TITLE':'Probability Modeling',
               'LECTURER':'Lec 12 STA',
               'GROUPS':['SC', 'ACS','AST'],
               'ROOM':['SR18','SR22']
              },
              {'CODE':'STA 424 /STA 424E',
               'YEAR':'4',
               'TITLE':'Stochastic Processes',
               'LECTURER':'Lec 13 STA',
               'GROUPS':['SC','ACS','AST'],
               'ROOM':['LR3','DC','SR18','CR-SC']
              },
              {'CODE':'STA 417/STA 429',
               'YEAR':'4',
               'TITLE':'Applied Multivariate Analysis',
               'LECTURER':'Lec 13 STA',
               'GROUPS':['SC', 'ACS','AST'],
               'ROOM':['LR3','DC','SR18','CR-SC']
               },
               {'CODE':'STA 102',
                'YEAR':'1',
                'TITLE':'Engineering Statistics I',
                'LECTURER':'Lec 11 MAT',
                'GROUPS':['ENG'],
                'ROOM':['DO','FL1']
              },
               {'CODE':'STA 304',
                'YEAR':'3',
                'TITLE':'Multivariate Probability Distribution',
                'LECTURER':'Lec 11 MAT',
                'GROUPS':['BSE','BAE', 'EDS',
                         'ED','EDB', 'EDG', 
                         'EDG','EDN'],
                'ROOM':['LR3','DC','SR18','CR-SC']
              },
               {'CODE':'STA 300',
                'YEAR':'3',
                'TITLE':'Biostatistics',
                'LECTURER':'Lec 13 STA',
                'GROUPS':['BSE','BAE', 'EDS',
                         'ED','EDB', 'EDG', 
                         'EDG','EDN'],
                'ROOM':['LR3','DC','SR18','CR-SC']
              }
             ]


PG_COURSES =[{'CODE':'STA 936',
               'YEAR':'PG',
               'TITLE':'Epidemiology II',
               'LECTURER':'Lec 6 STA',
               'GROUPS':['PG-STA'],
               'ROOM':['PG-ROOM']
              },
              {'CODE':'STA 937',
               'YEAR':'PG',
               'TITLE':'Design and Conduct of Clinical Trials',
               'LECTURER':'Lec 4 STA',
               'GROUPS':['PG-STA'],
               'ROOM':['PG-ROOM']
              },
              {'CODE':'STA 935',
               'YEAR':'PG',
               'TITLE':'Design and Analysis of Crossover Trials',
               'LECTURER':'Lec 3 STA',
               'GROUPS':['PG-STA'],
               'ROOM':['PG-ROOM']
              }
            ]


ACS_COURSES =[{'CODE':'ACS 122',
               'YEAR':'1',
               'TITLE':'Fundamentals of Actuarial Mathematics I',
               'LECTURER':'Lec 1 ACS',
               'GROUPS':['ACS'],
                'ROOM':['LR3','DC','SR18','CR-SC']
              },
              {'CODE':'ACS 123',
               'YEAR':'1',
               'TITLE':'Introduction to Non-Life Actuarial Mathematics',
               'LECTURER':'Lec 1 ACS',
               'GROUPS':['ACS'],
               'ROOM':['LR3','DC','SR18','CR-SC']
              },
              {'CODE':'ACS 406',
               'YEAR':'4',
               'TITLE':'Actuarial Theory of Pension Funds',
               'LECTURER':'Lec 1 ACS',
               'GROUPS':['ACS'],
               'ROOM':['AH1','LR3','DC','SR18','CR-SC']
              },
              {'CODE':'ACS 407',
               'YEAR':'4',
               'TITLE':'Life Contingencies II',
               'LECTURER':'Lec 8 STA',
               'GROUPS':['ACS'],
               'ROOM':['AH1','LR3','DC','SR18','CR-SC']
              },
              {'CODE':'ACS 350',
               'YEAR':'3',
               'TITLE':'Industrial Attachment',
               'LECTURER':'Lec 1 ACS',
               'GROUPS':['ACS'],
               'ROOM':['SR3']
              },
              {'CODE':'ACS 305',
               'YEAR':'3',
               'TITLE':'Life Contingencies I',
               'LECTURER':'Lec 8 STA',
               'GROUPS':[ 'ACS'],
               'ROOM':['AH1','LR3','DC','SR18','CR-SC']
              },
              {'CODE':'ACS 203',
               'YEAR':'2',
               'TITLE':'Principles of Microeconomics',
               'LECTURER':'Lec 10 STA',
               'GROUPS':['ACS'],
               'ROOM':['AH1','LR3','DC','SR18','CR-SC']
              },
              {'CODE':'ACS 204',
               'YEAR':'2',
               'TITLE':'Principles of Operation Research',
               'LECTURER':'Lec 10 STA',
               'GROUPS':['ACS'],
               'ROOM':['AH1','LR3','DC','SR18','CR-SC']
              },
              {'CODE':'ACS 306E',
               'YEAR':'3',
               'TITLE':'Methods of Actuarial Investigation I',
               'LECTURER':'Lec 10 STA',
               'GROUPS':['ACS'],
               'ROOM':['AH1','LR3','DC','SR18','CR-SC']
              },
              {'CODE':'ACS 307E',
               'YEAR':'3',
               'TITLE':'Methods of Actuarial Investigation II',
               'LECTURER':'Lec 2 ACS',
               'GROUPS':['ACS'],
               'ROOM':['AH1','LR3','DC','SR18','CR-SC']
              },
              {'CODE':'ACS 404',
               'YEAR':'4',
               'TITLE':'Computational Finance',
               'LECTURER':'Lec 2 ACS',
               'GROUPS':['ACS'],
               'ROOM':['AH1','LR3','DC','SR18','CR-SC']
              },
              {'CODE':'ACS 409',
               'YEAR':'4',
               'TITLE':'Loss Models II',
               'LECTURER':'Lec 2 ACS',
               'GROUPS':['ACS'],
               'ROOM':['AH1','LR3','DC','SR18','CR-SC']
              },
              {'CODE':'ACS 420',
               'YEAR':'4',
               'TITLE':'Project Actuarial Science',
               'LECTURER':'Lec 2 ACS',
               'GROUPS':['ACS'],
               'ROOM':['AH1','LR3','DC','SR18','CR-SC']
              },
              {'CODE':'ACS 302',
               'YEAR':'3',
               'TITLE':'Actuarial Mathematics II',
               'LECTURER':'Lec 3 ACS',
               'GROUPS':['ACS'],
               'ROOM':['AH1','LR3','DC','SR18','CR-SC']
              },
              {'CODE':'ACS 405',
               'YEAR':'4',
               'TITLE':'Business Finance',
               'LECTURER':'Lec 3 ACS',
               'GROUPS':['ACS'],
               'ROOM':['AH1','LR3','DC','SR18','CR-SC']
              }
             ]

COM_COURSES =[{'CODE':'CSC 122',
               'YEAR':'1',
               'TITLE':'Discrete Mathematics II',
               'LECTURER':'Lec 1 COM',
               'GROUPS':['COM'],
               'ROOM':['AH1','LR3','DC']
              },
              {'CODE':'COM 222',
               'YEAR':'2',
               'TITLE':'Internet Applications',
               'LECTURER':'Lec 1 COM',
               'GROUPS':['COM','BSE'],
               'ROOM':['LR3','DC']
              },
              {'CODE':'COM 224',
               'YEAR':'2',
               'TITLE':'Data Structures',
               'LECTURER':'Lec 1 COM',
               'GROUPS':['COM'],
               'ROOM':['LR3','DC']
              },
              {'CODE':'COM 215',
               'YEAR':'2',
               'TITLE':'Electrical Circuits',
               'LECTURER':'Lec 1 PHY',
               'GROUPS':['COM','BSE'],
               'ROOM':['LR3','DC']
              },
              {'CODE':'COM 324E',
               'YEAR':'3',
               'TITLE':'Microelectronics',
               'LECTURER':'Lec 3 PHY',
               'GROUPS':['SC', 'BAE', 'BSE','COM'],
               'ROOM':['LR3','DC']
              },
              {'CODE':'COM 326',
               'YEAR':'3',
               'TITLE':'Software Development',
               'LECTURER':'Lec 2 COM',
               'GROUPS':['COM'],
               'ROOM':['LR3','DC']
              },
              {'CODE':'COM 421',
               'YEAR':'4',
               'TITLE':'Engineering and Software Law',
               'LECTURER':'Lec 2 COM',
               'GROUPS':['COM'],
               'ROOM':['AH1','SR3']
              },
              {'CODE':'COM 431E',
               'YEAR':'4',
               'TITLE':'Human-Computer Interface Design',
               'LECTURER':'Lec 2 COM',
               'GROUPS':['COM'],
               'ROOM':['AH1','SR3']
              },
              {'CODE':'COM 329',
               'YEAR':'3',
               'TITLE':'Field/Industrial Attachment',
               'LECTURER':'Lec 2 COM',
               'GROUPS':['COM'],
               'ROOM':['SR3']
              },
              {'CODE':'COM 223',
               'YEAR':'2',
               'TITLE':'Operating Systems and Networks',
               'LECTURER':'Lec 3 COM',
               'GROUPS':['COM'],
               'ROOM':['AH1','LR3']
              },
              {'CODE':'COM 323E',
               'YEAR':'3',
               'TITLE':'Information Systems Security',
               'LECTURER':'Lec 3 COM',
               'GROUPS':['COM'],
               'ROOM':['AH1','LR3']
              },
              {'CODE':'COM 424E',
               'YEAR':'4',
               'TITLE':'Neural Networks',
               'LECTURER':'Lec 3 COM',
               'GROUPS':['COM'],
               'ROOM':['AH1','LR3']
              },
              {'CODE':'COM 423',
               'YEAR':'4',
               'TITLE':'Computer Science Project II',
               'LECTURER':'Lec 3 COM',
               'GROUPS':['COM'],
               'ROOM':['SR3']
              },
              {'CODE':'COM 318',
               'YEAR':'3',
               'TITLE':'Database Systems',
               'LECTURER':'Lec 4 COM',
               'GROUPS':['COM'],
               'ROOM':['AH1','LR3']
              },
              {'CODE':'CSC 121',
               'YEAR':'1',
               'TITLE':'Programming Methodology and Problem Solving',
               'LECTURER':'Lec 4 COM',
               'GROUPS':['COM'],
               'ROOM':['SL1']
              },
              {'CODE':'COM 220',
               'YEAR':'2',
               'TITLE':'Software Engineering I',
               'LECTURER':'Lec 4 COM',
               'GROUPS':['COM'],
               'ROOM':['DC','LR3','CR-SC']
              },
              {'CODE':'COM 400',
               'YEAR':'4',
               'TITLE':'Computer Programming II',
               'LECTURER':'Lec 4 COM',
               'GROUPS':['COM'],
               'ROOM':['SL1']
              },
              {'CODE':'COM 426',
               'YEAR':'4',
               'TITLE':'Simulation and Modeling',
               'LECTURER':'Lec 5 COM',
               'GROUPS':['COM'],
               'ROOM':['DC','LR3','CR-SC']
              },
              {'CODE':'COM 321',
               'YEAR':'3',
               'TITLE':'Compiler Design',
               'LECTURER':'Lec 5 COM',
               'GROUPS':['COM'],
               'ROOM':['DC','LR3','CR-SC']
              },
              {'CODE':'COM 221',
               'YEAR':'2',
               'TITLE':'Computer Organization',
               'LECTURER':'Lec 5 COM',
               'GROUPS':['COM'],
               'ROOM':['DC','LR3','CR-SC']
              },
              {'CODE':'COM 427E',
               'YEAR':'4',
               'TITLE':'Communication, Antennas and Propagation',
               'LECTURER':'Lec 6 COM',
               'GROUPS':['COM'],
               'ROOM':['AH1','SR3']
              },
              {'CODE':'COM 310',
               'YEAR':'3',
               'TITLE':'Computer Science',
               'LECTURER':'Lec 6 COM',
               'GROUPS':['COM'],
               'ROOM':['DC','LR3','CR-SC']
              },
              {'CODE':'COM 410',
               'YEAR':'4',
               'TITLE':'Data Processing',
               'LECTURER':'Lec 6 COM',
               'GROUPS':['COM'],
               'ROOM':['DC','LR3','CR-SC']
              },
              {'CODE':'COM 320',
               'YEAR':'3',
               'TITLE':'Digital Systems Design',
               'LECTURER':'Lec 7 COM',
               'GROUPS':['COM'],
               'ROOM':['DC','LR3','CR-SC']
              },
              {'CODE':'CSC 123',
               'YEAR':'1',
               'TITLE':'Systems Analysis and Design',
               'LECTURER':'Lec 7 COM',
               'GROUPS':['COM'],
               'ROOM':['DC','LR3','CR-SC']
              },
              {'CODE':'CSC 111',
               'YEAR':'1',
               'TITLE':'Computer Science',
               'LECTURER':'Lec 7 COM',
               'GROUPS':['COM'],
               'ROOM':['SL1','SR22','CR-SC']
              },
              {'CODE':'COM 210',
               'YEAR':'2',
               'TITLE':'Introduction to Computer Sciences',
               'LECTURER':'Lec 4 COM',
               'GROUPS':['COM'],
               'ROOM':['SL1','SR22','CR-SC']
              },
              {'CODE':'COE 120',
               'YEAR':'1',
               'TITLE':'Object Oriented Programming',
               'LECTURER':'Lec 4 COM',
               'GROUPS':['ENG'],
               'ROOM':['DO','FL']
              },
              {'CODE':'STA 224',
               'YEAR':'2',
               'TITLE':'Computational Methods and Data Analysis',
               'LECTURER':'Lec 4 STA',
               'GROUPS':['SC', 'ACS','AST'],
               'ROOM':['LR3','DC','SR18','CR-SC']
              }
             ]

CHE_COURSES =[{'CODE':'CHE 420',
               'YEAR':'4',
               'TITLE':'Research Project',
               'LECTURER':'Lec 1 CHE',
               'GROUPS':['SC','BSE'],
               'ROOM':['SR3']
              },
              {'CODE':'SCH 121',
               'YEAR':'1',
               'TITLE':'Introduction to Carbon Chemistry',
               'LECTURER':'Lec 2 CHE',
               'GROUPS':['SC','BIO',
                         'BSE','BAE', 'EDS',
                         'ED','EDB', 'EDG', 
                         'EDG','EDN', 'AGN'
                        ],
               'ROOM':['SL1','SR22']
              },
              {'CODE':'CHE 318',
               'YEAR':'3',
               'TITLE':'Coordination Chemistry',
               'LECTURER':'Lec 2 CHE',
               'GROUPS':['EDS','EDG', 'EDN'],
               'ROOM':['SR22','CR-SC']
              },              
              {'CODE':'CHE 318',
               'YEAR':'3',
               'TITLE':'Organometallic and Coordination Chemistry',
               'LECTURER':'Lec 2 CHE',
               'GROUPS':['SC','BSE'],
               'ROOM':['DC','SR18']
              },
              {'CODE':'CHE 416',
               'YEAR':'4',
               'TITLE':'Organic Synthesis',
               'LECTURER':'Lec 3 CHE',
               'GROUPS':['SC','BSE'],
               'ROOM':['DC', 'LR3']
              },
              {'CODE':'CHE 212',
               'YEAR':'2',
               'TITLE':'Basic Organic Chemistry',
               'LECTURER':'Lec 3 CHE',
               'GROUPS':['SC','BSE','BIO'],
               'ROOM':['DC', 'LR3']
              },
              {'CODE':'CHE 403',
               'YEAR':'4',
               'TITLE':'Heterocyclic and Stereochemistry',
               'LECTURER':'Lec 4 CHE',
               'GROUPS':['EDS','EDG','EDN'],
               'ROOM':['SR22', 'CR-SC']
              },
              {'CODE':'CHE 203',
               'YEAR':'2',
               'TITLE':'Organic Chemistry II',
               'LECTURER':'Lec 3 CHE',
               'GROUPS':['EDS','EDG','EDN'],
               'ROOM':['SR22', 'CR-SC']
              },
              {'CODE':'CHE 202',
               'YEAR':'2',
               'TITLE':'Chemical Thermodynamics and Phase Equilibria',
               'LECTURER':'Lec 5 CHE',
               'GROUPS':['EDS','EDG','EDN'],
               'ROOM':['SR22', 'CR-SC']
              },
              {'CODE':'CHE 320',
               'YEAR':'3',
               'TITLE':'Industrial Chemistry I',
               'LECTURER':'Lec 5 CHE',
               'GROUPS':['SC','BSE'],
               'ROOM':['DC', 'LR3']
              },
              {'CODE':'CHE 423',
               'YEAR':'4',
               'TITLE':'Medicinal Chemistry',
               'LECTURER':'Lec 4 CHE',
               'GROUPS':['SC','BSE'],
               'ROOM':['DC', 'LR3']
              },
              {'CODE':'CHE 416/CHE 303',
               'YEAR':'4',
               'TITLE':'Organic Synthesis',
               'LECTURER':'Lec 4 CHE',
               'GROUPS':['SC','BSE'],
               'ROOM':['DC', 'LR3']
              },
              {'CODE':'CHE 412',
               'YEAR':'4',
               'TITLE':'Chemistry of Natural Products',
               'LECTURER':'Lec 4 CHE',
               'GROUPS':['EDS','EDG','EDN'],
               'ROOM':['SR22', 'CR-SC']
              },
              {'CODE':'CHE 316',
               'YEAR':'3',
               'TITLE':'Analytical Techniques in Structure Determination I',
               'LECTURER':'Lec 6 CHE',
               'GROUPS':['SC','BSE'],
               'ROOM':['DC', 'LR3']
              },
              {'CODE':'CHE 415',
               'YEAR':'4',
               'TITLE':'Analytical Techniques in Structural Determination II',
               'LECTURER':'Lec 6 CHE',
               'GROUPS':['SC','BSE'],
               'ROOM':['DC', 'LR3']
              },
              {'CODE':'CHE 418',
               'YEAR':'4',
               'TITLE':'Industrial Chemistry II',
               'LECTURER':'Lec 6 CHE',
               'GROUPS':['SC','BSE'],
               'ROOM':['DC', 'LR3']
              },
              {'CODE':'BIO 316',
               'YEAR':'3',
               'TITLE':'Biochemical Endocrinology',
               'LECTURER':'Lec 7 CHE',
               'GROUPS':['BIO'],
               'ROOM':['AH1','DC', 'LR3']
              },
              {'CODE':'BIO 421E',
               'YEAR':'4',
               'TITLE':'Integrated Metabolic Regulation',
               'LECTURER':'Lec 7 CHE',
               'GROUPS':['BIO'],
               'ROOM':['AH1','DC', 'LR3']
              },
              {'CODE':'BIO 415',
               'YEAR':'4',
               'TITLE':'Research Project',
               'LECTURER':'Lec 7 CHE',
               'GROUPS':['BIO'],
               'ROOM':['SR3']
              },
              {'CODE':'BIO 416',
               'YEAR':'4',
               'TITLE':'Biochemical Pharmacology',
               'LECTURER':'Lec 4 CHE',
               'GROUPS':['BIO'],
               'ROOM':['AH1','DC', 'LR3']
              },
              {'CODE':'CHE 417',
               'YEAR':'4',
               'TITLE':'Coordination Chemistry',
               'LECTURER':'Lec 2 CHE',
               'GROUPS':['SC','BSE'],
               'ROOM':['AH1','DC', 'LR3']
              },
              {'CODE':'CHE 321',
               'YEAR':'3',
               'TITLE':'Organic Spectroscopy ',
               'LECTURER':'Lec 3 CHE',
               'GROUPS':['SC','BSE'],
               'ROOM':['SR3','DC', 'LR3']
              },
              {'CODE':'BIO 416',
               'YEAR':'4',
               'TITLE':'Biochemical Pharmacology',
               'LECTURER':'Lec 4 CHE',
               'GROUPS':['BIO'],
               'ROOM':['SR3','DC', 'LR3']
              },
              {'CODE':'CHE 420E',
               'YEAR':'4',
               'TITLE':'Photochemistry',
               'LECTURER':'Lec 6 CHE',
               'GROUPS':['SC','BSE'],
               'ROOM':['SR3','DC', 'LR3']
              },
              {'CODE':'CHE 418',
               'YEAR':'4',
               'TITLE':'Industrial Chemistry II',
               'LECTURER':'Lec 6 CHE',
               'GROUPS':['SC','BSE'],
               'ROOM':['SR3','DC', 'LR3']
              },
              {'CODE':'BIO 121',
               'YEAR':'1',
               'TITLE':'Basic metabolism',
               'LECTURER':'Lec 8 CHE',
               'GROUPS':['BIO'],
               'ROOM':['AH1','SR3']
              },
              {'CODE':'BIO 122',
               'YEAR':'1',
               'TITLE':'Structural Biochemistry',
               'LECTURER':'Lec 9 CHE',
               'GROUPS':['BIO'],
               'ROOM':['AH1','SR3']
              },
              {'CODE':'CHE 213',
               'YEAR':'2',
               'TITLE':'Basic Kinetics and Thermodynamics',
               'LECTURER':'Lec 10 CHE',
               'GROUPS':['SC','BSE',
                         'EDS','EDG','EDN'],
               'ROOM':['SR22', 'CR-SC']
              },
              {'CODE':'CHE 214',
               'YEAR':'2',
               'TITLE':'Biochemistry',
               'LECTURER':'Lec 11 CHE',
               'GROUPS':['SC','BSE',
                         'EDS','EDG','EDN'],
               'ROOM':['SR22', 'CR-SC']
              },
              {'CODE':'BIO 212',
               'YEAR':'2',
               'TITLE':'Basic Metabolism',
               'LECTURER':'Lec 9 CHE',
               'GROUPS':['SC','BSE'],
               'ROOM':['AH1','SR3']
              },
              {'CODE':'BIO 213',
               'YEAR':'2',
               'TITLE':'Basic Biochemistry Techniques',
               'LECTURER':'Lec 9 CHE',
               'GROUPS':['BIO'],
               'ROOM':['AH1','SR3']
              },
              {'CODE':'BIO 315',
               'YEAR':'3',
               'TITLE':'Biochemistry of Carbohydrates ',
               'LECTURER':'Lec 8 CHE',
               'GROUPS':['BIO'],
               'ROOM':['AH1','SR3']
              },
              {'CODE':'CHE 413',
               'YEAR':'3',
               'TITLE':'Environmental hemistry',
               'LECTURER':'Lec 5 CHE',
               'GROUPS':['EDS','EDG','EDN'],
               'ROOM':['SR22', 'CR-SC']
              },
              {'CODE':'BIO 317',
               'YEAR':'3',
               'TITLE':'Medical Biochemistry I',
               'LECTURER':'Lec 12 CHE',
               'GROUPS':['BIO'],
               'ROOM':['AH1','SR3']
              },
              {'CODE':'BIO 318',
               'YEAR':'3',
               'TITLE':'Ecological Biochemistry',
               'LECTURER':'Lec 13 CHE',
               'GROUPS':['BIO'],
               'ROOM':['AH1','SR3']
              },
              {'CODE':'BIO 319',
               'YEAR':'3',
               'TITLE':'Antibiotics',
               'LECTURER':'Lec 14 CHE',
               'GROUPS':['BIO'],
               'ROOM':['AH1','SR3']
              },
              {'CODE':'BIO 320',
               'YEAR':'3',
               'TITLE':'Industrial Attachment',
               'LECTURER':'-',
               'GROUPS':['BIO'],
               'ROOM':['SR3']
              },
              {'CODE':'CHE 306E',
               'YEAR':'3',
               'TITLE':'Biochemistry',
               'LECTURER':'Lec 11 CHE',
               'GROUPS':['EDS','EDG','EDN'],
               'ROOM':['SR22', 'CR-SC']
              },
              {'CODE':'CHE 317',
               'YEAR':'3',
               'TITLE':'Electrochemistry',
               'LECTURER':'Lec 10 CHE',
               'GROUPS':['SC','BSE'],
               'ROOM':['CR-SC','DC', 'LR3']
              },
              {'CODE':'CHE 319',
               'YEAR':'3',
               'TITLE':'Stereochemistry and Conformational Studies',
               'LECTURER':'Lec 15 CHE',
               'GROUPS':['SC','BSE',
                         'EDS','EDG','EDN'],
               'ROOM':['SR22', 'CR-SC']
              },
              {'CODE':'CHE 321',
               'YEAR':'3',
               'TITLE':'Organic Spectroscopy ',
               'LECTURER':'Lec 3 CHE',
               'GROUPS':['SC','BSE'],
               'ROOM':['CR-SC','DC', 'LR3']
              },
              {'CODE':'BIO 417',
               'YEAR':'4',
               'TITLE':'Current Topics in Biochemistry',
               'LECTURER':'Lec 8 CHE',
               'GROUPS':['BIO'],
               'ROOM':['AH1','CR-SC']
              },
              {'CODE':'BIO 418',
               'YEAR':'4',
               'TITLE':'Applied Biochemistry',
               'LECTURER':'Lec 13 CHE',
               'GROUPS':['BIO'],
               'ROOM':['AH1','CR-SC']
              },
              {'CODE':'CHE 413',
               'YEAR':'4',
               'TITLE':'Environmental Chemistry',
               'LECTURER':'Lec 5 CHE',
               'GROUPS':['EDS','EDG','EDN']
              },
              {'CODE':'CHE 419',
               'YEAR':'4',
               'TITLE':'Surface and Colloidal Chemistry',
               'LECTURER':'Lec 16 CHE',
               'GROUPS':['SC','BSE'],
               'ROOM':['SR22', 'CR-SC']
              },
              {'CODE':'CHP 214',
               'YEAR':'2',
               'TITLE':'Organic Chemistry',
               'LECTURER':'Lec 15 CHE',
               'GROUPS':['ENG'],
               'ROOM':['DO','FL1']
              }
             ]


ZOO_COURSES =[{'CODE':'SZL 121',
               'YEAR':'1',
               'TITLE':'Fundamentals of Zoology II',
               'LECTURER':'Lec 1 ZOO',
               'GROUPS':['SC','BIO', 'COM',
                         'BSE','BAE', 'EDS',
                         'ED','EDB', 'EDG', 
                         'EDG','EDN', 'AGN'
                        ],
               'ROOM':['SL1', 'SR22']
              },
              {'CODE':'ZOO 213',
               'YEAR':'2',
               'TITLE':'Introductory Animal Ecology',
               'LECTURER':'Lec 1 ZOO',
               'GROUPS':['SC','BSE','BAE',
                         'EDS','ED','EDB', 
                         'EDG', 'EDG','EDN',
                         'AGN'],
               'ROOM':['SR22', 'CR-SC']
              },
              {'CODE':'ZOO 315',
               'YEAR':'3',
               'TITLE':'Arthropod Biology',
               'LECTURER':'Lec 1 ZOO',
               'GROUPS':['SC','BSE','BAE',
                         'EDS','ED','EDB', 
                         'EDG', 'EDG','EDN',
                         'AGN'],
               'ROOM':['SR22', 'CR-SC']
              },
              {'CODE':'ZOO 421E',
               'YEAR':'2',
               'TITLE':'Parasitology II',
               'LECTURER':'Lec 1 ZOO',
               'GROUPS':['SC','BSE','BAE',
                         'EDS','ED','EDB', 
                         'EDG', 'EDG','EDN',
                         'AGN'],
               'ROOM':['SR22', 'CR-SC']
              },
              {'CODE':'MIC 413',
               'YEAR':'4',
               'TITLE':'Virology',
               'LECTURER':'Lec 2 ZOO',
               'GROUPS':['MIC'],
               'ROOM':['LR3']
              },
              {'CODE':'MIC 121',
               'YEAR':'1',
               'TITLE':'Microbial Ecology',
               'LECTURER':'Lec 3 ZOO',
               'GROUPS':['MIC'],
               'ROOM':['SR3','DC', 'LR3']
              },
              {'CODE':'MIC 416',
               'YEAR':'4',
               'TITLE':'Pathogenic Microorganisms',
               'LECTURER':'Lec 3 ZOO',
               'GROUPS':['MIC'],
               'ROOM':['AH1', 'SR3','LR3','DC']
              },
              {'CODE':'MIC 314',
               'YEAR':'3',
               'TITLE':'Symbiotic Interaction',
               'LECTURER':'Lec 3 ZOO',
               'GROUPS':['MIC'],
               'ROOM':['AH1', 'SR3','LR3','DC']
              },
              {'CODE':'MIC 212',
               'YEAR':'2',
               'TITLE':'Environmental Microbiology',
               'LECTURER':'Lec 4 ZOO',
               'GROUPS':['MIC'],
               'ROOM':['AH1','LR3','DC']
              },
              {'CODE':'MIC 213',
               'YEAR':'2',
               'TITLE':'Cell Biology',
               'LECTURER':'Lec 5 ZOO',
               'GROUPS':['MIC'],
               'ROOM':['AH1','LR3','DC']
              },
              {'CODE':'MIC 214',
               'YEAR':'2',
               'TITLE':'Systematic Microbiology',
               'LECTURER':'Lec 6 ZOO',
               'GROUPS':['MIC'],
               'ROOM':['AH1','LR3','DC']
              },
              {'CODE':'MIC 418',
               'YEAR':'4',
               'TITLE':'Industrial Microbiology',
               'LECTURER':'Lec 4 ZOO',
               'GROUPS':['MIC'],
               'ROOM':['AH1', 'SR3','LR3','DC']
              },
              {'CODE':'MIC 211',
               'YEAR':'2',
               'TITLE':'Microbial Ecology',
               'LECTURER':'Lec 4 ZOO',
               'GROUPS':['MIC'],
               'ROOM':['AH1', 'SR3','LR3','DC']
              },
              {'CODE':'MIC 313',
               'YEAR':'3',
               'TITLE':'Bacteriology',
               'LECTURER':'Lec 7 ZOO',
               'GROUPS':['MIC'],
               'ROOM':['AH1', 'SR3','LR3','DC']
              },
              {'CODE':'MIC 419',
               'YEAR':'4',
               'TITLE':'Molecular Cell Biology',
               'LECTURER':'Lec 7 ZOO',
               'GROUPS':['MIC'],
               'ROOM':['AH1', 'SR3','LR3','DC']
              },
              {'CODE':'ZOO 316',
               'YEAR':'3',
               'TITLE':'Vertebrate Zoology II',
               'LECTURER':'Lec 8 ZOO',
               'GROUPS':['SC','BSE'],
               'ROOM':['SR3', 'SR18']
              },
              {'CODE':'ZOO 414/ZOO 418E',
               'YEAR':'4',
               'TITLE':'Terrestrial Ecology II/Applied Terrestrial Ecology',
               'LECTURER':'Lec 8 ZOO',
               'GROUPS':['SC','BSE'],
               'ROOM':['AH1', 'SR3','LR3','DC']
              },
              {'CODE':'MIC 417/BOT 419/BOT 426E',
               'YEAR':'4',
               'TITLE':'Applied Microbiology/ Advanced Microbiology',
               'LECTURER':'Lec 8 ZOO',
               'GROUPS':['SC','BSE'],
               'ROOM':['AH1', 'SR3','LR3','DC']
              },
              {'CODE':'MIC 415',
               'YEAR':'4',
               'TITLE':'Biotechnology',
               'LECTURER':'Lec 9 ZOO',
               'GROUPS':['MIC'],
               'ROOM':['AH1','LR3','DC']
              },
              {'CODE':'MIC 215',
               'YEAR':'2',
               'TITLE':'Microbial Physiology',
               'LECTURER':'Lec 10 ZOO',
               'GROUPS':['MIC'],
               'ROOM':['AH1','LR3','DC']
              },
              {'CODE':'ZOO 415',
               'YEAR':'4',
               'TITLE':'History and Philosophy of Biology',
               'LECTURER':'Lec 10 ZOO',
               'GROUPS':['SC','BSE'],
               'ROOM':['AH1','LR3','DC']
              },
              {'CODE':'ZOO 417',
               'YEAR':'4',
               'TITLE':'Physiology I',
               'LECTURER':'Lec 10 ZOO',
               'GROUPS':['SC','BSE'],
               'ROOM':['AH1', 'LR3','DC']
              },
              {'CODE':'MIC 414',
               'YEAR':'4',
               'TITLE':'Molecular Genetics',
               'LECTURER':'Lec 10 ZOO',
               'GROUPS':['MIC'],
               'ROOM':['AH1', 'LR3','DC']
              },
              {'CODE':'ZOO 422/ZOO 422E',
               'YEAR':'4',
               'TITLE':'Physiology II',
               'LECTURER':'Lec 11 ZOO',
               'GROUPS':['SC','BSE'],
               'ROOM':['AH1', 'LR3','DC']
              },
              {'CODE':'ZOO 314',
               'YEAR':'3',
               'TITLE':'Environmental Physiology/Physiology I',
               'LECTURER':'Lec 11 ZOO',
               'GROUPS':['SC','BSE'],
               'ROOM':['AH1','LR3','DC']
              },
              {'CODE':'ZOO 212',
               'YEAR':'2',
               'TITLE':'Vertebrate Zoology I',
               'LECTURER':'Lec 11 ZOO',
               'GROUPS':['SC','BSE'],
               'ROOM':['AH1','LR3','DC']
              },
              {'CODE':'ZOO 220',
               'YEAR':'2',
               'TITLE':'Developmental Biology and Animal Physiology',
               'LECTURER':'Lec 11 ZOO',
               'GROUPS':['SC','BSE'],
               'ROOM':['AH1', 'SR3','LR3','DC']
              },
              {'CODE':'ZOO 318E',
               'YEAR':'3',
               'TITLE':'Comparative Endocrinology',
               'LECTURER':'Lec 12 ZOO',
               'GROUPS':['SC','BSE'],
               'ROOM':['AH1', 'SR3','LR3','DC']
              },
              {'CODE':'ZOO 321E',
               'YEAR':'3',
               'TITLE':'Introduction to Immunology',
               'LECTURER':'Lec 12 ZOO',
               'GROUPS':['SC','BSE'],
               'ROOM':['SR3', 'SR18']
              },
              {'CODE':'ZOO 427',
               'YEAR':'4',
               'TITLE':'Evolutionary Biology',
               'LECTURER':'Lec 12 ZOO',
               'GROUPS':['SC','BSE'],
               'ROOM':['AH1', 'LR3','DC']
              },
              {'CODE':'ZOO 419/MIC 420/BZE 410/BOT 421',
               'YEAR':'4',
               'TITLE':'Research Project',
               'LECTURER':'Lec 12 ZOO',
               'GROUPS':['SC','BSE'],
               'ROOM':['SR3']
              }
             ]



BOT_COURSES =[{'CODE':'SBT 121',
               'YEAR':'1',
               'TITLE':'Fundamentals of Botany 11',
               'LECTURER':'Lec 1 BOT',
               'GROUPS':['SC','BIO',
                         'BSE','BAE', 'EDS',
                         'ED','EDB', 'EDG', 
                         'EDG','EDN', 'AGN'
                        ],
               'ROOM':['SL1', 'SR22']
              },
              {'CODE':'ZOO 317/BOT 319/BZE 310/BOT 325',
               'YEAR':'3',
               'TITLE':'Zoology Field Course, Biology field course/Botany field Course',
               'LECTURER':'Lec 1 BOT',
               'GROUPS':['SC', 'BSE'],
               'ROOM':['AH1', 'SR3','LR3','DC']
              },
              {'CODE':'BOT 320',
               'YEAR':'3',
               'TITLE':'Mycology',
               'LECTURER':'Lec 4 ZOO',
               'GROUPS':['SC','BSE'],
               'ROOM':['AH1', 'SR3','LR3','DC']
              },
              {'CODE':'BOT 211',
               'YEAR':'2',
               'TITLE':'Plant Structure and Function',
               'LECTURER':'Lec 7 ZOO',
               'GROUPS':['SC','BSE'],
               'ROOM':['AH1', 'SR3','LR3','DC']
              },
              {'CODE':'BOT 317',
               'YEAR':'3',
               'TITLE':'Cytogenetics',
               'LECTURER':'Lec 7 ZOO',
               'GROUPS':['SC','BSE'],
               'ROOM':['AH1', 'SR3','LR3','DC']
              },
              {'CODE':'BOT 425',
               'YEAR':'4',
               'TITLE':'Conservation and Management of Natural Resource and Ethology',
               'LECTURER':'Lec 8 ZOO',
               'GROUPS':['SC','BSE'],
               'ROOM':['AH1', 'SR3','LR3','DC']
              },
              {'CODE':'BOT 212 / BOT 212E',
               'YEAR':'2',
               'TITLE':'Plant Ecology',
               'LECTURER':'Lec 9 ZOO',
               'GROUPS':['SC','BSE'],
               'ROOM':['AH1', 'SR3','LR3','DC']
              },
              {'CODE':'BOT 324',
               'YEAR':'3',
               'TITLE':'Advanced Ecology',
               'LECTURER':'Lec 5 ZOO',
               'GROUPS':['SC','BSE'],
               'ROOM':['AH1','LR3','DC']
              },
              {'CODE':'BOT 412/ BOT 412E',
               'YEAR':'4',
               'TITLE':'Biosystematics',
               'LECTURER':'Lec 2 BOT',
               'GROUPS':['SC','BSE'],
               'ROOM':['AH1','LR3','DC']
              },
              {'CODE':'BOT 415',
               'YEAR':'4',
               'TITLE':'Plant Physiology II',
               'LECTURER':'Lec 2 BOT',
               'GROUPS':['SC','BSE'],
               'ROOM':['AH1','LR3','DC']
              },
              {'CODE':'BOT 313',
               'YEAR':'3',
               'TITLE':'Plant Physiology',
               'LECTURER':'Lec 5 ZOO',
               'GROUPS':['SC','BSE'],
               'ROOM':['AH1','LR3','DC']
              },
              {'CODE':'BOT 220',
               'YEAR':'2',
               'TITLE':'Developmental Biology and Physiology',
               'LECTURER':'Lec 1 BOT',
               'GROUPS':['SC','BSE'],
               'ROOM':['AH1', 'SR3','LR3','DC']
              }
             ]
COMMON_COURSES =[{'CODE':'SBE 121',
               'YEAR':'1',
               'TITLE':'Introduction to Entrepreneurship',
               'LECTURER':'Lec 1 UCU',
               'GROUPS':['SC','BIO','MIC'],
               'ROOM':['SL1', 'SR22']
              },
              {'CODE':'IRD 400',
               'YEAR':'4',
               'TITLE':'Development Project Appraisal',
               'LECTURER':'Lec 2 UCU',
               'GROUPS':['SC', 'COM','BIO', 'MIC', 'BSE'],
               'ROOM':['SL1', 'SR22']
              }
             ]


def get_course_data_frame(subject_courses):
    df_subject_courses = [pd.DataFrame([subject_courses[i]]) 
                          for i in range(len(subject_courses))]
    return pd.concat(df_subject_courses)


df_mat_courses = get_course_data_frame(MAT_COURSES)
df_phy_courses = get_course_data_frame(PHY_COURSES)
df_sta_courses = get_course_data_frame(STA_COURSES)
df_acs_courses = get_course_data_frame(ACS_COURSES)
df_com_courses = get_course_data_frame(COM_COURSES)
df_che_courses  = get_course_data_frame(CHE_COURSES)
df_bot_courses  = get_course_data_frame(BOT_COURSES)
df_zoo_courses  = get_course_data_frame(ZOO_COURSES)
df_pg_courses  = get_course_data_frame(PG_COURSES)
df_common_courses  = get_course_data_frame(COMMON_COURSES)

df_courses = [df_mat_courses, df_phy_courses, df_sta_courses, df_acs_courses, 
              df_com_courses, df_che_courses,df_bot_courses,df_zoo_courses,
              df_pg_courses, df_common_courses]

COM_codes = df_com_courses.loc[:,"CODE"].values
ACS_codes = df_acs_courses.loc[:,"CODE"].values
STA_codes = df_sta_courses.loc[:,"CODE"].values
MAT_codes = df_mat_courses.loc[:,"CODE"].values
PHY_codes = df_phy_courses.loc[:,"CODE"].values
CHE_codes = df_che_courses.loc[:,"CODE"].values
BOT_codes = df_bot_courses.loc[:,"CODE"].values
ZOO_codes = df_zoo_courses.loc[:,"CODE"].values
PG_codes = df_pg_courses.loc[:,"CODE"].values
COMMON_codes = df_common_courses.loc[:,"CODE"].values

course_codes = [COM_codes, ACS_codes, STA_codes, MAT_codes, PHY_codes,
                CHE_codes, BOT_codes, ZOO_codes, PG_codes, COMMON_codes]

COM_lecturers = df_com_courses.loc[:,"LECTURER"].values
ACS_lecturers = df_acs_courses.loc[:,"LECTURER"].values
STA_lecturers = df_sta_courses.loc[:,"LECTURER"].values
MAT_lecturers = df_mat_courses.loc[:,"LECTURER"].values
PHY_lecturers = df_phy_courses.loc[:,"LECTURER"].values
CHE_lecturers = df_che_courses.loc[:,"LECTURER"].values
BOT_lecturers = df_bot_courses.loc[:,"LECTURER"].values
ZOO_lecturers = df_zoo_courses.loc[:,"LECTURER"].values
PG_lecturers = df_pg_courses.loc[:,"LECTURER"].values
COMMON_lecturers = df_common_courses.loc[:,"LECTURER"].values

course_lecturers = [list(COM_lecturers), list(ACS_lecturers), list(STA_lecturers), 
                    list(MAT_lecturers), list(PHY_lecturers), list(CHE_lecturers),
                    list(BOT_lecturers),list(ZOO_lecturers),list(PG_lecturers), 
                    list(COMMON_lecturers)]

COM_years = df_com_courses.loc[:,"YEAR"].values
ACS_years = df_acs_courses.loc[:,"YEAR"].values
STA_years = df_sta_courses.loc[:,"YEAR"].values
MAT_years = df_mat_courses.loc[:,"YEAR"].values
PHY_years = df_phy_courses.loc[:,"YEAR"].values
CHE_years = df_che_courses.loc[:,"YEAR"].values
BOT_years = df_bot_courses.loc[:,"YEAR"].values
ZOO_years = df_zoo_courses.loc[:,"YEAR"].values
PG_years = df_pg_courses.loc[:,"YEAR"].values
COMMON_years = df_common_courses.loc[:,"YEAR"].values

course_years = [list(COM_years), list(ACS_years), list(STA_years),
                list(MAT_years), list(PHY_years), list(CHE_years), 
                list(BOT_years),list(ZOO_years),list(PG_years),
                list(COMMON_years) ]

COM_groups = df_com_courses.loc[:,"GROUPS"].values 
ACS_groups = df_acs_courses.loc[:,"GROUPS"].values
STA_groups = df_sta_courses.loc[:,"GROUPS"].values
MAT_groups = df_mat_courses.loc[:,"GROUPS"].values
PHY_groups = df_phy_courses.loc[:,"GROUPS"].values
CHE_groups = df_che_courses.loc[:,"GROUPS"].values
BOT_groups = df_bot_courses.loc[:,"GROUPS"].values
ZOO_groups = df_zoo_courses.loc[:,"GROUPS"].values
PG_groups = df_pg_courses.loc[:,"GROUPS"].values
COMMON_groups = df_common_courses.loc[:,"GROUPS"].values

course_groups = [list(COM_groups), list(ACS_groups), list(STA_groups),
                 list(MAT_groups), list(PHY_groups), list(CHE_groups), 
                 list(BOT_groups),list(ZOO_groups),list(PG_groups), 
                 list(COMMON_groups)]

COM_rooms = df_com_courses.loc[:,"ROOM"].values 
ACS_rooms = df_acs_courses.loc[:,"ROOM"].values
STA_rooms = df_sta_courses.loc[:,"ROOM"].values
MAT_rooms = df_mat_courses.loc[:,"ROOM"].values
PHY_rooms = df_phy_courses.loc[:,"ROOM"].values
CHE_rooms = df_che_courses.loc[:,"ROOM"].values
BOT_rooms = df_bot_courses.loc[:,"ROOM"].values
ZOO_rooms = df_zoo_courses.loc[:,"ROOM"].values
PG_rooms = df_pg_courses.loc[:,"ROOM"].values
COMMON_rooms = df_common_courses.loc[:,"ROOM"].values

course_rooms = [list(COM_rooms), list(ACS_rooms), list(STA_rooms),
                list(MAT_rooms), list(PHY_rooms), list(CHE_rooms), 
                list(BOT_rooms),list(ZOO_rooms),list(PG_rooms), 
                list(COMMON_rooms)]

COM_titles = df_com_courses.loc[:,"TITLE"].values 
ACS_titles = df_acs_courses.loc[:,"TITLE"].values
STA_titles = df_sta_courses.loc[:,"TITLE"].values
MAT_titles = df_mat_courses.loc[:,"TITLE"].values
PHY_titles = df_phy_courses.loc[:,"TITLE"].values
CHE_titles = df_che_courses.loc[:,"TITLE"].values
BOT_titles = df_bot_courses.loc[:,"TITLE"].values
ZOO_titles = df_zoo_courses.loc[:,"TITLE"].values
PG_titles = df_pg_courses.loc[:,"TITLE"].values
COMMON_titles = df_common_courses.loc[:,"TITLE"].values

course_titles = [list(COM_titles), list(ACS_titles), list(STA_titles),
                 list(MAT_titles), list(PHY_titles), list(CHE_titles), 
                 list(BOT_titles),list(ZOO_titles),list(PG_titles), 
                 list(COMMON_titles)]
