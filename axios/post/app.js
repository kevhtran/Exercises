// async function getUsers() {
//     const res = await axios.get('https://reqres.in/api/users')
// }

// async function createUsers() {
//     const res = await axios.post('https://reqres.in/api/users', { username: 'ButtersTheChicken', email: 'butters@gmail.com', age: 1 })
//     console.log(res)
// }
// https://hackorsnoozev3.docs.apiary.io/#introduction/authentication
// token:"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImJyb3NraSIsImlhdCI6MTY2OTY3OTk3OH0.eRdYF0OOcdn8D2_pbwj0dhaYbYTIskTRE81nLE8ie6E"
async function getUsers(token) {
    const res = await axios.get('https://hack-or-snooze-v3.herokuapp.com/users', { params: { token } });
    console.log(res);
}

async function signUp(username, password, name) {
    const res = await axios.post('https://hack-or-snooze-v3.herokuapp.com/signup', { user: { name, username, password } });
    console.log(res);
}
async function logIn(username, password) {
    const res = await axios.post('https://hack-or-snooze-v3.herokuapp.com/login', { user: { username, password } });
    console.log(res);
    return res.data.token;
}

async function getUsersWithAuth() {
    const token = await logIn('broski', '1222')
    getUsers(token);
}

async function createStory() {
    const token = await logIn('broski', '1222');
    const newStory = {
        token, story: { author: 'Broskki', title: 'the dude who schooled', url: 'http://chickens4lyfe.com' }
    }
    const res = await axios.post('https://hack-or-snooze-v3.herokuapp.com/stories', newStory);
    console.log(res)
}
// signUp('broski', '1222', 'bro')
logIn('broski', '1222')
// getUsersWithAuth();
// createStory();
