import express from 'express';
import bodyParser from 'body-parser';
import fetch from 'node-fetch';

const app = express();
app.use(bodyParser.json());

const HCAPTCHA_SECRET = process.env.HCAPTCHA_SECRET;

app.post('/verify', async (req, res) => {
  const { token } = req.body;
  if (typeof token !== 'string') {
    return res.status(400).json({ success: false, error: 'Invalid token' });
  }

  try {
    const resp = await fetch('https://hcaptcha.com/siteverify', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      body: `secret=${encodeURIComponent(HCAPTCHA_SECRET)}&response=${encodeURIComponent(token)}`
    });

    const data = await resp.json();
    return res.json(data);
  } catch (e) {
    console.error('hCaptcha error:', e);
    return res.status(500).json({ success: false, error: 'verification_failed' });
  }
});

app.listen(5000, () => {
  console.log('Verifier listening on :5000');
});
