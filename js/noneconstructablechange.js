function nonConstructibleChange(coins) {
    let change = 0;
    let sorted = coins.sort(function(a, b){return a-b});
    for (var i = 0; i < sorted.length; i++) {
        if (sorted[i] > (change + 1)) {
            return change += 1;
        }
        else {
            change += sorted[i]
        }
        }
    return change + 1;
}
console.log(nonConstructibleChange([1, 2, 4, 5, 100]));