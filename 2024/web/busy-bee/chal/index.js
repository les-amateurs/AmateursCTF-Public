// INTERACTION DOCS
//  Interacting with hive deposits any honey on bee
//  Interacting with flower obtains one honey, unless it is fully grown, after 7 ticks it will be worth more
//  Interacting with empty tile will place honey, enemies stepping on it will die

const U = 0;
const D = 1;
const L = 2;
const R = 3;
const I = 4;

const defaultCode =
  atob(document.location.hash.substring(1)) || localStorage.code || "return U;";

const editor = CodeMirror.fromTextArea(document.getElementById("editor"), {
  styleActiveLine: true,
  lineNumbers: true,
  mode: "javascript",
  theme: "ayu-dark",
});

editor.setValue(defaultCode);
const log = document.getElementById("log");
const putLog = (msg) => {
  const p = document.createElement("p");
  p.setHTML(msg);
  log.appendChild(p);
};
const canvas = document.getElementById("canvas");
/** @type {CanvasRenderingContext2D} */
const ctx = canvas.getContext("2d");

const honeyBar = document.getElementById("honeyBar");
const honeyBarText = document.getElementById("honeyBarText");

const sprites = {};
const loadSprite = (path) => {
  if (sprites[path]) return sprites[path];
  const sprite = new Image();
  sprite.src = "sprites/" + path;
  sprites[path] = sprite;
  return sprite;
};

let world = {
  running: false,
  tick: 0,
  flowerCooldown: 0,
  enemyCooldown: 70,
  // grid has things like obstacles and flowers and what not
  grid: Array.from(Array(20), () => new Array(20)),
  totalHoney: 0,
  honey: 0,
  beesProduced: 1,
  honeyRequired: 2,
  entities: [],
  workers: [],
};

const reset = () => {
  for (const worker of world.workers) {
    worker.worker.terminate();
  }
  world = {
    running: false,
    tick: 0,
    flowerCooldown: 0,
    enemyCooldown: 70,
    // grid has things like obstacles and flowers and what not
    grid: Array.from(Array(20), () => new Array(20)),
    totalHoney: 0,
    honey: 0,
    beesProduced: 1,
    honeyRequired: 2,
    entities: [],
    workers: [],
  };

  setCell([10, 10], {
    type: "hive",
    sprite: loadSprite("hive.png"),
  });
};

const getCell = (pos) => world.grid[pos[0]][pos[1]];
const setCell = (pos, val) => (world.grid[pos[0]][pos[1]] = val);

const serializeWorld = (world) => {
  return {
    tick: world.tick,
    flowerCooldown: world.flowerCooldown,
    honey: world.honey,
    honeyRequired: world.honeyRequired,
    grid: world.grid.map((col) =>
      col.map((cell) => ({ ...cell, sprite: undefined }))
    ),
    entities: world.entities.map((entity) => ({
      ...entity,
      sprite: undefined,
      worker: undefined,
    })),
  };
};

const GRID_SIZE = 20;
const CELL_SIZE = 640 / GRID_SIZE;

const randomFlowerSprite = () => {
  if (Math.random() < 0.0001) return loadSprite("flower_orz.png");
  return loadSprite(
    ["flower_red.png", "flower_butterfly.png", "flower_star.png"][
      Math.floor(Math.random() * 3)
    ]
  );
};

const randomWorkerBeeSprite = () => {
  return loadSprite(
    [
      "bee_flocto.png",
      "bee_helloperson.png",
      "bee_helloperson_copyright_infingment.png",
      "bee_voxal.png",
    ][Math.floor(Math.random() * 4)]
  );
};

const createWorkerBee = (pos, lifetime) => {
  const bee = {
    type: "worker",
    pos,
    sprite: randomWorkerBeeSprite(),
    lifetime,
    honey: 2,
    worker: new Worker("worker.js"),
  };
  world.entities.push(bee);
  world.workers.push(bee);

  bee.worker.postMessage({ type: "init", code: editor.getValue() });
};

const createFlower = (pos) => {
  const flower = {
    type: "flower",
    pos,
    sprite: randomFlowerSprite(),
    growth: 0,
  };

  setCell(pos, flower);
  return flower;
};

const createEnemy = () => {
  const side = Math.floor(Math.random() * 20);
  const pos = [
    [side, 0],
    [side, 19],
    [0, side],
    [19, side],
  ][Math.floor(Math.random() * 4)];
  const enemy = {
    type: "enemy",
    pos,
    sprite: loadSprite("enemy.png"),
  };
  world.entities.push(enemy);

  return enemy;
};

const checkCollision = (entity) => {
  // boo hoo for me writing inefficent code :(
  for (const other of world.entities.filter((e) => e.type !== entity.type)) {
    if (other === null) return;
    if (other.pos[0] === entity.pos[0] && other.pos[1] === entity.pos[1]) {
      return other;
    }
  }
};

const requestAndHandleAction = (bee) =>
  new Promise((res, rej) => {
    if (bee === null) res();
    bee.worker.onmessage = (e) => {
      if (e.data.type === "action") {
        switch (e.data.action) {
          case U:
            bee.pos[1] = Math.max(0, bee.pos[1] - 1);
            break;
          case D:
            bee.pos[1] = Math.min(GRID_SIZE - 1, bee.pos[1] + 1);
            break;
          case L:
            bee.pos[0] = Math.max(0, bee.pos[0] - 1);
            break;
          case R:
            bee.pos[0] = Math.min(GRID_SIZE - 1, bee.pos[0] + 1);
            break;
          case I:
            const cell = getCell(bee.pos);
            switch (cell?.type) {
              case "flower":
                let honeyGain = 0;
                if (cell.growth >= 7) honeyGain = 2;
                else honeyGain = 1;
                if (bee.honey + honeyGain > 3) {
                  putLog(
                    `<span class="text-yellow-500">&gt; Warning: A bee has discarded honey. Bees cannot hold more than 3 honey at a time.</span>`
                  );
                }
                bee.honey = Math.min(3, bee.honey + honeyGain);
                break;
              case "hive":
                world.totalHoney += bee.honey;
                world.honey += bee.honey;
                bee.honey = 0;
                honeyBar.style.height = `${
                  (world.honey * 100) / world.honeyRequired
                }%`;
                honeyBarText.innerText = `${world.honey}/${world.honeyRequired}`;
                if (world.honey > world.honeyRequired) {
                  createWorkerBee([10, 10], 100);
                  world.honey -= world.honeyRequired;
                  world.honeyRequired = Math.floor(3 + world.beesProduced / 5);
                }
                break;
              default:
                if (bee.honey > 0) {
                  setCell(bee.pos, {
                    type: "honey",
                    lifetime: 10,
                    sprite: loadSprite("honey.png"),
                  });
                  bee.honey--;
                } else {
                  putLog(
                    `<span class="text-yellow-500">&gt; Warning: A bee attempted to put down honey, but didn't have any on hand.</span>`
                  );
                }
            }
          default:
            break;
        }
        const collide = checkCollision(bee);
        if (collide && collide.type === "enemy") {
          world.entities[world.entities.indexOf(bee)] = null;
          world.entities[world.entities.indexOf(collide)] = null;
          world.workers[world.workers.indexOf(bee)] = null;
          bee.worker.terminate();
        }
        res(e.data.action);
      } else if (e.data.type === "error") {
        putLog(e.data.msg);
        res();
      }
    };
    const me = { ...bee, worker: null, sprite: null };
    bee.worker.postMessage({ type: "tick", world: serializeWorld(world), me });
    return bee;
  });

const tick = async () => {
  if (world.tick === 1) createWorkerBee([10, 10], 100);
  // TODO workers are not destroyed
  for (const entity of world.entities) {
    if (entity.lifetime) entity.lifetime -= 1;
  }
  world.entities = world.entities.filter((e) =>
    e.lifetime ? e.lifetime > 0 : true
  );
  for (const x in world.grid) {
    for (const y in world.grid[x]) {
      const cell = world.grid[x][y];
      if (!cell) continue;
      if (cell.type === "flower") {
        cell.growth++;
      }

      if (cell.lifetime) {
        cell.lifetime--;
        if (cell.lifetime <= 0) {
          setCell([x, y], undefined);
        }
      }
    }
  }
  world.tick++;
  world.flowerCooldown--;
  world.enemyCooldown--;
  // game logic
  await Promise.all([...world.workers.map(requestAndHandleAction)]);
  // clean up any possible collisions
  world.entities = world.entities.filter((e) => e !== null);
  world.workers = world.workers.filter((e) => e !== null);
  for (const entity of world.entities.filter((e) => e.type === "enemy")) {
    const dx = Math.sign(10 - entity.pos[0]);
    const dy = Math.sign(10 - entity.pos[1]);

    if (dx && dy) {
      if (Math.random() > 0.5) {
        entity.pos[0] += dx;
      } else {
        entity.pos[1] += dy;
      }
    } else if (dx) {
      entity.pos[0] += dx;
    } else if (dy) {
      entity.pos[1] += dy;
    }
    if (entity.pos[0] === 10 && entity.pos[1] === 10) {
      putLog("> GAME OVER <");
      putLog("> Total Honey: " + world.totalHoney);
      putLog("> Ticks Survived: " + world.tick);
      putLog("=== GAME RESET ===");
      reset();
      return;
    }
    const collide = checkCollision(entity);
    if (collide && collide.type === "worker") {
      world.entities[world.entities.indexOf(entity)] = null;
      world.entities[world.entities.indexOf(collide)] = null;
      collide.worker.terminate();
    }
  }

  world.entities = world.entities.filter((e) => e !== null);
  world.workers = world.workers.filter((e) => e !== null);

  // flowers spawn after bees move so they don't move erratically
  if (world.flowerCooldown <= 0) {
    world.flowerCooldown = 10 - world.tick / 100;

    while (true) {
      const pos = [
        Math.floor(Math.random() * 20),
        Math.floor(Math.random() * 20),
      ];
      if (getCell(pos)) continue;
      else {
        createFlower(pos);
        break;
      }
    }
  }
  if (world.enemyCooldown <= 0) {
    world.enemyCooldown = 15 - world.tick / 80;
    createEnemy();
  }

  // rendering
  ctx.fillStyle = "#15803d";
  ctx.fillRect(0, 0, 640, 640);

  ctx.strokeStyle = "#16a34a";
  for (let i = 0; i < GRID_SIZE; i++) {
    ctx.beginPath();
    ctx.moveTo(i * CELL_SIZE, 0);
    ctx.lineTo(i * CELL_SIZE, 640);
    ctx.closePath();
    ctx.stroke();
  }

  for (let i = 0; i < GRID_SIZE; i++) {
    ctx.beginPath();
    ctx.moveTo(0, i * CELL_SIZE);
    ctx.lineTo(640, i * CELL_SIZE);
    ctx.closePath();
    ctx.stroke();
  }

  // draw grid stuff
  for (const x in world.grid) {
    for (const y in world.grid[x]) {
      const cell = world.grid[x][y];
      if (cell?.sprite) {
        ctx.save();
        if (cell.type === "flower" && cell.growth < 7) ctx.globalAlpha = 0.25;
        ctx.drawImage(
          cell.sprite,
          x * CELL_SIZE,
          y * CELL_SIZE,
          CELL_SIZE,
          CELL_SIZE
        );
        ctx.restore();
      }
    }
  }

  for (const entity of world.entities) {
    ctx.drawImage(
      entity.sprite,
      entity.pos[0] * CELL_SIZE,
      entity.pos[1] * CELL_SIZE,
      CELL_SIZE,
      CELL_SIZE
    );
  }

  if (!world.running) return;

  // i know i can do something with rAF but im feeling lazy let me be :)
  setTimeout(() => tick(), 333);
};
reset();
setTimeout(() => tick(), 100);
window.tick = tick;
window.world = world;

const controls = [...document.getElementById("controls").children];
controls[0].onclick = () => {
  world.running = !world.running;
  if (world.running) {
    controls[0].innerHTML = "Pause";
  } else {
    controls[0].innerHTML = "Play";
  }
  tick();
};
controls[1].onclick = () => {
  if (world.running) return;
  tick();
};
controls[2].onclick = () => {
  localStorage.code = editor.getValue();
  putLog("> Saved code to localStorage");
};
controls[3].onclick = () => {
  document.location.hash = btoa(editor.getValue());
  putLog("> Copy the URL to share with others!");
};
controls[4].onclick = () => {
  reset();
  putLog("=== GAME RESET ===");
};