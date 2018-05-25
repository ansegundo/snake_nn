var drawInit = (function() {
  // coloring the snake's and fruit's body
  var snakeBody = function(x, y) {
    context.fillStyle = "black";
    context.fillRect(x * snake_size, y * snake_size, snake_size, snake_size);
    context.strokeStyle = "white";
    context.strokeRect(x * snake_size, y * snake_size, snake_size, snake_size);
  };

  var pizza = function(x, y) {
    context.fillStyle = "blue";
    context.fillRect(x * snake_size, y * snake_size, snake_size, snake_size);
    context.fillStyle = "yellow";
    context.fillRect(
      x * snake_size + 1,
      y * snake_size + 1,
      snake_size - 2,
      snake_size - 2
    );
  };

  // text on screen
  var scoreText = function() {
    var score_text = "Score: " + score;
    context.fillStyle = "red";
    context.fillText(score_text, 50, hei - 5);
  };

  var epochText = function() {
    var epoch_text = "Epoch: " + epoch;
    context.fillStyle = "red";
    context.fillText(epoch_text, 100, hei - 5);
  };

  //setting up snake parts
  var drawSnake = function() {
    var length = 3;
    snake = [];
    for (var i = length - 1; i >= 0; i--) {
      snake.push({ x: i, y: 0 });
    }
  };

  var createFood = function() {
    food = {
      x: Math.floor(Math.random() * 19 + 1),
      y: Math.floor(Math.random() * 19 + 1)
    };

    for (var i = 0; i > snake.length; i++) {
      var snakeX = snake[i].x;
      var snakeY = snake[i].y;

      if (
        food.x === snakeX ||
        food.y === snakeY ||
        (food.y === snakeY && food.x === snakeX)
      ) {
        food.x = Math.floor(Math.random() * 19 + 1);
        food.y = Math.floor(Math.random() * 19 + 1);
      }
    }
  };

  var checkCollision = function(x, y, array) {
    for (var i = 0; i < array.length; i++) {
      if (array[i].x === x && array[i].y === y) return true;
    }
    return false;
  };

  var distance = function(food, snakeX, snakeY) {
    var a = snakeX - food.x;
    var b = snakeY - food.y;
    var c = Math.sqrt(a * a + b * b);
    return c;
  };

  var paint = function() {
    // coloring the board
    context.fillStyle = "white";
    context.fillRect(0, 0, wid, hei);
    context.strokeStyle = "black";
    context.strokeRect(0, 0, wid, hei);

    btn_start.setAttribute("disabled", true);

    var snakeX = snake[0].x;
    var snakeY = snake[0].y;
    var ndirection = 0;
    // console.log('snake position: ' + snake[0].x + ',' + snake[0].y)

    if (direction == "right") {
      ndirection = 0;
      snakeX++;
    } else if (direction == "left") {
      ndirection = 1;
      snakeX--;
    } else if (direction == "up") {
      ndirection = 2;
      snakeY--;
    } else if (direction == "down") {
      ndirection = 3;
      snakeY++;
    }

    if (
      snakeX == -1 ||
      snakeX == wid / snake_size ||
      snakeY == -1 ||
      snakeY == hei / snake_size ||
      checkCollision(snakeX, snakeY, snake)
    ) {
      btn_start.removeAttribute("disabled", true);

      context.clearRect(0, 0, wid, hei);
      gameloop = clearInterval(gameloop);

      console.log(data_json);
      score = 0;
      epoch = 0;
      return;
    }

    if (snakeX == food.x && snakeY == food.y) {
      var tail = {
        x: snakeX,
        y: snakeY
      };
      score++;
      createFood();
    } else {
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

    data_json.push([
      snakeX,
      snakeY,
      food.x,
      food.y,
      distance(food, snakeX, snakeY),
      score,
      ndirection
    ]);
  };

  var init = function() {
    direction = "right";
    drawSnake();
    createFood();
    gameloop = setInterval(paint, 100);
  };

  return {
    init: init
  };
})();
