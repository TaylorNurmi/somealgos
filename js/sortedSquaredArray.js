function sortedSquaredArray(array) {
    const squared = array.map( val => val*val );
    let sorted = squared.sort(function(a, b){return a-b})
    return sorted;
}
console.log(sortedSquaredArray([1, 2, 3, 5, 6, 8, 9]));