#
# Test/test_expectations.py
# jParser
#
# Written by Firsov Georgy
# Copyright © 2019 Firsov Georgy. All rights reserved.
# Licensed with GNU GPL v3
#

# JSON sources:
#   - https://opensource.adobe.com/Spry/samples/data_region/JSONDataSetSample.html
#   - https://json.org/example.html
#   - https://www.javatpoint.com/json-example

# ----------------------------------------   ! WARNING !   ---------------------------------------- #
#                           Just don't try to read this. Save your eyes!                            #
#                             These objects are necessary for testing.                              #
# ------------------------------------------------------------------------------------------------- #

expected_1 = \
    [
        {
            'id': '0001',
            'type': 'donut',
            'name': 'Cake',
            'ppu': 0.55,
            'batters':
                {
                    'batter':
                        [
                            {
                                'id': '1001',
                                'type': 'Regular'
                            },
                            {
                                'id': '1002',
                                'type': 'Chocolate'
                            },
                            {
                                'id': '1003',
                                'type': 'Blueberry'
                            },
                            {
                                'id': '1004',
                                'type': "Devil's Food"
                            }
                        ]
                },
            'topping':
                [
                    {
                        'id': '5001',
                        'type': 'None'
                    },
                    {
                        'id': '5002',
                        'type': 'Glazed'
                    },
                    {
                        'id': '5005',
                        'type': 'Sugar'
                    },
                    {
                        'id': '5007',
                        'type': 'Powdered Sugar'
                    },
                    {
                        'id': '5006',
                        'type': 'Chocolate with Sprinkles'
                    },
                    {
                        'id': '5003',
                        'type': 'Chocolate'
                    },
                    {
                        'id': '5004',
                        'type': 'Maple'
                    }
                ]
        },
        {
            'id': '0002',
            'type': 'donut',
            'name': 'Raised',
            'ppu': 0.55,
            'batters':
                {
                    'batter':
                        [
                            {
                                'id': '1001',
                                'type': 'Regular'
                            }
                        ]
                },
            'topping':
                [
                    {
                        'id': '5001',
                        'type': 'None'
                    },
                    {
                        'id': '5002',
                        'type': 'Glazed'
                    },
                    {
                        'id': '5005',
                        'type': 'Sugar'
                    },
                    {
                        'id': '5003',
                        'type': 'Chocolate'
                    },
                    {
                        'id': '5004', 'type': 'Maple'
                    }
                ]
        },
        {
            'id': '0003',
            'type': 'donut',
            'name': 'Old Fashioned',
            'ppu': 0.55,
            'batters':
                {
                    'batter':
                        [
                            {
                                'id': '1001',
                                'type': 'Regular'
                            },
                            {
                                'id': '1002',
                                'type': 'Chocolate'
                            }
                        ]
                },
            'topping':
                [
                    {
                        'id': '5001',
                        'type': 'None'},
                    {
                        'id': '5002',
                        'type': 'Glazed'
                    },
                    {
                        'id': '5003',
                        'type': 'Chocolate'
                    },
                    {
                        'id': '5004',
                        'type': 'Maple'
                    }
                ]
        }
    ]

expected_2 = \
    [
        {
            'color': 'red',
            'value': '#f00'
        },
        {
            'color': 'green',
            'value': '#0f0'
        },
        {
            'color': 'blue',
            'value': '#00f'
        },
        {
            'color': 'cyan',
            'value': '#0ff'
        },
        {
            'color': 'magenta',
            'value': '#f0f'
        },
        {
            'color': 'yellow',
            'value': '#ff0'
        },
        {
            'color': 'black',
            'value': '#000'
        }
    ]


expected_3 = \
    {
        'id': '0001',
        'type': 'donut',
        'name': 'Cake',
        'image':
            {
                'url': 'images/0001.jpg',
                'width': 200,
                'height': 200
            },
        'thumbnail':
            {
                'url': 'images/thumbnails/0001.jpg',
                'width': 32,
                'height': 32
            }
    }

expected_4 = \
    {
        'markers':
            [
                {
                    'name': 'Rixos The Palm Dubai',
                    'position': [25.1212, 55.1535]
                },
                {
                    'name': 'Shangri-La Hotel',
                    'location': [25.2084, 55.2719]
                },
                {
                    'name': 'Grand Hyatt',
                    'location': [25.2285, 55.3273]
                }
            ]
    }

expected_5 = \
    {
        'destination_addresses':
            [
                'Washington, DC, USA', 'Philadelphia, PA, USA', 'Santa Barbara, CA, USA',
                'Miami, FL, USA', 'Austin, TX, USA', 'Napa County, CA, USA'
            ],
        'origin_addresses':
            ['New York, NY, USA'],
        'rows':
            [
                {
                    'elements':
                        [
                            {
                                'distance':
                                    {
                                        'text': '227 mi',
                                        'value': 365468
                                    },
                                'duration':
                                    {
                                        'text': '3 hours 54 mins',
                                        'value': 14064
                                    },
                                'status': 'OK'
                            },
                            {
                                'distance':
                                    {
                                        'text': '94.6 mi',
                                        'value': 152193
                                    },
                                'duration':
                                    {
                                        'text': '1 hour 44 mins',
                                        'value': 6227
                                    },
                                'status': 'OK'
                            },
                            {
                                'distance':
                                    {
                                        'text': '2,878 mi',
                                        'value': 4632197
                                    },
                                'duration':
                                    {
                                        'text': '1 day 18 hours',
                                        'value': 151772
                                    },
                                'status': 'OK'
                            },
                            {
                                'distance':
                                    {
                                        'text': '1,286 mi',
                                        'value': 2069031
                                    },
                                'duration':
                                    {
                                        'text': '18 hours 43 mins',
                                        'value': 67405
                                    },
                                'status': 'OK'
                            },
                            {
                                'distance':
                                    {
                                        'text': '1,742 mi',
                                        'value': 2802972
                                    },
                                'duration':
                                    {
                                        'text': '1 day 2 hours',
                                        'value': 93070
                                    },
                                'status': 'OK'
                            },
                            {
                                'distance':
                                    {
                                        'text': '2,871 mi',
                                        'value': 4620514
                                    },
                                'duration':
                                    {
                                        'text': '1 day 18 hours',
                                        'value': 152913
                                    },
                                'status': 'OK'
                            }
                        ]
                }
            ],
        'status': 'OK'
    }

expected_6 = \
    {
        'medications':
            [
                {
                    'aceInhibitors':
                        [
                            {
                                'name': 'lisinopril',
                                'strength': '10 mg Tab',
                                'dose': '1 tab',
                                'route': 'PO',
                                'sig': 'daily',
                                'pillCount': '#90',
                                'refills': 'Refill 3'
                            }
                        ],
                    'antianginal':
                        [
                            {
                                'name': 'nitroglycerin',
                                'strength': '0.4 mg Sublingual Tab',
                                'dose': '1 tab',
                                'route': 'SL',
                                'sig': 'q15min PRN',
                                'pillCount': '#30',
                                'refills': 'Refill 1'
                            }
                        ],
                    'anticoagulants':
                        [
                            {
                                'name': 'warfarin sodium',
                                'strength': '3 mg Tab',
                                'dose': '1 tab',
                                'route': 'PO',
                                'sig': 'daily',
                                'pillCount': '#90',
                                'refills': 'Refill 3'
                            }
                        ],
                    'betaBlocker':
                        [
                            {
                                'name': 'metoprolol tartrate',
                                'strength': '25 mg Tab',
                                'dose': '1 tab',
                                'route': 'PO',
                                'sig': 'daily',
                                'pillCount': '#90',
                                'refills': 'Refill 3'
                            }
                        ],
                    'diuretic':
                        [
                            {
                                'name': 'furosemide',
                                'strength': '40 mg Tab',
                                'dose': '1 tab',
                                'route': 'PO',
                                'sig': 'daily',
                                'pillCount': '#90',
                                'refills': 'Refill 3'
                            }
                        ],
                    'mineral':
                        [
                            {
                                'name': 'potassium chloride ER',
                                'strength': '10 mEq Tab',
                                'dose': '1 tab',
                                'route': 'PO',
                                'sig': 'daily',
                                'pillCount': '#90',
                                'refills': 'Refill 3'
                            }
                        ]
                }
            ],
        'labs':
            [
                {
                    'name': 'Arterial Blood Gas',
                    'time': 'Today',
                    'location': 'Main Hospital Lab'
                },
                {
                    'name': 'BMP',
                    'time': 'Today',
                    'location': 'Primary Care Clinic'
                },
                {
                    'name': 'BNP',
                    'time': '3 Weeks',
                    'location': 'Primary Care Clinic'
                },
                {
                    'name': 'BUN',
                    'time': '1 Year',
                    'location': 'Primary Care Clinic'
                },
                {
                    'name': 'Cardiac Enzymes',
                    'time': 'Today',
                    'location': 'Primary Care Clinic'
                },
                {
                    'name': 'CBC',
                    'time': '1 Year',
                    'location': 'Primary Care Clinic'
                },
                {
                    'name': 'Creatinine',
                    'time': '1 Year',
                    'location': 'Main Hospital Lab'
                },
                {
                    'name': 'Electrolyte Panel',
                    'time': '1 Year',
                    'location': 'Primary Care Clinic'
                },
                {
                    'name': 'Glucose',
                    'time': '1 Year',
                    'location': 'Main Hospital Lab'
                },
                {
                    'name': 'PT/INR',
                    'time': '3 Weeks',
                    'location': 'Primary Care Clinic'
                },
                {
                    'name': 'PTT',
                    'time': '3 Weeks',
                    'location': 'Coumadin Clinic'
                },
                {
                    'name': 'TSH',
                    'time': '1 Year',
                    'location': 'Primary Care Clinic'
                }
            ],
        'imaging':
            [
                {
                    'name': 'Chest X-Ray',
                    'time': 'Today',
                    'location': 'Main Hospital Radiology'
                },
                {
                    'name': 'Chest X-Ray',
                    'time': 'Today',
                    'location': 'Main Hospital Radiology'
                },
                {
                    'name': 'Chest X-Ray',
                    'time': 'Today',
                    'location': 'Main Hospital Radiology'
                }
            ]
    }

expected_7 = \
    {
        'web-app':
            {
                'servlet':
                    [
                        {
                            'servlet-name': 'cofaxCDS',
                            'servlet-class': 'org.cofax.cds.CDSServlet',
                            'init-param':
                                {
                                    'configGlossary:installationAt': 'Philadelphia, PA',
                                    'configGlossary:adminEmail': 'ksm@pobox.com',
                                    'configGlossary:poweredBy': 'Cofax',
                                    'configGlossary:poweredByIcon': '/images/cofax.gif',
                                    'configGlossary:staticPath': '/content/static',
                                    'templateProcessorClass': 'org.cofax.WysiwygTemplate',
                                    'templateLoaderClass': 'org.cofax.FilesTemplateLoader',
                                    'templatePath': 'templates',
                                    'templateOverridePath': '',
                                    'defaultListTemplate': 'listTemplate.htm',
                                    'defaultFileTemplate': 'articleTemplate.htm',
                                    'useJSP': False,
                                    'jspListTemplate': 'listTemplate.jsp',
                                    'jspFileTemplate': 'articleTemplate.jsp',
                                    'cachePackageTagsTrack': 200,
                                    'cachePackageTagsStore': 200,
                                    'cachePackageTagsRefresh': 60,
                                    'cacheTemplatesTrack': 100,
                                    'cacheTemplatesStore': 50,
                                    'cacheTemplatesRefresh': 15,
                                    'cachePagesTrack': 200,
                                    'cachePagesStore': 100,
                                    'cachePagesRefresh': 10,
                                    'cachePagesDirtyRead': 10,
                                    'searchEngineListTemplate': 'forSearchEnginesList.htm',
                                    'searchEngineFileTemplate': 'forSearchEngines.htm',
                                    'searchEngineRobotsDb': 'WEB-INF/robots.db',
                                    'useDataStore': True,
                                    'dataStoreClass': 'org.cofax.SqlDataStore',
                                    'redirectionClass': 'org.cofax.SqlRedirection',
                                    'dataStoreName': 'cofax',
                                    'dataStoreDriver': 'com.microsoft.jdbc.sqlserver.SQLServerDriver',
                                    'dataStoreUrl': 'jdbc:microsoft:sqlserver://LOCALHOST:1433;DatabaseName=goon',
                                    'dataStoreUser': 'sa',
                                    'dataStorePassword': 'dataStoreTestQuery',
                                    'dataStoreTestQuery': "SET NOCOUNT ON;select test='test';",
                                    'dataStoreLogFile': '/usr/local/tomcat/logs/datastore.log',
                                    'dataStoreInitConns': 10,
                                    'dataStoreMaxConns': 100,
                                    'dataStoreConnUsageLimit': 100,
                                    'dataStoreLogLevel': 'debug',
                                    'maxUrlLength': 500
                                }
                        },
                        {
                            'servlet-name': 'cofaxEmail',
                            'servlet-class': 'org.cofax.cds.EmailServlet',
                            'init-param':
                                {
                                    'mailHost': 'mail1',
                                    'mailHostOverride': 'mail2'
                                }
                        },
                        {
                            'servlet-name': 'cofaxAdmin',
                            'servlet-class': 'org.cofax.cds.AdminServlet'
                        },
                        {
                            'servlet-name': 'fileServlet',
                            'servlet-class': 'org.cofax.cds.FileServlet'
                        },
                        {
                            'servlet-name': 'cofaxTools',
                            'servlet-class': 'org.cofax.cms.CofaxToolsServlet',
                            'init-param':
                                {
                                    'templatePath': 'toolstemplates/',
                                    'log': 1,
                                    'logLocation': '/usr/local/tomcat/logs/CofaxTools.log',
                                    'logMaxSize': '',
                                    'dataLog': 1,
                                    'dataLogLocation': '/usr/local/tomcat/logs/dataLog.log',
                                    'dataLogMaxSize': '',
                                    'removePageCache': '/content/admin/remove?cache=pages&id=',
                                    'removeTemplateCache': '/content/admin/remove?cache=templates&id=',
                                    'fileTransferFolder': '/usr/local/tomcat/webapps/content/fileTransferFolder',
                                    'lookInContext': 1,
                                    'adminGroupID': 4,
                                    'betaServer': True
                                }
                        }
                    ],
                'servlet-mapping':
                    {
                        'cofaxCDS': '/',
                        'cofaxEmail': '/cofaxutil/aemail/*',
                        'cofaxAdmin': '/admin/*',
                        'fileServlet': '/static/*',
                        'cofaxTools': '/tools/*'
                    },
                'taglib':
                    {
                        'taglib-uri': 'cofax.tld',
                        'taglib-location': '/WEB-INF/tlds/cofax.tld'
                    }
            }
    }
