// forEach
// doubleValues
array1 = [1, 2, 3] // [2,4,6]
array2 = [5, 1, 2, 3, 10] // [10,2,4,6,20]
array3 = [
    { name: 'Elie' },
    { name: 'Tim' },
    { name: 'Matt' },
    { name: 'Colt' }
]
// function doubleValues(arr) {
//     let newArr = [];
//     for (let i = 0; i < arr.length; i++) {
//         newArr.push(arr[i] * 2)
//     };
//     return newArr;
// }
function doubleValues(arr) {
    let newArr = [];
    arr.forEach(function (value) {
        newArr.push(value * 2)
    }
    )
    return newArr
}

function onlyEvenValues(arr) {
    let newArr = [];
    arr.forEach(function (value) {
        if (value % 2 === 0) {
            newArr.push(value);
        }
    })
    return newArr
}

function showFirstAndLast(arr) {
    let newArr = [];
    arr.forEach(function (value) {
        newArr.push(value[0] + value[value.length - 1]);
    })
    return newArr;
}

function addKeyandValue(arr, key, value) {
    arr.forEach(function (val) {
        val[key] = value
    })
    return arr
}

function vowelCount(string) {
    let lowerCaseString = string.toLowerCase()
    let strArr = lowerCaseString.split("");
    let vowels = 'aeiou'
    let obj = {}
    strArr.forEach(function (strArr) {
        //*
        if (vowels.indexOf(strArr) !== -1) {
            if (obj[strArr]) {
                obj[strArr]++;
            }
            else {
                obj[strArr] = 1
            }
        }
    })
    return obj;
}
// map

function doubleValuesWithMap(arr) {
    return arr.map(function (val) {
        return val * 2
    })
}

function valTimesIndex(arr) {
    return arr.map(function (val, i) {
        return val * i
    })
}

function extractKey(arr, key) {
    return arr.map(function (val) {
        return val[key];
    });
}

function extractFullName(arr) {
    return arr.map(function (val) {
        return val.first + ' ' + val.last
    })
}

// filter

function filterByValue(arr, key) {
    return arr.filter(function (val) {
        return val[key] !== undefined;
    });
}

function find(arr, searchValue) {
    return arr.filter(function (val) {
        return val === searchValue;
    })
    // need to set array to a value bc if the array cannot be returned, it will show as an empty array.
    [0];
}

function findInObj(arr, key, value) {
    return arr.filter(function (val) {
        return val[key] === value;
    })
}

function removeVowels(string) {
    let lowerCaseStr = string.toLowerCase();
    let strArr = lowerCaseStr.split("");
    let vowels = 'aeiou';
    return strArr.filter(function (val) {
        return vowels.indexOf(val) === -1
    }).join("");
}

function doubleOddNumbers(arr) {
    let oddNum = arr.filter(function (val) {
        return val % 2 !== 0
    })
    return oddNum.map(function (val) {
        return val * 2
    })
}