
function add_tarefas(){
    window.location.href = "tarefa"
}

function enviar(){
    form = document.querySelector(".formulario");
    input = document.querySelector("#search");
    form.submit();
}

function editar(id){
    window.location.href = `editar/${id}`
}

function home(){
    window.location.href="/"
}

function deletar(id){
    botao = document.querySelector(".bi-trash");
    window.location.href = `deletar/${id}`;
    window.alert("Deletado com sucesso!")
}

function temas(){
    botao = document.querySelector(".tema");
    content = document.querySelector(".content");
    cabecalho = document.querySelector(".cabecalho");

    botao.id == "red" ? botao.id = "dark" : botao.id = "red"
    if (botao.id == "red"){
        cabecalho.style.background = "linear-gradient(rgb(175, 6, 6), rgb(94, 5, 5), rgb(146, 45, 45))";
        content.style.background = "linear-gradient(rgb(175, 6, 6), rgb(94, 5, 5), rgb(146, 45, 45))";
        botao.innerText = "Modo claro";
    }
    else{
        botao.innerText = "Modo escuro";
        cabecalho.style.background = "linear-gradient(rgb(0, 0, 0), rgb(26, 24, 24), rgb(20, 19, 19), rgb(8, 8, 8))";  
        content.style.background = "linear-gradient(rgb(0, 0, 0), rgb(26, 24, 24), rgb(20, 19, 19), rgb(8, 8, 8))";
    }
}
