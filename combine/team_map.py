def map_team_names(name: str):
    if name.split(' ')[-1] == 'St.':
        return name.replace('St.', 'State')
    if name == 'University of California':
        return 'California'
    if name == 'Central Connecticut':
        return 'Central Connecticut State'
    if name == 'Illinois Chicago':
        return 'Illinois-Chicago'
    if name == 'North Carolina-Wilmington' or name == 'North Carolina Wilmington':
        return 'UNC Wilmington'
    if name == 'Pennsylvania':
        return 'Penn'
    if name == 'St. John\'s (NY)':
        return 'St. John\'s'
    if name == 'Miami FL' or name == 'Miami Fl':
        return 'Miami (FL)'
    if name == 'Southern California':
        return 'USC'
    if name == 'UC-Santa Barbara' or name == 'California Santa Barbara':
        return 'UC Santa Barbara'
    if name == 'Troy':
        return 'Troy State'
    if name == 'Brigham Young':
        return 'BYU'
    if name == 'Louisiana State':
        return 'LSU'
    if name == 'North Carolina-Asheville' or name == 'North Carolina Asheville':
        return 'UNC Asheville'
    if name == 'Alabama-Birmingham' or name == 'Alabama Birmingham':
        return 'UAB'
    if name == 'Texas-El Paso' or name == 'Texas El Paso':
        return 'UTEP'
    if name == 'Texas-San Antonio' or name == 'Texas San Antonio':
        return 'UTSA'
    if name == 'Louisiana' or name == 'Louisiana-Lafayette':
        return 'Louisiana Lafayette'
    if name == 'Virginia Commonwealth':
        return 'VCU'
    if name == 'Central Florida':
        return 'UCF'
    if name == "Saint Mary's (CA)":
        return "Saint Mary's"
    if name == 'Albany (NY)':
        return 'Albany'
    if name == 'Texas A&M Corpus Chris' or name == 'Texas Am Corpus Christi':
        return 'Texas A&M-Corpus Christi'
    if name == 'Miami (OH)' or name == 'Miami Oh':
        return 'Miami OH'
    if name == 'Nevada-Las Vegas' or name == 'Nevada Las Vegas':
        return 'UNLV'
    if name == 'Maryland-Baltimore County' or name == 'Maryland Baltimore County':
        return 'UMBC'
    if name == 'Texas-Arlington' or name == 'Texas Arlington':
        return 'UT Arlington'
    if name == 'Cal St. Fullerton':
        return 'Cal State Fullerton'
    if name == 'Cal St. Northridge':
        return 'Cal State Northridge'
    if name == 'Arkansas-Pine Bluff':
        return 'Arkansas Pine Bluff'
    if name == 'Little Rock':
        return 'Arkansas Little Rock'
    if name == 'Long Island University':
        return 'LIU Brooklyn'
    if name == 'Loyola (MD)' or name == "Loyola Md":
        return 'Loyola MD'
    if name == 'Detroit Mercy':
        return 'Detroit'
    if name == 'Southern Mississippi':
        return 'Southern Miss'
    if name == 'Southern Methodist':
        return 'SMU'
    if name == 'UC-Irvine' or name == 'California Irvine':
        return 'UC Irvine'
    if name == 'Cal St. Bakersfield':
        return 'Cal State Bakersfield'
    if name == 'UC-Davis' or name == 'California Davis':
        return 'UC Davis'
    if name == 'North Carolina-Greensboro' or name == 'North Carolina Greensboro':
        return 'UNC Greensboro'
    if name == 'Texas Christian':
        return 'TCU'
    if name == 'Loyola (IL)' or name == 'Loyola Il':
        return 'Loyola Chicago'
    if name == 'Gardner-Webb':
        return 'Gardner Webb'
    if name == 'Prairie View':
        return 'Prairie View A&M'
    if name == 'St Johns Ny':
        return 'St. John\'s'
    if name == 'Ucla':
        return 'UCLA'
    if name == 'Mcneese State':
        return 'McNeese State'
    if name == 'Saint Josephs':
        return 'Saint Joseph\'s'
    if name == 'Iupui':
        return 'IUPUI'
    if name == 'Depaul':
        return 'DePaul'
    if name == 'Florida Am':
        return 'Florida A&M'
    if name == 'Alabama Am':
        return 'Alabama A&M'
    if name == 'Saint Marys Ca':
        return "Saint Mary's"
    if name == 'Texas Am':
        return 'Texas A&M'
    if name == 'Albany Ny':
        return 'Albany'
    if name == 'Mount St Marys':
        return "Mount St. Mary's"
    if name == 'Stephen F Austin':
        return 'Stephen F. Austin'
    if name == 'Saint Peters':
        return "Saint Peter's"
    if name == 'St Bonaventure':
        return "St. Bonaventure"
    if name == 'North Carolina At':
        return "North Carolina A&T"
    if name == 'College Of Charleston':
        return 'College of Charleston'
    if name == 'N.C. State' or name == 'NCSU' or name == 'North Carolina State' or name == 'North Carolina State University':
        return 'NC State'
    return name
