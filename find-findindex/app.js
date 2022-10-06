const users = [
    { username: 'mlewis' },
    { username: 'akagen' },
    { username: 'msmith' }
];

function findUserByUsername(arr, string) {
    return arr.find(function (val) {
        return val.username === string
    })
}

function removeUser(arr, username) {
    let foundIndex = arr.findIndex(function (user) {
        return user.username === username
    })
    if (foundIndex === -1) return;
    return arr.splice(foundIndex, 1)[0];
}