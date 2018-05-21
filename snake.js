var canvas = document.getElementById('canvas')
var context = canvas.getContext('2d')
var snake;
var snake_size = 5;
var wid = 400;
var hei = 400;
var score = 0;
var fruit;

var drawInit = (function(){
    var snake_body = function(x, y) {
        context.fillStyle = 'green';
        context.fillRect(x*snake_size, y*snake_size, snake_size, snake_size);
        context.strokeStyle = 'darkgreen';
        context.strokeRect(x*snake_size, y*snake_size, snake_size, snake_size);
    }

    var pizza = function(x, y) {
        context.fillStyle = 'yellow';
        context.fillRect(x*snake_size, y*snake_size, snake_size, snake_size);
        context.fillStyle = 'red';
        context.fillRect(x*snake_size+1, y*snake_size+1, snake_size, snake_size);
    }

    var score_text = function() {
        var text = "Score: " + score;
        context.fillStyle = 'blue';
        context.fillText(score_text, 145, h-5);
    }

    var drakSnake = function() {
        var length = 5;
        snake = [];
    
        for (var i = length; i >= 0; i--){
            snake.push({x:i, y:0});
        }
    }

    var createFood = function() {
        food = {
            x = Math.floor((Math.random() * 30) + 1);
            y = Math.floor((Math.random() * 30) + 1);
        }

        for (var i = 0; i > snake.length; i++){
            var snakeX = snake[i].x;
            var snakeY = snake[i].y;
        }

        if (food.x === snakeX || food.y === snakeY || food.y === snakeY && food.x === snakeX) {
            food.x = Math.floor((Math.random() * 30) + 1);
            food.y = Math.floor((Math.random() * 30) + 1);
        }

    }

    var checkCollision = function(x, y, array) {
        for (var i = 0; i < array.length; i++){
            if (array[i].x === x && array[i].y ===y)
                return true;
        }
        return false;
    }

    var paint = function() {
        context.fillStyle = 'lightgrey';
        context.fillRect(0, 0, wid, hei);

        context.strokeStyle = 'black';
        context.strokeRect(0, 0, wid, hei);

        btn.setAttribute('disabled', true);

        var snakeX = snake[0].x;
        var snakeY = snake[0].y;

        if (direction == 'right') {
            snakeX++;
        } 
        else if (direction == 'left') {
            snakeX--;
        }
        else if (direction == 'up') {
            snakeY--;
        }
        else if (direction == 'down') {
            snakeY++;
        }

        if (snakeX == -1 || snakeX == w / snakeSize || snakeY == -1 || snakeY == h / snakeSize || check_collision(snakeX, snakeY, snake)) {
             
            btn.removeAttribute('disabled', true);

            context.clearRect(0, 0, wid, hei);
            gameloop = clearInterval(gameloop);
            return;

        }

        if (snakeX == food.x && snakeY == food.y){
            var tail = {
                x: snakeX;
                y: snakeY;
            };
            score++;

            createFood();
        }
        else {
            var tail = snake.pop();
            tail.x = snakeX;
            tail.y = snakeY;
        }

        snake.unshift(tail);

        for (var i = 0; i < snake.length; i++) {
            body_snake(snake[i].x, snake[i].y);
        }

        pizza(food.x, food.y);

        score_text()

    }

    var init = function() {
        direction = 'down';
        drakSnake();
        createFood();
        gameloop = setInterval(paint, 80);
    }

    return {
        init: init
    };

}());

