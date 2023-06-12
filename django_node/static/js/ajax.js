async function getMessage(url, html_id, key, prefix) {

    let html_element = document.getElementById(html_id)


    try {
            html_element.style.backgroundColor = "blue"
            html_element.innerText = prefix + 'loading...'

            let response = await fetch('ajax', {
            method: 'get',
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
                'Content-Type': 'application/json',
                'Target-Url': url
            }
        })


        let json_response = await response.json()

        html_element.innerText = prefix + json_response[key]
        html_element.style.backgroundColor = "green"

    }
    catch{
        html_element.style.backgroundColor = "red"
        html_element.innerText = prefix + 'ERROR'
    }

}