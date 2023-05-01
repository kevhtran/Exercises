// http://api.giphy.com/v1/gifs/search

const form = document.querySelector('#searchForm')
const input = document.querySelector('#search')
const body = document.body
const gifDiv = document.querySelector('#gifs')
const $gifDiv = $("#gifs");
const rmvButton = document.querySelector('#remove')

form.addEventListener('submit', async function (e) {
    e.preventDefault();
    const res = await axios.get('http://api.giphy.com/v1/gifs/search', { params: { api_key: "zOS5YKzLmWAQx9cQ0hEoFfgxfUYloZhd", q: input.value, } })
    let numResults = res.data.data.length

    if (numResults) {
        let randomIdx = Math.floor(Math.random() * numResults);
        let newImg = document.createElement('img');
        let newDiv = document.createElement('div');
        console.log(res.data.data[randomIdx].images.original.url)
        newImg.src = res.data.data[randomIdx].images.original.url
        newDiv.append(newImg)
        gifDiv.append(newDiv)
    }
    input.value = ""
})
$("#remove").on('click', function () {
    $gifDiv.empty();
})
