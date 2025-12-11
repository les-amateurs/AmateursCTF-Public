import express from 'express';
import fs from 'fs';
import * as bot from './bot.js';

const app = express();

const source = fs.readFileSync('./admin-bot-server.js', 'utf8');
const policy = fs.readFileSync('./policy.json', 'utf8');
const dockerfile = fs.readFileSync('./Dockerfile', 'utf8');
const botSource = fs.readFileSync('./bot.js', 'utf8');

// imaginaryCTF ah challenge explaining
app.get('/', (req, res) => {
    res.type('text/plain').send(source);
});

app.get('/policy', (req, res) => {
    res.type('text/plain').send(policy);
});

app.get('/dockerfile', (req, res) => {
    res.type('text/plain').send(dockerfile);
});

app.get('/bot', (req, res) => {
    res.type('text/plain').send(botSource);
});

app.get('/submit', (req, res) => {
    res.send("<form method='POST' action='/submit'>\n" +
        "<input type='url' name='url' placeholder='https://orange-skies-amateurs-ctf-2025.pages.dev/'>\n" +
        "<input type='submit' value='Submit'>\n" +
        "</form>");
});

app.use(express.urlencoded({ extended: false }));

app.post('/submit', (req, res) => {

    if(!req.body || !req.body.url || typeof req.body.url !== 'string') {
        res.status(400).send("Invalid URL");
        return;
    }

    if(!req.body.url.startsWith('https://orange-skies-amateurs-ctf-2025.pages.dev/')) {
        res.status(400).send("URL must start with https://orange-skies-amateurs-ctf-2025.pages.dev/");
        return;
    }

    // run admin bot
    const [ok, msg] = bot.canRunBot();
    if(ok) {
        bot.runBot(req.body.url);
    }
    res.send(msg);
});

const port = parseInt(process.env.PORT || "3000");
app.listen(port, () => {
    console.log(`Listening on port ${port}`);
});