class Arco {
  constructor(x, y, raio) {
    this.x = x;
    this.y = y;
    this.raio = raio;
  }

  show() {
    strokeWeight(2);
    stroke(255);
    noFill();
    circle(0, 0, this.raio);
    fill(255);
  }

  bola(tempo, i) {
    let angulo = tempo / (50 + 1 * i);
    circle((cos(angulo) * this.raio / 2), -Math.abs(sin(angulo) * this.raio / 2), 20);
    // if (tempo % 20 == 0) {
    //   console.log((cos(angulo) * this.raio / 2), (sin(angulo) * this.raio / 2));
    // }
  }
}

function ligades () {
  if (ligado == false) {
    ligado = true;
  } else {
    ligado = false;
  }
}

let ligado = true;
let subindo = 0;
let arcos = [];
let qts = 10;

function setup() {
  createCanvas(1200, 600);

  for (let i = 0; i < qts; i++) {
    arcos.push(new Arco(width / 2, height - 50, 2 * (500 - (450 * (i / qts)))));
  }
}

function draw() {
  translate(width / 2, height - 50);

  // console.log(subindo);

  // if (subindo % 20 == 0) {
  //   console.log(ligado);
  // }

  if (ligado == true) {
    background(0);
    fill(255);

    for (let i = 0; i < arcos.length; i++) {
      arcos[i].show();
    }

    fill(0);
    stroke(0);
    rect(-600, 0, width, 50);
    stroke(255);
    fill(255);
    line(-550, 0, 550, 0);

    subindo += 1;

    for (let i = 0; i < arcos.length; i++) {
      arcos[i].bola(subindo, i);
    }
  }
}