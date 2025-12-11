const express = require('express');
const rateLimit = require('express-rate-limit');
const puppeteer = require('puppeteer');

const app = express();
const port = 5000;
const flag = process.env.FLAG || 'amateursCTF{t3st_f14g}';

const limiter = rateLimit({
  windowMs: 1 * 60 * 1000,
  max: 10,
  message: 'Too many requests, please try again after a minute.'
});

async function viewPage(username) {
  const browser = await puppeteer.launch({
    headless: true,
    executablePath: "/usr/bin/chromium",
    args: [
      "--no-sandbox",
      "--disable-dev-shm-usage",
      "--disable-gpu",
      '--js-flags="--noexpose_wasm"',
    ],
    pipe: true,
  });

  await browser.setCookie({
    name: 'flag',
    value: flag,
    url: 'http://web:4000/',
    sameSite: 'Lax',
  });

  const page = await browser.newPage();
  const url = `http://web:4000/index.php?username=${username}`;
  await page.goto(url, { waitUntil: 'networkidle2' });
  await browser.close();
}

app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use('/', limiter);

// Small helper to render the HTML page with optional status message
function renderPage(statusMessage = '', isError = false) {
  return `
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <title>Cyrene Viewer Bot</title>
      <style>
        body {
          margin: 0;
          padding: 0;
          font-family: system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
          background: radial-gradient(circle at top, #4131a8 0, #050318 45%, #050318 100%);
          color: #fdf9ff;
          min-height: 100vh;
          display: flex;
          align-items: center;
          justify-content: center;
        }
        .card {
          background: rgba(5, 3, 24, 0.92);
          border-radius: 14px;
          padding: 22px 24px 20px;
          box-shadow: 0 18px 40px rgba(0, 0, 0, 0.75);
          max-width: 420px;
          width: 100%;
          border: 1px solid rgba(255, 255, 255, 0.18);
        }
        h1 {
          margin: 0 0 6px;
          font-size: 1.3rem;
        }
        .subtitle {
          font-size: 0.85rem;
          opacity: 0.8;
          margin-bottom: 16px;
        }
        form {
          display: flex;
          gap: 8px;
          margin-bottom: 10px;
        }
        label {
          display: block;
          font-size: 0.8rem;
          margin-bottom: 4px;
        }
        input[type="text"] {
          flex: 1;
          padding: 8px 10px;
          border-radius: 999px;
          border: 1px solid rgba(255, 255, 255, 0.26);
          background: rgba(3, 1, 18, 0.95);
          color: #fdf9ff;
          outline: none;
        }
        button {
          padding: 8px 14px;
          border-radius: 999px;
          border: 1px solid rgba(255, 255, 255, 0.4);
          background: radial-gradient(circle at top left, #f8a7ff, #88e4ff);
          color: #050318;
          font-weight: 500;
          cursor: pointer;
          white-space: nowrap;
        }
        button:hover {
          filter: brightness(1.05);
        }
        .hint {
          font-size: 0.78rem;
          opacity: 0.8;
        }
        .rate {
          font-size: 0.72rem;
          opacity: 0.65;
          margin-top: 4px;
        }
        .status {
          margin-top: 10px;
          padding: 8px 10px;
          border-radius: 8px;
          font-size: 0.8rem;
        }
        .status-success {
          background: rgba(88, 214, 141, 0.12);
          border: 1px solid rgba(88, 214, 141, 0.6);
        }
        .status-error {
          background: rgba(255, 99, 132, 0.12);
          border: 1px solid rgba(255, 99, 132, 0.7);
        }
      </style>
    </head>
    <body>
      <div class="card">
        <h1>Cyrene Viewer Bot</h1>
        <p class="subtitle">
          Submit a username and the bot will visit the Cyrene page with that name on your behalf.
        </p>
        <form method="POST" action="/">
          <div style="flex:1;">
            <label for="username">Trailblazer name</label>
            <input type="text" id="username" name="username" required />
          </div>
          <div style="display:flex;align-items:flex-end;">
            <button type="submit">Send to bot</button>
          </div>
        </form>
        <p class="hint">
          The bot will open <code>index.php?username=&lt;your_name&gt;</code> on the internal Cyrene site.
        </p>
        <p class="rate">
          Note: Limited to 10 requests per minute.
        </p>
        ${
          statusMessage
            ? `<div class="status ${isError ? 'status-error' : 'status-success'}">${statusMessage}</div>`
            : ''
        }
      </div>
    </body>
    </html>
  `;
}

app.get('/', (req, res) => {
  res.send(renderPage());
});

app.post('/', async (req, res) => {
  const username = req.body.username;
  if (!username) {
    return res
      .status(400)
      .send(renderPage('Bad Request: Missing username parameter.', true));
  }

  try {
    await viewPage(username);
    res
      .status(200)
      .send(renderPage('Page viewed successfully by the bot.'));
  } catch (error) {
    console.error(error);
    res
      .status(500)
      .send(renderPage('Internal Server Error while the bot was viewing the page.', true));
  }
});

app.listen(port, '0.0.0.0', () => {
  console.log(`Bot listening at http://0.0.0.0:${port}`);
});
