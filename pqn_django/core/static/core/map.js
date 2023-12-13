const locations = [
    { lat: -41.00011649999999, lng: -71.5000395, name: "Parque Nacional Nahuel Huapi" },
    { lat: -39.9510918, lng: -71.07070089999999, name: "Parque Nacional Lanín" },
    { lat: -39.0564814, lng: -70.3482994, name: "Parque Nacional Laguna Blanca" },
    { lat: -40.78392, lng: -71.66046899999999, name: "Parque Nacional Los Arrayanes" },
    { lat: -38.0053902, lng: -65.576475, name: "Parque Nacional Lihué Calel" },
    { lat: -42.9741301, lng: -71.6438598, name: "Parque Nacional Los Alerces" },
    { lat: -42.0972699, lng: -71.6197991, name: "Parque Nacional Lago Puelo" },
    { lat: -50.4162628, lng: -73.27693140000001, name: "Parque Nacional los Glaciares" },
    { lat: -47.8920673, lng: -72.0345914, name: "Parque Nacional Perito Moreno" },
    { lat: -47.1524611, lng: -71.3206299, name: "Parque Nacional Patagonia" },
    { lat: -47.67210120000001, lng: -67.9917364, name: "Parque Nacional Bosques Petrificados de Jaramillo" },
    { lat: -50.26423030000001, lng: -68.9584374, name: "Parque Nacional Monte Lenín" },
    { lat: -54.83492529999999, lng: -68.4465053, name: "Parque Nacional Tierra del Fuego" },
    { lat: -31.6113985, lng: -64.71288609999999, name: "Parque Nacional Quebrada del Condorito" },
    { lat: -29.24254, lng: -69.3537, name: "Parque Nacional San Guillermo" },
    { lat: -31.7974153, lng: -69.37395099999999, name: "Parque Nacional El Leoncito" },
    { lat: -29.7826667, lng: -67.83539999999999, name: "Parque Nacional Talampaya - Patrimonio de la Humanidad" },
    { lat: -32.49792499999999, lng: -67.0085459, name: "Parque Nacional Sierra de las Quijadas" },
    { lat: -32.12160290000001, lng: -60.6340393, name: "Parque Nacional Pre Delta" },
    { lat: -31.86378, lng: -58.25909000000001, name: "Parque Nacional El Palmar" },
    { lat: -34.2266714, lng: -58.89727019999999, name: "Parque Nacional Ciervo de los Pantanos" },
    { lat: -36.3786852, lng: -56.90448919999999, name: "Parque Nacional Campos del Tuyá" },
    { lat: -25.6829476, lng: -54.45463389999999, name: "Área Cataratas | Parque Nacional Iguazú" },
    { lat: -26.7932203, lng: -59.6183926, name: "Parque Nacional Chaco" },
    { lat: -24.9457065, lng: -61.04352409999999, name: "Parque Nacional El Impenetrable" },
    { lat: -28.3430649, lng: -57.3431396, name: "Parque Nacional Iberá" },
    { lat: -28.0112609, lng: -58.00937949999999, name: "Parque Nacional Mburucuyá" },
    { lat: -25.0722457, lng: -58.14098589999999, name: "Parque Nacional Río Pilcomayo" },
    { lat: -24.8174308, lng: -65.4343252, name: "Parque Nacional El Baritu" },
    { lat: -24.7, lng: -64.633333, name: "Parque Nacional El Rey" },
    { lat: -25.216297, lng: -66.023744, name: "Parque Nacional Los Cardones" },
    { lat: -27.2928882, lng: -65.8627795, name: "Parque Nacional Aconquija" },
    { lat: -23.6715743, lng: -64.8668311, name: "Parque Nacional Calilegua" },
    { lat: -26.2374033, lng: -61.8330167, name: "Parque Nacional Copo" }
    // Agrega más ubicaciones si es necesario
];

function initMap() {
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 4,
        center: { lat: -30, lng: -65 }, // Cambia las coordenadas del centro según sea necesario
    });

    // Recorre las ubicaciones y agrega un marcador para cada una
    for (let i = 0; i < locations.length; i++) {
        new google.maps.Marker({
            position: locations[i],
            map,
            title: locations[i].name,
        });
    }
}
