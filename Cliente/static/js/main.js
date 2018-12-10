$(document).ready(function(){
	var BACK = 40, 
	FRONT  = 38, 
	LEFT = 37, 
    RIGHT = 39; 
    
    var pressionada = false;
    var clicada = false;
    var ultima_tecla;

    var conectado = false;

    setInterval(function() {
        if (!conectado) {
            $.ajax({
                url: window.location.href+'connect',
                    success: function (e) {
                        conectado = true;
                        $("p:first").html('Conectado');
                        $("p:first").css('color', 'green');
                    },
                    error: function (e) {
                        conectado = false;
                        $("p:first").html('Desconectado');
                        $("p:first").css('color', 'red');
                    },
                type: 'POST',
            }); 
        }  
    }, 1000);

	function comando(tipo){
		$.ajax({
			url: window.location.href+'mover',
            error: function (e) {
                conectado = false;
                $("p:first").html('Desconectado');
                $("p:first").css('color', 'red');
            },
            headers: {
                mov: tipo
            },
            type: 'POST',
		});
    }

    function down(tecla, click) {
        if((!pressionada && !click && !clicada) || (!clicada && click && !pressionada)){
            if(tecla == LEFT) 
                comando('E');
            else if(tecla == RIGHT) 
                comando('D');
            else if(tecla == FRONT) 
                comando('F');
            else if(tecla == BACK) 
                comando('B');
            
            if (click)
                clicada = true;
            else 
                pressionada = true;

            ultima_tecla = tecla;
        }
    }

    function up(tecla, click) {
        if ((pressionada && click) || (clicada && !click))
            return

        if (tecla != ultima_tecla)
            return
        else
            comando('B');
        
        if (click)
            clicada = false;
        else
 		    pressionada = false;
    }

	document.querySelector('body').addEventListener('keydown', function(event) {
        down(event.keyCode, false);        
    });

	document.querySelector('body').addEventListener('keyup', function(event) {
        up(event.keyCode, false);
    });

    $("#btn_cima").mousedown(function(){
        down(FRONT, true);
    })

    $("#btn_baixo").mousedown(function(){
        down(BACK, true);
    })

    $("#btn_esquerda").mousedown(function(){
        down(RIGHT, true);
    })

    $("#btn_direita").mousedown(function(){
        down(LEFT, true);
    })

    $("#btn_cima").mouseup(function(){
        up(FRONT, true);
    })

    $("#btn_baixo").mouseup(function(){
        up(BACK, true);
    })

    $("#btn_esquerda").mouseup(function(){
        up(RIGHT, true);
    })

    $("#btn_direita").mouseup(function(){
        up(LEFT, true);
    })
});