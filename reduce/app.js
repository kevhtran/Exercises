const arr1 = [{ name: 'Elie' }, { name: 'Tim' }, { name: 'Matt' }, { name: 'Colt' }]

function extractValue(arr, key) {
    return arr.reduce(function (acc, nextVal) {
        acc.push(nextVal[key]);
        return acc
        // need second parameter, starting with 0/empty array so that we start with an empty array at acc
    }, []);
}
// still keep forgetting how to work with objects, especially counting how many letters in something
function vowelCount(string) {
    let lowerCaseStr = string.toLowerCase()
    let vowels = 'aeiou'
    let newArr = lowerCaseStr.split("")
    return newArr.reduce(function (acc, next) {
        // this has come up multiple times, but keep forgetting how to do this part
        if (vowels.indexOf(next) !== -1) {
            if (acc[next]) {
                acc[next]++;
            }
            else {
                acc[next] = 1;
            }
        }
        // keep forgetting to return the accumulator
        return acc
    }, {})
}
const arr = [{ name: 'Elie' }, { name: 'Tim' }, { name: 'Matt' }, { name: 'Colt' }];

function addKeyAndValue(arr, key, value) {
    return arr.reduce(function (acc, next, idx) {
        // not quite sure what is going on here? i guess we're pulling up each object by acc[idx] (index) and then chaining [key] on to it so that is is basicaly alo obj[key] and setting a new value??
        acc[idx][key] = value;
        return acc;
        // need to start with the array, becuase we are adding to it
    }, arr);
}