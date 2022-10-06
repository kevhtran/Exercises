function hasOddNumber(arr) {
    return arr.some(function (val) {
        return val % 2 !== 0
    })
}

function hasAZero(num) {
    return num.toString().split("").some(function (val) {
        // '0' bc it's a string inside an array, not a number
        return val === '0'
    })
}

function hasOnlyOddNumbers(array) {
    return array.every(function (val) {
        return val % 2 !== 0
    })
}

function hasNoDuplicates(arr) {
    return arr.every(function (val) {
        return arr.indexOf(val) === arr.lastIndexOf(val)
    })
}
let arr1 = [
    { title: "Instructor", first: 'Elie', last: "Schoppik" },
    { title: "Instructor", first: 'Tim', last: "Garcia", isCatOwner: true },
    { title: "Instructor", first: 'Matt', last: "Lane" },
    { title: "Instructor", first: 'Colt', last: "Steele", isCatOwner: true }
]

function hasCertainKey(arr, key) {
    return arr.every(function (val) {
        return val[key]
    })
}

let arr2 = [
    { title: "Instructor", first: 'Elie', last: "Schoppik" },
    { title: "Instructor", first: 'Tim', last: "Garcia", isCatOwner: true },
    { title: "Instructor", first: 'Matt', last: "Lane" },
    { title: "Instructor", first: 'Colt', last: "Steele", isCatOwner: true }
]

function hasCertainValue(arr, key, value) {
    return arr.every(function (val) {
        return val[key] === value
    })
}