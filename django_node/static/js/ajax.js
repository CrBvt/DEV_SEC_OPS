//const getMessage = () => console.log("AAAA")

async function getMessage(url) {
    let response = await fetch('ajax', {
        method: 'get',
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/json',
            'Target-Url': url
        }
    })

//    let message = document.getElementById('engine_status')
    {{ engine_status }} = await response.json()
}