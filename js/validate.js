const array = [5, 1, 22, 25, 6, -1, 8, 10];
const sequence = [1, 6, -1, 10];
function isValidSubsequence(array, sequence) {
    let counter = 0;
    for (var i = 0; i < array.length; i++) {
        if (array[i] == sequence[counter]) {
            counter++;
        }
    }
    if (counter == sequence.length) {
        return true
    }
    else {
        return false
    }
}
console.log(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))
