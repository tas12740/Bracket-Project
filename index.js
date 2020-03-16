const kenPom = {
    'teams': [
        ['1. Kansas', '16. Michigan'],
        ['8. Ohio State', '9. Louisville'],
        ['4. Dayton', '13. BYU'],
        ['5. Duke', '12. Creighton'],
        ['2. Gonzaga', '15. Florida State'],
        ['7. Michigan State', '10. West Virginia'],
        ['3. Baylor', '14. Houston'],
        ['6. San Diego State', '11. Maryland']
    ],
    'results': [
        [[88.0, 12.0], [57.5, 42.5], [67.8, 32.2], [54.1, 45.9], [67.4, 32.6], [64.4, 35.6], [61.3, 38.7], [64.9, 35.1]],
        [[84.2, 15.8], [39.8, 60.2], [82.4, 17.6], [46.2, 53.8]],
        [[71.9, 28.1], [74.3, 25.7]],
        [[62.6, 37.4]]
    ]
}

const kenPomParams = {
    teamWidth: 120,
    scoreWidth: 40,
    matchMargin: 10,
    roundMargin: 50,
    skipConsolationRound: true,
    init: kenPom
}

const net = {
    'teams': [
        ['1. Gonzaga', '16. Ohio State'],
        ['8. Louisville', '9. BYU'],
        ['4. San Diego State', '13. Villanova'],
        ['5. Baylor', '12. Oregon'],
        ['2. Kansas', '15. Seton Hall'],
        ['7. Michigan State', '10. Florida State'],
        ['3. Dayton', '14. Arizona'],
        ['6. Duke', '11. Creighton']
    ],
    'results': [
        [[82.1, 17.9], [30.3, 69.7], [28.2, 71.8], [57.2, 42.8], [84.6, 15.4], [27.6, 72.4], [74.1, 25.9], [54.1, 45.9]],
        [[83.2, 16.8], [71.9, 28.1], [78.1, 21.9], [39.8, 60.2]],
        [[58.4, 41.6], [71.9, 28.1]],
        [[37.4, 62.6]]
    ]
}

const netParams = {
    teamWidth: 120,
    scoreWidth: 40,
    matchMargin: 10,
    roundMargin: 50,
    skipConsolationRound: true,
    init: net
}

const ap = {
    'teams': [
        ['1. Kansas', '16. Seton Hall'],
        ['8. Kentucky', '9. Michigan State'],
        ['4. Florida State', '13. Oregon'],
        ['5. Baylor', '12. Maryland'],
        ['2. Gonzaga', '15. Louisville'],
        ['7. Creighton', '10. Duke'],
        ['3. Dayton', '14. BYU'],
        ['6. San Diego State', '11. Villanova']
    ],
    'results': [
        [[84.6, 15.4], [60.7, 39.3], [59.1, 40.9], [64.8, 35.2], [84.3, 15.7], [43.8, 56.2], [67.8, 32.2], [29.6, 70.4]],
        [[84.5, 15.5], [55.2, 44.8], [62.7, 37.3], [33.5, 66.5]],
        [[78.5, 21.5], [59.2, 40.8]],
        [[62.6, 37.4]]
    ]
}

const apParams = {
    teamWidth: 120,
    scoreWidth: 40,
    matchMargin: 10,
    roundMargin: 50,
    skipConsolationRound: true,
    init: ap
}

const coaches = {
    'teams': [
        ['1. Kansas', '16. BYU'],
        ['8. Villanova', '9. Creighton'],
        ['4. Florida State', '13. Oregon'],
        ['5. Baylor', '12. Michigan State'],
        ['2. Gonzaga', '15. Seton Hall'],
        ['7. Kentucky', '10. Duke'],
        ['3. Dayton', '14. Louisville'],
        ['6. San Diego State', '11. Maryland']
    ],
    'results': [
        [[84.9, 15.1], [59.7, 40.3], [59.1, 40.9], [71.8, 28.2], [83.9, 16.1], [20.8, 79.2], [75.2, 24.8], [64.9, 35.1]],
        [[64.3, 35.7], [55.2, 44.8], [62.7, 37.3], [53.4, 46.6]],
        [[78.5, 21.5], [72.2, 27.8]],
        [[62.6, 37.4]]
    ]
}

const coachesParams = {
    teamWidth: 120,
    scoreWidth: 40,
    matchMargin: 10,
    roundMargin: 50,
    skipConsolationRound: true,
    init: coaches
}

const bpi = {
    'teams': [
        ['1. Kansas', '16. Villanova'],
        ['8. Louisville', '9. Ohio State'],
        ['4. Michigan State', '13. Oregon'],
        ['5. Dayton', '12. Florida State'],
        ['2. Duke', '15. Houston'],
        ['7. San Diego State', '10. Arizona'],
        ['3. Gonzaga', '14. Maryland'],
        ['6. Baylor', '11. West Virginia']
    ],
    'results': [
        [[62.9, 37.1], [40.5, 59.5], [38.2, 61.8], [46.2, 53.8], [76.0, 24.0], [76.3, 23.7], [79.1, 20.9], [72.0, 28.0]],
        [[84.2, 15.8], [39.2, 60.8], [59.1, 40.9], [70.8, 29.2]],
        [[78.1, 21.9], [36.0, 64.0]],
        [[62.6, 37.4]]
    ]
}

const bpiParams = {
    teamWidth: 120,
    scoreWidth: 40,
    matchMargin: 10,
    roundMargin: 50,
    skipConsolationRound: true,
    init: bpi
}

$(function () {
    $('#kenpom').bracket(kenPomParams);
    $('#net').bracket(netParams);
    $('#ap').bracket(apParams);
    $('#coaches').bracket(coachesParams);
    $('#bpi').bracket(bpiParams);
})