
function add_tarefas(){
    window.location.href = "tarefas"
}

function enviar(){
    form = document.querySelector(".formulario");
    input = document.querySelector("#search");
    form.submit();
}

function editar(){
    window.location.href = "editar"
}