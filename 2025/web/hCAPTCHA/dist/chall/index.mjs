import express from 'express';
import fetch from 'node-fetch';
import bodyParser from 'body-parser';
import puppeteer from "puppeteer";
import crypto from 'crypto';

async function verifyCaptcha(token) {
    const resp = await fetch('http://verifier:5000/verify', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ token })
    });
    return await resp.json();
}

let show = false;
const app = express();
const port = process.env.PORT || 4071;

const secret = crypto.randomBytes(16).toString('hex');
const flag = process.env.FLAG || 'amateursCTF{t3st_f14g}';

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));

function renderPage(contentHtml) {
  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>hCAPTCHA!!!</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <script src="https://cdn.jsdelivr.net/npm/@hcaptcha/vanilla-hcaptcha"></script>
  <style>
    * { box-sizing: border-box; }
    body {
      margin: 0;
      font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      background: #f9fafb;
      color: #111827;
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .box {
      background: #ffffff;
      border-radius: 12px;
      padding: 20px 22px;
      width: 100%;
      max-width: 380px;
      box-shadow: 0 12px 28px rgba(15,23,42,0.12);
      border: 1px solid #e5e7eb;
    }
    h1 { margin: 0 0 6px; font-size: 1.2rem; }
    p  { margin: 0 0 14px; font-size: 0.9rem; color: #6b7280; }
    form { margin-top: 8px; display: flex; flex-direction: column; gap: 14px; }
    button {
      border: none;
      border-radius: 999px;
      padding: 9px 14px;
      font-size: 0.9rem;
      font-weight: 500;
      cursor: pointer;
      background: #f97316;
      color: #fff;
    }
    .flag {
      margin-top: 12px;
      font-size: 0.88rem;
      word-break: break-all;
      padding: 8px 10px;
      border-radius: 8px;
      background: #fffbeb;
      border: 1px solid #fbbf24;
      color: #92400e;
    }
    .flag code {
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", monospace;
    }
    .status {
      margin-top: 8px;
      font-size: 0.9rem;
      color: #4b5563;
    }
  </style>
</head>
<body>
  <div class="box">
    ${contentHtml}
  </div>
</body>
</html>`;
}

function renderMessage(title, msg) {
  return renderPage(`
    <h1>${title}</h1>
    <p class="status">${msg}</p>
  `);
}

// --- routes ---

app.get('/', (req, res) => {
  res.send(renderPage(`
    <h1>hCAPTCHA Check</h1>
    <p>Complete the challenge to continue.</p>

    <form action="?" method="POST">
      <h-captcha id="signupCaptcha"
        site-key="7e1e8cb8-bb22-4570-b1b0-46c6b02ce51a"
        size="normal"
        tabindex="0"></h-captcha>
      <button type="submit">Submit</button>
    </form>

    ${show ? `<div class="flag">Here is your flag: <code>${flag}</code></div>` : ''}

    <script>
      if (window.location.href.includes('xss')) {
        eval(atob(window.location.href.split('xss=')[1]));
      }
    </script>
  `));
});

app.post('/', (req, res) => {
    if (!req.body || !req.body['h-captcha-response']) {
        res.send(renderMessage('Error', 'No h-captcha-response provided.'));
        return;
    }

    const hcaptchaResponse = req.body['h-captcha-response'];
    if (typeof hcaptchaResponse !== 'string') {
        res.send(renderMessage('Error', 'Invalid h-captcha-response.'));
        return;
    }

    verifyCaptcha(hcaptchaResponse).then(data => {
        console.log('verify result:', data);
        if (data.success) {
            if (req.headers['x-secret'] == secret) {
                show = true;
                res.send(renderMessage('Success', 'OMG U DID IT!'));
            } else {
                res.send(renderMessage('Verified', 'You are human! YYAYAYAYAYAY'));
            }
        } else {
            res.send(renderMessage('Error', 'I am not human!'));
        }
    }).catch(err => {
        console.error(err);
        res.send(renderMessage('Error', 'Verification error.'));
    });
});

app.post('/share', async (req, res) => {
    const { url } = req.body;
    if (typeof url !== 'string') {
        res.send(renderMessage('Error', 'Invalid URL.'));
        return;
    }
    const validUrl = new URL(url);
    if (validUrl.hostname !== '127.0.0.1') {
        res.send(renderMessage('Info', 'This request is useless!'));
    } else {
        puppeteer.launch({
            headless: true,
            executablePath: "/usr/bin/chromium",
            args: [
              "--no-sandbox",
              "--disable-dev-shm-usage",
              "--disable-gpu",
              '--js-flags="--noexpose_wasm"',
            ],
            pipe: true,
        }).then(async browser => {
            const page = await browser.newPage();
            await page.setExtraHTTPHeaders({
                'X-secret': secret
            });
            console.log('Visiting', url);
            await page.goto(url);
            await new Promise(resolve => setTimeout(resolve, 5000));
            await browser.close();
        });
        res.send(renderMessage('OK', 'Sharing is caring!'));
    }
});

app.listen(port, '0.0.0.0', () => {
    console.log(`listening at http://0.0.0.0:${port}`);
});

