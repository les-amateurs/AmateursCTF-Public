import { launch } from "puppeteer";
import path from "path";

let lastBotRun = 0;
const botCooldown = 30 * 1000; // 30 seconds
let botIsRunning = false;

function sleep(ms){
    return new Promise(resolve => setTimeout(resolve, ms));
}

export async function runBot(url) {
    if (botIsRunning) {
        return;
    }
    botIsRunning = true;
    lastBotRun = Date.now();

    const browser = await launch({
            headless: process.env.HEADLESS || false,
            defaultViewport: null,
            pipe: true,
            args: ['--no-sandbox', '--disable-setuid-sandbox',
            '--enable-benchmarking',
            '--js-flags=--jitless,--noexpose_wasm', // no zero day pls pls pls
            ],
            dumpio: true,
            slowMo: process.env.SLOWMO ? 200 : 0,
        });

    try {

        await browser.setCookie({
            name: 'FLAG',
            value: process.env.FLAG || "amateursCTF{y0u_f0rg0t_an_3nv_var}", // this is a test flag for players to test locally with, do not submit it
            httpOnly: false,
            secure: true,
            domain: 'orange-skies-amateurs-ctf-2025.pages.dev',
            path: '/',
        });

        const page = await browser.newPage();
        await Promise.race([page.goto(url), sleep(5000)]);
        await page.close();

    } catch (ex) {
        console.error(ex);
    }

    await browser.close();

    botIsRunning = false;
}

export function canRunBot() {
    const now = Date.now();
    if (now - lastBotRun < botCooldown && !process.env.DISABLE_COOLDOWN) {
        return [false, "Wait " + (botCooldown - (now - lastBotRun)) / 1000 + " seconds before running again"];
    }
    if(botIsRunning){
        return [false, "Bot is currently running."];
    }
    return [true, "Conditions passed."];
}