import { readFile } from 'fs/promises';
import { createInterface } from 'readline/promises';
import { stdin as input, stdout as output } from "node:process";

const buffer = await readFile("./module.wasm");
const { instance } = await WebAssembly.instantiate(buffer);
const memory = new Uint8Array(instance.exports.memory.buffer);

const rl = createInterface({ input, output });
const flag = (await rl.question("Enter the flag: ")).trim();
rl.close();

for (let i = 0; i < flag.length; i++) {
    memory[i] = flag.charCodeAt(i);
}

if (flag.length === 43 && instance.exports.check()) {
    console.log("nice job!");
} else {
    console.log("nope.");
}
