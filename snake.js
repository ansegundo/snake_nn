var drawInit = ( function() {

    var snakeBody = function(x, y) {
        context.fillStyle = 'green';
        context.fillRect(x*snake_size, y*snake_size, snake_size, snake_size);
        context.strokeStyle = 'darkgreen';
        context.strokeRect(x*snake_size, y*snake_size, snake_size, snake_size);
    }

    var pizza = function(x, y) {
        context.fillStyle = 'yellow';
        context.fillRect(x*snake_size, y*snake_size, snake_size, snake_size);
        context.fillStyle = 'red';
        context.fillRect(x*snake_size+1, y*snake_size+1, snake_size-2, snake_size-2);
    }

    var scoreText = function() {
        var score_text = "Score: " + score;
        context.fillStyle = 'blue';
        context.fillText(score_text, 145, hei-5);
    }

    var epochText = function () {
        var epoch_text = "Epoch: " + epoch;
        context.fillStyle = 'blue';
        context.fillText(epoch_text, 245, hei-5);
    }

    var drawSnake = function() {
        var length = 4;
        snake = [];
        for (var i = length-1; i>=0; i--) {
            snake.push({x:i, y:0});
        }  
    }

    var paint = function() {
        context.fillStyle = 'lightgrey';
        context.fillRect(0, 0, wid, hei);
        context.strokeStyle = 'black';
        context.strokeRect(0, 0, wid, hei);

        btn_start.setAttribute('disabled', true);

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
        } else if(direction == 'down') { 
            snakeY++; 
        }

        if (snakeX == -1 || snakeX == wid / snake_size || snakeY == -1 || snakeY == hei / snake_size || checkCollision(snakeX, snakeY, snake)) {
             
            btn_start.removeAttribute('disabled', true);

            context.clearRect(0, 0, wid, hei);
            gameloop = clearInterval(gameloop);
            return;

        }

        if (snakeX == food.x && snakeY == food.y){
            var tail = {
                x: snakeX,
                y: snakeY
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
            snakeBody(snake[i].x, snake[i].y);
        }

        pizza(food.x, food.y);

        scoreText();
        epochText();
        epoch++;
    }

    var createFood = function() {
        food = {
            x: Math.floor((Math.random() * 30) + 1),
            y: Math.floor((Math.random() * 30) + 1)
        }

        for (var i = 0; i > snake.length; i++){
            var snakeX = snake[i].x;
            var snakeY = snake[i].y;

            if (food.x === snakeX || food.y === snakeY || food.y === snakeY && food.x === snakeX) {
                food.x = Math.floor((Math.random() * 30) + 1);
                food.y = Math.floor((Math.random() * 30) + 1);
            }
        }
    }

    var checkCollision = function(x, y, array) {
        for (var i = 0; i < array.length; i++){
            if (array[i].x === x && array[i].y ===y)
                return true;
        }
        return false;
    }

    var init = function(){
        direction = 'down';
        drawSnake();
        createFood();
        gameloop = setInterval(paint, 80);
    }

    return {
        init: init
    };

}());


