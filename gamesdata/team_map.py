def team_mapper(name):
    if name.split()[-1] == 'St':
        return ' '.join(name.split()[:-1]) + ' State'
    if name == 'Cinci':
        return 'Cincinnati'
    if name == 'Miami-Florida' or name == 'Miami-FL':
        return 'Miami (FL)'
    if name == 'Miss St' or name == 'Mississippi St' or name == 'Miss State':
        return 'Mississippi State'
    if name == 'North Carolina St':
        return 'North Carolina State'
    if name == 'Pitt':
        return 'Pittsburgh'
    if name == 'Southern Cal':
        return 'USC'
    if name == 'UConn':
        return 'Connecticut'
    if name == 'UNCW':
        return 'UNC Wilmington'
    if name == 'Boston U':
        return 'Boston University'
    if name == 'Central Conn':
        return 'Central Connecticut State'
    if name == 'Cal':
        return 'California'
    if name == 'Creigh':
        return 'Creighton'
    if name == 'Florida Atl':
        return 'Florida Atlantic'
    if name == 'Illinois-Chi':
        return 'Illinois-Chicago'
    if name == 'Pennsylvania':
        return 'Penn'
    if name == 'SIU' or name == 'Southern Ill':
        return 'Southern Illinois'
    if name == 'W Forest':
        return 'Wake Forest'
    if name == 'Western Ky':
        return 'Western Kentucky'
    if name == 'Wis':
        return 'Wisconsin'
    if name == 'ND':
        return 'Notre Dame'
    if name == 'Ariz State':
        return 'Arizona State'
    if name == 'CMU' or name == 'Central Mich':
        return 'Central Michigan'
    if name == 'East Tenn State':
        return 'East Tennessee State'
    if name == 'Louis':
        return 'Louisville'
    if name == 'Marq':
        return 'Marquette'
    if name == 'Mich State':
        return 'Michigan State'
    if name == 'Okla State':
        return 'Oklahoma State'
    if name == 'Sam Houston':
        return 'Sam Houston State'
    if name == 'Troy':
        return 'Troy State'
    if name == 'UNCA':
        return 'UNC Asheville'
    if name == 'Wis-Milwaukee':
        return 'Milwaukee'
    if name == "St. Joseph's" or name == 'St Joe':
        return "Saint Joseph's"
    if name == 'BC':
        return 'Boston College'
    if name == 'Eastern Wash':
        return 'Eastern Washington'
    if name == 'Ga Tech':
        return 'Georgia Tech'
    if name == 'TX Tech':
        return 'Texas Tech'
    if name == 'TX-San Antonio':
        return 'UTSA'
    if name == 'UL-Lafayette':
        return 'Louisiana Lafayette'
    if name == 'UNC':
        return 'North Carolina'
    if name == 'Vandy':
        return 'Vanderbilt'
    if name == 'Western Mich':
        return 'Western Michigan'
    if name == 'Manh':
        return 'Manhattan'
    if name == 'FAMU':
        return 'Florida A&M'
    if name == 'SHU':
        return 'Seton Hall'
    if name == 'Eastern Ky':
        return 'Eastern Kentucky'
    if name == "G'town":
        return 'Georgetown'
    if name == 'George Wash':
        return 'George Washington'
    if name == 'Long Beach':
        return 'Long Beach State'
    if name == 'Miami-Ohio':
        return 'Miami OH'
    if name == 'TAMU-CC':
        return 'Texas A&M-Corpus Christi'
    if name == 'TX A&M':
        return 'Texas A&M'
    if name == 'Tenn':
        return 'Tennessee'
    if name == 'Va Tech':
        return 'Virginia Tech'
    if name == 'Wash State':
        return 'Washington State'
    if name == "St. Mary's":
        return "Saint Mary's"
    if name == 'Nova':
        return 'Villanova'
    if name == 'SE Louisiana':
        return 'Southeastern Louisiana'
    if name == 'Wash':
        return 'Washington'
    if name == 'West Va':
        return 'West Virginia'
    if name == 'Wis-Mil':
        return 'Milwaukee'
    if name == 'GMU':
        return 'George Mason'
    if name == 'GWU':
        return 'George Washington'
    if name == 'NW State':
        return 'Northwestern State'
    if name == 'Southern U':
        return 'Southern'
    if name == 'Wich State':
        return 'Wichita State'
    if name == 'Ark-PB' or name == 'Ark-Pine Bluff':
        return 'Arkansas Pine Bluff'
    if name == 'Kan State':
        return 'Kansas State'
    if name == 'Murray':
        return 'Murray State'
    if name == 'N Iowa':
        return 'Northern Iowa'
    if name == 'ODU':
        return 'Old Dominion'
    if name == 'St Mary':
        return "Saint Mary's"
    if name == 'UNM':
        return 'New Mexico'
    if name == 'CS Fullerton':
        return 'Cal State Fullerton'
    if name == 'MSM' or name == "Mt St. Mary's":
        return "Mount St. Mary's"
    if name == 'Miss Valley State':
        return 'Mississippi Valley State'
    if name == 'SD':
        return 'San Diego'
    if name == 'TX-Arlington':
        return 'UT Arlington'
    if name == 'WKU':
        return 'Western Kentucky'
    if name == 'CS Northridge':
        return 'Cal State Northridge'
    if name == 'Cleve State':
        return 'Cleveland State'
    if name == 'Morehead':
        return 'Morehead State'
    if name == 'Ark-Little Rock' or name == 'Ark-LR':
        return 'Arkansas Little Rock'
    if name == 'Fla State':
        return 'Florida State'
    if name == 'Long Island':
        return 'LIU Brooklyn'
    if name == 'Norf State':
        return 'Norfolk State'
    if name == 'St Louis':
        return 'Saint Louis'
    if name == 'USF':
        return 'South Florida'
    if name == 'TX-SA':
        return 'UTSA'
    if name == "St. Peter's":
        return "Saint Peter's"
    if name == 'SD State':
        return "San Diego State"
    if name == 'Loyola-Maryland':
        return 'Loyola MD'
    if name == 'FGCU':
        return 'Florida Gulf Coast'
    if name == 'JMU':
        return 'James Madison'
    if name == 'Middle Tenn State':
        return 'Middle Tennessee'
    if name == 'Minn':
        return "Minnesota"
    if name == 'NC A&T':
        return "North Carolina A&T"
    if name == 'Ole Miss':
        return 'Mississippi'
    if name == 'Colo State':
        return 'Colorado State'
    if name == 'NCCU':
        return 'North Carolina Central'
    if name == 'ND State':
        return 'North Dakota State'
    if name == 'SFA':
        return 'Stephen F. Austin'
    if name == 'Ga State':
        return 'Georgia State'
    if name == 'Rbt Mor':
        return 'Robert Morris'
    if name == 'CS Bakersfield':
        return 'Cal State Bakersfield'
    if name == 'Holy Cr':
        return 'Holy Cross'
    if name == 'MTSU' or name == 'Middle Tennessee State':
        return 'Middle Tennessee'
    if name == 'Prov':
        return 'Providence'
    if name == 'Wis-Green Bay':
        return 'Green Bay'
    if name == 'Coll of Charleston':
        return 'College of Charleston'
    if name == 'Loy-Chi' or name == 'Loyola-Chicago':
        return 'Loyola Chicago'
    if name == 'Rhode Is':
        return 'Rhode Island'
    if name == 'St Bonny':
        return "St. Bonaventure"
    if name == 'TX So':
        return 'Texas Southern'
    if name == 'Nwestern':
        return 'Northwestern'
    if name == 'SC':
        return 'South Carolina'
    if name == 'North Carolina State':
        return 'NC State'
    return name
