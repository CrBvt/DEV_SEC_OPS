//const getMessage = () => console.log("AAAA")

async function getMessage(url, html_id, key, prefix) {

    try {
            let response = await fetch('ajax', {
            method: 'get',
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
                'Content-Type': 'application/json',
                'Target-Url': url
            }
        })


        let json_response = await response.json()

        let html_element = document.getElementById(html_id)
        html_element.innerText = prefix + json_response[key]
    }
    catch{
        let html_element = document.getElementById(html_id)
        html_element.innerText = prefix + 'ERROR'
    }

}