function tournamentWinner(competitions, results) {
    let teams = {};
    let winner = competitions[0][0];
    for (var i = 0; i < competitions.length; i++) {
        for (var j = 0; j < competitions[i].length; j++) {
            if (competitions[i][j] in teams == false) {
                teams[competitions[i][j]] = 0;
            }
        }
    }
    for (var x = 0; x < results.length; x++) {
        if (results[x] == 0) {
            teams[competitions[x][1]] += 3;
        }
        else {
            teams[competitions[x][0]] += 3;
        }
    }
    for (key in teams) {
        console.log(teams[key])
        if (teams[key] >= teams[winner]) {
            winner = key;
        }
    }
    return winner;
}
console.log(tournamentWinner([["HTML", "Java"], ["Java", "Python"], ["Python", "HTML"]], [0, 1, 1]))

const competitions = [
    ['HTML', 'C#'],
    ['C#', 'Python'],
    ['Python', 'HTML'],
  ];
  const results = [0, 0, 1];