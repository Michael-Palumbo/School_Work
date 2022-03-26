var canvas = document.getElementById('Panel');

var SIZE = 30;

canvas.width = window.innerWidth-(window.innerWidth%SIZE)-SIZE;
canvas.height = window.innerHeight-(window.innerHeight%SIZE)-SIZE;

var c = canvas.getContext('2d');

var GRID_WIDTH = Math.floor(canvas.width/SIZE);
var GRID_HEIGHT = Math.floor(canvas.height/SIZE);

var player = {x:2,y:2,vx:0,vy:0};

var trail = [];
var tail = 0;

var apple = {x:0,y:0};

placeApple();

setInterval(update, 1000/15);

document.addEventListener('keydown', keyPushed);

function update(){

  player.x += player.vx;
  player.y += player.vy;

  playerWrap();

  if(player.x == apple.x && player.y == apple.y){
    placeApple();
    tail += 3;
  }

  c.fillStyle = "lightgray";
  c.fillRect(0,0,canvas.width,canvas.height);


  c.fillStyle = "#333333";
  c.fillRect(player.x*SIZE,player.y*SIZE,SIZE,SIZE);

  for(var i = 0; i < trail.length ; i ++){
    c.fillRect(trail[i].x*SIZE,trail[i].y*SIZE,SIZE,SIZE);
    if(trail[i].x == player.x && trail[i].y == player.y)
      tail = 2;
  }

  c.fillStyle = "red";
  c.fillRect(apple.x*SIZE,apple.y*SIZE,SIZE,SIZE);



   trail.unshift({x:player.x,y:player.y});

   while(trail.length > tail)
     trail.pop();
}
function keyPushed(e){
  switch(e.keyCode){
    case 37:
      player.vx = -1;
      player.vy = 0;
      break;
    case 38:
      player.vx = 0;
      player.vy = -1;
      break;
    case 39:
      player.vx = 1;
      player.vy = 0;
      break;
    case 40:
      player.vx = 0;
      player.vy = 1;
      break;
  }
}

function playerWrap(){
  if(player.x < 0)
    player.x = GRID_WIDTH-1;
  if(player.x >= GRID_WIDTH)
    player.x = 0;
  if(player.y < 0)
    player.y = GRID_HEIGHT-1;
  if(player.y >= GRID_HEIGHT)
    player.y = 0;
}
function placeApple(){
  let tempX, tempY;
   do{
     tempX = Math.floor(Math.random()*GRID_WIDTH);
     tempY = Math.floor(Math.random()*GRID_HEIGHT);
   }while(findLoc(tempX,tempY));
   apple.x = tempX;
   apple.y = tempY;
}

function findLoc(x,y){
  for(loc of trail)
    if(loc.x == x && loc.y == y)
      return true;
  return false;
  // for(var i ; i < trail.length ; i++)
  //   if(trail[i].x == x && trail[i].y == y)
  //     return i;
  // return -1;
}
