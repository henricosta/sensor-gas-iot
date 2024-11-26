let lastTimestamp = null
let ultimoVazamento = null
 
const API_URL_RECUPERAR_DADOS = API_URL + '/api/recuperar-dados'
const API_URL_ULTIMA_LEITURA = API_URL + '/api/ultima-leitura'

function formatDate(dateString) {
    const date = new Date(dateString);
    
    const options = {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
        hour12: false
    };
    
    return date.toLocaleString('pt-BR', options);
}

function renderVazamento(uv) {
    if (uv != null) {
        const vazamentoComponent = `
            <div class="box">
                <h2 class="title is-5">Último vazamento detectado:</h2>
                <p id="ultimo-vazamento-timestamp">${uv.timestamp}</p>
                <p id="ultimo-vazamento-value"><strong>Valor:</strong> ${uv.value}</p>
            </div>
        `

        $('#ultimo-vazamento-container').empty().append(vazamentoComponent)
    }
}

$(document).ready(() => {
    $.ajax({
        url: API_URL_RECUPERAR_DADOS,
        method: 'GET',
        success: (response) => {
            $('#message-list').empty()

            response['data'].forEach(leitura => {
                const listItem = $('<li class="message-item"></li>').text(`(${leitura.identificador}) [${formatDate(leitura.timestamp)}] - ${leitura.value}`);
                $('#message-list').append(listItem);

                if (leitura.vazamento === 1) {
                    ultimoVazamento = leitura
                }
            });

            if (response['data'].length > 0) {
                lastTimestamp = response['data'][0].timestamp;
            }

            renderVazamento(ultimoVazamento)
        }
    })
})


setInterval(() => {
    $.ajax({
        url: API_URL_ULTIMA_LEITURA,
        method: 'GET',
        success: (response) => {
            const latestReading = response['data'][0];

            if (latestReading.timestamp !== lastTimestamp) {
                lastTimestamp = latestReading.timestamp;
                
                const listItem = $('<li class="message-item"></li>').text(`(${latestReading.identificador}) [${formatDate(latestReading.timestamp)}] - ${latestReading.value}`);
                $('#message-list').prepend(listItem);
            }

            if (latestReading.vazamento === 1) {
                ultimoVazamento = latestReading
                renderVazamento(ultimoVazamento)
            }
        }
    });
}, 15000);